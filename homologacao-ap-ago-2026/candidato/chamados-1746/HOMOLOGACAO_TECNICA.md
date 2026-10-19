# Chamados 1746 | Homologação técnica

Identificação: `CHA-2026-09-15-TEC-01`.

## Escopo

- competência mais recente: agosto/2026;
- data de corte: 04/09/2026;
- histórico congelado até julho/2026;
- fonte analítica: `chamados_cube.js`;
- fonte geográfica: `chamados_data.js`.

## Resultado

Homologação técnica aprovada com ressalva de cobertura da dimensão Área de Planejamento em agosto. A validação visual no endereço publicado, em desktop e celular, permanece pendente.

## Totais protegidos

| Período | 2025 | 2026 | Diferença | Variação |
|---|---:|---:|---:|---:|
| Janeiro a agosto | 202.728 | 230.077 | 27.349 | 13,49% |
| Agosto | 21.764 | 29.605 | 7.841 | 36,03% |

## Verificações executadas

- 114 conciliações internas aprovadas, sem reprovação;
- totais gerais conciliados com séries mensais;
- tipos conciliados com o total geral;
- subtipos conciliados com os respectivos tipos;
- gerências e bairros conciliados com os totais;
- sintaxe dos arquivos JavaScript e dos scripts internos aprovada;
- botão Home presente e apontando para `../index.html`;
- 12 botões com tipo explícito;
- quatro gráficos com identificação acessível;
- nenhum travessão na interface do módulo;
- redução de movimento respeitada;
- regressão geral do HUB: 604 aprovações e nenhuma reprovação.

## Ressalva de qualidade

A dimensão Área de Planejamento não cobre todos os registros de agosto:

| Competência | Total | Classificados em AP | Sem AP | Cobertura |
|---|---:|---:|---:|---:|
| Agosto/2025 | 21.764 | 21.286 | 478 | 97,80% |
| Agosto/2026 | 29.605 | 28.904 | 701 | 97,63% |

O ranking mensal de AP permanece oculto em agosto para impedir uma leitura incompleta. Essa limitação não altera os totais gerais.

## Mudanças técnicas desta versão

- removidos os agregados antigos e não utilizados de `chamados_data.js`;
- preservados os 215 elementos geográficos usados no mapa;
- mantido `chamados_cube.js` como única origem dos números analíticos;
- substituídos efeitos decorativos por cores sólidas;
- preservados apenas os gradientes funcionais do gráfico de composição e da escala do mapa;
- adicionadas melhorias estáticas de acessibilidade e movimento reduzido;
- números, filtros, competências e regras de negócio não foram alterados.

## Integridade dos arquivos principais

| Arquivo | SHA-256 |
|---|---|
| `index.html` | `32d542d97ab5ccae8054194b82b7933b71beb815e9c0f1765f9e818522fa9649` |
| `chamados_data.js` | `b6a8889e39de9faf590a61d957fa47cb5461cefd8bd5f0cf2afb957a2d68d34b` |
| `chamados_cube.js` | `49a05292371cf5a1a86a410908ce486eb2fa8d46c8762931c00a4fd355f333f4` |
| `data-cutoff.json` | `9068327471277ef97926a024ca4a235d7444fbdcca95e7c1f4852a5aa7870ce4` |

## Critério para homologação final

Após a publicação, testar em desktop e celular: carregamento, Home, alternância entre acumulado e agosto, filtros, drill-down de tipo e subtipo, mapa, tabelas e mensagens de ausência de AP. Registrar aprovador funcional e resultado em `BASELINE_HOMOLOGACAO.md`.


---

# Registro de homologação técnica — SET/2026

Identificação: `CHA-2026-10-05-TEC-01`.

## Escopo

- competência mais recente: setembro/2026;
- data de corte: 05/10/2026;
- histórico congelado até agosto/2026;
- total oficial Set/2026: 24.695;
- acumulado oficial Jan–Set/2026: 254.772;
- fonte analítica: `chamados_cube.js`;
- fonte geográfica: `chamados_data.js`.

## Ressalvas vigentes

- Agosto/2025 (478) e agosto/2026 (701) permanecem sem classificação de AP no histórico congelado e são representados como `SEM AP (AGO)`, sem reclassificação retroativa.
- Os subtipos de PAPELEIRA mudaram de regra de classificação a partir de agosto; a comparação acumulada desses subtipos não é homogênea.
- Por decisão de governança no fechamento SET/2026, `IMPERIAL DE SAO CRISTOVAO` é tratado exclusivamente no join cartográfico como equivalente ao polígono `SAO CRISTOVAO`. O join agrega os volumes de todos os nomes do cubo que apontam para a mesma chave geográfica antes do desenho do mapa; o nome oficial do cubo não é alterado. Cobertura cartográfica: 100%.
- Datas de corte individuais de Jan–Jul/2026 não foram localizadas na documentação disponível e permanecem `NÃO RASTREADO` na base auditável.

