#!/usr/bin/env python

stringa = "nid0[0254,4448,1602,4864,4866,5207,1010,3078,0685,0545,5189,0326,3559,5337,0018,0322,0426,0486,4286,4542,0966,1910,3582,0007,0845,0682,2474,1486,1478,1507,2239,0255,3477,0343],nid0004,nid00[100-103],nid050[01-04],nid040[06,07,09-11],nid[00002-00005]"


stringa = list(stringa)


lung = 4  #lunghezza della stampa


parte = ""
ris = []

def range1(s):
	del s[-1]
	s = ''.join(map(str,s))
	s = s.split('[')
	p1 = s[0]
	p2 = s[1].split(',')
	p2fin = []
	for j in p2:
		if "-" in j:
			n = j.split('-')
			for jj in range (int(n[0]),int(n[1])+1):
				if jj < 10:
					p2fin.append(str(0)+str(jj))
				else:
					p2fin.append(jj)
		else:
			p2fin.append(j)
			
	#print p1, p2fin
	for xy in p2fin:
		ris.append(str(p1) + str(xy))
	
def range2(s):
	del s[-1]
	s = ''.join(map(str,s))
	s = s.split('[')
	p1 = str(s[0])
	p2 = s[1].split(',')
	#print p1, p2[1]
	for xy in p2:
		ris.append(str(p1) + str(xy))
	
def elabora(t):
	t = t.translate(None, "id")
	t = list(t)
	if t[0] == "[": t = ['0'] + t
	if t[len(t)-1] == ",": del t[-1]
	if "-" in t:
		range1(t)
	elif "," in t:
		range2(t)
	else:
		ris.append(''.join(map(str,t)))


for x in range (1,len(stringa)):
	if stringa[x] == "n" and parte != "":
		elabora(parte)
		parte = ""
	elif x == len(stringa)-1:
		parte = str(parte) + str(stringa[x])
		elabora(parte)
	elif stringa != "n":
		parte = str(parte) + str(stringa[x])
	else:
		print "Errore sconosciuto"
		exit()

def allunga(n,t):
	stampa = ""
	for j in range (n,lung):
		stampa = str('0') + str(stampa)
	print str(stampa) + str(t)

for k in ris:
	if len(k) > lung: print k[len(k)-lung:]
	if len(k) < lung: allunga(len(k),str(k))
	if len(k) == lung: print str(k)

exit()
