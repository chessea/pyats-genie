from pyats.topology.loader import load

testbed = load('src/mock/my_testbed.yaml')

# Recorre los equipos y realiza comandos sh bgp y ospf
learnt = {}
for name, dev in testbed.devices.items():
    dev.connect()
    learnt[name] = {}
    learnt[name]['bgp'] = dev.learn('bgp')
    learnt[name]['ospf'] = dev.learn('ospf')



exit()