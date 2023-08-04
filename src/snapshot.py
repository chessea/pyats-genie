from pyats.topology.loader import load



testbed = load('src/mock/my_testbed.yaml')
output1 = {}
for name, dev in testbed.devices.items():
   dev.connect(mit=True)
   output1[name] = {}
   output1[name]['bgp'] = dev.learn('bgp')



exit()
