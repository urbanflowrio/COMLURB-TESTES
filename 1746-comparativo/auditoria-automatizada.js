const fs=require('fs');const vm=require('vm');const path=require('path');const root=__dirname;const ctx={window:{}};vm.createContext(ctx);
for(const file of ['chamados_cube.js','populacao_ibge_2022.js'])vm.runInContext(fs.readFileSync(path.join(root,file),'utf8'),ctx,{filename:file});
const cube=ctx.window.CHAMADOS_CUBE;const pop=ctx.window.POP_BAIRROS_CENSO_2022;const html=fs.readFileSync(path.join(root,'index.html'),'utf8');
function ok(x,label){if(!x)throw Error(label);console.log('OK',label)}
console.log('Cubo:',Object.keys(cube));console.log('Pop:',pop?.registros?.length);
ok(!!cube&&!!pop&&Array.isArray(pop.registros),'ambas as bases carregam');
ok(html.includes('src="./chamados_cube.js"')&&html.includes('src="./populacao_ibge_2022.js"'),'scripts locais');
ok(html.includes("fetch('./data-cutoff.json'"),'corte local');
const acc=cube.periods?.acumulado?.all;ok(!!acc,'acumulado presente');
ok(acc.total2025===224004&&acc.total2026===254772,'totais acumulados oficiais');
const cut=JSON.parse(fs.readFileSync(path.join(root,'data-cutoff.json'),'utf8'));ok(!!cut&&typeof cut==='object','corte JSON valido');
console.log('VALIDACAO DO COMPARATIVO CONCLUIDA');
