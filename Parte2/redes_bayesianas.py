import re

probabilidad = ("(['P'|'p'])['('](((?:['!']?[a-z][a-z]*))+(['|'|','](((?:['!']?[a-z][a-z]*))+(,)*)+)*)[')'](=)([0-9]+([.][0-9]+)*)")
rg = re.compile(probabilidad,re.IGNORECASE|re.DOTALL)
rg_sol = re.compile("(['P'|'p'])['('](((?:['!']?[a-z][a-z]*))+(['|'|','](((?:['!']?[a-z][a-z]*))+(,)*)+)*)[')']",re.IGNORECASE|re.DOTALL)
F = open('red.txt','r')
info = F.read().split('\n')
error = []
red = []
grupo = []
childs = []
for item in info:
	x = info.index(item)
	info[x] = item.replace(" ","")
	#print (x+1,info[x])
	if not rg.match(info[x]):
		error.append(('linea '+str(x+1)+': probabilidad mal escrita'))
	else:
		red.append(rg.match(info[x]))
		grupo.append(rg.match(info[x]).group(2))
		#print('success',rg.match(info[x]).groups())
		#print (rg.match(info[x])).group(0)



def tree(red):
	arbol = {}
	elevaciones = []

	for nodo in red:
	#	print('arbol', arbol)
		
		try:
			#print nodo.group(2)
			hijo,padres = nodo.group(2).split('|')
			if len(padres)> 1:
				padres = list(padres)
				while ',' in padres: padres.remove(',')
				while '!' in padres: padres.remove('!')
			#print ('primer ',hijo,padres)
			if len(hijo)> 1:
				hijo = list(hijo)
				while ',' in hijo: hijo.remove(',')
				while '!' in hijo: hijo.remove('!')
			#print ('segundo ',hijo,padres)

			#print (hijo,padres)
			for padre in padres:
				#print ('lol',padre,(arbol[padre]))
				if padre not in arbol.keys():
					arbol[padre] = hijo
					
				elif hijo[0] not in arbol[padre]:
					hijos = []
					hijos.extend(arbol[padre])
					hijos.extend(hijo)
					arbol[padre] = hijos
			'''
			except:
				for padre in padres:	
					if padre not in arbol.keys():
						arbol[padre] = hijo
					elif hijo not in arbol[padre]:
						elevaciones.append(len(padres))
						hijos = []
						hijos.extend(arbol[padre])
						hijos.extend(hijo) 
						arbol[padre] = hijos
			'''
		except:
			arbol[nodo.group(2)] = ""
	return arbol
	#print (arbol)
def comp_num(arbol):
	nodos = []
	nodos = set(nodos)
	number = 1
	padres = []
	for key in arbol:
		nodos.add(key)
		for p in arbol[key]:
			padres.append(p)
		number += 2**(len(arbol[key]))
	for x in padres:
	 if padres.count(x) > 1 and x not in nodos:
	 	number += 1
	 	nodos.add(x)
	return number,nodos
Tree = tree(red)
#print Tree
num,nodos = comp_num(Tree)

#print num 

for i in Tree:
	childs.extend(Tree[i])
#print childs
#print nodos


def getCompact(Tree,childs):
	compact = []
	mini = {1:2}
	for key in Tree:
		for item in Tree[key]:
			#print item,key
			if key not in childs and key not in compact:
				compact.append(key)
			if not(childs.count(item)>1):
				compact.append(item+'|'+key)
			else:
				if item in mini.keys():
					mini[item].extend(key)
				else:
					mini[item] = [key]
	#print mini
	for key in mini:
		try:
			no = key/2
		except:
			if len(mini[key]) > 1:
				dep = ""
				for i in mini[key]:
					dep += i
				compact.append(key+"|"+dep)
			else:
				compact.append(key+"|"+mini[key][0])
	return compact

def paso1(user):
	print (user)
	if "|" not in user:
		user = set(user)
		for n in compact:
			print(('!'+n) not in user)
			if ('!'+n) not in user:
				user.add(n[0])
		return [user]
	else:
		num,den = [],[]
		prob,dado = user[:user.index('|')],user[user.index('|')+1:]
		num.extend(prob)
		num.extend(dado)
		den.extend(dado)
		print ('num', num)
		num,den = set(num),set(den)
		for n in compact:
			print(('!'+n) not in num)
			if ('!'+n) not in num:
				num.add(n[0])
				den.add(n[0])
		return [num,den]

if len(error) : print(error) 
else: 
	compact = getCompact(tree(red),childs)
	print('Forma compacta: ',compact)
while True:
	user_input = input('Ingrese la query que desea consultar: ')
	print(user_input)
	user = list(user_input.upper())
	user.remove('(')
	user.remove(')')
	user.remove('P')
	for i in range(len(user)-1):
		if user[i] == '!':
			user[i+1] = '!'+str(user[i+1])
			user.remove('!')
	print(user)
	user_in = paso1(user)
	print(user_in)




#print getCompact(Tree,childs)






'''
def parseo1(grupo):
	for i in grupo:
		try:
			first,second = i.split("|")
			change = first[1:] if '!' in frist else '!'+first
			if first+"|"+second in grupo:
				return False
				break
		except:
			first=i[1:] if '!' in i else '!'+i
			if first in grupo:
				return False
				break
	return True
'''
#print parseo(grupo)
#print grupo






#(['P'|'p'])['('](((?:[a-z][a-z]*))(['|'|','](((?:[a-z][a-z]*))+(,)*)+)*)[')']
#(['P'|'p'])['('](((?:[a-z][a-z]*))(['|'|','](((?:[a-z][a-z]*))+(,)*)+)*)[')'](=)([0-9]+([.][0-9]+)*)
#(['P'|'p'])['('](((?:['!']?[a-z][a-z]*))(['|'|','](((?:['!']?[a-z][a-z]*))+(,)*)+)*)[')'](=)([0-9]+([.][0-9]+)*)
#(['P'|'p'])['('](((?:['!']?[a-z][a-z]*))+(['|'|','](((?:['!']?[a-z][a-z]*))+(,)*)+)*)[')'](=)([0-9]+([.][0-9]+)*)

#m = rg.match(txt1)
#print m.group(0)
'''
if m:
    var1=m.group(1)
    rbraces1=m.group(2)
    ws1=m.group(3)
    c1=m.group(4)
    ws2=m.group(5)
    int1=m.group(6)
    print m.groups(),"("+var1+")"+"("+rbraces1+")"+"("+ws1+")"+"("+c1+")"+"("+ws2+")"+"("+int1+")"+"\n"
'''