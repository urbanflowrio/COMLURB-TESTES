#!/usr/bin/env bash
# ============================================================
# Verificação limpa dos pacotes DIM-01, CAS-01 e TST-01
#
# Uso:
#   bash verificar-pacotes.sh <pasta-dos-pacotes> <copia-limpa-do-COMLURB-3b41330> [pasta-candidato]
#
#   pasta-candidato (opcional): módulos publicados para conferência visual;
#   cada arquivo deve ser idêntico ao resultado de base + DIM-01 + CAS-01.
#
# Não altera nenhum repositório: trabalha em cópias temporárias.
# Sai com código 1 se qualquer verificação falhar.
# ============================================================
set -u
PKG="$(cd "$1" && pwd)"; BASE="$(cd "$2" && pwd)"; CAND="${3:-}"
TMP="$(mktemp -d)"; FALHAS=0
ok(){ echo "  [OK]    $*"; }
erro(){ echo "  [FALHA] $*"; FALHAS=$((FALHAS+1)); }
sha(){ sha256sum "$1" | cut -c1-64; }

aplicar(){ # destino pacote...
  local dst="$1"; shift
  for p in "$@"; do cp -r "$PKG/$p/arquivos/." "$dst/"; done
}
copia(){ rm -rf "$TMP/$1"; cp -r "$BASE" "$TMP/$1"; }
rodar(){ # pasta script esperado(0|1) rotulo
  ( cd "$TMP/$1" && node "testes/$2" . > "$TMP/$1-$2.log" 2>&1 ); local rc=$?
  local tot; tot=$(tail -1 "$TMP/$1-$2.log")
  if { [ "$3" = 0 ] && [ $rc = 0 ]; } || { [ "$3" = 1 ] && [ $rc != 0 ]; }; then ok "$4 · $tot"; else erro "$4 · código $rc · $tot"; fi
}

echo "== 1. Manifestos: hashes 'antes' = base 3b41330, 'depois' = arquivos entregues"
for p in DIM-01 CAS-01 TST-01; do
  while IFS='|' read -r _ f antes depois _; do
    f=$(echo "$f" | tr -d ' `'); antes=$(echo "$antes" | tr -d ' `'); depois=$(echo "$depois" | tr -d ' `')
    [ -z "$f" ] || [ "$f" = "Arquivo" ] || [[ "$f" == ---* ]] && continue
    [ "$(sha "$PKG/$p/arquivos/$f")" = "$depois" ] || erro "$p · $f: hash 'depois' não confere"
    if [ "$p" != TST-01 ]; then
      if [ "$antes" = "(novo)" ]; then [ ! -e "$BASE/$f" ] || erro "$p · $f declarado novo mas existe na base"
      else [ "$(sha "$BASE/$f")" = "$antes" ] || erro "$p · $f: hash 'antes' não confere com a base"; fi
    fi
  done < "$PKG/$p/evidencias/manifesto-sha256.md"
  ok "$p · manifesto conferido ($(grep -c '^| `' "$PKG/$p/evidencias/manifesto-sha256.md") arquivos)"
done

echo "== 2. Patches aplicam limpos sobre a base"
for p in DIM-01 CAS-01; do
  copia "patch-$p"; ( cd "$TMP/patch-$p" && git init -q && git apply --check "$PKG/$p/evidencias/diff.patch" ) && ok "$p · git apply --check" || erro "$p · patch não aplica"
done

echo "== 3. Independência de DIM-01 e CAS-01"
comum=$(comm -12 <(sort "$PKG/DIM-01/evidencias/arquivos-alterados.txt") <(sort "$PKG/CAS-01/evidencias/arquivos-alterados.txt"))
[ -z "$comum" ] && ok "nenhum arquivo em comum" || erro "arquivos em comum: $comum"
copia ordem1; aplicar "$TMP/ordem1" DIM-01 CAS-01
copia ordem2; aplicar "$TMP/ordem2" CAS-01 DIM-01
diff -rq "$TMP/ordem1" "$TMP/ordem2" >/dev/null && ok "DIM→CAS e CAS→DIM produzem árvores idênticas" || erro "ordem de aplicação altera o resultado"

echo "== 4. Testes dos pacotes em cada combinação (npm ci uma vez)"
( cd "$BASE" && [ -d node_modules ] ) || ( cd "$TMP" && cp "$BASE/package.json" "$BASE/package-lock.json" . && npm ci --silent >/dev/null 2>&1 )
NM="$BASE/node_modules"; [ -d "$NM" ] || NM="$TMP/node_modules"
for c in base dim cas dimcas; do copia "$c"; ln -s "$NM" "$TMP/$c/node_modules"; done
aplicar "$TMP/dim" DIM-01; aplicar "$TMP/cas" CAS-01; aplicar "$TMP/dimcas" DIM-01 CAS-01
cp "$PKG/DIM-01/arquivos/testes/testar-cobertura-ap.js" "$TMP/base/testes/"
cp "$PKG/CAS-01/arquivos/testes/testar-cascata-territorial.js" "$TMP/base/testes/"
cp "$PKG/CAS-01/arquivos/testes/testar-cascata-territorial.js" "$TMP/dim/testes/"
cp "$PKG/DIM-01/arquivos/testes/testar-cobertura-ap.js" "$TMP/cas/testes/"
rodar base testar-cobertura-ap.js 1 "base · teste DIM reprova (detecta o problema)"
rodar base testar-cascata-territorial.js 1 "base · teste CAS reprova (detecta o problema)"
rodar dim testar-cobertura-ap.js 0 "DIM · teste DIM aprova"
rodar dim testar-cascata-territorial.js 1 "DIM sozinho não corrige a cascata (esperado)"
rodar cas testar-cascata-territorial.js 0 "CAS · teste CAS aprova"
rodar cas testar-cobertura-ap.js 1 "CAS sozinho não corrige AP (esperado)"
rodar dimcas testar-cobertura-ap.js 0 "DIM+CAS · teste DIM aprova"
rodar dimcas testar-cascata-territorial.js 0 "DIM+CAS · teste CAS aprova"

