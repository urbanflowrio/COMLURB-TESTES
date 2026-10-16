# Auditoria territorial V4.3.1 — matriz preliminar
Data: 16/10/2026. Ambiente: COMLURB-TESTES, sem alteração da produção.

## Resultado tabular verificável
- DLU: 215 feições, 32 códigos de gerências, 5 feições sem `gerdlu`. Prefixo **C → LRC** aplicado a 7 códigos: CG08T, CG09V, CG10R, CG12I, CG13M, CG13P, CG20G.
- UCV: 6 polígonos de gerência; 260 registros de interseção bairro-gerência; 165 pares distintos bairro/AP; **64 pares bairro/AP com mais de uma gerência intersectada** (contagem por chave nome+AP; não equivale à contagem por nome isolado).
- UCS: 182 feições de bairro. Categorias territoriais (5): SEM GERÊNCIA DEFINIDA (1), UDS-N (91), UDS-O 4 (28), UDS-O 5 (29), UDS-S (33).
- UGU: 182 feições de bairro. Categorias territoriais (5): UGU-B (29), UGU-N (84), UGU-O (BANGU) (11), UGU-O (SANTA CRUZ) (17), UGU-S (41).
- Diferenças de nomes de bairro normalizados (maiúsculas e acentos) entre DLU e UCS: 0. Divergências remanescentes exigem análise individual antes de reconciliar códigos.
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
