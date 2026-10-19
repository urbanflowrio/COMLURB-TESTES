# Reconciliação preliminar de AP — Agosto/2026

Data: 19/10/2026. Ambiente COMLURB-TESTES. Sem alteração nas séries oficiais.

## Fontes
- Drive COMLURB: `BASE AUDITÁVEL CHAMADOS 1746 — FECHAMENTO AGO 2026`, aba `Dados_Mes`, 2.768 linhas com dados; colunas `AP`, `Qtd_Competencia_Atual`.
- Drive COMLURB: `BASE AUDITÁVEL OUVIDORIAS 1746 — FECHAMENTO AGO 2026`, aba `Dados_Mes`; 1.674 linhas com conteúdo, operacional definido como `Flag_Operacional=1` (PCO excluída); colunas `AP`, `Qtd_Competencia_Atual`.
- Repositório oficial: `chamados-1746/HOMOLOGACAO_TECNICA.md`, `ouvidoria/HOMOLOGACAO_TECNICA.md`; cubos canônicos `chamados_cube.js` e `ouvidoria_cube.js`.

## Agosto/2026 — valores da base auditável

| AP | Chamados | Ouvidorias operacionais |
|---|---:|---:|
| AP1 | 1.223 | 102 |
| AP2 | 5.306 | 467 |
| AP3 | 11.033 | 1.177 |
| AP4 | 4.636 | 605 |
| AP5 | 7.407 | 903 |
| **Total** | **29.605** | **3.254** |
| Sem AP na base auditável | 0 | 0 |

## Divergência com o fechamento agregado

A documentação oficial da homologação anterior informa, para agosto/2026:
- Chamados: 28.904 classificados em AP e 701 sem AP (total 29.605).
- Ouvidorias: 3.138 classificados em AP e 116 sem AP (total 3.254).

Os cubos atuais preservam no acumulado as categorias `SEM AP (AGO)` com 701/116, mas os agregados `periods.acumulado.all.ap` não disponibilizam diretamente a distribuição *apenas de agosto* por AP. O detalhamento da base auditável contém AP para todas as linhas da competência e fecha os mesmos totais.

### Controles necessários antes de corrigir
1. Confirmar origem, data e regra que gerou `SEM AP (AGO)` no fechamento agregado original; conferir se houve reclassificação posterior nas bases auditáveis.
2. Extrair as linhas de agosto classificadas como sem AP **na fonte original do cubo**, se disponíveis. Sem identificador estável de registro, não há reconciliação 1:1 garantida.
3. Calcular diferenças originais por AP a partir de fonte que preserve a segmentação de agosto (não estimar rateio).
4. Preservar os valores oficiais, a série histórica congelada e as ressalvas até autorização explícita.
5. Se for aprovada a correção, realizar testes de soma por AP, bairro, tipo, subtipo e gerência, além de 2025/2026; registrar revisão histórica auditável.

**Veredito:** não existe AP não preenchida nas linhas auditáveis analisadas; totais de 2026 conciliados. A origem precisa da divergência de classificação no cubo continua não comprovada. Nenhuma alteração de produção autorizada.
