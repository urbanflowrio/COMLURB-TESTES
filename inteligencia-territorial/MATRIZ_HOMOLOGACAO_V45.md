# Matriz de homologação territorial V4.5
**Data:** 16/10/2026 · **Ambiente:** COMLURB-TESTES · **Natureza:** controle de aceite, sem alteração das camadas.

## Critérios
- **Confirmado (C):** sustentado pelo cadastro administrativo ou por decisão operacional explícita, no escopo indicado.
- **Confirmado apenas como geometria (G):** desenho e interseção válidos para exploração, sem demonstrar responsabilidade administrativa.
- **Pendente (P):** precisa de validação operacional ou de vigência documental antes de atribuir responsabilidade.
- **Preservado (R):** decisão de não alterar nomes, subdivisões, polígonos e filtros aprovados.
- **Não homologado (NH):** não promover à produção como verdade administrativa.

| ID | Unidade | Objeto | Evidência / fundamento | Status | Encaminhamento |
|---|---|---|---|---|---|
| V45-01 | DLU | 5 superintendências, 32 gerências e nomes cadastrais | ENDERECOS_ATUALIZADOS.xlsx, auditoria V4.4 | C | Manter hierarquia e códigos atuais |
| V45-02 | DLU | 51 diferenças de código SIURB × HUB | matriz_bairros_siurb_hub.csv e reconciliação V4.4 | P | Usar ponte de leitura; confirmar vigência antes de substituir |
| V45-03 | DLU | Brás de Pina | SIURB NG11P/NG14I; HUB NG11P | P | Validar regra de responsabilidade |
| V45-04 | DLU | Vila da Penha | SIURB NG11P/NG14I; HUB NG14I | P | Validar regra de responsabilidade |
| V45-05 | DLU | Vista Alegre | SIURB NG11P/NG14I/NG31V; HUB NG14I | P | Validar regra de responsabilidade |
| V45-06 | UCV | 6 gerências cadastrais e seus nomes | Cadastro administrativo V4.4 | C | Preservar estrutura |
| V45-07 | UCV | 260 interseções e 64 pares bairro/AP multicruzados | ucv_intersecoes.json, auditoria V4.3.1 | G | Exibir como interseção, não atribuição |
| V45-08 | UCV | Responsabilidade exclusiva por bairro | Interseção não prova competência | NH | Exigir fonte operacional |
| V45-09 | UCS | UDS-O 4 e UDS-O 5 | Decisão expressa: subdivisões por AP | R | Preservar rótulos, filtros e polígonos |
| V45-10 | UCS | Paquetá, AP 1, SEM GERÊNCIA DEFINIDA | ucs.geojson | P | Solicitar identificação da divisão UCS |
| V45-11 | UGU | UGU-O (BANGU) e UGU-O (SANTA CRUZ) | Decisão expressa: subdivisões por AP | R | Preservar rótulos, filtros e polígonos |
| V45-12 | Geral | Navegação e avisos V4.4.1 no tablet | Confirmação funcional da responsável | C | Manter interface e alertas |
| V45-13 | Geral | Homologação administrativa integral para produção | Existem pendências V45-02/03/04/05/08/10 | NH | Não promover à produção sem autorização explícita |

## Regras de aceite
1. Não confundir **cadastro de unidades**, **geometria de interseção** e **atribuição operacional**.
2. Não alterar ou unificar subdivisões por AP da UCS/UGU.
3. Não escolher gerência para Paquetá com base em DLU, UCV ou UGU.
4. Não resolver bairros multicódigo DLU pela maior área sem critério formal.
5. O aceite funcional do tablet **não** implica aceite administrativo.
6. Publicação no HUB oficial exige homologação do conteúdo aplicável e autorização explícita.

## Evidências
- `AUDITORIA_TERRITORIAL_V43.md`
- `AUDITORIA_ADMINISTRATIVA_V44.md`
- `DIVERGENCIAS_V44_CONCILIADAS.md`
- `PENDENCIAS_PONTUAIS_V44.csv`

**Decisão V4.5:** matriz de controle produzida; homologação territorial **parcial**, com pendências claramente identificadas. Nenhuma mudança de geometria ou navegação.
