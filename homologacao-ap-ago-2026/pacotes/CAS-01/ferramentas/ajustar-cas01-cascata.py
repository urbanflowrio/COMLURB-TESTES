"""Ajuste CAS-01 — grafia de bairros na cascata da Linha do Tempo (19/10/2026).

Uso (a partir da raiz do repositório):
    python3 ajustar-cas01-cascata.py .

1746-timeline/cascade_data.js: BRAZ DE PINA e OSWALDO CRUZ estavam como
   "SEM AP / NÃO INFORMADA" por divergência de grafia com o GeoJSON oficial
   (Brás de Pina / Osvaldo Cruz). Recebem AP e gerência do próprio GeoJSON
   (AP3/NG11P e AP3/NG15H), mesma regra dos outros 159 bairros da cascata.

Nenhuma soma muda. Sai com código 1 se qualquer conferência falhar.
"""
import json, os, sys

RAIZ = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else ".")
ROTULO = "SEM AP (AGO)"
CAMPOS = ["c2025", "c2026", "o2025", "o2026"]
log = []

def falha(msg):
    print("FALHA: " + msg); sys.exit(1)

def abrir(rel):
    s = open(os.path.join(RAIZ, rel), encoding="utf-8").read()
    i = s.index("{"); j = s.rstrip().rstrip(";").rindex("}") + 1
    obj = json.loads(s[i:j])
    if s[:i] + json.dumps(obj, ensure_ascii=False, separators=(",", ":")) + s[j:] != s:
        falha("serialização não reproduz o original: " + rel)
    return s[:i], obj, s[j:]

def gravar(rel, pre, obj, pos):
    with open(os.path.join(RAIZ, rel), "w", encoding="utf-8") as f:
        f.write(pre + json.dumps(obj, ensure_ascii=False, separators=(",", ":")) + pos)

def ajustar_cascata(rel):
    pre, obj, pos = abrir(rel); n = 0
    corrigir = {"BRAZ DE PINA": ("AP3", "NG11P"), "OSWALDO CRUZ": ("AP3", "NG15H")}
    def percorrer(o):
        nonlocal n
        if isinstance(o, list):
            for x in o: percorrer(x)
            return
        if not isinstance(o, dict): return
        if o.get("ap") == "SEM AP":
            c = corrigir.get(o.get("nome"))
            if not c or o.get("gerencia") != "NÃO INFORMADA": falha(rel + ": SEM AP inesperado em " + str(o.get("nome")))
            o["ap"], o["gerencia"] = c; n += 1
        for v in o.values(): percorrer(v)
    percorrer(obj)
    if '"ap":"SEM AP"' in json.dumps(obj, ensure_ascii=False, separators=(",", ":")): falha(rel + ": SEM AP remanescente")
    gravar(rel, pre, obj, pos)
    log.append(f"{rel}: {n} linhas de bairro corrigidas (BRAZ DE PINA → AP3/NG11P; OSWALDO CRUZ → AP3/NG15H)")

ajustar_cascata("1746-timeline/cascade_data.js")
print("\n".join(log)); print("OK")
