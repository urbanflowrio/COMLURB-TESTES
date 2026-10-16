import json,csv,collections,pathlib
P=pathlib.Path('inteligencia-territorial')
def js(p):return json.loads(pathlib.Path(p).read_text(encoding='utf-8'))
dlu=js('fonte-oficial/assets/geojson/DLU_Novos_Bairros_estrutura2025.geojson')['features']
ucv=js('fonte-oficial/assets/geojson/GERENCIAS_DSU.geojson')['features']
ucs=js(P/'ucs.geojson')['features'];ugu=js(P/'ugu.geojson')['features']
cross=js(P/'ucv_intersecoes.json')['registros']
def val(f,k):return str(f.get('properties',{}).get(k) or '').strip()
def distinct(fs,k):return sorted(set(val(f,k) for f in fs if val(f,k)))
def rows(fs,k,label):return [{'unidade':label,'codigo_territorial':val(f,k),'bairro':val(f,'nome'),'ap':val(f,'area_plane'),'origem':'GeoJSON bairro SIURB de referência','situacao':'SEM GERÊNCIA DEFINIDA' if 'SEM GERÊNCIA' in val(f,k).upper() else 'Associação territorial por atributo; vigência não confirmada'} for f in fs]
allrows=rows(ucs,'gerencia_12','UCS')+rows(ugu,'gerencia_1','UGU')
allrows.extend({'unidade':'UCV','codigo_territorial':r['gerencia'],'bairro':r['bairro'],'ap':r['ap'],'origem':'Interseção geométrica UCV × bairro','situacao':'INTERSEÇÃO, NÃO RESPONSABILIDADE OFICIAL'} for r in cross)
allrows.extend(rows(dlu,'gerdlu','DLU'))
header=['unidade','codigo_territorial','bairro','ap','origem','situacao']
with (P/'MATRIZ_TERRITORIAL_VALIDACAO.csv').open('w',newline='',encoding='utf-8-sig') as file:
    w=csv.DictWriter(file,fieldnames=header);w.writeheader();w.writerows(allrows)
overlap=collections.defaultdict(set)
for r in cross:overlap[(r['bairro'],r['ap'])].add(r['gerencia'])
multiple={k:v for k,v in overlap.items() if len(v)>1}
with (P/'SOBREPOSICOES_UCV.csv').open('w',newline='',encoding='utf-8-sig') as file:
    w=csv.writer(file);w.writerow(['bairro','ap','quantidade_gerencias','gerencias'])
    for (b,a),groups in sorted(multiple.items()):w.writerow([b,a,len(groups),'; '.join(sorted(groups))])
managers=distinct(dlu,'gerdlu');lrc=[m for m in managers if m.upper().startswith('C')]
no_manager=sum(not val(f,'gerdlu') for f in dlu)
ucscount=collections.Counter(val(f,'gerencia_12') for f in ucs)
ugucount=collections.Counter(val(f,'gerencia_1') for f in ugu)
dlu_bairros=set(val(f,'nome') for f in dlu if val(f,'nome'))
siurb_bairros=set(val(f,'nome') for f in ucs if val(f,'nome'))
different=sorted(dlu_bairros^siurb_bairros)
assert len(ucv)==6 and len(managers)==32,(len(ucv),len(managers))
assert len(ucs)==182 and len(ugu)==182
assert len(cross)==260 and len(overlap)==165
assert len(lrc)>=1
report=f"""# Auditoria territorial V4.3.1 — matriz preliminar
Data: 16/10/2026. Ambiente: COMLURB-TESTES, sem alteração da produção.

## Resultado tabular verificável
- DLU: {len(dlu)} feições, {len(managers)} códigos de gerências, {no_manager} feições sem `gerdlu`. Prefixo **C → LRC** aplicado a {len(lrc)} códigos: {', '.join(lrc)}.
- UCV: {len(ucv)} polígonos de gerência; {len(cross)} registros de interseção bairro-gerência; {len(overlap)} pares distintos bairro/AP; **{len(multiple)} bairros/AP com mais de uma gerência intersectada**.
- UCS: {len(ucs)} feições de bairro. Categorias territoriais ({len(ucscount)}): {', '.join(f'{k} ({v})' for k,v in sorted(ucscount.items()))}.
- UGU: {len(ugu)} feições de bairro. Categorias territoriais ({len(ugucount)}): {', '.join(f'{k} ({v})' for k,v in sorted(ugucount.items()))}.
- Diferenças literais de nomes de bairro entre DLU e UCS: {len(different)}; exigem normalização antes de comparar divergências de gerência.
- A interface UCV usa interseção espacial: **não equivale à atribuição administrativa**; bairro pode intersectar várias gerências.
- `SEM GERÊNCIA DEFINIDA` é categoria pendente de saneamento, e **não uma gerência oficial UCS**.
- Subdivisões UGU constantes em campos territoriais SIURB são códigos de atuação; não presumir que sejam gerências formais.
- UCP/UGT fora do mapa por ausência de geometria validada.

## Restrições da auditoria
1. Esta matriz concilia atributos territoriais dos arquivos disponíveis, **não valida a vigência, atos oficiais nem endereço/nome formal de cada unidade**. A planilha cadastral de unidades deve ser cruzada em etapa posterior.
2. A base DLU histórica diverge do SIURB consolidado: reconciliação anterior apontou **54 bairros com diferenças de gerência e 51 de superintendência**. Essas divergências não foram resolvidas por esta matriz e não devem ser suprimidas nem imputadas.
3. O GeoJSON DLU pode conter feições de nível superior sem `gerdlu`; não contabilizar como gerência ausente.
4. Um filtro visual confirmado no tablet não prova a correção administrativa da atribuição.
5. Arquivos gerados: `MATRIZ_TERRITORIAL_VALIDACAO.csv` e `SOBREPOSICOES_UCV.csv`.

## Decisão
**Validação funcional preliminar das quatro unidades; homologação territorial/administrativa pendente.** Nenhum merge no HUB oficial.
"""
(P/'AUDITORIA_TERRITORIAL_V43.md').write_text(report,encoding='utf-8')
print(report)
