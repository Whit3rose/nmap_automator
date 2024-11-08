import port
import machine

import xml.etree.ElementTree as ET


def parse_nmap_file(nmap_filename: str):
    tree = ET.parse(nmap_filename)
    root = tree.getroot()

    all_machines = []

    # find all scanned ip addresses
    scanned_addresses = tree.findall('.//address')

    # find all open ports for all ip addresses
    for address in scanned_addresses:
        all_ports = tree.findall('.//port')
        machine_ports = []
        for single_port in all_ports:
            machine_ports.append(port.Port(single_port.attrib.get('portid'), single_port.attrib.get('protocol')))
        all_machines.append(machine.Machine(address.attrib.get('addr'), machine_ports))
    return all_machines
