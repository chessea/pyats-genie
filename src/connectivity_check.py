# loader our newly minted testbed file
from pyats.topology import loader
testbed = loader.load('src/mock/testbed.pyats.yaml')

testbed.devices
ios_1 = testbed.devices['devnet']
ios_2 = testbed.devices['devnet'] # simula el ejemplo de 2 router 


# find links from one device to another
for link in ios_1.find_links(ios_2):
    print(repr(link))
# <Link link-1 at 0xf744ef8c>


# establish basic connectivity
ios_1.connect(mit=True)


# issue commands
print(ios_1.execute('show version'))
ios_1.configure('''
    interface GigabitEthernet0/0/1
        ip address 10.10.10.1 255.255.255.0
''')


# establish multiple, simultaneous connections
ios_2.connect(alias = 'console', via = 'a' ,mit=True)
ios_2.connect(alias = 'console', via = 'a',mit=True)


# issue commands through each connection separately
ios_2.vty_1.execute('show running')
ios_2.console.execute('reload')


# issue commands through each connection separately
ios_2.vty_1.execute('show running')
ios_2.console.execute('reload')


def sleep(seconds):
    ios_2.pool.execute('sleep %s' % seconds)
import multiprocessing
p1 = multiprocessing.Process(target=sleep, args = (10, ))
p2 = multiprocessing.Process(target=sleep, args = (10, ))
p3 = multiprocessing.Process(target=sleep, args = (10, ))
p1.start(); p2.start(); p3.start()
p1.join(); p2.join(); p3.join()