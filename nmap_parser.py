import xml.etree.ElementTree as ET

tree = ET.parse('test_nmap.xml')
root = tree.getroot()

# find all scanned ip addresses
scanned_addresses= tree.findall('.//address')

# find all open ports for all ip addresses
for address in scanned_addresses:
    print(address.attrib)
    all_ports = tree.findall('.//port')
    for port in all_ports:
        print(port.attrib)
