#!/usr/bin/env python

stringa = "nid0[0254,4448,1602,4864,4866,5207,1010,3078,0685,0545,5189,0326,3559,5337,0018,0322,0426,0486,4286,4542,0966,1910,3582,0007,0845,0682,2474,1486,1478,1507,2239,0255,3477,0343],nid0004,nid00[100-103],nid050[01-04]";

stringa = stringa.translate(None, "[]nid")

stringa = stringa.split(",")

for i in stringa:
	if len(i) == 4: print i
	elif len(i) > 4:
		if "-" in i:
			numeri = i.split("-")
			if len(numeri[0]) > 4: numeri[0] = numeri[0][1:]
			numeri[1] = str(numeri[0][:4 - len(numeri[1])]) + str(numeri[1])
			for j in range(int(numeri[0]),int(numeri[1])+1):
				if len(str(j)) < 4: print str(0) + str(j)
				elif len(str(j)) == 4: print str(j)
				else:
					print "Errore"
					exit()
		else:
			if i[:1] == "0": print i[1:]
	else:
		print "Errore"
		exit()
