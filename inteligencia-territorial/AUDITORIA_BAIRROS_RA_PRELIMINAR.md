# Auditoria auxiliar de bairros × RA — 19/10/2026

**Estado:** levantamento preliminar, não homologado. **Escopo:** arquivo `bairros com ra.xlsx` apresentado para análise, confrontado com `cadastro_unidades_v44.json`. Sem alterações de geometria, filtros, vínculos operacionais ou matriz V4.5.

## Contagem da planilha
- 1.192 linhas de dados; 162 denominações de bairro; 35 códigos de RA; 53 códigos no campo Gerência.
- 0 linhas exatamente repetidas.
- 14 bairros apresentam mais de uma RA na planilha. O fato exige verificação de fonte e vigência, não demonstra por si só dupla jurisdição geográfica.
- Os seguintes códigos constam da planilha e **não constam como chave** no cadastro V4.4: `FCZ`, `LDE`, `LDN`, `LDO`, `LDS`, `UDR-N`, `UDR-O`, `UDR-S`. Sua natureza deve ser examinada antes de classificar como erro.
- Os registros de subdivisão `UDS-O 4`, `UDS-O 5`, `UGU-O (BANGU)`, `UGU-O (SANTA CRUZ)` e `SEM GERÊNCIA DEFINIDA` não aparecem com as mesmas chaves na planilha; **não devem ser excluídos nem substituídos**.

## Bairros com mais de uma RA informada

| Bairro | RAs informadas |
|---|---|
| Camorim | 16ª, 24ª |
| Cidade de Deus | 16ª, 34ª |
| Itanhangá | 16ª, 24ª |
| Maré | 10ª, 30ª |
| Ramos | 10ª, 12ª |
| Complexo do Alemão | 12ª, 29ª |
| Sampaio | 13ª, 13ª-A |
| Gávea | 06ª, 27ª |
| Realengo | 17ª, 33ª |
| Santa Cruz | 18ª, 19ª |
| Sepetiba | 19ª, 26ª |
| Vigário Geral | 11ª, 31ª |
| Paquetá | 02ª, 21ª |
| São Conrado | 06ª, 27ª |

## Limites e condições de aceite

1. A planilha não tem coluna AP e não contém polígonos nem datas de vigência.
2. A associação `Gerência × Bairro × RA` é tabular; não comprova recorte cartográfico oficial nem responsabilidade operacional exclusiva.
3. Não promover filtros por RA sem conciliar com cadastro oficial de RA e vínculos por AP.
4. Não alterar os rótulos de UCS e UGU preservados por AP.
5. A pendência UCS/Paquetá permanece aberta; outras RAs ou unidades não determinam sua responsabilidade.
6. Preservar todo o conteúdo V4.5 e mapas V4.4.1 até novo aceite explícito.

**Próxima etapa sugerida:** conciliar os nomes de bairro e RAs com fonte administrativa oficial vigente e testar a cardinalidade AP × RA × bairro, sem inserir filtros em produção.
