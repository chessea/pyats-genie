from genie.utils.diff import Diff
import json


ruta_archivo1 = "resultado1.json"

with open(ruta_archivo1, "r") as archivo:
    po1_cargado = json.load(archivo)

ruta_archivo2 = "resultado2.json"

with open(ruta_archivo1, "r") as archivo:
    po2_cargado = json.load(archivo)

print(type(po1_cargado))
print(type(po2_cargado))

diff = Diff(po1_cargado, po2_cargado)
diff.findDiff()
print(diff)