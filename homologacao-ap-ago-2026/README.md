# Homologação — AP de agosto/2026 (DIM-01, CAS-01, TST-01)

Ambiente de homologação no **COMLURB-TESTES**. Esta pasta **não altera o HUB oficial**: os módulos em `candidato/` são cópias para conferência visual, e a verificação automática lê o `urbanflowrio/COMLURB` somente no commit base `3b41330`.

## Conteúdo

| Caminho | O que é |
|---|---|
| `pacotes/` | DIM-01, CAS-01 e TST-01 como entregues, com `arquivos/`, `ferramentas/`, `evidencias/` e o parecer v2. |
| `verificar-pacotes.sh` | Verificação automática completa. Detalhes abaixo. |
| `candidato/` | Chamados 1746, Ouvidoria, Histórico 1746 e Linha do Tempo já com DIM-01 + CAS-01, para conferência visual. |
| `../.github/workflows/homologacao-ap-ago-2026.yml` | Roda a verificação no GitHub Actions a cada push nesta pasta, ou manualmente. |

## 1. Verificação automática

O workflow, ou o comando `bash verificar-pacotes.sh pacotes <COMLURB-3b41330> candidato`, confere:

1. **Manifestos:** os hashes "antes" batem com o commit base e os hashes "depois" batem com os arquivos entregues.
2. **Patches:** os patches de DIM-01 e CAS-01 aplicam limpos sobre a base.
3. **Independência:** DIM-01 e CAS-01 não têm arquivo em comum e dão o mesmo resultado em qualquer ordem.
4. **Testes nas combinações:**
   - Na base, cada teste novo reprova, ou seja, detecta o problema.
   - Com o seu pacote, cada teste aprova.
   - Um pacote sozinho não corrige o problema do outro.
5. **Regressão completa:**
   - DIM-01 sozinho: 668.
   - CAS-01 sozinho: 668.
   - DIM-01 + CAS-01 + TST-01: 752.
   - TST-01 sem os outros dois: reprova, o que confirma a dependência.
6. **Invariantes:** nos cubos, só a AP muda. Na cascata, só `ap` e `gerencia` mudam.
7. **Candidato:** cada arquivo de `candidato/` é idêntico ao resultado esperado.

Resultado local em 19/10/2026: **todas as verificações aprovadas, em Node 22 e em Node 20** (o Node 20 é a versão usada no workflow).

## 2. Conferência visual

Endereço, se o GitHub Pages estiver habilitado: `https://urbanflowrio.github.io/COMLURB-TESTES/homologacao-ap-ago-2026/candidato/<módulo>/`

Compare cada tela com a versão oficial publicada. Faça a conferência em **desktop e celular**.

### Chamados 1746 — `candidato/chamados-1746/`
- [ ] Gráfico de AP no acumulado: só AP1 a AP5, sem barra cinza `SEM AP (AGO)`.
- [ ] AP3 no acumulado: **88.037** (2025) e **99.580** (2026).
- [ ] Totais inalterados: **224.004** (2025) e **254.772** (2026).
- [ ] Recorte de setembro inalterado: AP3 **8.748**.
- [ ] Filtros, drill-down de tipo e subtipo e mapa funcionando, com os mesmos números do oficial fora da AP.

### Ouvidoria — `candidato/ouvidoria/`
- [ ] Gráfico de AP sem `SEM AP (AGO)`.
- [ ] AP3 no acumulado: **10.443** (2025) e **11.729** (2026).
- [ ] Totais inalterados: **25.495** (2025) e **30.349** (2026).
- [ ] PCO e camada institucional inalterados.

### Histórico 1746 — `candidato/1746-historico/`
- [ ] Agosto, AP3: chamados **8.446 / 11.033** e ouvidorias **844 / 1.177**.
- [ ] Acumulado, AP3: chamados **88.037 / 99.580**.
- [ ] Nenhuma linha `SEM AP (AGO)`. A matriz de agosto mostra "Taxa válida".

### Linha do Tempo — `candidato/1746-timeline/`
- [ ] AP do acumulado e de agosto sem `SEM AP (AGO)`.
- [ ] Cascata: qualquer serviço → subtipo → **AP3 → NG11P → BRAZ DE PINA**.
- [ ] Cascata: qualquer serviço → subtipo → **AP3 → NG15H → OSWALDO CRUZ**.
- [ ] Nenhuma gerência "NÃO INFORMADA" na cascata.

Nota: o botão Home dos módulos candidatos aponta para a raiz do COMLURB-TESTES.

## 3. Critério de aceite e registro

Os pacotes são aceitos quando todos os itens abaixo estiverem cumpridos:

1. Verificação automática aprovada no Actions, com o log `verificacao-ap-ago-2026` anexado.
2. Conferência visual concluída em desktop e celular.
3. Aceite independente registrado.

Depois disso, com **autorização expressa**, aplique no COMLURB nesta ordem: DIM-01, CAS-01 e TST-01.

Em seguida, registre na tabela "Registro obrigatório de homologação" de `BASELINE_HOMOLOGACAO.md`:

| Data | Módulo | Versão | Competência | Testes executados | Responsável funcional | Aprovador | Resultado |
|---|---|---|---|---|---|---|---|
| __/__/2026 | Chamados 1746 e Ouvidoria | `CHA/OUV-2026-10-19-DIM-01` | Set/2026 | Verificação automática (Actions #__), visual desktop e celular | Greicy Moreira | ________ | Aprovado ou rejeitado |
| __/__/2026 | Linha do Tempo 1746 | `CAS-2026-10-19-01` | Set/2026 | Verificação automática (Actions #__), cascata AP3 → NG11P/NG15H | Greicy Moreira | ________ | Aprovado ou rejeitado |
| __/__/2026 | Regressão HUB | `TST-2026-10-19-01` | Não se aplica | `npm test` com 752 casos | Greicy Moreira | ________ | Aprovado ou rejeitado |

## 4. Pendências conhecidas

- **Autoria da edição posterior:** identificar autor e data exata do preenchimento da AP3 nas bases de agosto. A versão de 04/09/2026 tinha AP nula, e a atual tem AP3.
- **Errata:** circular a errata das Leituras Executivas de agosto/2026, em `pacotes/DIM-01/ERRATA_LEITURA_EXECUTIVA_AGO26.md`.
- **Efeito colateral do `npm test`:** o comando regrava `engenharia-operacional/piloto/saida-canonica-exemplo.json`. Comportamento anterior aos pacotes; restaurar antes de commitar.
- **Depois da publicação oficial**, atualizar no COMLURB-TESTES:
  - textos de `inteligencia-territorial/consulta-integrada-v1.html` e `-v2.html`, que descrevem `SEM AP (AGO)` como vigente. Essas páginas leem os cubos ao vivo do HUB oficial;
  - `inteligencia-territorial/RASTREAMENTO_SEM_AP_AGO2026_V2.md`, que ainda registra a origem como pendente;
  - a cópia local `1746-comparativo/chamados_cube.js`, hoje idêntica ao cubo de `3b41330`. O comparativo não usa AP, então não há efeito numérico, mas a cópia fica desatualizada.
