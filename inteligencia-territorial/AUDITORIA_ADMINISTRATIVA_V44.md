# V4.4 — Auditoria administrativa e territorial (preliminar)
Data: 16/10/2026. Fontes: planilha **ENDERECOS_ATUALIZADOS.xlsx**, aba ENDEREÇOS, colunas SETOR/NOMESETOR/PAISETOR, e os arquivos geográficos auditados na V4.3.1. Não são divulgados endereços, telefones ou dados de contato.

## Resultado
| Unidade | Cadastro administrativo | Chaves territoriais disponíveis | Diagnóstico |
| --- | --- | --- | --- |
| DLU | 5 superintendências e 32 gerências correspondentes ao mapa | 32 códigos gerenciais | **32/32 conciliados** em código e nome; hierarquia oficial identificada. Há subdivisões/adjuntas adicionais no cadastro, fora da geometria consolidada. |
| UCV | 6 gerências subordinadas à coordenadoria UCV | 6 gerências | **6/6 conciliadas**; cruzamento de AP/bairro é *interseção geométrica*, não responsabilidade oficial. |
| UCS | 3 divisões: UDS-N, UDS-S, UDS-O | 4 territórios: UDS-N, UDS-S, UDS-O 4, UDS-O 5; e 1 feição sem gerência | N/S coincidem; **UDS-O 4/5 não são códigos administrativos do cadastro**. Não afirmar automaticamente que representam divisões formais ou que substituem UDS-O. |
| UGU | 4 gerências subordinadas à UGU: UGU-N/S/B/O | 5 etiquetas de mapa: UGU-N/S/B, UGU-O (BANGU), UGU-O (SANTA CRUZ) | N/S/B coincidem. **UGU-O se apresenta dividida em duas etiquetas territoriais**, sem correspondência cadastral direta; vínculo provável a UGU-O indicado apenas como agrupamento de análise, **não como reclassificação homologada**. |

## Hierarquia comprovada
- DLU → LRB, LRC, LRN, LRO, LRS → 32 gerências cujos nomes e vínculos constam em `cadastro_unidades_v44.json`.
- DSU → UCV (Coordenadoria de Manejo Arbóreo) → UGV-B/M/N/O/S/T.
- DSU → UCS (Coordenadoria de Coleta Seletiva e Reciclagem) → UDS-N, UDS-O e UDS-S, identificadas como **divisões**, não gerências.
- DSU → UGU (Gerência de Conservação e Revitalização de Mobiliário Urbano) → UGU-B/N/O/S.
- DSU → UCP (Coordenadoria de Serviços Hospitalares e Prediais) → UGT (Gerência de Pesquisas e Controle de Vetores) → UGR → UDR-N/O/S. Sem mapa validado.

## Pendências
1. **UCV:** 260 pares bairro×gerência por interseção espacial e 64 combinações bairro/AP com sobreposição; não equivalem à atribuição administrativa.
2. **UCS:** registrar e resolver a feição `SEM GERÊNCIA DEFINIDA`. Confirmar se `UDS-O 4` e `UDS-O 5` são recortes válidos de `UDS-O`, com vigência e responsabilidade.
3. **UGU:** homologar a relação entre as etiquetas `UGU-O (BANGU)` / `UGU-O (SANTA CRUZ)` e o cadastro `UGU-O`.
4. **DLU:** diferenças pré-existentes entre o mapa histórico do HUB e o SIURB: 54 bairros em gerência e 51 em superintendência. Requer confirmação de fonte vigente, não substituição automática.
5. Os bairros foram associados a códigos territoriais, mas ainda **não existe homologação independente de atribuição formal bairro→gerência**.

## Decisão
Conciliação de **códigos e hierarquia** DLU e UCV concluída. UCS e UGU com divergências documentadas. O funcionamento do mapa no tablet não confere homologação administrativa. **V4.4 permanece em testes; não publicar no HUB oficial.**
