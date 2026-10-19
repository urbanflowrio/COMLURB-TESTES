/* ============================================================
   HUB COMLURB · testes/testar-cobertura-ap.js
   Cobertura e conciliação da dimensão Área de Planejamento (outubro/2026).

   Uso (a partir da raiz do repositório):

     node testes/testar-cobertura-ap.js .

   Origem: o cubo de agosto/2026 foi publicado com a soma das APs menor
   que o total (701 chamados e 116 ouvidorias com AP nula na base de
   04/09/2026), sem que nenhum teste acusasse. Este arquivo impede que isso se repita:

   1. em Chamados 1746 e Ouvidoria, toda lista "ap" soma exatamente o
      total do nó a que pertence, só contém AP1 a AP5 e não usa a
      categoria SEM AP;
   2. os espelhos em assets/data são idênticos aos cubos dos módulos;
   3. Histórico e Linha do Tempo conciliam AP com os cubos;
   4. data-cutoff.json declara cobertura integral coerente com o cubo;
   5. valores protegidos da regularização AGO/2026 (registro DIM-01).

   A cascata territorial da Linha do Tempo é coberta por
   testes/testar-cascata-territorial.js (registro CAS-01).

   Somente leitura: não escreve em disco e não acessa rede.
   ============================================================ */
"use strict";

var fs = require("fs");
var path = require("path");
var vm = require("vm");

