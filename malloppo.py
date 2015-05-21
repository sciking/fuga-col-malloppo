#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os 
os.system("clear")
print "Fuga col malloppo"
print "Il gioco in cui devi truffare più persone possibile prima di essere arrestato!"
import random
turno = 1
#ord1 = 0
#ord2 = 0
nuovo = 0
#ord3 = 0
ordtot = 0
soldi = 10000
print """ Benvenuto. Il tuo obiettivo è quello di truffare più persone possibili. Sfrutta al massimo i primi cinque turni in cui non puoi essere arrestato e in cui tutti presumeranno la tua buona fede."""
print " Gioco creato da Sciking"
tuonome = raw_input("Come ti chiami?: ")
nome = raw_input("Come vuoi chiamare il tuo negozio? ")
raw_input("Premi invio per iniziare:")
os.system("clear")
def gioco():
	global turno
	#global ord1
	#global ord2
	#global ord3
	global ordtot
	global soldi
	evadi = 0
	nuovo = random.randint(300,555)
	ordtot = ordtot+nuovo
	print nome, "di", tuonome, "- Sistema Informatico"
	print "Turno", turno
	print "Hai", ordtot, "ordini"
	spesa = random.randint(180,245)
	print "Ogni ordine ti frutta 200€. Tu per evadere un ordine ne spendi", spesa
	soldi = soldi + (nuovo * 200)
	try:
		while evadi <= 0:
			evadi = input("Quanti ordini vuoi evadere?")
	except SyntaxError:
		print "Errore!"
		os.system("clear")
		global soldi
		global nuovi
		os.system("clear")
		ordtot = ordtot - nuovi
		soldi = soldi - (nuovo*200)
		gioco()
	ordtot = ordtot-evadi
	soldi = soldi - (spesa*evadi)
	print "Ora hai", soldi, "Euro"
	svizzera = raw_input("Scrivi scappa e premi ok per scappare in Svizzera. Costerà 1/3 del tuo budget.: ")
	raw_input("Clicca su invio per continuare")
	turno = turno +1 
	if soldi < 0:
		l = random.randint(1,6)
		if l == 3:
			print "sono un anonimo benefattore e salverò la tua azienda"
			soldi = 1000
			gioco()
		else:
			print "Gendarmeria Fiscale. Lei è in arresto per fallimento"
			print "La Gendarmeria Fiscale ha chiuso", nome
			print nome, "viene scarcerato subito e non potrà avviare imprese per 5 anni"
			exit()
	while ordtot > evadi*6 or evadi < 10 and soldi > 50000:
		k =random.randint(1,10)
		print k 
		if k == 8:
			print "Buongiorno Polizia"
			print "Sono state segnalate irregolarità nel suo negozio"
			print "Lei è stato denunziato e il suo negozio verrà chiuso"
			print nome, "è stato chiuso al turno", turno, "dalla Polizia che ha sequestrato Euro", soldi
			print tuonome, "viene arrestato il giorno dopo dalla Polizia per truffa"
			exit()
		elif k == 2:
			print "Buongiorno Gendarmeria fiscale"
			print "Lei ha commesso reati fiscali!"
			print "Paga il 5% per coprire tutto"
			soldi = soldi*0.95
			os.system("clear")
			gioco()
		else:
			os.system("clear")
			gioco()
			
	if svizzera == "scappa":
		suisse = random.randint(1,6)
		if suisse == 4:
			print "Sei stato fermato al valico di Brogeda dalle autorità italiane"
			print "Sei in arresto per truffa e contrabbando"
			print "La Polizia ha chiuso", nome, "e ha sequestrato", soldi*0.66
			print "Il giorno dopo i giornali titolano 'Arrestato", tuonome, "al valico di frontiera'"
		elif suisse == 3:
			print "C'è stato un grave problema. Perdi metà dei tuoi soldi"
			print "Sei fuggito in Svizzera con", soldi/2
			exit()
		elif suisse == 6:
			print "Signor", tuonome, "i suoi documenti non sono validi"
			print "La Svizzera ti ha respinto, torni in Italia."
			gioco()
		else:
			print "Benvenuto in Svizzera, signor", tuonome
			print "Sei stato ammesso in Svizzera con Euro", soldi*0.66
			print "Le autorità hanno chiuso", nome
			exit()
	else:
		os.system("clear")
		gioco()
	

	
def gioco5():
	global turno
	while turno < 6:
		print nome, "di", tuonome, "- Sistema Informatico"
		print "Turno", turno
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
		print "Ogni ordine ti frutta 200€. Tu per evadere un ordine ne spendi 175"
		soldi = soldi + (nuovo * 200)
		try:
			while evadi <= 0:
				evadi = input("Quanti ordini vuoi evadere?")
		except SyntaxError:
			print "errore!"
			global soldi
			global nuovi
			os.system("clear")
			ordtot = ordtot - nuovi
			soldi = soldi - (nuovo*200)
			gioco5()
		ordtot = ordtot-evadi
		soldi = soldi - (175*evadi)
		print "Ora hai", soldi, "Euro"
		raw_input("Clicca su invio per continuare")
		turno = turno +1 
		os.system("clear")
	gioco()
gioco5()		

	
	
