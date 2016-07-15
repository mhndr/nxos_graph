import json
import sys

##############################################
# usage: python nxos-graph.py < nxos-deps.json 
##############################################

data = json.load(sys.stdin)

service_users_dict = {}
service_providers_dict = {}

scope_colors= {'boot':0x110000,'infra':0x880000,'control':0xcc0001,'':0xff0000}
mode_colors = {'asap':0x001100,'conditional':0x008800,'on_demand':0x00cc00,'':0x00ff00}
condition_colors = {'optional':0x000011,'compulsory':0x000088,'':0x0000cc}
 
#generate dot file
print " digraph G { \ncenter=true;\n rankdir=LR; \nranksep=equally ;\n ratio=fill;\n  size = \"7.5,7.5\";"
for obj in data:
	service_user =  obj['service_name']
	service_providers =  obj['service_dependency']
	service_providers_dict[service_user] = service_providers
	service_scope = obj["scope"]
	node_color =  scope_colors[obj['scope']] | mode_colors[obj['run_mode']] | condition_colors[obj['run_condition']] 
	node_color = str(hex(node_color)) 	
	node_color = node_color.replace('0x','')	
	service_user = service_user.replace('-','_')
	print  service_user+" [label="+service_user+", fontcolor=\"#"+node_color+"\",color=\"#"+node_color+"\"]"
	
for service_user, service_providers in service_providers_dict.iteritems():
	service_user = service_user.replace('-','_')
	if service_providers:
		for provider in service_providers:
			provider = provider.replace('-','_')
			print service_user+"->"+provider+"[color=\"#AABBCC\"];"
	else:
		print service_user+";"	
print "}"


