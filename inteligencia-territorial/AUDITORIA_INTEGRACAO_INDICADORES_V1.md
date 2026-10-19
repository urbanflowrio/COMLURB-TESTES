# Auditoria de integração territorial e indicadores — 19/10/2026

**Ambiente de trabalho:** COMLURB-TESTES. **Origem consultada:** urbanflowrio/COMLURB, branch main, árvore 3b41330fd394b4b6ed2b595f160522d133750f93. **Estado:** diagnóstico arquitetural inicial, sem migração nem alteração de dados.

## 1746

- Fonte canônica dos números: `chamados-1746/chamados_cube.js`; geometria: `chamados-1746/chamados_data.js`; recortes e ressalvas: `chamados-1746/data-cutoff.json`.
- Competência set/2026, corte 05/10/2026. Série jan–ago congelada. AP em agosto/2025 e agosto/2026 com registros sem classificação, rotulados `SEM AP (AGO)`, não reclassificar.
- Alias `IMPERIAL DE SAO CRISTOVAO` → `SAO CRISTOVAO` exclusivamente para junção cartográfica; manter nomes e quantidades originais do cubo.
- Subtipos de PAPELEIRA não são historicamente homogêneos no acumulado.
- Integração segura inicialmente por bairro/AP já disponíveis no cubo, após validação de chave e cobertura; gerência operacional não deve ser recalculada a partir de polígonos.

## Ouvidoria

- Fonte canônica: `ouvidoria/ouvidoria_cube.js`; geometria: `ouvidoria/ouvidoria_data.js`; metadados de corte: `ouvidoria/data-cutoff.json`.
- Set/2026, corte 05/10/2026, histórico anterior congelado; setembro: institucional 2650, PCO 174, operacional 2476; jan–set operacional 30349.
- Exclusão PCO só demonstrada nos agregados publicados; reexecução da exclusão requer base bruta e trilha por competência.
- AP sem classificação em agosto histórico permanece `SEM AP (AGO)`; alias São Cristóvão só em junção geográfica.
- Consultar bairro/AP sem fundir categoria institucional e operacional.

## IPL

- Fontes de produção declaradas no script de `ipl/index.html`. `ipl/app.js` é legado inativo.
- Nota oficial SARC provém da fonte oficial, selecionando `Acumulado` ou o mês; não recalcular a nota histórica com médias simples.
- Diagnóstico por trecho e bairro é **cálculo analítico distinto**. Não transformar prioridade territorial em indicador oficial.
- Pendência de conciliação externa por amostra do SARC, indicação de responsável institucional e validação visual conforme `ipl/HOMOLOGACAO_TECNICA.md`.

## Regras transversais

1. A ligação entre bairro, AP, mapa e gerência precisa ter tipos explícitos: cartográfica, administrativa, operacional.
2. Atribuição gerencial DLU tem pendências de códigos e bairros multicódigo (Brás de Pina, Vila da Penha, Vista Alegre).
3. UCV possui interseções geográficas, não responsabilidade exclusiva; UCS/Paquetá segue pendente.
4. Não editar o cadastro ou geoJSON de DLU, UCV, UCS, UGU nem suas subdivisões por AP.
5. Não copiar cubos enormes para o repositório de testes sem controle de versão, origem e corte. Prototipar consultas read-only, sem mudar totais oficiais.
6. Esta auditoria é da arquitetura e dos registros de homologação; **não** é reconciliação linha a linha dos três cubos nem aceite operacional completo.

## Próxima execução

A) Inspecionar esquemas efetivos dos cubos e tabelas por dimensão, período e chave; B) comparar conjuntos de nomes normalizados de bairro/AP e dimensões; C) criar relatório de cobertura e chaves sem correspondência; D) prototipar componente independente de integração por bairro/AP com alertas de qualidade; E) testar os drill-downs e fechar aceite antes de qualquer promoção de ambiente.

**Não publicado em produção.**
