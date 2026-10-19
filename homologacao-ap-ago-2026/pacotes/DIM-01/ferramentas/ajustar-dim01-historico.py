"""Ajuste DIM-01 — regularização de AP de agosto/2026 · parte 2: Histórico e Linha do Tempo.

Uso (a partir da raiz do repositório):
    python3 ajustar-dim01-historico.py .

1. 1746-historico/data.js e 1746-timeline/data.js: em toda lista "aps", soma a
   linha "SEM AP (AGO)" em "AP3" (Chamados e Ouvidoria), recalcula cdif, odif,
   cvar, ovar, rate2025 e rate2026 (taxa = ouvidorias por 1.000 chamados, mesma
   fórmula das demais linhas) e remove a linha. Ajusta dois textos do histórico.
Nenhuma soma muda. Sai com código 1 se qualquer conferência falhar.
"""
import json, os, sys

RAIZ = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else ".")
ROTULO = "SEM AP (AGO)"
CAMPOS = ["c2025", "c2026", "o2025", "o2026"]
log = []

def falha(msg):
    print("FALHA: " + msg); sys.exit(1)

def abrir(rel):
    s = open(os.path.join(RAIZ, rel), encoding="utf-8").read()
    i = s.index("{"); j = s.rstrip().rstrip(";").rindex("}") + 1
    obj = json.loads(s[i:j])
    if s[:i] + json.dumps(obj, ensure_ascii=False, separators=(",", ":")) + s[j:] != s:
        falha("serialização não reproduz o original: " + rel)
    return s[:i], obj, s[j:]

def gravar(rel, pre, obj, pos):
    with open(os.path.join(RAIZ, rel), "w", encoding="utf-8") as f:
        f.write(pre + json.dumps(obj, ensure_ascii=False, separators=(",", ":")) + pos)

def recalcular(x):
    x["cdif"] = x["c2026"] - x["c2025"]; x["odif"] = x["o2026"] - x["o2025"]
    x["cvar"] = x["cdif"] / x["c2025"] if x["c2025"] else None
    x["ovar"] = x["odif"] / x["o2025"] if x["o2025"] else None
    x["rate2025"] = x["o2025"] / x["c2025"] * 1000 if x["c2025"] else None
    x["rate2026"] = x["o2026"] / x["c2026"] * 1000 if x["c2026"] else None

def soma(L):
    return [sum((x.get(k) or 0) for x in L) for k in CAMPOS]

def ajustar_aps(rel, textos=None):
    pre, obj, pos = abrir(rel); n = 0
    def percorrer(o):
        nonlocal n
        if isinstance(o, list):
            for x in o: percorrer(x)
            return
        if not isinstance(o, dict): return
        L = o.get("aps")
        if isinstance(L, list):
            s = next((x for x in L if x.get("nome") == ROTULO), None)
            if s:
                antes = soma(L)
                ordenado = all(L[i-1]["c2026"] >= L[i]["c2026"] for i in range(1, len(L)))
                ap3 = next((x for x in L if x.get("nome") == "AP3"), None)
                if not ap3: falha(rel + ": AP3 inexistente")
                for k in CAMPOS: ap3[k] += s[k]
                recalcular(ap3)
                L.remove(s)
                if ordenado: L.sort(key=lambda x: -x["c2026"])  # sort estável
                if soma(L) != antes: falha(rel + ": somas alteradas")
                n += 1
        for v in o.values(): percorrer(v)
    percorrer(obj)
    if textos: textos(obj)
    if ROTULO in json.dumps(obj, ensure_ascii=False): falha(rel + ": rótulo remanescente")
    gravar(rel, pre, obj, pos)
    log.append(f"{rel}: {n} listas aps ajustadas")

def textos_historico(d):
    m = d.get("matrix") or []
    if len(m) > 1 and len(m[1]) > 3 and m[1][3] == "Taxa válida + SEM AP":
        m[1][3] = "Taxa válida"
    g = d.get("governance") or []
    antigo = "Agosto × AP preserva SEM AP (AGO) como resíduo explícito, sem redistribuição."
    if antigo in g:
        g[g.index(antigo)] = ("Agosto × AP: o resíduo de agosto foi regularizado em AP3 em 19/10/2026 (DIM-01). Na versão de 04/09/2026 "
                              "da base auditável essas linhas tinham AP nula; a AP3 foi atribuída depois, por bairro. Totais inalterados.")
    if "SEM AP" in json.dumps(d, ensure_ascii=False): falha("historico: texto SEM AP remanescente")

ajustar_aps("1746-historico/data.js", textos_historico)
ajustar_aps("1746-timeline/data.js")
print("\n".join(log)); print("OK")
