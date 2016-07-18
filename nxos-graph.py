import json
import sys

##############################################
# usage: python nxos-graph.py < nxos-deps.json 
##############################################

data = json.load(sys.stdin)

service_users_dict = {}
service_providers_dict = {}


colors = { 
'boot':'red',
'bootasap':'blue3',
'asap':'turquoise',
'controlon_demand':'blue',
'controlconditional':'blueviolet',
'controlasap':'green',
'controlconditionalcompulsory':'limegreen',
'infraconditional':'forestgreen',
'infraconditionalcompulsory':'yellow',
'controlconditionaloptional':'firebrick4',
'infraasap':'orange',
'conditionalcompulsory':'orange3',
'on_demand':'slateblue',
'infraasapcompulsory':'cyan4'
}

#generate dot file
print " digraph G { \ncenter=true;\n rankdir=LR; \nranksep=equally ;\n ratio=fill;\n  size = \"7.5,7.5\";"
for key in  colors:
	print key+" [shape=rectangle,color="+colors[key]+",style=filled];"
for obj in data:
	service_user =  obj['service_name']
	service_providers =  obj['service_dependency']
	service_providers_dict[service_user] = service_providers
	color_key = ''
	if 'scope' in obj and obj['scope']:
		color_key = obj['scope']
	if 'run_mode' in obj and obj['run_mode']:
		color_key = color_key + obj['run_mode']
	if 'run_condition' in obj and obj['run_condition']:
		color_key = color_key + obj['run_condition']
	print color_key
	node_color = colors[color_key]
	service_user = service_user.replace('-','_')
	print  service_user+" [label="+service_user+", style=filled ,color="+node_color+"]"
	
for service_user, service_providers in service_providers_dict.iteritems():
	service_user = service_user.replace('-','_')
	if service_providers:
		for provider in service_providers:
			provider = provider.replace('-','_')
			print service_user+"->"+provider+"[color=\"#AABBCC\"];"
	else:
		print service_user+";"	
print "}"


