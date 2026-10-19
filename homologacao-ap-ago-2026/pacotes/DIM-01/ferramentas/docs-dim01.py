import json, hashlib
def sha(p): return hashlib.sha256(open(p,'rb').read()).hexdigest()
def rep(p, old, new, count=1):
    s=open(p,encoding='utf-8').read()
    assert s.count(old)==count, (p, old[:70], s.count(old))
    open(p,'w',encoding='utf-8').write(s.replace(old,new))
BAIRROS_CHA="Engenho Novo 327, Riachuelo 109, Rocha 82, Jacaré 70, Sampaio 67, São Francisco Xavier 46"
BAIRROS_OUV="Engenho Novo 50, Jacaré 17, Bonsucesso 14, Riachuelo 11, Sampaio 10, Rocha 7, São Francisco Xavier 7"
# data-cutoff
def upd(f, mod, n25, n26, chave_conc, reg, bairros):
    d=json.load(open(f,encoding='utf-8')); q=d['qualidade']
    q[chave_conc]=(("Conciliação dos totais oficiais preservada. " if mod=='cha' else "Conciliação dos totais operacionais preservada. ")+
       "Cobertura integral de AP no acumulado desde 19/10/2026: os registros de agosto antes exibidos como SEM AP (AGO) foram regularizados em AP3 (registro "+reg+"). A AP3 foi atribuída por bairro após o fechamento de 04/09/2026; totais inalterados.")
    q['tratamento_interface']="Setembro e acumulado possuem cobertura integral de AP. Não há categoria SEM AP na interface."
    for ano,n in (('2025',n25),('2026',n26)):
        a=q['area_planejamento_acumulado'][ano]; assert a['sem_classificacao']==n
        a['classificados']=a['total']; a['sem_classificacao']=0; a['cobertura_percentual']=100.0
    q['regularizacao_ap_agosto']={
        "registro": reg, "data": "2026-10-19", "competencia_afetada": "2026-08",
        "natureza": "Regularização posterior da classificação de AP. Não é recuperação de classificação existente no fechamento original nem revisão retroativa da fonte.",
        "estado_no_fechamento_original": "Versão de 04/09/2026 da base auditável AGO/2026: AP nula (Nulo, vazia ou SEM AP) nessas linhas",
        "estado_atual_da_base": "Base auditável AGO/2026 com AP3 preenchida nessas linhas, edição posterior a 04/09/2026",
        "criterio": "AP do bairro no GeoJSON oficial DLU_Novos_Bairros_estrutura2025 (todos os bairros envolvidos pertencem à AP3)",
        "bairros_2026": bairros,
        "destino": "AP3", "quantidade_2025": n25, "quantidade_2026": n26, "totais_alterados": False,
        "pendente": "Identificar autor e data exata do preenchimento no histórico de versões da planilha"
    }
    open(f,'w',encoding='utf-8').write(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
upd('chamados-1746/data-cutoff.json','cha',478,701,'conciliacao_totais','CHA-2026-10-19-DIM-01',BAIRROS_CHA)
upd('ouvidoria/data-cutoff.json','ouv',74,116,'conciliacao_interna','OUV-2026-10-19-DIM-01',BAIRROS_OUV)
# READMEs
rep('chamados-1746/README.md',"No acumulado, os registros de agosto sem AP permanecem congelados e são representados como `SEM AP (AGO)`.",
 "No acumulado, a cobertura de AP também é de 100% desde 19/10/2026: os 701 registros de agosto/2026 (478 em agosto/2025) antes exibidos como `SEM AP (AGO)` foram regularizados em AP3 (registro `CHA-2026-10-19-DIM-01`). No fechamento original de 04/09/2026 essas linhas tinham AP nula; a AP3 foi atribuída depois, pelo bairro. Totais inalterados.")
rep('ouvidoria/README.md',"No acumulado, os registros de agosto sem AP permanecem congelados e são representados como `SEM AP (AGO)`.",
 "No acumulado, a cobertura de AP também é de 100% desde 19/10/2026: as 116 manifestações de agosto/2026 (74 em agosto/2025) antes exibidas como `SEM AP (AGO)` foram regularizadas em AP3 (registro `OUV-2026-10-19-DIM-01`). No fechamento original de 04/09/2026 essas linhas tinham AP nula; a AP3 foi atribuída depois, pelo bairro. Totais inalterados.")
rep('1746-historico/README.md',"- Agosto × AP mantém `SEM AP (AGO)` como resíduo explícito.",
 "- Agosto × AP: o antigo resíduo `SEM AP (AGO)` foi regularizado em AP3 em 19/10/2026 (`CHA-2026-10-19-DIM-01` e `OUV-2026-10-19-DIM-01`). No fechamento original essas linhas tinham AP nula; a AP3 foi atribuída depois, pelo bairro. Totais inalterados.")
rep('MATRIZ_OFICIAL_MODULOS.md',"AP histórica de agosto representada por `SEM AP (AGO)`. Subtipos de PAPELEIRA",
 "AP de agosto regularizada em AP3 em 19/10/2026 (`CHA-2026-10-19-DIM-01`, atribuição posterior ao fechamento); cobertura de AP 100%. Subtipos de PAPELEIRA")
rep('MATRIZ_OFICIAL_MODULOS.md',"AP histórica de agosto representada por `SEM AP (AGO)`. PCO mantido",
 "AP de agosto regularizada em AP3 em 19/10/2026 (`OUV-2026-10-19-DIM-01`, atribuição posterior ao fechamento); cobertura de AP 100%. PCO mantido")
rep('MATRIZ_OFICIAL_MODULOS.md',"| Correções pós-auditoria executadas. Nova auditoria independente pendente |",
 "| Correções pós-auditoria executadas. Regularização de AP de 19/10/2026 executada, aceite independente pendente |",2)
s=open('BASELINE_HOMOLOGACAO.md',encoding='utf-8').read()
i=s.index("| 05/10/2026 | Ouvidoria | `OUV-2026-10-05-TEC-01` |"); j=s.index('\n',i)+1
novas=("| 19/10/2026 | Chamados 1746 | `CHA-2026-10-19-DIM-01` | Set/2026. Corte em 05/10/2026 (inalterado) | Regularização de AP: `SEM AP (AGO)` → AP3 (478 em 2025; 701 em 2026), linhas com AP nula no fechamento de 04/09/2026 e AP3 atribuída depois por bairro (6 bairros, todos AP3 no GeoJSON oficial); totais inalterados; teste `testes/testar-cobertura-ap.js` | Greicy Moreira | Executado. Aceite independente pendente |\n"
       "| 19/10/2026 | Ouvidoria | `OUV-2026-10-19-DIM-01` | Set/2026. Corte em 05/10/2026 (inalterado) | Regularização de AP: `SEM AP (AGO)` → AP3 (74 em 2025; 116 em 2026), linhas com AP nula no fechamento de 04/09/2026 e AP3 atribuída depois por bairro (7 bairros, todos AP3 no GeoJSON oficial); totais e PCO inalterados; teste `testes/testar-cobertura-ap.js` | Greicy Moreira | Executado. Aceite independente pendente |\n")
open('BASELINE_HOMOLOGACAO.md','w',encoding='utf-8').write(s[:j]+novas+s[j:])
def registro(mod):
    if mod=='cha':
        p='chamados-1746'; ident='CHA-2026-10-19-DIM-01'; prev='CHA-2026-10-05-TEC-01'; cubo='chamados_cube.js'; data='chamados_data.js'
        tab=[("Acumulado 2025","87.559","478","88.037"),("Acumulado 2026","98.879","701","99.580"),("Agosto 2025","7.968","478","8.446"),("Agosto 2026","10.332","701","11.033")]
        nos='34'; base_tot='29.605 (agosto/2026) e 21.764 (agosto/2025)'; commit='9e886d1'
        comp="Limpeza 357, Remoção gratuita 184, Coleta domiciliar 70, Manejo arbóreo 56, Vetores 31, Fiscalização de grande gerador 1, Remoção de carcaça 1, Remoção gratuita transferência 1"
        bairros="| Engenho Novo | CG13M | 240 | 327 |\n| Riachuelo | CG13M | 75 | 109 |\n| Rocha | CG13M | 49 | 82 |\n| Jacaré | CG12I | 45 | 70 |\n| Sampaio | CG13M | 28 | 67 |\n| São Francisco Xavier | CG13M | 41 | 46 |\n| **Total** | | **478** | **701** |"
        nulo="`Nulo`"; extra=""
    else:
        p='ouvidoria'; ident='OUV-2026-10-19-DIM-01'; prev='OUV-2026-10-05-TEC-01'; cubo='ouvidoria_cube.js'; data='ouvidoria_data.js'
        tab=[("Acumulado 2025","10.369","74","10.443"),("Acumulado 2026","11.613","116","11.729"),("Agosto 2025","770","74","844"),("Agosto 2026","1.061","116","1.177")]
        nos='26'; base_tot='3.254 (agosto/2026) e 2.005 (agosto/2025)'; commit='82f486c'
        comp="Limpeza 95, Remoção gratuita 10, Coleta domiciliar 6, Manejo arbóreo 5"
        bairros="| Engenho Novo | CG13M | 29 | 50 |\n| Jacaré | CG12I | 5 | 17 |\n| Bonsucesso | CG10R | 16 | 14 |\n| Riachuelo | CG13M | 11 | 11 |\n| Sampaio | CG13M | 3 | 10 |\n| Rocha | CG13M | 7 | 7 |\n| São Francisco Xavier | CG13M | 3 | 7 |\n| **Total** | | **74** | **116** |"
        nulo="vazia, `Nulo` ou `SEM AP`"; extra="- PCO inalterado: a regularização atua somente na camada operacional já publicada.\n"
    t="\n".join(f"| {a} | {b} | +{c} | {d} |" for a,b,c,d in tab)
    return f"""

---

# Registro de regularização de AP — 19/10/2026

Identificação: `{ident}`.

Este registro **não é nova competência, não é revisão retroativa da fonte e não é recuperação de uma classificação que existia no fechamento original**. É a **regularização posterior** da AP de linhas que, no fechamento de agosto, estavam sem AP. Nenhum total muda. Substitui a ressalva de AP de agosto registrada em `{prev}`.

## Evidência

- **Fechamento original (04/09/2026):** na versão de 04/09/2026 da base auditável AGO/2026 (histórico de versões do Google Sheets, recuperado na revisão independente), essas linhas tinham AP {nulo}. As quantidades sem AP coincidem exatamente com o `SEM AP (AGO)` dos cubos.
- **Cubo de agosto (commit `{commit}`, 04/09/2026):** a AP3 de agosto saiu sem essas linhas, coerente com a base daquela data.
- **Base atual:** em edição posterior a 04/09/2026, a planilha passou a ter AP3 nessas linhas. A soma por AP fecha com o total oficial ({base_tot}). Autor e data exata dessa edição: **a identificar no histórico de versões**.
- **Critério territorial:** todos os bairros envolvidos pertencem à AP3 no GeoJSON oficial `assets/geojson/DLU_Novos_Bairros_estrutura2025.geojson`. Em toda a base, cada bairro tem uma única AP, igual à do GeoJSON.
- **Leitura Executiva de agosto/2026:** o PDF publicou o acumulado por AP com essa diferença. Errata recomendada em separado.

## Linhas regularizadas (agosto, por bairro)

| Bairro | Gerência regional | 2025 | 2026 |
|---|---|---:|---:|
{bairros}

Composição por tipo em 2026: {comp}. A soma desses bairros na base atual reproduz exatamente, tipo a tipo, a diferença de AP3 do cubo de agosto.

## Alteração

| Recorte | AP3 antes | Regularizado | AP3 depois |
|---|---:|---:|---:|
{t}

- `{cubo}`: {nos} listas de AP ajustadas (acumulado geral, por tipo e por tipo × subtipo). Os campos `dif`, `var`, `contrib` e `part` de AP3 foram recalculados com as fórmulas do próprio cubo, e a categoria `SEM AP (AGO)` foi removida.
- `assets/data/{p}/{cubo}`: espelho atualizado por cópia idêntica.
- `1746-historico/data.js` e `1746-timeline/data.js`: linhas de AP de agosto e do acumulado ajustadas, com a taxa por 1.000 chamados recalculada.
- `index.html`: somente o parâmetro de cache dos scripts de dados (`?v=20261005` → `?v=20261019`).
- `data-cutoff.json`: cobertura de AP no acumulado = 100% e bloco `regularizacao_ap_agosto`.
{extra}
## Verificação

- totais, séries mensais, tipos, subtipos, gerências e bairros idênticos antes e depois;
- em todas as listas de AP do cubo, soma = total do nó (2025 e 2026);
- agosto em Histórico e Linha do Tempo igual à base auditável atual nas 5 APs, nos dois anos;
- teste `testes/testar-cobertura-ap.js`: aprovado após o ajuste e reprovado com os dados anteriores.

## Integridade dos arquivos após a regularização

| Arquivo | SHA-256 |
|---|---|
| `index.html` | `{sha(p+'/index.html')}` |
| `{data}` | `{sha(p+'/'+data)}` |
| `{cubo}` | `{sha(p+'/'+cubo)}` |
| `data-cutoff.json` | `{sha(p+'/data-cutoff.json')}` |

Status deste registro: executado; aceite técnico independente pendente; validação visual publicada pendente; autoria da edição posterior da base pendente de identificação.
"""
for m,p in (('cha','chamados-1746'),('ouv','ouvidoria')):
    f=p+'/HOMOLOGACAO_TECNICA.md'; s=open(f,encoding='utf-8').read().rstrip('\n')+'\n'
    open(f,'w',encoding='utf-8').write(s+registro(m))
