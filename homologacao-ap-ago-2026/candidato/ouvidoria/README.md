# Ouvidoria | HUB COMLURB

Painel executivo interativo das ouvidorias operacionais da COMLURB.

## Escopo

- Comparação jan a set/2026 x jan a set/2025
- Recorte setembro/2026 x setembro/2025
- Análise restrita às ouvidorias operacionais
- Exclusão dos registros tratados internamente pela PCO
- Visão executiva, territorial e analítica
- Drill-down por tipo e subtipo
- Mapa por bairro, com AP e gerência no detalhamento

## Corte e atualização

- Competência mais recente: setembro/2026
- Data de corte deste pacote: 05/10/2026
- Regra histórica: janeiro a agosto permanece congelado conforme os fechamentos anteriores; setembro foi incorporado como nova competência.
- Retificações retroativas devem ser registradas e autorizadas separadamente, sem reprocessamento silencioso do histórico fechado.

## Publicação

O arquivo `index.html` é autônomo e deve ser publicado nesta pasta no GitHub Pages.

URL esperada:

`https://urbanflowrio.github.io/COMLURB/ouvidoria/`

Para atualizar o módulo, publique em conjunto `index.html`, `ouvidoria_data.js`, `ouvidoria_cube.js` e `data-cutoff.json`.

## Arquitetura dos dados

- `ouvidoria_cube.js`: fonte analítica canônica dos totais, séries, tipos, subtipos, gerências, áreas de planejamento e bairros.
- `ouvidoria_data.js`: contém exclusivamente o GeoJSON utilizado pelo mapa.
- `data-cutoff.json`: registra competência, corte, congelamento histórico e ressalvas de qualidade.

## Qualidade conhecida

Os totais e a série operacional oficial de setembro foram preservados. Setembro/2026 possui cobertura de AP de 100%. No acumulado, a cobertura de AP também é de 100% desde 19/10/2026: as 116 manifestações de agosto/2026 (74 em agosto/2025) antes exibidas como `SEM AP (AGO)` foram regularizadas em AP3 (registro `OUV-2026-10-19-DIM-01`). No fechamento original de 04/09/2026 essas linhas tinham AP nula; a AP3 foi atribuída depois, pelo bairro. Totais inalterados. O PCO permanece na base institucional e é excluído somente das análises operacionais. Revisões retroativas permanecem documentadas fora da série oficial.

A exclusão dos registros tratados internamente pela PCO está declarada no escopo, mas não pode ser reexecutada ou auditada somente com os arquivos agregados deste pacote. A comprovação exige a base bruta e a regra de exclusão aplicada.
