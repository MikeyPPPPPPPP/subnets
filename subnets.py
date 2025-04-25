import socket, sys, os, random




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
	#
	#The reson it worked with the data of httprobe is beacause they were all just tested as live sites, so when Igave it sites that might nod be up there was no error handling. 
	#

	hostnames = []
	ips = {}

	#parse the file to a list
	with open(file, "r") as Ofile:
		for line in Ofile.readlines():
			try:

			#url to hostname
				if line.strip().startswith("http"):
					hostnames.append(line.strip().split("://")[1])
				elif len(line.strip()) > 7:
					#the hope is that the small bits of data will be less then "https://"
					#hostnames.append(line.strip())


					#If the hostname is a list of hostnames and httprobe hasn't ran yet, we need to asume some hosts are not valide and so error handling was added.
					try:
						ips[line.strip()] = socket.gethostbyname(line.strip())
					except socket.gaierror:
						pass

				else:
					pass
			except Exception as e:
				print(e)
			
	

	#set tor proxy
	#get A format

	#ips = {host:socket.gethostbyname(host) for host in hostnames}


	#############################################################################
	#############################################################################
	#############################################################################
	#############################################################################


	#Get the unique subnets.
	subnets: list[str] = parse_subnets(ips)

	if not os.path.exists("a_subnets.txt"):
		with open("all_subnets.txt", "w") as file:
			for x in subnets:
				file.write(x+"\n")



if __name__ == "__main__":
	main()
