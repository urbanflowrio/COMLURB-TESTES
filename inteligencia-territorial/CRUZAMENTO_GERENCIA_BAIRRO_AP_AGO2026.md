# Cruzamento da matriz gerencial com bases auditáveis — Agosto/2026

Data: 19/10/2026. Ambiente: COMLURB-TESTES. **Não altera os dados oficiais.**

## Método
Cruzamento por código de gerência + denominação normalizada de bairro + AP das bases auditáveis no Drive COMLURB contra `MATRIZ_TERRITORIAL_VALIDACAO.csv`. Normalização apenas de maiúsculas, acentos e espaços, sem inventar equivalências nominais ou recortes. Ouvidorias: `Flag_Operacional=1`.

## Resultados
| Indicador | 1746 | Ouvidorias |
|---|---:|---:|
| Total da competência | 29.605 | 3.254 |
| Volume com vínculo na matriz e AP coincidente | 16.538 | 2.393 |
| Volume sem par gerência+bairro na matriz | 13.067 | 861 |
| Volume com AP divergente dentre os pares encontrados | 0 | 0 |
| Grupos gerência+bairro+AP distintos | 834 | 556 |
| Grupos com AP coincidente | 397 | 326 |
| Grupos sem correspondência | 437 | 230 |

**Interpretação:** `sem correspondência` não significa `sem AP`. Todas essas linhas têm AP preenchida na base auditável. A matriz de homologação territorial possui associações por atributo cuja vigência ainda não foi confirmada. Códigos de outras unidades ou grafias não coincidentes podem explicar parte dos não encontrados.

## Restrição fundamental
O cubo oficial conserva categorias agregadas `SEM AP (AGO)` de 701 chamados e 116 ouvidorias. Não há, nos dados vistos, identificadores que liguem essas parcelas às linhas auditáveis específicas; portanto não se pode deduzir quais bairros ou gerências compõem essas quantidades nem alterar o histórico por inferência. O cruzamento aqui apresentado verifica coerência dos vínculos encontrados, **não** reconciliação individual da classe SEM AP.

## Encaminhamento rápido
1. Criar tabela de equivalências explícitas e rastreáveis dos códigos e dos bairros para ampliar cobertura.
2. Confrontar a composição agregada da categoria SEM AP da geração original, caso seja recuperável.
3. Exibir separadamente cenário auditável e cenário histórico no protótipo.
4. Não alterar `COMLURB/main`, os polígonos, filtros aprovados ou subdivisões UCS/UGU por AP.

Fonte da matriz: `COMLURB-TESTES/inteligencia-territorial/MATRIZ_TERRITORIAL_VALIDACAO.csv`. Fonte das quantidades: planilhas Google Drive dos fechamentos de agosto de 1746 e Ouvidorias.
