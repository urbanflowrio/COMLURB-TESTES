import json, zipfile
from pathlib import Path
from collections import Counter
from shapely.geometry import shape
from shapely.ops import transform
from shapely.validation import make_valid
from pyproj import Transformer

from pathlib import Path
ucv=json.loads(Path('source/COMLURB/assets/geojson/GERENCIAS_DSU.geojson').read_text())
bairros=json.loads(Path('inteligencia-territorial/ucs.geojson').read_text())
projection=Transformer.from_crs('EPSG:4326','EPSG:31983',always_xy=True).transform
gerencias=[(f['properties']['gerencia'],transform(projection,make_valid(shape(f['geometry'])))) for f in ucv['features']]
rows=[]
for bairro in bairros['features']:
    p=bairro['properties']
    geo=transform(projection,make_valid(shape(bairro['geometry'])))
    if geo.area<=0:continue
    for nome,g in gerencias:
        if not g.intersects(geo):continue
        inter=g.intersection(geo).area
        if inter<=1:continue
        rows.append({'bairro':p['nome'],'ap':str(p['area_plane']),'gerencia':nome,'percentual_area_bairro':round(inter/geo.area*100,2),'intersecao_m2':round(inter)})
assert len(set(r['bairro'] for r in rows))==165
assert len(set(r['gerencia'] for r in rows))==6
out={'metodo':'Intersecao geometrica de limites UCV com bairros de referencia SIURB; area em EPSG:31983, intersecao acima de 1 m²','aviso':'Intersecao nao estabelece responsabilidade operacional. Um bairro pode pertencer a varias intersecoes. O mapa mostra o poligono completo da gerencia, nao o recorte do bairro.','registros':rows}
Path('inteligencia-territorial/ucv_intersecoes.json').write_text(json.dumps(out,ensure_ascii=False,separators=(',',':')))
print('Intersecoes',len(rows),'Bairros',len(set(r['bairro'] for r in rows)),'multi',sum(v>1 for v in Counter(r['bairro'] for r in rows).values()))
