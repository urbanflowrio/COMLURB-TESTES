# Rastreamento de SEM AP (AGO) — 19/10/2026

## Evidências de origem
- Bases Google Sheets da pasta agosto: `BASE AUDITÁVEL CHAMADOS 1746 — FECHAMENTO AGO 2026` e `BASE AUDITÁVEL OUVIDORIAS 1746 — FECHAMENTO AGO 2026`.
- `Controle_Corte`: fechamento 04/09/2026; 1746 fonte `chamados(1).xlsx`; ouvidorias fonte `ouvidorias(5).xlsx`; histórico congelado até julho.
- `Validacao`: 1746 total 29.605 e ouvidorias operacionais 3.254; aceites de fechamento OK.
- Arquivos atuais de governança oficial: `chamados-1746/data-cutoff.json` e `ouvidoria/data-cutoff.json`: apresentam 701 e 116 na categoria `SEM AP (AGO)` no acumulado 2026, sem alteração do total.

## Recontagem das bases de agosto/2026

| AP | Chamados | Ouvidorias operacionais |
|---|---:|---:|
| AP1 | 1.223 | 102 |
| AP2 | 5.306 | 467 |
| AP3 | 11.033 | 1.177 |
| AP4 | 4.636 | 605 |
| AP5 | 7.407 | 903 |
| **Total** | **29.605** | **3.254** |

Nenhum valor sem AP encontrado nas linhas com dados; ouvidorias contabilizadas com `Flag_Operacional=1`. Os valores da base auditável incluem agregações por tipo/subtipo/gerência/bairro, não identificadores transacionais para reconciliação individual.

## Origem da divergência ainda não demonstrada
Não há, nas fontes inspecionadas, trilha que atribua individualmente os 701/116 registros à condição de AP vazia na construção anterior do cubo. Os números foram retidos por decisão explícita de governança no fechamento. A diferença dos agregados não prova que houve erro na origem, nem permite reconstruir com certeza qual AP deveria absorver cada parcela.

## Decisão técnica
- Manter série oficial, regras de PCO e histórico congelado sem alteração.
- Não realizar rateio proporcional nem reatribuição administrativa por geometrias.
- Antes de qualquer retificação, recuperar a base original do gerador da categoria `SEM AP (AGO)` ou um snapshot dimensional de agosto com AP e chaves de conciliação. Conferir ambos os anos (2025 e 2026).
- Tratar eventual versão recalculada por AP como **cenário de revisão**, com reconciliação integral e autorização expressa, não substituição silenciosa do oficial.
- A integração territorial por bairro e AP pode avançar com ressalva visível e leitura separada do cenário auditável.

**Status:** bases auditáveis completas por AP confirmadas; origem exata do `SEM AP` no cubo ainda pendente. Nenhuma alteração no HUB oficial.
