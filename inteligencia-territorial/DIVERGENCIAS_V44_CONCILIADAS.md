# V4.4 — Conciliação das divergências territoriais
**Data:** 16/10/2026 · **Ambiente:** COMLURB-TESTES · **Status:** auditoria técnica, sem homologação de mudanças administrativas.

## 1. DLU — 54 divergências de códigos gerenciais

A matriz anterior de reconciliação `matriz_bairros_siurb_hub.csv` (165 bairros, colunas `gerdlu_siurb` e `gerdlu_hub`) foi reavaliada por tipo de diferença:

- **51 casos**: divergência de **código**, conciliável mediante tabela de correspondência entre versões, **sem substituir os códigos oficiais do HUB**.
- **3 casos**: SIURB atribui **mais de uma gerência ao bairro**, enquanto a base histórica do HUB apresenta apenas uma. São conflitos de granularidade territorial e exigem confirmação do critério administrativo/cartográfico.

| Código SIURB | Código no HUB | Situação |
|---|---|---|
| SG08T | CG08T | Equivalência de referência, confirmar vigência |
| SG09V | CG09V | Equivalência de referência, confirmar vigência |
| NG10R | CG10R | Equivalência de referência, confirmar vigência |
| NG12I | CG12I | Equivalência de referência, confirmar vigência |
| NG13M | CG13M | Equivalência de referência, confirmar vigência |
| NG13P | CG13P | Equivalência de referência, confirmar vigência |
| NG20G | CG20G | Equivalência de referência, confirmar vigência |

A regra administrativa confirmada é **código DLU iniciado por C → LRC**. A fonte SIURB registra 51 diferenças de superintendência na comparação histórica; todas ocorrem no subconjunto das 51 diferenças conciliáveis de código. Não recodificar SIURB ou alterar LRC no HUB sem informação de vigência.

### Três bairros cuja atribuição não é unívoca

| Bairro | SIURB (multicódigo) | HUB histórico (código único) | Tratamento |
|---|---|---|---|
| BRAS DE PINA | NG11P; NG14I | NG11P | Manter divergência explícita |
| VILA DA PENHA | NG11P; NG14I | NG14I | Manter divergência explícita |
| VISTA ALEGRE | NG11P; NG14I; NG31V | NG14I | Manter divergência explícita |

**Não escolher por área predominante, não duplicar chamados e não somar territórios automaticamente.**

## 2. UCS — feição sem gerência

**PAQUETA, AP 1** é a única feição identificada no mapa UCS como `SEM GERÊNCIA DEFINIDA`. Conferências cruzadas:
- Na fonte DLU histórica e na matriz SIURB: `SG02C` / `LRS`.
- Na UCV: `UGV-S` por campo SIURB e interseção geométrica (aproximadamente **94,62%** da área de referência do bairro).
- Na UGU: `UGU-S`.
- **Nenhuma dessas atribuições prova qual divisão UCS responde por Paquetá.** Manter `SEM GERÊNCIA DEFINIDA` até confirmação operacional.

## 3. UCS e UGU — manter subdivisões por AP

Conforme decisão expressa da responsável:
- UCS: `UDS-O 4` e `UDS-O 5` são subdivisões por AP do recorte `UDS-O`.
- UGU: `UGU-O (BANGU)` e `UGU-O (SANTA CRUZ)` são subdivisões por AP do recorte `UGU-O`.
- **Preservar exatamente filtros, nomes e geometrias existentes.** Essas subdivisões não são novas gerências administrativas.

## 4. UCV — limites do cruzamento

O cruzamento apresenta 260 registros de interseção e 64 pares bairro/AP com múltiplas gerências. É uma leitura **geométrica**, não uma relação formal de responsabilidade. O drill-down por AP/bairro pode ser usado como exploração territorial, mas não como prova de competência administrativa exclusiva.

## Encaminhamento e critério de aceite

1. DLU: manter tabela de equivalências como **ponte de leitura**, não como substituição de base; resolver separadamente os três bairros multicódigo.
2. UCS: solicitar confirmação operacional da divisão que atende Paquetá; até lá exibir `SEM GERÊNCIA DEFINIDA`.
3. UCV: conservar destaque de bairros como interseção, não atribuição.
4. UCS e UGU: nenhuma alteração nos recortes por AP.
5. **Proibida promoção para `COMLURB/main` com base apenas nesta auditoria**.

Fontes examinadas: cadastro administrativo `ENDERECOS_ATUALIZADOS.xlsx`; matriz entregue `matriz_bairros_siurb_hub.csv`; camadas públicas DLU/UCV; arquivos `ucs.geojson`, `ugu.geojson` e `ucv_intersecoes.json` disponíveis neste repositório de testes.
