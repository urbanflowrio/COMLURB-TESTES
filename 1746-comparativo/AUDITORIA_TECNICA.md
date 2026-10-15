# Aceite técnico parcial — Comparativo Territorial 1746

Data: 14/10/2026. Ambiente: COMLURB-TESTES, sem autorização automática de publicação na main oficial.

## Verificações positivas
- Usuária confirmou abertura da página, carregamento da base e funcionamento dos filtros no celular.
- Os 162 nomes de bairro do cubo possuem correspondência populacional; há 161 códigos demográficos distintos.
- Somatórios do cubo por bairro e por serviço conciliados para acumulado jan–set e setembro, em 2025 e 2026.
- Totais oficiais: jan–set/2025=224.004, jan–set/2026=254.772, set/2025=21.276, set/2026=24.695.
- Teste independente via Node VM: **330 asserções aprovadas** (cobertura populacional em ambos os períodos, totais por ano e serviço, compartilhamento do código e denominador São Cristóvão/Imperial).
- São Cristóvão e Imperial de São Cristóvão compartilham o código IBGE e **28.016 habitantes**: taxas por linha são válidas, mas os denominadores não podem ser somados. Taxa agrupada dos 1.146 chamados: 409,1 por 10 mil.
- Scripts do site de testes referenciam `./chamados_cube.js` e `./populacao_ibge_2022.js` locais; referência de corte `./data-cutoff.json`.

## Restrições do aceite

- **Homologação final não emitida**: a suíte completa `npm test` não concluiu, pois `papaparse@5.4.1` não está disponível neste ambiente; tentativa de `npm ci` falhou por DNS no acesso ao registro npm. O selftest inicial passou (40 casos).
- Verificação visual de cenários específicos de taxa e expansão completa dos subtipos ainda não documentada individualmente pela usuária.
- Censo 2022 é denominador fixo de registros 2025/2026; indicador é volume de chamados por residente, não qualidade do serviço ou pessoas reclamantes distintas.
- Arquivos públicos devem identificar a referência temporal do cubo/copias locais. Se o oficial for atualizado, o ambiente de testes exigirá sincronização do cubo.
- Não alterar indicadores nem publicar na `main` até concluir a regressão exigida para homologação definitiva.

## Decisão

**Aceite técnico parcial com conferência numérica e celular; produção bloqueada pela pendência de regressão integral.**
