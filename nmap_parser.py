import port
import machine

import xml.etree.ElementTree as ET

tree = ET.parse('test_nmap.xml')
root = tree.getroot()

all_machines = []

# find all scanned ip addresses
scanned_addresses= tree.findall('.//address')

# find all open ports for all ip addresses
for address in scanned_addresses:
    print(address.attrib)
    all_ports = tree.findall('.//port')
    ports = []
    for single_port in all_ports:
        ports.append(port.Port(single_port.attrib.get('portid'), single_port.attrib.get('protocol')))
        print(ports)
    all_machines.append(machine.Machine(address.attrib.get('addr'), ports))
    print(all_machines)
