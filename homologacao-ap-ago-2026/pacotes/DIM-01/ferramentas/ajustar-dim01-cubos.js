/* ============================================================
   Ajuste dimensional de AP — AGO/2026 (19/10/2026) · DIM-01 · parte 1: cubos

   Uso (a partir da raiz do repositório):
     node ajustar-dim01-cubos.js .

   O que faz:
   1. Cubos de Chamados 1746 e Ouvidoria (e seus espelhos em assets/data):
      em toda lista "ap", soma o nó "SEM AP (AGO)" ao nó "AP3",
      recalcula dif, var, contrib e part com as mesmas fórmulas do cubo
      e remove o nó "SEM AP (AGO)".
   2. Copia os cubos ajustados para os espelhos em assets/data.
   Histórico e Linha do Tempo são ajustados por
   ajustar-dim01-historico.py (arquivos gerados em Python; a
   serialização Python reproduz o original byte a byte).

   Não altera nenhum total, série mensal, tipo, subtipo, gerência ou bairro
   dos cubos. Falha (exit 1) se qualquer conferência não fechar.
   ============================================================ */
"use strict";
var fs = require("fs");
var path = require("path");

var raiz = path.resolve(process.argv[2] || ".");
var ROTULO = "SEM AP (AGO)";
var log = [];

function ler(rel) { return fs.readFileSync(path.join(raiz, rel), "utf8"); }
function abrir(rel) {
  var s = ler(rel), i = s.indexOf("{"), j = s.trimEnd().replace(/;$/, "").lastIndexOf("}") + 1;
  var obj = JSON.parse(s.slice(i, j));
  if (s.slice(0, i) + JSON.stringify(obj) + s.slice(j) !== s) throw new Error("Serialização não reproduz o original: " + rel);
  return { pre: s.slice(0, i), obj: obj, pos: s.slice(j) };
}
function gravar(rel, a) { fs.writeFileSync(path.join(raiz, rel), a.pre + JSON.stringify(a.obj) + a.pos, "utf8"); }
function falha(msg) { console.error("FALHA: " + msg); process.exit(1); }
function ordenadoDesc(lista, campo) { return lista.every(function (x, i) { return i === 0 || lista[i - 1][campo] >= x[campo]; }); }
function ordenarDescEstavel(lista, campo) {
  return lista.map(function (x, i) { return [x, i]; })
    .sort(function (a, b) { return (b[0][campo] - a[0][campo]) || (a[1] - b[1]); })
    .map(function (p) { return p[0]; });
}

/* ---------- 1 · cubos ---------- */
function ajustarCubo(rel) {
  var a = abrir(rel), nos = 0, movido = { v2025: 0, v2026: 0 };
  (function percorrer(o) {
    if (Array.isArray(o)) { o.forEach(percorrer); return; }
    if (!o || typeof o !== "object") return;
    if (Array.isArray(o.ap) && "total2026" in o) {
      var L = o.ap, iS = L.findIndex(function (x) { return x.nome === ROTULO; });
      if (iS >= 0) {
        var s = L[iS], estavaOrdenado = ordenadoDesc(L, "v2026");
        var ap3 = L.find(function (x) { return x.nome === "AP3"; });
        if (!ap3) { s.nome = "AP3"; ap3 = s; L.splice(iS, 1); L.push(ap3); }
        else { ap3.v2025 += s.v2025; ap3.v2026 += s.v2026; L.splice(L.indexOf(s), 1); }
        movido.v2025 += s.v2025; movido.v2026 += s.v2026;
        ap3.dif = ap3.v2026 - ap3.v2025;
        ap3.var = ap3.v2025 ? ap3.dif / ap3.v2025 : null;
        ap3.contrib = o.dif ? ap3.dif / o.dif : 0;
        ap3.part = o.total2026 ? ap3.v2026 / o.total2026 : 0;
        if (estavaOrdenado) o.ap = ordenarDescEstavel(L, "v2026");
        nos++;
      }
      var s26 = o.ap.reduce(function (t, x) { return t + x.v2026; }, 0);
      var s25 = o.ap.reduce(function (t, x) { return t + x.v2025; }, 0);
      if (s26 !== o.total2026 || s25 !== o.total2025) falha(rel + ": soma das APs difere do total após ajuste");
    }
    for (var k in o) percorrer(o[k]);
  })(a.obj);
  if (JSON.stringify(a.obj).indexOf(ROTULO) >= 0) falha(rel + ": rótulo remanescente");
  gravar(rel, a);
  log.push(rel + ": " + nos + " nós ajustados; movido para AP3 no acumulado geral e recortes");
  return a.obj;
}

/* ---------- execução ---------- */
var antes = {};
["chamados-1746/chamados_cube.js", "ouvidoria/ouvidoria_cube.js"].forEach(function (rel) {
  var o = abrir(rel).obj.periods.acumulado.all;
  antes[rel] = { total2025: o.total2025, total2026: o.total2026, ap: o.ap.map(function (x) { return [x.nome, x.v2025, x.v2026]; }) };
});
var cha = ajustarCubo("chamados-1746/chamados_cube.js");
var ouv = ajustarCubo("ouvidoria/ouvidoria_cube.js");
fs.copyFileSync(path.join(raiz, "chamados-1746/chamados_cube.js"), path.join(raiz, "assets/data/chamados-1746/chamados_cube.js"));
fs.copyFileSync(path.join(raiz, "ouvidoria/ouvidoria_cube.js"), path.join(raiz, "assets/data/ouvidoria/ouvidoria_cube.js"));
log.push("espelhos em assets/data atualizados por cópia idêntica");



[["chamados-1746/chamados_cube.js", cha], ["ouvidoria/ouvidoria_cube.js", ouv]].forEach(function (p) {
  var o = p[1].periods.acumulado.all, a0 = antes[p[0]];
  if (o.total2025 !== a0.total2025 || o.total2026 !== a0.total2026) falha(p[0] + ": total alterado");
  log.push(p[0] + " · AP antes: " + JSON.stringify(a0.ap));
  log.push(p[0] + " · AP depois: " + JSON.stringify(o.ap.map(function (x) { return [x.nome, x.v2025, x.v2026]; })));
});
console.log(log.join("\n"));
console.log("OK");
