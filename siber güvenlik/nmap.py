import nmap

scanner = nmap.PortScanner()

ip = "10.10.10.10"
scanner.scan(ip,'0-100','-sV')

for port in scanner[ip]['tcp'].keys():
    name = scanner[ip]['tcp'][port]['name']
    product = scanner[ip]['tcp'][port]['product']
    version = scanner[ip]['tcp'][port]['version']
    print(port,name,product,version)


