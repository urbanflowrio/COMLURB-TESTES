# 1746 Timeline — V6

Base visual: V4, preservada.
Drill-down: cascata ampla e legível.

Caminho:
Serviço → Subtipo → AP → Gerência → Bairro.

Disponibilidade:
- Jan–Set acumulado: cascata completa.
- Agosto e Setembro: cascata completa.
- Demais meses: a cascata para quando a fonte oficial não sustenta o cruzamento mensal por território.

A taxa é sempre explicada como ouvidorias por 1.000 chamados.


---

## Registro CAS-01 — grafia de bairros na cascata (19/10/2026)

Identificação: `CAS-2026-10-19-01`. Independente do registro de AP de agosto (`CHA-2026-10-19-DIM-01` / `OUV-2026-10-19-DIM-01`).

**Problema.** Na cascata Serviço → Subtipo → AP → Gerência → Bairro, BRAZ DE PINA e OSWALDO CRUZ apareciam como `SEM AP` e gerência `NÃO INFORMADA` em todos os períodos (167 linhas). A causa é a grafia: o GeoJSON oficial `assets/geojson/DLU_Novos_Bairros_estrutura2025.geojson` usa "Brás de Pina" e "Osvaldo Cruz". Os outros 159 bairros da cascata já tinham AP e gerência iguais às do GeoJSON.

**Alteração.** Somente os campos `ap` e `gerencia` dessas linhas em `cascade_data.js`, pela mesma regra dos demais bairros:

| Bairro na cascata | Polígono no GeoJSON | AP | Gerência |
|---|---|---|---|
| BRAZ DE PINA | Brás de Pina | AP3 | NG11P |
| OSWALDO CRUZ | Osvaldo Cruz | AP3 | NG15H |

Quantidades, serviços, subtipos e estrutura da cascata ficaram idênticos (conferido campo a campo, ignorando apenas `ap` e `gerencia`).

**Teste.** `testes/testar-cascata-territorial.js`, com 12 casos: 6 reprovados nos dados anteriores e 12 aprovados após o ajuste. O teste confere que todo bairro tem AP1–AP5 e gerência, que AP e gerência batem com o GeoJSON (com a equivalência de grafia declarada no teste) e que os dois bairros estão corretos.

**Integridade.** `cascade_data.js` antes: `b0f05d6d8b1d619d6f7199bf873901514db8c7c325e7a154881107d298bf582d`; depois: `027db1b2d42aea66fe25c695941496df976a557a72f75f1a0ff6e997c808b5ad`.

Status: executado; aceite independente e conferência visual da cascata pendentes. Registrar em `BASELINE_HOMOLOGACAO.md` após o aceite.