var raiz = process.argv[2];
if (!raiz) {
  console.error("Uso: node testes/testar-cobertura-ap.js <raiz-do-repositorio>");
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
function carregarGlobal(rel, nome) {
  var ctx = { window: {} };
  vm.runInNewContext(ler(rel), ctx, { filename: rel });
  return ctx.window[nome];
}
function percorrer(o, caminho, fn) {
  if (Array.isArray(o)) { o.forEach(function (x, i) { percorrer(x, caminho + "/" + i, fn); }); return; }
  if (!o || typeof o !== "object") return;
  fn(o, caminho);
  Object.keys(o).forEach(function (k) { percorrer(o[k], caminho + "/" + k, fn); });
}
var APS_VALIDAS = { AP1: 1, AP2: 1, AP3: 1, AP4: 1, AP5: 1 };
function soma(lista, campo) { return lista.reduce(function (t, x) { return t + (x[campo] || 0); }, 0); }
function apDe(lista, nome) { return (lista || []).filter(function (x) { return x.nome === nome; })[0]; }

var MODULOS = [
  { pasta: "chamados-1746", cubo: "chamados_cube.js", global: "CHAMADOS_CUBE", prefixo: "c",
    ap3: { v2025: 88037, v2026: 99580 }, realocado: { 2025: 478, 2026: 701 } },
  { pasta: "ouvidoria", cubo: "ouvidoria_cube.js", global: "OUVIDORIA_CUBE", prefixo: "o",
    ap3: { v2025: 10443, v2026: 11729 }, realocado: { 2025: 74, 2026: 116 } }
];
var cubos = {};

/* ---------- 1 · cubos ---------- */
MODULOS.forEach(function (mod) {
  grupo(mod.pasta + " · toda lista de AP concilia com o total do nó");
  var cubo = carregarGlobal(mod.pasta + "/" + mod.cubo, mod.global);
  cubos[mod.pasta] = cubo;
  verdadeiro("Cubo carregado", !!(cubo && cubo.periods));
  if (!cubo || !cubo.periods) return;
  var nos = 0, divergentes = [], invalidas = [];
  percorrer(cubo, "", function (o, c) {
    if (!Array.isArray(o.ap) || !("total2026" in o)) return;
    nos++;
    if (soma(o.ap, "v2026") !== o.total2026 || soma(o.ap, "v2025") !== o.total2025) divergentes.push(c);
    o.ap.forEach(function (x) { if (!APS_VALIDAS[x.nome]) invalidas.push(c + " → " + x.nome); });
  });
  verdadeiro("Há listas de AP no cubo", nos > 0, nos);
  caso("Nenhuma lista de AP com soma diferente do total (2025 e 2026)", divergentes, []);
  caso("Somente AP1 a AP5 como categoria de AP", invalidas, []);
  verdadeiro("Rótulo SEM AP ausente do cubo", ler(mod.pasta + "/" + mod.cubo).indexOf("SEM AP") < 0);
});

/* ---------- 2 · espelhos ---------- */
grupo("Espelhos em assets/data idênticos aos cubos dos módulos");
MODULOS.forEach(function (mod) {
  var espelho = "assets/data/" + mod.pasta + "/" + mod.cubo;
  verdadeiro(espelho + " idêntico a " + mod.pasta + "/" + mod.cubo,
    fs.existsSync(path.join(raiz, espelho)) && ler(espelho) === ler(mod.pasta + "/" + mod.cubo));
});

/* ---------- 3 · Histórico e Linha do Tempo ---------- */
[
  { rel: "1746-historico/data.js", global: "HIST1746_V4", acumulado: function (d) { return d.periods.accumulated.aps; }, agosto: function (d) { return d.periods.august.aps; } },
  { rel: "1746-timeline/data.js", global: "TIMELINE1746_DATA", acumulado: function (d) { return d.accumulated.aps; }, agosto: function (d) { return d.periods.august.aps; } }
].forEach(function (pag) {
  grupo(pag.rel + " · AP concilia com os cubos");
  var d = carregarGlobal(pag.rel, pag.global);
  verdadeiro("Dados carregados", !!d);
  if (!d) return;
  verdadeiro("Rótulo SEM AP ausente", ler(pag.rel).indexOf("SEM AP") < 0);
  var acc = pag.acumulado(d) || [];
  MODULOS.forEach(function (mod) {
    var cubo = cubos[mod.pasta];
    if (!cubo) return;
    var all = cubo.periods.acumulado.all, p = mod.prefixo;
    caso(mod.pasta + " · soma das APs 2025 = total do cubo", soma(acc, p + "2025"), all.total2025);
    caso(mod.pasta + " · soma das APs 2026 = total do cubo", soma(acc, p + "2026"), all.total2026);
    Object.keys(APS_VALIDAS).forEach(function (ap) {
      var a = apDe(acc, ap) || {}, b = apDe(all.ap, ap) || {};
      caso(mod.pasta + " · " + ap + " igual ao cubo", [a[p + "2025"], a[p + "2026"]], [b.v2025, b.v2026]);
    });
  });
  var ago = pag.agosto(d) || [];
  caso("Agosto · AP3 de Chamados igual à base auditável fechada AGO/2026", [apDe(ago, "AP3").c2025, apDe(ago, "AP3").c2026], [8446, 11033]);
  caso("Agosto · AP3 de Ouvidoria igual à base auditável fechada AGO/2026", [apDe(ago, "AP3").o2025, apDe(ago, "AP3").o2026], [844, 1177]);
  caso("Agosto · soma das APs de Chamados = total de agosto", [soma(ago, "c2025"), soma(ago, "c2026")], [21764, 29605]);
  caso("Agosto · soma das APs de Ouvidoria = total de agosto", [soma(ago, "o2025"), soma(ago, "o2026")], [2005, 3254]);
});

/* ---------- 4 e 5 · data-cutoff.json e valores protegidos ---------- */
MODULOS.forEach(function (mod) {
  grupo(mod.pasta + " · data-cutoff.json e valores protegidos da realocação AGO/2026");
  var corte = JSON.parse(ler(mod.pasta + "/data-cutoff.json"));
  var cubo = cubos[mod.pasta];
  if (!cubo) return;
  var all = cubo.periods.acumulado.all, q = corte.qualidade || {}, acc = q.area_planejamento_acumulado || {};
  ["2025", "2026"].forEach(function (ano) {
    var a = acc[ano] || {};
    caso("Acumulado " + ano + " · total declarado = cubo", a.total, all["total" + ano]);
    caso("Acumulado " + ano + " · sem classificação = 0", a.sem_classificacao, 0);
    caso("Acumulado " + ano + " · cobertura 100%", a.cobertura_percentual, 100);
  });
  var r = q.regularizacao_ap_agosto || {};
  caso("Registro de regularização declara destino AP3", r.destino, "AP3");
  caso("Registro de regularização declara totais inalterados", r.totais_alterados, false);
  caso("Quantidades regularizadas declaradas", [r.quantidade_2025, r.quantidade_2026], [mod.realocado[2025], mod.realocado[2026]]);
  var ap3 = apDe(all.ap, "AP3") || {};
  caso("AP3 acumulado protegido (2025, 2026)", [ap3.v2025, ap3.v2026], [mod.ap3.v2025, mod.ap3.v2026]);
});

/* ---------- relatório ---------- */
grupos.forEach(function (g) {
  console.log("== " + g.nome + " ==");
  g.casos.forEach(function (c) {
    console.log("  [" + (c.ok ? "PASSOU" : "FALHOU") + "] " + c.nome + (c.ok ? "" : " · obtido: " + JSON.stringify(c.obtido) + " · esperado: " + JSON.stringify(c.esperado)));
  });
});
console.log("TOTAL: " + (totais.pass + totais.fail) + " casos | APROVADOS: " + totais.pass + " | REPROVADOS: " + totais.fail);
process.exit(totais.fail ? 1 : 0);
