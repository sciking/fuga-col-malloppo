#!/usr/bin/ python
# -*- coding: utf-8 -*-
import os 
def clear():
	os.system('cls' if os.name == 'nt' else 'clear')
clear()
print "Fuga col malloppo"
print "Il gioco in cui devi truffare più persone possibile prima di essere arrestato!"
import random
turno = 1
#ord1 = 0
#ord2 = 0
galera = 0
halt = 0
nuovo = 0
#ord3 = 0
ordtot = 0
pomi = 100
trei = 0
evadi = 0
soldi = 10000
print """ Benvenuto. Il tuo obiettivo è quello di truffare più persone possibili. Sfrutta al massimo i primi cinque turni in cui non puoi essere arrestato e in cui tutti presumeranno la tua buona fede."""
print " Gioco creato da Sciking"
tuonome = raw_input("Come ti chiami?: ")
nome = raw_input("Come vuoi chiamare il tuo negozio? ")
raw_input("Premi invio per iniziare:")
clear()
def poss():
	global ordtot
	global soldi
	global galera
	poss = random.randint(1,30)
	if poss == 1:
		print "Hai vinto 1000 Ambrogi al lotto"
		soldi = soldi + 1000
		gioco()
	elif poss == 2:
		print "Hai ricevuto una multa di 1000 Ambrogi dalla Gendarmeria Fiscale"
		soldi = soldi-1000
		gioco()
	elif poss == 3:
		print "Un fornitore polacco ti trova dei cellulari più economici e guadagni 2500 Ambrogi"
		soldi = soldi + 2500
		gioco()
	elif poss == 4:
		print "Dei ladri ti hanno rapinato il negozio. Perdi 5000Å, ma l'assicurazione te ne ridà 3000"
		soldi = soldi - 2000
		gioco()
	elif poss == 5 and soldi > 100000 and galera > 2:
		print "Riesci a truffare il fisco per 15000Å, ma per evitare l'arresto fuggi in Svizzera."
		print "Benvenuto in Svizzera, signor", tuonome
		print "La polizia ha chiuso", nome, "alla settimana", turno
		soldi = soldi + 15000
		print "Hai ottenuto", soldi
		punt()
	elif poss == 5:
		print "Sei riuscito a rubare dei telefoni per soddisfare ordini."
		ordtot = int(ordtot*0.75)
		gioco()
	elif poss == 6 and galera == 2:
		print "Tenti di andare in Tirolo per ripulire soldi"
		print "Buonciorno zignore"
		print "Lei è in ztato di fermo"
		print "La polizia tirolese arresta", tuonome, "e fa chiudere", nome
		print "Sono stati sequestrati Ambrogi", soldi
		exit()
	elif poss == 6:
		print "Vendi coltelli a serramanico nel negozio \nLa Polizia ti fa 3500Å di multa"
		soldi = soldi - 3500
		gioco()
	elif poss == 7:
		print "Il tuo fornitore sammarinese ti fa degli sconti per l'abbassamento dell'IVA locale. Prendi il 10% dei tuoi soldi"
		soldi = int(soldi*1.10)
		gioco()
	elif poss == 8:
		print "Aumenta l'IVA. Perdi il 3 % dei tuoi soldi"
		soldi = int(soldi*0.97)
		gioco()
	elif poss == 9:
		print "Vieni recensito da un blog famoso e ottieni molti nuovi ordini!"
		isoldi = int(soldi + soldi*(ordtot/10))
		ordtot = int(ordtot*1.10)
		gioco()
	elif poss == 10:
		print "Paghi 5000Å un noto blogger per ottenere una buona recensione"
		soldi = soldi - 5000
	elif poss == 11:
		print "Un uomo travestito da panino che fa versi da scimmia vicino a", nome,"fa divertire i turisti"
		gioco()
	elif poss == 12:
		print "Vai in un postribolo d'alto bordo con un tuo fornitore. Spendi 1500Å"
		soldi = soldi - 1500
		gioco()
	elif poss == 13:
		print "Trovi 688Å davanti al negozio"
		soldi = soldi + 688
		gioco()
	elif poss == 14:
		print "Tuo figlio vince la gara di rutti in dialetto indetta dalla scuola"
		gioco()
	elif poss == 15:
		print "Ottieni un rimborso IVA di 2500Å"
		soldi = soldi + 2500
		gioco()
	elif poss == 16:
		print "Hai immatricolato male il veicolo, vieni multato dalla Polizia"
		soldi = int(soldi*0.97)
		gioco()
	elif poss == 17 and soldi > 65000:
		print "Sei stato denunziato per attività scorrette"
		print "Sei multato per 50000Å"
		soldi = soldi - 50000
		gioco()
	elif poss == 18 and evadi > 50:
		print "Hai vinto un premio di stato di 25000Å"
		soldi = soldi + 25000
		gioco()
	elif poss == 19:
		print "Vinci 1000 Å alla lotteria"
		soldi = soldi +1000
		gioco()
	elif poss == 20:
		print "Fallisci investimenti. Perdi il 30% dei tuoi soldi"
		soldi = int(soldi*0.7)
		gioco()
	elif poss == 21:
		print "I sorvegliant di Como ti multano per 500Å"
		soldi = soldi - 500
		gioco()
	elif poss ==  22:
		print "Hai investito in un negozio di papòss"
		if turno%2 == 0:
			print "Guadagni 5000Å"
			soldi = soldi + 5000
		else:
			print "Perdi 6500Å"
			soldi = soldi - 6500
		gioco()
	elif poss == 23:
		print "Vendi per errore telefoni a Chiasso, e devi pagare le imposte alla Svizzera"
		soldi = int(soldi - ((ordtot/5)*15))
		gioco()
	elif poss == 24:
		print "Subaffitti parte del tuo negozio ad un losco individuo che millanta di curare gente \nCi guadagni 3500 Å, ma quello è davvero strano"
		soldi = soldi + 3500
		gioco()
	elif poss == 25:
		print "Devi rimborsare", int(ordtot/10), "ordini"
		soldi = int(soldi - (ordtot/10)*195)
		ordtot = int(ordtot*0.9)
	elif poss == 26:
		print "Accedi ad un fondo del governo per le piccole imprese"
		soldi = soldi+1500
	elif poss == 27:
		print "Vieni multato per oscenità dopo aver fatto sesso con una ragazza nel negozio"
		soldi = soldi-2000
	elif poss == 28:
		print "La Gendarmeria Fiscale scopre che hai diritto ad un rimborso per tasse pagate per errore"
		soldi = int(soldi+soldi*0.3)
	elif poss == 29:
		print "La Gendarmeria Fiscale scopre che hai evaso somme sulla vendita di cover e ricevi una piccola sanzione"
		soldi = soldi - 1000
	elif poss == 30:
		print "Un tuo amico subaffitta 40 ordini a te per 250Å"
		ordtot = ordtot + 40
		soldi = soldi + 10000
		
		
	else:
		gioco()
	gioco()
	
