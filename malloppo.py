#!/usr/bin/ python
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
evadi = 0
soldi = 10000
print """ Benvenuto. Il tuo obiettivo è quello di truffare più persone possibili. Sfrutta al massimo i primi cinque turni in cui non puoi essere arrestato e in cui tutti presumeranno la tua buona fede."""
print " Gioco creato da Sciking"
tuonome = raw_input("Come ti chiami?: ")
nome = raw_input("Come vuoi chiamare il tuo negozio? ")
raw_input("Premi invio per iniziare:")
os.system("clear")
def poss():
	global soldi
	poss = random.randint(1,20)
	if poss == 1:
		print "Hai vinto 1000 Euro al lotto"
		soldi = soldi + 1000
		gioco()
	elif poss == 2:
		print "Hai ricevuto una multa di 1000 Euro dalla Gendarmeria Fiscale"
		soldi = soldi-1000
		gioco()
	elif poss == 3:
		print "Un fornitore polacco ti trova dei cellulari più economici e guadagni 700 Euro"
		soldi = soldi + 700
		gioco()
	elif poss == 4:
		print "Dei ladri ti hanno rapinato il negozio. Perdi 5000€, ma l'assicurazione te ne ridà 3000"
		soldi = soldi - 2000
		gioco()
	elif poss == 5:
		print "Riesci a truffare il fisco per 15000€, ma per evitare l'arresto fuggi in Svizzera."
		print "Benvenuto in Svizzera, signor", tuonome
		print "La polizia ha chiuso", nome, "al turno", turno
		soldi = soldi + 15000
		print "Hai ottenuto", soldi
		exit()
	elif poss == 6:
		print "Tenti di andare in Slovenia per ripulire soldi"
		print "Buongiorno signore"
		print "Lei è in stato di fermo"
		print "La polizia slovena arresta", tuonome,	"e fa chiudere", nome
		print "Sono stati sequestrati Euro", soldi
		exit()
	elif poss == 7:
		print "Il tuo fornitore sammarinese ti fa degli sconti per l'abbassamento dell'IVA locale. Prendi il 10% dei tuoi soldi"
		soldi = soldi*1.10
		gioco()
	elif poss == 8:
		print "Aumenta l'IVA. Perdi il 3 % dei tuoi soldi"
		gioco()
	elif poss == 9:
		print "Vieni recensito da un blog famoso e ottieni molti nuovi ordini!"
		soldi = soldi*1.5
		gioco()
	elif poss == 10:
		print "Paghi 5000€ un noto blogger per ottenere una buona recensione"
		soldi = soldi - 50000
	elif poss == 11:
		print "Un uomo travestito da panino che fa versi da scimmia vicino a", nome,"fa divertire i turisti"
		gioco()
	elif poss == 12:
		print "Vai in un postribolo d'alto bordo con un tuo fornitore. Spendi 1500€"
		soldi = soldi - 1500
		gioco()
	elif poss == 13:
		print "Trovi 688€ davanti al negozio"
		soldi = soldi + 688
		gioco()
	elif poss == 14:
		print "Tuo figlio vince la gara di rutti in dialetto indetta dalla scuola"
		gioco()
	elif poss == 15:
		print "Ottieni un rimborso IVA di 2500€"
		soldi = soldi + 2500
		gioco()
	elif poss == 16:
		print "Hai immatricolato male il veicolo, vieni multato dalla Polizia"
		soldi = soldi*0.97
		gioco()
	elif poss == 17 and evadi < 40:
		print "Sei stato denunziato per attività scorrette"
		print "Sei multato per 100000€"
		soldi = soldi - 100000
		gioco()
	elif poss == 18 and evadi > 50:
		print "Hai vinto un premio di stato di 25000€"
		soldi = soldi + 25000
		gioco()
	elif poss == 19:
		print "Vinci 1000 € alla lotteria"
		soldi = soldi +1000
		gioco()
	elif poss == 20:
		print "Fallisci investimenti. Perdi il 30% dei tuoi soldi"
		soldi = soldi*0.7
		gioco()
	else:
		gioco()
	gioco()
	
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
	except SyntaxError or NameError:
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
			poss()
		else:
			print "Gendarmeria Fiscale. Lei è in arresto per fallimento"
			print "La Gendarmeria Fiscale ha chiuso", nome
			print tuonome, "viene scarcerato subito e non potrà avviare imprese per 5 anni"
			exit()
	while ordtot > evadi*6 or evadi < 30 and soldi > 50000:
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
			input("premi invio per continuare")
			os.system("clear")
			poss()
		else:
			os.system("clear")
			poss()
			
	if svizzera == "scappa":
		suisse = random.randint(1,6)
		if suisse == 4:
			print "Sei stato fermato al valico di Brogeda dalle autorità italiane"
			print "Sei in arresto per truffa e contrabbando"
			print "La Polizia ha chiuso", nome, "e ha sequestrato", soldi*0.66
			print "Il giorno dopo i giornali titolano 'Arrestato", tuonome, "al valico di frontiera'"
			exit()
		elif suisse == 3:
			print "C'è stato un grave problema. Perdi metà dei tuoi soldi"
			print "Sei fuggito in Svizzera con", soldi/2
			exit()
		elif suisse == 6:
			print "Signor", tuonome, "i suoi documenti non sono validi"
			print "La Svizzera ti ha respinto, torni in Italia."
			poss()
		else:
			print "Benvenuto in Svizzera, signor", tuonome
			print "Sei stato ammesso in Svizzera con Euro", soldi*0.66
			print "Le autorità hanno chiuso", nome
			exit()
	else:
		os.system("clear")
		poss()
	

	
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
		except SyntaxError or NameError:
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
