import subprocess as sub
import optparse as opt


def get_arguments():
    parser = opt.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")

    return parser.parse_args()


def change_mac(interface, new_mac):
    print(f"[+] Changing MAC address for {interface} to {new_mac}")
    print(sub.call("ifconfig"))

    sub.call(["ifconfig", interface, "down"])
    sub.call(["ifconfig", interface, "hw", "ether", new_mac])
    sub.call(["ifconfig", interface, "up"])


(options, arguments) = get_arguments()
change_mac(options.interface, options.new_mac)
