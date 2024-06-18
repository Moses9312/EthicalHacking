import subprocess as sub

interface = "eth0"
new_mac = "00:11:22:33:44:77"
print("[+] Changing MAC address for " + interface + " to " + new_mac)


sub.call(f"ifconfig {interface}", shell=True)
sub.call(f"ifconfig {interface} hw ether {new_mac}", shell=True)
sub.call(f"ifconfig {interface} up", shell=True)