#!/usr/bin/env python

stringa = "nid0[0254,4448,1602,4864,4866,5207,1010,3078,0685,0545,5189,0326,3559,5337,0018,0322,0426,0486,4286,4542,0966,1910,3582,0007,0845,0682,2474,1486,1478,1507,2239,0255,3477,0343],nid0004,nid00[100-103],nid050[01-04],nid040[06,07,09-11]"

##########	VARIABILI
nlist = 0
finito = 0
char = ""
output = []
##########

stringa = stringa.translate(None, "nid")
array = list(stringa)

################
def stampa(array):
	tras = 0
	if "[" in array:
		tras = 1
		array = array.split("[")
		n1 = array[0]
		n2 = array[1]
		n2 = n2.split("]")
		n2 = filter(lambda a: a != "," and a != "", n2)
		for jn in n2:
			if "-" in jn:
				arrayj = jn.split(",")
				for jj in arrayj:
					#print jj + str("--")
					if "-" in jj:
						conta = jj.split("-")
						for n in range(int(conta[0]),int(conta[1])+1):
							if n < 10: output.append(str(n1) + str(0) + str(n))
							if n > 9: output.append(str(n1) + str(n))
					else:
						output.append(output.append(str(n1) + str(jj)))
			else:
				arrayj = jn.split(",")
				for cj in arrayj:
					ris =  str(n1) + str(cj)
					if len(ris) > 4: ris = ris[1:]
					output.append(ris)
		#return None
	if tras == 0 and array.translate(None,",") != "": output.append(array.translate(None,","))
	#return "0"


################

for c in array:
	char = str(char) + str(c)
	if c == ",":
		finito = 1
	elif c == "[":
		nlist = 1
	elif c == "]":
		nlist = 0

	if finito == 1 and nlist == 0:
		#print "------------------"
		if stampa(char) != "" or stampa(char) != "0": output.append(stampa(char))
		finito = 0
		char = ""

for i in output:
	if i != None:
		if len(i) > 4:
			print i[1:]
		else:
			print i

exit()
