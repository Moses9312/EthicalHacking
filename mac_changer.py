import subprocess as sub

print(sub.call("ifconfig"))
interface = input("interface > ")
new_mac = input("new MAC > ")
print("[+] Changing MAC address for " + interface + " to " + new_mac)


sub.call("ifconfig " + interface + " down", shell=True)
sub.call("ifconfig " + interface + " hw ether " + new_mac, shell=True)
sub.call("ifconfig " + interface + " up", shell=True)