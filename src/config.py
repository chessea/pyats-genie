from pyats.topology.loader import load
from genie.conf.base import Interface





testbed = load('src/mock/my_testbed.yaml')
uut = testbed.devices['DEVNET_TEST']
uut.connect(mit=True)




# Configuracion para Interface
nxos_interface = Interface(device=uut, name='gigabitEthernet0/0/1')


nxos_interface.ipv4 = '200.1.1.3'
nxos_interface.ipv4.netmask ='255.255.255.0'
nxos_interface.description ='Configurado con pyats'
nxos_interface.shutdown= False



# Aplica la configuracion
nxos_interface.build_config(apply=True)


# remueve la configuracion
nxos_interface.build_unconfig(apply=True)

exit()