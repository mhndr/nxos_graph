import json
import sys

##############################################
# usage: python nxos-graph.py < nxos-deps.json 
##############################################

data = json.load(sys.stdin)

service_users_dict = {}
service_providers_dict = {}

for obj in data:
	service_user =  obj['service_name']
	service_providers =  obj['service_dependency']
	service_providers_dict[service_user] = service_providers

#generate dot file
print " digraph G { \ncenter=true;\n  rankdir=LR;\nranksep=equally ;\n ratio=fill;\n  size = \"7.5,7.5\";"
for service_user, service_providers in service_providers_dict.iteritems():
	service_user = service_user.replace('-','_')
	if service_providers:
		for provider in service_providers:
			provider = provider.replace('-','_')
			print service_user+"->"+provider+";"
	else:
		print service_user+";"	
print "}"


	 
