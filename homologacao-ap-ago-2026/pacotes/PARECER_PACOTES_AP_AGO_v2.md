# Parecer v2 — pacotes DIM-01, CAS-01 e TST-01

Data: 19/10/2026
Base: `urbanflowrio/COMLURB`, commit `3b41330` (16/10/2026)
Substitui o parecer v1 (`PARECER_AJUSTE_AP_AGO.md`, pacote único).
Situação: nada publicado. Os três pacotes aguardam aceite independente e homologação visual no COMLURB-TESTES.

## O que mudou em relação à v1

1. **Natureza do ajuste corrigida.** A v1 dizia que a AP3 "já constava da base fechada". A revisão independente recuperou as versões de 04/09/2026 das duas bases e mostrou o contrário: no fechamento original, essas linhas tinham AP `Nulo`, vazia ou `SEM AP`. A AP3 foi preenchida depois de 04/09. O ajuste passa a ser documentado como **regularização posterior da classificação**, e não como recuperação.
2. **Bairros identificados.** Os bairros vieram da revisão independente e foram conferidos por mim contra a base atual:
   - **Chamados:** Engenho Novo, Riachuelo, Rocha, Jacaré, Sampaio e São Francisco Xavier. Somam exatamente 701 em 2026 e 478 em 2025.
   - **Ouvidoria:** os mesmos seis, mais Bonsucesso. Somam exatamente 116 em 2026 e 74 em 2025.
   - A composição por tipo desses bairros reproduz, tipo a tipo, a diferença de AP3 do cubo de agosto.
   - Todos são AP3 no GeoJSON oficial.
3. **Entregas separadas:**
   - **DIM-01:** regularização de AP de agosto.
   - **CAS-01:** grafia de Braz de Pina e Oswaldo Cruz na cascata.
   - **TST-01:** inclusão dos dois testes no `npm test`.
4. **Errata** das Leituras Executivas de agosto incluída no DIM-01.

## Pacotes

| Pacote | Arquivos | Depende de | Pode homologar isolado? |
|---|---|---|---|
| **DIM-01** · regularização de AP de agosto | 18 | — | Sim |
| **CAS-01** · cascata territorial | 3 | — | Sim |
| **TST-01** · testes no `npm test` | 3 | DIM-01 e CAS-01 | Não. Aplicar por último |

DIM-01 e CAS-01 **não têm nenhum arquivo em comum**. Podem ser aplicados e homologados em qualquer ordem.

### DIM-01 — `CHA-2026-10-19-DIM-01` e `OUV-2026-10-19-DIM-01`

**Alteração**
- `SEM AP (AGO)` → AP3 em todas as listas de AP dos dois cubos: 34 listas em Chamados e 26 em Ouvidoria. As fórmulas do cubo foram conferidas em 100% dos nós antes da alteração.
- Mesmo ajuste nos espelhos em `assets/data`, no Histórico e na Linha do Tempo (`data.js`).
- `index.html`: só o parâmetro de cache dos scripts.
- `data-cutoff.json`: novo bloco `regularizacao_ap_agosto`, com natureza, estado no fechamento original, estado atual, critério, bairros e pendência.
- Documentação: `HOMOLOGACAO_TECNICA.md`, READMEs, matriz de módulos e baseline.

**Resultado no acumulado Jan–Set, AP3**

| | Antes | Depois |
|---|---:|---:|
| Chamados 2025 | 87.559 | 88.037 |
| Chamados 2026 | 98.879 | 99.580 |
| Ouvidoria 2025 | 10.369 | 10.443 |
| Ouvidoria 2026 | 11.613 | 11.729 |

Totais inalterados.

**Testes**
- `testes/testar-cobertura-ap.js`: 72/72 aprovados após o ajuste. Com os dados de `3b41330`, reprova 26 casos.
- Regressão `npm test`: 668/668.

**Pendência registrada:** autor e data exata do preenchimento da AP3 na planilha (histórico de versões).

### CAS-01 — `CAS-2026-10-19-01`

**Alteração**
- Em `cascade_data.js`, só os campos `ap` e `gerencia` de BRAZ DE PINA (→ AP3/NG11P) e OSWALDO CRUZ (→ AP3/NG15H), em 167 linhas.
- Regra aplicada: a mesma dos outros 159 bairros, todos iguais ao GeoJSON.
- Quantidades e estrutura idênticas, conferidas campo a campo.

**Testes**
- `testes/testar-cascata-territorial.js`: 12/12 aprovados após o ajuste. Com os dados de `3b41330`, reprova 6 casos.
- O teste confere AP e gerência de **todos** os bairros contra o GeoJSON, com a equivalência de grafia declarada no próprio teste.
- Regressão `npm test`: 668/668.

**Documentação:** registro em `1746-timeline/README.md`. Ele não toca o `BASELINE_HOMOLOGACAO.md`, para manter o pacote independente. A linha da baseline deve ser registrada após o aceite.

### TST-01 — `TST-2026-10-19-01`

**Alteração**
- `package.json`: scripts `test:cobertura-ap` e `test:cascata-territorial`, incluídos em `test:regression`.
- `testes/testar-fase7b.js`: hash protegido de `package.json` passa de `1b742c37…` para `5670e553…`. O hash anterior fica registrado em comentário, no mesmo padrão já usado no pacote de confiabilidade 1.
- Linha nova em `BASELINE_HOMOLOGACAO.md`.

**Testes:** `npm test` com DIM-01 + CAS-01 + TST-01 dá 752/752 (668 + 72 + 12).

## Observações para quem for executar

- O `npm test` regrava `engenharia-operacional/piloto/saida-canonica-exemplo.json`, que é um arquivo versionado. O comportamento já existia. Restaure o arquivo antes de commitar.
- Não há workflow de regressão configurado no COMLURB-TESTES. Rode `npm ci && npm test` localmente ou configure o workflow antes de usar como evidência.

## Sequência sugerida

1. Aceite independente deste parecer e dos `diff.patch` de cada pacote.
2. Aplicar DIM-01 e CAS-01 no COMLURB-TESTES e conferir visualmente:
   - DIM-01: gráfico de AP de Chamados e Ouvidoria, Histórico e Linha do Tempo.
   - CAS-01: cascata da Linha do Tempo, navegando AP3 → NG11P → Braz de Pina e AP3 → NG15H → Oswaldo Cruz.
3. Aplicar TST-01 e rodar `npm test`.
4. Publicar no COMLURB e registrar os aceites na baseline.
5. Circular a errata de agosto.

## Conteúdo

```
DIM-01/  arquivos/  ferramentas/  evidencias/  ERRATA_LEITURA_EXECUTIVA_AGO26.md
CAS-01/  arquivos/  ferramentas/  evidencias/
TST-01/  arquivos/  evidencias/
```

Cada `evidencias/` contém:
- `diff.patch`
- `manifesto-sha256.md`
- `arquivos-alterados.txt`
- saídas dos testes antes e depois
- regressão completa