echo "== 5. Regressão completa (npm test)"
regressao(){ ( cd "$TMP/$1" && npm test > "$TMP/$1-npm.log" 2>&1 ); local rc=$?
  local n; n=$(grep -hoE "APROVADOS: [0-9]+|[0-9]+ aprovados|[0-9]+ casos executados" "$TMP/$1-npm.log" | grep -oE "[0-9]+" | paste -sd+ | bc)
  if { [ "$2" = 0 ] && [ $rc = 0 ]; } || { [ "$2" = 1 ] && [ $rc != 0 ]; }; then ok "$3 · $n aprovações · código $rc"; else erro "$3 · código $rc"; fi
  grep -h "FALHOU" "$TMP/$1-npm.log" | head -3 | sed 's/^/          /'; }
regressao dim 0 "DIM-01"
regressao cas 0 "CAS-01"
copia full; ln -s "$NM" "$TMP/full/node_modules"; aplicar "$TMP/full" DIM-01 CAS-01 TST-01
regressao full 0 "DIM-01 + CAS-01 + TST-01"
copia tstsozinho; ln -s "$NM" "$TMP/tstsozinho/node_modules"; aplicar "$TMP/tstsozinho" TST-01
regressao tstsozinho 1 "TST-01 sem DIM/CAS reprova (dependência confirmada)"

echo "== 6. Invariantes de dados (DIM+CAS)"
node - "$BASE" "$TMP/dimcas" <<'EOF' && ok "totais, séries, tipos, gerências e bairros dos cubos idênticos; só AP mudou" || erro "invariantes de dados"
const fs=require("fs"),path=require("path");const [b,d]=process.argv.slice(2);
const L=f=>{const s=fs.readFileSync(f,"utf8");return JSON.parse(s.slice(s.indexOf("{"),s.trimEnd().replace(/;$/,"").lastIndexOf("}")+1));};
const sem=o=>Array.isArray(o)?o.map(sem):(o&&typeof o==="object")?Object.fromEntries(Object.entries(o).filter(([k])=>k!=="ap").map(([k,v])=>[k,sem(v)])):o;
let ok=true;
for(const f of ["chamados-1746/chamados_cube.js","ouvidoria/ouvidoria_cube.js"]){ if(JSON.stringify(sem(L(path.join(b,f))))!==JSON.stringify(sem(L(path.join(d,f))))){console.log("  diferença fora de AP em",f);ok=false;} }
const sc=o=>Array.isArray(o)?o.map(sc):(o&&typeof o==="object")?Object.fromEntries(Object.entries(o).filter(([k])=>k!=="ap"&&k!=="gerencia").map(([k,v])=>[k,sc(v)])):o;
if(JSON.stringify(sc(L(path.join(b,"1746-timeline/cascade_data.js"))))!==JSON.stringify(sc(L(path.join(d,"1746-timeline/cascade_data.js"))))){console.log("  diferença fora de ap/gerencia na cascata");ok=false;}
process.exit(ok?0:1);
EOF

if [ -n "$CAND" ]; then
  echo "== 7. Candidato visual: identidade completa, exceto supressão textual autorizada"
  n=0; d=0
  while IFS= read -r -d '' f; do rel="${f#$CAND/}"; n=$((n+1))
    if [[ "$rel" == "chamados-1746/index.html" || "$rel" == "ouvidoria/index.html" ]]; then
      # Única exceção visual autorizada: remover explicação obsoleta de agosto.
      python3 - "$TMP/dimcas/$rel" "$f" <<'PY' || { d=$((d+1)); erro "candidato difere: $rel"; }
import pathlib, sys
origem = pathlib.Path(sys.argv[1]).read_bytes()
candidato = pathlib.Path(sys.argv[2]).read_bytes()
# Literal em UTF-8, evitando interpretação de escapes da documentação.
trecho = " • Agosto/2025 e agosto/2026 constam no histórico oficial congelado sem classificação de AP. Os registros aparecem como 'Sem AP (Ago)'.".encode("utf-8")
sys.exit(0 if origem.count(trecho) == 1 and origem.replace(trecho, b"") == candidato else 1)
PY
    else
      cmp -s "$f" "$TMP/dimcas/$rel" || { d=$((d+1)); erro "candidato difere: $rel"; }
    fi
  done < <(find "$CAND" -type f -print0)
  [ $d = 0 ] && ok "$n arquivos do candidato conferidos, com exceção textual estritamente validada"
fi

echo
[ $FALHAS = 0 ] && echo "RESULTADO: todas as verificações aprovadas" || echo "RESULTADO: $FALHAS falha(s)"
rm -rf "$TMP"; exit $([ $FALHAS = 0 ] && echo 0 || echo 1)
