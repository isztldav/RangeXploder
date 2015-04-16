#!/usr/bin/env python

####################   CONFIG

lung = 4  #lunghezza della stampa
tipos = 2 #tipo di stampa 1 verticale - 2 orizzontale 

####################


####################   VARIABILI
stringa = "nid0[0254,4448,1602,4864,4866,5207,1010,3078,0685,0545,5189,0326,3559,5337,0018,0322,0426,0486,4286,4542,0966,1910,3582,0007,0845,0682,2474,1486,1478,1507,2239,0255,3477,0343],nid0004,nid00[100-103],nid050[01-04],nid040[06,07,09-11],nid[00002-00005]"
stringa = list(stringa) #metti ogni carattere in array

parte = ""  #parte dell'input letto
ris = []    #array risultato
####################


####################   FUNZIONI
def range1(s):
	del s[-1]   #cancella la parentesi "]" alla fine
	s = ''.join(map(str,s)) #trasforma l'array in un testo normale
	s = s.split('[')    #dividi il numero di "nid" dal resto
	p1 = s[0]   #numero nid
	p2 = s[1].split(',')    #gli altri numeri mettili in array
	p2fin = []  #array dove andranno i numeri elaborati
	for j in p2:    #per i numeri nell'array
		if "-" in j:    #se un range
			n = j.split('-')    #dividi range
			for jj in range (int(n[0]),int(n[1])+1):    #per il range crea i numeri mancanti
				if jj < 10: #se minore di 10 metti lo 0 davanti al numero
					p2fin.append(str(0)+str(jj))    #salva
				else:   #se maggiore di 10
					p2fin.append(jj)    #salva
		else:   #se numero
			p2fin.append(j) #salva
			
	for xy in p2fin:    #per tutti i numeri elaborati
		ris.append(str(p1) + str(xy)) #mettili nella variabile finale
	
def range2(s):
	del s[-1]   #cancella la parentesi "]" alla fine
	s = ''.join(map(str,s)) #trasforma l'array in un testo normale
	s = s.split('[')    #dividi il numero di "nid" dal resto
	p1 = str(s[0])  #numero nid
	p2 = s[1].split(',')    #gli altri numeri mettili in array

	for xy in p2:   #per tutti i numeri elaborati
		ris.append(str(p1) + str(xy))   #mettili nella variabile finale
	
def elabora(t):
	t = t.translate(None, "id") #togli le lettere
	t = list(t) #metti ogni carattere in array
	if t[0] == "[": t = ['0'] + t   #se comincia senza un numero aggiungi 0
	if t[len(t)-1] == ",": del t[-1]#se alla fine c'e' una virgola allora toglilo
	if "-" in t:    #se i numeri sono in un range esegui questo
		range1(t)
	elif "," in t:  #se sono una lista di numeri esegui questo
		range2(t)
	else:   #se e 'gia' un numero allora salvalo per la stampa
		ris.append(''.join(map(str,t)))

def allunga(n,t):   #ricevi lunghezza e numero
	stampa = ""
	for j in range (n,lung): #per la lunghezza mancante
		stampa = str('0') + str(stampa) #aggiungi uno 0
	return str(stampa) + str(t) #restituisci il numero corretto

def stampa():
    #STAMPA
    if tipos == 1:  #se verticale
        for k in ris:   #per tutti i numeri
                if len(k) > lung: print k[len(k)-lung:] #se troppo lungo accorcia e stampa
                if len(k) < lung: print allunga(len(k),str(k))    #se troppo corto usa la funzione allunga e stampa
                if len(k) == lung: print str(k) #se perfetto allora stampa
    elif tipos == 2:
        finorizz = ""   #variabile per stampare orizzontale
        for k in ris:   #per tutti i numeri
                if len(k) > lung: finorizz = str(finorizz) + "," + str(k[len(k)-lung:]) #se troppo lungo accorcia e salva
                if len(k) < lung: finorizz = str(finorizz) + "," + str(allunga(len(k),str(k)))    #se troppo corto usa la funzione salva e stampa
                if len(k) == lung: finorizz = str(finorizz) + "," + str(str(k)) #se perfetto allora salva
        print finorizz[1:]  #stampa orizzontale
    else:
        print "Errore stampa!"
        exit(1)

####################   FINE FUNZIONI

#START #################################################################
for x in range (1,len(stringa)):    #leggi lettera per lettera
	if stringa[x] == "n": #and parte != "": #se leggi una "n" allora elabora cio' che hai letto
		elabora(parte)
		parte = ""
	elif x == len(stringa)-1:   #se hai letto tutto l'input allora elabora il rimanente
		parte = str(parte) + str(stringa[x])
		elabora(parte)
	elif stringa != "n":    #se diverso da "n" allora aggiungi carattere alla variabile da elaborare
		parte = str(parte) + str(stringa[x])
	else:   #se non previsto dai errore ed esci
		print "Errore sconosciuto"
		exit(1)

stampa()
########################################################################
