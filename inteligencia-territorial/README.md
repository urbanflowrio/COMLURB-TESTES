# Inteligência Territorial V4.2 — ambiente de testes

Piloto independente e não homologado. Endereço: https://urbanflowrio.github.io/COMLURB-TESTES/inteligencia-territorial/

- DLU: utiliza SOMENTE o GeoJSON público do HUB oficial `DLU_Novos_Bairros_estrutura2025.geojson`, atributo `gerdlu`. Feições de superintendência sem `gerdlu` não integram as contagens.
- DSU: mapeia UCV com as seis gerências disponíveis em `GERENCIAS_DSU.geojson`. UCS, UCP/UGT e UGU são reconhecidas como níveis administrativos sem geometria pública validada no piloto.
- A associação DLU código inicial C → LRC está explícita.
- Nenhuma camada SIURB fornecida privadamente, planilha de endereços ou contato pessoal foi publicada.
- Os limites e vínculos territoriais permanecem sujeitos a homologação cartográfica. Sem métricas 1746/Ouvidoria/IPL nesta versão.
- Biblioteca Leaflet e tiles OpenStreetMap demandam acesso à internet; em caso de bloqueio da CDN, o mapa não inicia.
- Não alterar a main oficial com base neste piloto sem validação funcional, administrativa e geométrica.
