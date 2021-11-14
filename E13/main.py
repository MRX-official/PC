import subprocess, sys, time

# https://github.com/BornToBeRoot/PowerShell_IPv4NetworkScanner
def IPv4NetworkScan(IP):
    p = subprocess.Popen(["powershell.exe",f"./IPv4NetworkScan.ps1 -IPv4Address {IP} -Mask 255.255.255.0 -DisableDNSResolvin"], stdout=sys.stdout)
    print(p)

# https://github.com/BornToBeRoot/PowerShell_IPv4PortScanner
def PortScanner(Hostname):
    p = subprocess.Popen(["powershell.exe",f"./PortScanner.ps1 -ComputerName {Hostname} -StartPort 1 -EndPort 1000"], stdout=sys.stdout)
    print(p)

opt = 1
while opt != 0:
    opt = int(input("Select a Option \n1)IPv4 Hosts Discover Scanner \n2)Port Scanner \n0)Exit \n>"))
    if opt == 1:
        IP = input("Give me your IPv4: ")
        IPv4NetworkScan(IP)
        time.sleep(130)
    elif opt == 2:
        Host = input("Hostname: ")
        PortScanner(Host)
        time.sleep(150)
