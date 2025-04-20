import socket, sys, os




def parse_subnets(hosts: dict[str:str]):
	"""
	
	.23 - > 0/24


	"""
	
	counter = 0

	#should be filterd because the subnet is the key.
	parsedSubnets = {}

	for _, ip in hosts.items():
		#3.3.3.3   ->   3.3.3.0/24
		parsedSubnets['.'.join(ip.split(".")[:3])+".0/24"] = str(counter)
		counter += 1 

	return [ip for ip, _ in parsedSubnets.items()]



def main():
	if len(sys.argv) > 0:
		file = sys.argv[1]

	else: 
		raise "No file Found."
	

	#############################################################################
	#
	#
	#
	#      these two functions are so fucking awesome!!!!!!!!
	#############################################################################
	hostnames = []
	
	#parse the file to a list
	with open(file, "r") as Ofile:
		for line in Ofile.readlines():
			try:
			#url to hostname
				hostnames.append(line.strip().split("://")[1])
			except:
				pass
			
	

	#set tor proxy
	#get A format
	ips = {host:socket.gethostbyname(host) for host in hostnames}
	#############################################################################
	#############################################################################
	#############################################################################
	#############################################################################


	#Get the unique subnets.
	subnets: list[str] = parse_subnets(ips)

	if not os.path.exists("subnets.txt"):
		with open("subnets.txt", "w") as file:
			for x in subnets:
				file.write(x+"\n")



if __name__ == "__main__":
	main()
