
import socket
import termcolor


def scan(target, ports):
	print('\n' + 'Starting Scan for ' + str(target))
	for port in range(1, ports):
		port_scanner(target,port)

def port_scanner(ipAddress, ports):

		try:
			sock = socket.socket()
			sock.connect((ipAddress,ports))
			print("[+] Port Opened " + str(ports))	
			sock.close()

		except:
			pass

targets= input("[*] Enter Targets to Scan : ")
ports= int(input("[*] Enter How many Ports You want to scan : "))

if ',' in targets:
	print(termcolor.colored(("[+] Scanning multiple Host"),'red'))
	for ip_addr in targets.split(','):
		scan(ip_addr.strip(' '),ports)
else:
	scan(targets,ports)
