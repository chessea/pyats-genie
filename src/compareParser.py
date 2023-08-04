from pyats.topology.loader import load
import json


testbed = load('src/mock/my_testbed.yaml')
dev = testbed.devices['DEVNET_TEST']
dev.connect()
po1 = dev.parse('show ip interface brief')

# Ruta del archivo donde guardaremos la data en formato txt
ruta_archivo = "resultado2.json"

# Guardamos la data en el archivo de texto plano
with open(ruta_archivo, "w") as archivo:
    json.dump(po1, archivo, indent=4)

dev.disconnect()
exit()

