# Conciliação do cadastro geocodificado — 19/10/2026

**Escopo:** conferência do arquivo `unidades_comlurb.csv` enviado nesta conversa com `urbanflowrio/COMLURB/territorial/data/unidades_comlurb.csv` e o cadastro `COMLURB-TESTES/inteligencia-territorial/cadastro_unidades_v44.json`.

## Identidade com o repositório oficial
- SHA Git blob do arquivo recebido: `f092022e1e5ea64c82d76388ee4d6b50eb0e40d3`.
- SHA Git blob do arquivo publicado em `COMLURB/main/territorial/data/unidades_comlurb.csv`: `f092022e1e5ea64c82d76388ee4d6b50eb0e40d3`.
- **Conclusão: conteúdo idêntico**. Nenhuma necessidade de substituição no HUB.

## Estrutura do CSV
- 342 registros, 25 colunas, 342 códigos `setor` distintos.
- 0 coordenadas ausentes; 1 registro com `diretoria` vazia.
- 79 valores distintos de bairro de **localização física**.
- Sem duplicatas exatas.

## Correspondência de unidades administrativas V4.4
| Unidade | Códigos-base no cadastro V4.4 | Localizados no CSV | Ausentes |
|---|---:|---:|---:|
| DLU | 32 | 32 | 0 |
| UCV | 6 | 6 | 0 |
| UCS | 3 | 3 | 0 |
| UGU | 4 | 4 | 0 |

Não aparecem como códigos do CSV as subdivisões cartográficas `UDS-O 4`, `UDS-O 5`, `UGU-O (BANGU)`, `UGU-O (SANTA CRUZ)` e `SEM GERÊNCIA DEFINIDA`. **Isso é esperado e não implica exclusão:** as subdivisões AP permanecem na matriz geográfica V4.4/V4.5, distinta do cadastro físico.

## Limites de interpretação e próximos passos
1. O bairro informado neste CSV é o **endereço da unidade**; não comprova bairro sob sua responsabilidade.
2. A existência das 45 chaves-base nos dois cadastros suporta o relacionamento **código de unidade → cadastro físico**, não a atribuição de 1746, Ouvidoria ou IPL.
3. Para a integração analítica, relacionar os indicadores diretamente por bairro/AP presentes nas fontes canônicas, mantendo rótulos, data de corte e limitações.
4. Não usar ponto de latitude/longitude para atribuir a uma gerência a responsabilidade operacional pelos indicadores.
5. Manter a confirmação de vínculo DLU para bairros multigerenciais, de UCV e de UCS/Paquetá como pendências independentes.
6. Sem alteração no HUB oficial, mapas ou filtros já aprovados.

**Status:** conciliação de chaves-base aprovada; homologação de responsabilidade territorial permanece parcial.