def gioco():
	global turno
	#global ord1
	#global ord2
	#global ord3
	global ordtot
	global galera
	global soldi
	global trei
	global pomi
	global halt
	int(soldi)
	evadi = 0
	nuovo = random.randint(300,555)
	nuovopom = random.randint(5,100)
	ordtot = ordtot+nuovo
	if trei == 1:
		soldi = soldi - 100
	print nome, "di", tuonome, "- Sistema Informatico"
	print "Settimana", turno
	print "Hai", ordtot, "ordini"
	print "Hai", soldi, "Ambrogi"
	spesa = random.randint(180,245)
	print "Ogni ordine ti frutta 200Å. Tu per evadere un ordine ne spendi", spesa
	soldi = soldi + (nuovo * 200)
	try:
		while evadi <= 0:
			evadi = input("Quanti ordini vuoi evadere?")
	except SyntaxError or NameError:
		print "Errore!"
		clear()
		global soldi
		global nuovi
		clear()
		ordtot = ordtot - nuovi
		soldi = soldi - (nuovo*200)
		gioco()
	ordtot = ordtot-evadi
	soldi = soldi - (spesa*evadi)
	pomord = 0
	if turno%5 == 0 and trei == 1:
		print "Quanti PomPhone vuoi ordinare per queste cinque settimane? \n Massimo 500, un PomPhone costa 300Å"
		while pomord > 500 or pomord < 1:
			pomord = input(">>>")
		soldor = soldi
		soldi = soldi-(300*pomord)
		if soldi < 1000:
			print "Ordine annullato"
			soldi = soldor
		pomi = pomord
		pomik = random.randint(1,500)
		if pomik > pomi:
			pomik = pomi
			print "Non riesci a soddisfare tutti gli ordini di Pomphone"
			soldi = soldi+(pomik*400)
		else:
			print "Hai un disavanzo"
			soldi = soldi+(pomik*400)
			disav = pomi - pomik
			soldi = soldi + (disav*50)
			print "La PomTecnologie di Manerbio ti da 50Å per pezzo non venduto"
		pomi = 0
		



	soldi = int(soldi)
	print "Ora hai", soldi, "Ambrogi"
	svizzera = raw_input("Scrivi scappa e premi ok per scappare in Svizzera. Costerà 1/3 del tuo budget.: ")
	raw_input("Clicca su invio per continuare")
	if soldi > 200000 and trei == 0:
		print "Ora puoi aprire una nuova sede, il che ti darà più ordini e gli esclusivi PomPhone."
		noeuvnegozzi = raw_input("Scrivi Si per abbandonare Como e aprire una nuova sede a Treviglio: ")
		noeuvnegozzi = noeuvnegozzi.lower()
		if noeuvnegozzi == "si":
			trei = 1
	turno = turno +1 
	if soldi < -2500:
		l = random.randint(1,5)
		if l == 3:
			print "sono un anonimo benefattore e salverò la tua azienda"
			soldi = 5000
			poss()
		else:
			print "Gendarmeria Fiscale. Lei è in arresto per fallimento"
			print "La Gendarmeria Fiscale ha chiuso", nome
			print tuonome, "viene scarcerato subito e non potrà avviare imprese per 5 anni"
			exit()
	while ordtot > evadi*6 or evadi < ordtot/6 and soldi > 20000:
		k =random.randint(1,10)
		#print k 
		if k == 8:
			galera = galera + 1
		elif k == 8 and galera > 3:
			print "Buongiorno Polizia"
			print "Sono state segnalate irregolarità nel suo negozio"
			print "Lei è stato denunziato e il suo negozio verrà chiuso"
			print nome, "è stato chiuso alla settimana", turno, "dalla Polizia che ha sequestrato Ambrogi", soldi
			print tuonome, "viene arrestato il giorno dopo dalla Polizia per truffa"
			exit()
		elif k == 2:
			print "Buongiorno Gendarmeria fiscale"
			print "Lei ha commesso reati fiscali!"
			print "Paga il 5% per coprire tutto"
			soldi = int(soldi*0.95)
			raw_input("premi invio per continuare")
			clear()
			poss()
		else:
			clear()
			break
			
	if svizzera == "scappa":
		suisse = random.randint(1,6)
		if suisse == 4:
			print "Sei stato fermato al valico del Bernina dalle autorità lombarde"
			print "Sei in arresto per truffa e contrabbando"
			print "La Polizia Doganale ha chiuso", nome, "e ha sequestrato", int(soldi*0.66)
			print "Il giorno dopo i giornali titolano 'Arrestato", tuonome, "al valico di frontiera'"
			exit()
		elif suisse == 3:
			print "C'è stato un grave problema. Perdi metà dei tuoi soldi"
			soldi = int(soldi/2)
			print "Sei fuggito in Svizzera con", soldi
			punt()
		elif suisse == 6:
			soldi = soldi*0.66
			print "Signor", tuonome, "i suoi documenti non sono validi"
			print "La Svizzera ti ha respinto, torni a Milano."
			clear()
			poss()
		else:
			print "Benvenuto in Svizzera, signor", tuonome
			print "Sei stato ammesso in Svizzera con Ambrogi", soldi*0.66
			print "Le autorità hanno chiuso", nome
			punt()
	else:
		clear()
		poss()
	
