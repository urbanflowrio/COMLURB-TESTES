# Conciliação dimensional 1746 × Ouvidorias — 19/10/2026

**Fonte:** `urbanflowrio/COMLURB/main/chamados-1746/chamados_cube.js` e `ouvidoria/ouvidoria_cube.js`. Inspeção dos objetos `window.CHAMADOS_CUBE` e `window.OUVIDORIA_CUBE`. Nenhuma alteração nas bases canônicas.

## Acumulado jan–set/2026

| Verificação | Chamados 1746 | Ouvidoria operacional |
|---|---:|---:|
| Total oficial `periods.acumulado.all.total2026` | 254.772 | 30.349 |
| Nº bairros com linha no cubo | 162 | 162 |
| Soma de `bairros[].v2026` | 254.772 | 30.349 |
| Nº categorias de AP | 6 | 6 |
| Soma de `ap[].v2026` | 254.772 | 30.349 |
| `SEM AP (AGO)` em 2026 | 701 | 116 |
| Nº códigos gerenciais | 53 | 54 |

- **Os conjuntos de 162 nomes de bairro coincidem exatamente** entre os dois cubos; a ordenação das linhas é diferente.
- **Os conjuntos de 6 categorias de AP coincidem exatamente** entre os dois cubos; incluem `SEM AP (AGO)`.
- **Diferença em gerência:** `LRS` aparece somente em Ouvidoria. Os demais 53 códigos coincidem. Sem tratar o código ausente como erro sem investigar sua natureza.
- Conciliação bairro/AP acumulado fechou em ambos os cubos, mas não é prova de cruzamento conjunto AP×bairro ou de competência por gerência.

## Setembro de 2026

| Verificação | Chamados | Ouvidoria |
|---|---:|---:|
| Total | 24.695 | 2.476 |
| Bairros com linha | 160 | 158 |
| Nº categorias de AP | 5 | 5 |
| Gerências com linha | 53 | 53 |
| Soma por bairro | 24.695 | 2.476 |
| Soma por AP | 24.695 | 2.476 |

## Restrições para protótipo

1. O conjunto completo de bairros deve ser construído a partir do acumulado; em setembro, alguns bairros não têm linha no cubo, o que não significa ausência territorial.
2. Para consulta por bairro e por AP, usar dimensões agregadas existentes separadamente; o objeto `periods.*.all` não estabelece por si só o cruzamento simultâneo bairro×AP.
3. Não aplicar filtro cruzado bairro×AP como se existissem dados de granularidade conjunta antes de verificar as chaves de cubo específicas.
4. Não atribuir chamados ou ouvidorias a gerências via interseção cartográfica; pendências V4.5 preservadas.
5. Não agregar os resultados de 1746 e Ouvidorias como se fossem a mesma métrica. Ouvidorias permanecem com exclusão operacional da PCO.
6. Manter `SEM AP (AGO)`, histórico congelado, cortes e aliases cartográficos existentes.
7. A futura interface pode oferecer comparativos lado a lado por bairro e AP, mantendo seleções independentes ou condicionadas apenas quando chaves conjuntas forem demonstradas.

**Resultado:** compatibilidade nominal de bairro/AP aprovada entre cubos; validação gerencial e granularidade cruzada ainda pendentes.
