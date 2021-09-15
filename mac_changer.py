#!/usr/bin/env python

import subprocess
import optparse


def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="The interface of which you want to change the MAC Address.")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC Address.")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify an interface. Use --help for more info.")
    elif not options.new_mac:
        parser.error("[-] Please specify a new MAC Address. Use --help for more info.")
    return options


def change_mac(interface, new_mac):
    subprocess.run(["ifconfig", interface, "down"])
    subprocess.run(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.run(["ifconfig", interface, "up"])
    subprocess.run(["ifconfig", interface])
    if new_mac == options.new_mac:
        print("[+] The MAC Address of", interface, "has been changed to", new_mac + ".")
    else:
        print("[-] The MAC Address has not been changed.")


options = get_arguments()
change_mac(options.interface, options.new_mac)