def punt():
	global soldi
	global turno
	global ordtot
	print "*"*20
	coef = round(turno/10,1)
	if turno <= 10:
		coeff = 1

	punti = (soldi*coef)-(ordtot*2.75)
	punti = round(punti,0)
	punti = int(punti)
	if punti > 0:
		print "Hai vinto"
		print "Hai ottenuto", punti, "punti!"
		exit()
	else:
		print "Hai perso"
		print "Hai ottenuto", punti, "punti :( "
	exit()

	
	
def gioco5():
	global turno
	while turno < 6:
		print nome, "di", tuonome, "- Sistema Informatico"
		print "Settimana", turno
		#global ord1
		#global ord2
		#global ord3
		global ordtot
		global soldi
		global nuovo
		evadi = 0
		nuovo = random.randint(50,250)
		ordtot = ordtot+nuovo
		print "Hai", ordtot, "ordini"
		print "Ogni ordine ti frutta 200Å. Tu per evadere un ordine ne spendi 175"
		soldi = soldi + (nuovo * 200)
		try:
			while evadi <= 0:
				evadi = input("Quanti ordini vuoi evadere?")
		except SyntaxError or NameError:
			print "errore!"
			global soldi
			global nuovi
			clear()
			ordtot = ordtot - nuovi
			soldi = soldi - (nuovo*200)
			gioco5()
		ordtot = ordtot-evadi
		soldi = soldi - (175*evadi)
		soldi = int(soldi)
		print "Ora hai", soldi, "Ambrogi"
		raw_input("Clicca su invio per continuare")
		turno = turno +1 
		clear()
	gioco()
gioco5()		
