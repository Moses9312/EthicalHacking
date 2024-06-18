import subprocess as sub

interface = "eth0"
new_mac = "00:11:22:33:44:88"
print("[+] Changing MAC address for " + interface + " to " + new_mac)


sub.call("ifconfig " + interface + " down", shell=True)
sub.call("ifconfig " + interface + " hw ether " + new_mac, shell=True)
sub.call("ifconfig " + interface + " up", shell=True)