## Integridade dos arquivos principais após correção pós-auditoria

| Arquivo | SHA-256 |
|---|---|
| `index.html` | `fc6d56bfa85b488bdf81b014108a54aa70d3c7190084ccf38a622224c7963713` |
| `chamados_data.js` | `b6a8889e39de9faf590a61d957fa47cb5461cefd8bd5f0cf2afb957a2d68d34b` |
| `chamados_cube.js` | `3e1f33732b76384b00c44a208b0808f6196df34257d5f7531285cee55b08a201` |
| `data-cutoff.json` | `173ba46bba3cd6702e8f8a1a9ae9fe2c4c66c9db69d497ba68b17801fbc4940c` |
| Base auditável pós-auditoria | `108745d02b2b60ea7b1d7d3f88b1943a214e527e5989ad36dd5f6bad67a4be0c` |

Status deste registro: correções executadas; aceite técnico independente aprovado — T1 a T10.

---

# Registro de revisão editorial — 08/10/2026

Identificação: `CHA-2026-10-08-EDT-01`.

Registrado em 14/10/2026, após reconciliação com o histórico do repositório. Este registro **não é nova homologação de dados**: documenta uma alteração de redação feita depois de `CHA-2026-10-05-TEC-01` e confirma que ela não afeta resultados.

## Origem

- versão homologada em `CHA-2026-10-05-TEC-01`: commit `7caafd9` (06/10/2026), SHA-256 `fc6d56bfa85b488bdf81b014108a54aa70d3c7190084ccf38a622224c7963713`;
- alteração posterior: commit `6d2ad9f` (08/10/2026), que modificou somente `chamados-1746/index.html` e `ouvidoria/index.html`, 2 linhas em cada.

## Alteração

Redação de dois cartões da leitura executiva, para não atribuir causa a uma participação na variação:

| Antes | Depois |
|---|---|
| Principal motor da mudança | Principal contribuição para a variação |
| Respondeu por X da alta/redução anual | Representou X da variação anual |
| Os dois principais fatores explicam X | As duas principais contribuições representam X |
| Explicou X da variação acumulada | Representou X da variação acumulada |

## Verificação

- cálculos exibidos idênticos antes e depois: `pct(shareOfMovement(a.dif, x.dif))`, `signed(a.dif)`, `pct(combined)`, `fmt(x.total2026)`, `pctSigned(x.var)`;
- única expressão removida: a escolha da palavra "alta" ou "redução";
- nenhuma alteração de cálculo, filtro, classificação, AP, gerência, bairro, alias cartográfico ou PCO;
- cubo, GeoJSON e `data-cutoff.json` inalterados (hashes do registro anterior conferem);
- revisão independente da reconciliação: aprovada.

## Integridade após a revisão editorial

| Arquivo | SHA-256 |
|---|---|
| `index.html` | `96c09524842f6fa300137526e0c3bfb75af72ed9ed5c2cc69b05e5b92cdc7068` |

Os demais arquivos mantêm os hashes do registro `CHA-2026-10-05-TEC-01`. O hash anterior de `index.html` fica preservado acima como histórico.

Status deste registro: revisão editorial documentada; resultados homologados em `CHA-2026-10-05-TEC-01` preservados.

---

## Homologação técnica do Pacote de Confiabilidade 1 — CHA-2026-10-14-TEC-02

Data do registro: 14/10/2026. Referência: `CONF-2026-10-P1`.

- Base editorial preservada: registro `CHA-2026-10-08-EDT-01`.
- Publicação em `main`: commit `2b11b85ac7942546d91c692b2dc9e37f230829a5`.
- Alteração: exibição de competência, data de corte e histórico congelado a partir de `data-cutoff.json`, sem mudança nos cubos ou nas regras oficiais.
- Verificações técnicas: 668 testes aprovados e 0 reprovados, conforme execução independente documentada na preparação do pacote; hashes e lista de sete arquivos conferidos na publicação.
- Evidência visual: captura da página publicada conferida nesta conversa (desktop); confirmação da usuária de funcionamento no celular, em 14/10/2026. Totais na tela mantidos.
- Limite do aceite: a confirmação de navegação móvel é declarada pela usuária; não representa nova conferência dos dados brutos nem inspeção de todos os filtros individualmente.

| Arquivo | SHA-256 do P1 |
|---|---|
| `index.html` | `aa3ff3ee2886dbd28fb671ed97c1d1c1c9c9851c6ccd0002df0f9b2aac4e8979` |

Resultado: **aceite técnico e visual do escopo P1 registrado**. O histórico de homologação anterior permanece válido; esta seção documenta exclusivamente as modificações de confiabilidade do P1.


---

# Registro de regularização de AP — 19/10/2026

Identificação: `CHA-2026-10-19-DIM-01`.

