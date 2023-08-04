from genie.testbed import load
import json


# Simple conexion por ssh
tb = load('src/mock/my_testbed.yaml')
dev = tb.devices['DEVNET_TEST']

# Elimina la canfiguracion por defecto
dev.connect(mit=True)


# Trasnformar a formato JSON
p1 = dev.parse('show inventory')
print(f"Imprimir el sn: {p1['main']['chassis']['ISR4221/K9']['sn']}")
print(json.dumps(p1['main'], indent=4))


# Envia comandos show al router referente a bgp
output= dev.learn("bgp")
ruta= "src/learns/output.txt"

with open(ruta, "w") as archivo:
    archivo.write(str(output))



# pyats learn bgp ospf --testbed-file src/mock/my_testbed.yaml --output_folder





#Salir del equipo
exit()