/* ============================================================
   HUB COMLURB · testes/testar-cascata-territorial.js
   Cascata territorial da Linha do Tempo 1746 (registro CAS-01, outubro/2026).

   Uso (a partir da raiz do repositório):

     node testes/testar-cascata-territorial.js .

   Origem: BRAZ DE PINA e OSWALDO CRUZ apareciam como "SEM AP" e
   gerência "NÃO INFORMADA" em toda a cascata, porque o GeoJSON oficial
   grafa "Brás de Pina" e "Osvaldo Cruz". Este arquivo garante que:

   1. toda linha de bairro da cascata tem AP entre AP1 e AP5 e gerência;
   2. AP e gerência de cada bairro são as do GeoJSON oficial
      (assets/geojson/DLU_Novos_Bairros_estrutura2025.geojson), com
      equivalência de grafia declarada abaixo;
   3. os dois bairros corrigidos estão em AP3/NG11P e AP3/NG15H.

   Somente leitura: não escreve em disco e não acessa rede.
   ============================================================ */
"use strict";

var fs = require("fs");
var path = require("path");
var vm = require("vm");

var raiz = process.argv[2];
if (!raiz) {
  console.error("Uso: node testes/testar-cascata-territorial.js <raiz-do-repositorio>");
  process.exit(1);
}
raiz = path.resolve(raiz);

var grupos = [], atual = null, totais = { pass: 0, fail: 0 };
function grupo(nome) { atual = { nome: nome, casos: [] }; grupos.push(atual); }
function caso(nome, obtido, esperado) {
  var ok = JSON.stringify(obtido) === JSON.stringify(esperado);
  atual.casos.push({ nome: nome, ok: ok, obtido: obtido, esperado: esperado });
  totais[ok ? "pass" : "fail"]++;
}
function verdadeiro(nome, cond, detalhe) {
  atual.casos.push({ nome: nome, ok: !!cond, obtido: detalhe === undefined ? !!cond : detalhe, esperado: true });
  totais[cond ? "pass" : "fail"]++;
}
function ler(rel) { return fs.readFileSync(path.join(raiz, rel), "utf8"); }
function norm(s) { return String(s == null ? "" : s).normalize("NFD").replace(/[̀-ͯ]/g, "").toUpperCase().trim(); }
function carregarGlobal(rel, nome) {
  var ctx = { window: {} };
  vm.runInNewContext(ler(rel), ctx, { filename: rel });
  return ctx.window[nome];
}
function percorrer(o, fn) {
  if (Array.isArray(o)) { o.forEach(function (x) { percorrer(x, fn); }); return; }
  if (!o || typeof o !== "object") return;
  fn(o);
  Object.keys(o).forEach(function (k) { percorrer(o[k], fn); });
}

var APS_VALIDAS = { AP1: 1, AP2: 1, AP3: 1, AP4: 1, AP5: 1 };
// Equivalência de grafia entre a cascata (fonte 1746) e o GeoJSON oficial.
var GRAFIA_GEOJSON = { "BRAZ DE PINA": "BRAS DE PINA", "OSWALDO CRUZ": "OSVALDO CRUZ" };

var geo = {};
JSON.parse(ler("assets/geojson/DLU_Novos_Bairros_estrutura2025.geojson")).features.forEach(function (f) {
  var p = f.properties || {};
  if (p.nome) geo[norm(p.nome)] = { ap: "AP" + String(p.area_plane).trim(), gerencia: p.gerdlu };
});

var cascata = carregarGlobal("1746-timeline/cascade_data.js", "TIMELINE1746_CASCADE");

grupo("1746-timeline/cascade_data.js · todo bairro tem AP e gerência");
verdadeiro("Cascata carregada", !!cascata);
var linhas = [], semAp = {}, semGer = {};
if (cascata) percorrer(cascata, function (o) {
  if (!("ap" in o) || !("gerencia" in o) || !o.nome) return;
  linhas.push(o);
  if (!APS_VALIDAS[o.ap]) semAp[o.nome] = o.ap;
  if (!o.gerencia || o.gerencia === "NÃO INFORMADA") semGer[o.nome] = o.gerencia;
});
verdadeiro("Há linhas de bairro na cascata", linhas.length > 0, linhas.length);
caso("Nenhum bairro fora de AP1 a AP5", semAp, {});
caso("Nenhum bairro sem gerência", semGer, {});
verdadeiro("Rótulo SEM AP ausente da cascata", ler("1746-timeline/cascade_data.js").indexOf('"ap":"SEM AP"') < 0);

grupo("Cascata × GeoJSON oficial · AP e gerência por bairro");
var bairros = {}, divergentes = {}, semPoligono = {};
linhas.forEach(function (o) {
  var chave = norm(o.nome);
  var g = geo[GRAFIA_GEOJSON[chave] || chave];
  bairros[chave] = 1;
  if (!g) { semPoligono[o.nome] = 1; return; }
  if (g.ap !== o.ap || g.gerencia !== o.gerencia) divergentes[o.nome] = { cascata: [o.ap, o.gerencia], geojson: [g.ap, g.gerencia] };
});
verdadeiro("Bairros distintos na cascata", Object.keys(bairros).length > 0, Object.keys(bairros).length);
caso("Todo bairro da cascata tem polígono no GeoJSON (com equivalência de grafia)", Object.keys(semPoligono), []);
caso("AP e gerência de todo bairro iguais às do GeoJSON", divergentes, {});

grupo("Bairros corrigidos no registro CAS-01");
[["BRAZ DE PINA", "AP3", "NG11P"], ["OSWALDO CRUZ", "AP3", "NG15H"]].forEach(function (b) {
  var doBairro = linhas.filter(function (o) { return o.nome === b[0]; });
  verdadeiro(b[0] + " presente na cascata", doBairro.length > 0, doBairro.length);
  caso(b[0] + " em " + b[1] + "/" + b[2] + " em todas as linhas",
    doBairro.filter(function (o) { return o.ap !== b[1] || o.gerencia !== b[2]; }).length, 0);
});

grupos.forEach(function (g) {
  console.log("== " + g.nome + " ==");
  g.casos.forEach(function (c) {
    console.log("  [" + (c.ok ? "PASSOU" : "FALHOU") + "] " + c.nome + (c.ok ? "" : " · obtido: " + JSON.stringify(c.obtido) + " · esperado: " + JSON.stringify(c.esperado)));
  });
});
console.log("TOTAL: " + (totais.pass + totais.fail) + " casos | APROVADOS: " + totais.pass + " | REPROVADOS: " + totais.fail);
process.exit(totais.fail ? 1 : 0);