Este registro **não é nova competência, não é revisão retroativa da fonte e não é recuperação de uma classificação que existia no fechamento original**. É a **regularização posterior** da AP de linhas que, no fechamento de agosto, estavam sem AP. Nenhum total muda. Substitui a ressalva de AP de agosto registrada em `CHA-2026-10-05-TEC-01`.

## Evidência

- **Fechamento original (04/09/2026):** na versão de 04/09/2026 da base auditável AGO/2026 (histórico de versões do Google Sheets, recuperado na revisão independente), essas linhas tinham AP `Nulo`. As quantidades sem AP coincidem exatamente com o `SEM AP (AGO)` dos cubos.
- **Cubo de agosto (commit `9e886d1`, 04/09/2026):** a AP3 de agosto saiu sem essas linhas, coerente com a base daquela data.
- **Base atual:** em edição posterior a 04/09/2026, a planilha passou a ter AP3 nessas linhas. A soma por AP fecha com o total oficial (29.605 (agosto/2026) e 21.764 (agosto/2025)). Autor e data exata dessa edição: **a identificar no histórico de versões**.
- **Critério territorial:** todos os bairros envolvidos pertencem à AP3 no GeoJSON oficial `assets/geojson/DLU_Novos_Bairros_estrutura2025.geojson`. Em toda a base, cada bairro tem uma única AP, igual à do GeoJSON.
- **Leitura Executiva de agosto/2026:** o PDF publicou o acumulado por AP com essa diferença. Errata recomendada em separado.

## Linhas regularizadas (agosto, por bairro)

| Bairro | Gerência regional | 2025 | 2026 |
|---|---|---:|---:|
| Engenho Novo | CG13M | 240 | 327 |
| Riachuelo | CG13M | 75 | 109 |
| Rocha | CG13M | 49 | 82 |
| Jacaré | CG12I | 45 | 70 |
| Sampaio | CG13M | 28 | 67 |
| São Francisco Xavier | CG13M | 41 | 46 |
| **Total** | | **478** | **701** |

Composição por tipo em 2026: Limpeza 357, Remoção gratuita 184, Coleta domiciliar 70, Manejo arbóreo 56, Vetores 31, Fiscalização de grande gerador 1, Remoção de carcaça 1, Remoção gratuita transferência 1. A soma desses bairros na base atual reproduz exatamente, tipo a tipo, a diferença de AP3 do cubo de agosto.

## Alteração

| Recorte | AP3 antes | Regularizado | AP3 depois |
|---|---:|---:|---:|
| Acumulado 2025 | 87.559 | +478 | 88.037 |
| Acumulado 2026 | 98.879 | +701 | 99.580 |
| Agosto 2025 | 7.968 | +478 | 8.446 |
| Agosto 2026 | 10.332 | +701 | 11.033 |

- `chamados_cube.js`: 34 listas de AP ajustadas (acumulado geral, por tipo e por tipo × subtipo). Os campos `dif`, `var`, `contrib` e `part` de AP3 foram recalculados com as fórmulas do próprio cubo, e a categoria `SEM AP (AGO)` foi removida.
- `assets/data/chamados-1746/chamados_cube.js`: espelho atualizado por cópia idêntica.
- `1746-historico/data.js` e `1746-timeline/data.js`: linhas de AP de agosto e do acumulado ajustadas, com a taxa por 1.000 chamados recalculada.
- `index.html`: somente o parâmetro de cache dos scripts de dados (`?v=20261005` → `?v=20261019`).
- `data-cutoff.json`: cobertura de AP no acumulado = 100% e bloco `regularizacao_ap_agosto`.

## Verificação

- totais, séries mensais, tipos, subtipos, gerências e bairros idênticos antes e depois;
- em todas as listas de AP do cubo, soma = total do nó (2025 e 2026);
- agosto em Histórico e Linha do Tempo igual à base auditável atual nas 5 APs, nos dois anos;
- teste `testes/testar-cobertura-ap.js`: aprovado após o ajuste e reprovado com os dados anteriores.

## Integridade dos arquivos após a regularização

| Arquivo | SHA-256 |
|---|---|
| `index.html` | `4048e27c1df8e73becd17d6e05089cdc50ce66fe30a92328a6c4279245d15134` |
| `chamados_data.js` | `b6a8889e39de9faf590a61d957fa47cb5461cefd8bd5f0cf2afb957a2d68d34b` |
| `chamados_cube.js` | `7c56598ff061413a59b245810bcc9cb29139ec36d0d1b5cbdef557ffe25fdd8a` |
| `data-cutoff.json` | `4532f562581a7ca85070c4e87408384d52f87246cf1bd70dc7a8d8725018076b` |

Status deste registro: executado; aceite técnico independente pendente; validação visual publicada pendente; autoria da edição posterior da base pendente de identificação.
