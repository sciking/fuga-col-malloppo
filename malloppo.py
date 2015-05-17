# -*- coding: utf-8 -*-
print "Fuga col malloppo"
print "Il gioco in cui devi truffare più persone possibile prima di essere arrestato!"
import os 
import random
turno = 1
#ord1 = 0
#ord2 = 0
#ord3 = 0
ordtot = 0
soldi = 1000
print """ Benvenuto. Il tuo obiettivo è quello di truffare più persone possibili. Sfrutta al massimo i primi cinque turni in cui non puoi essere arrestato e in cui tutti presumeranno la tua buona fede."""
print " Gioco creato da Sciking"
nome = raw_input("Come vuoi chiamare il tuo negozio? ")
raw_input("Premi invio per iniziare:")
os.system("clear")
def gioco():
	global turno
	print "Turno", turno
	#global ord1
	#global ord2
	#global ord3
	global ordtot
	global soldi
	nuovo = random.randint(30,55)
	ordtot = ordtot+nuovo
	print "Hai", ordtot, "ordini"
	spesa = random.randint(185,250)
	print "Ogni ordine ti frutta 200€. Tu per evadere un ordine ne spendi", spesa
	soldi = soldi + (nuovo * 200)
	evadi = input("Quanti ordini vuoi evadere?")
	ordtot = ordtot-evadi
	soldi = soldi - (spesa*evadi)
	print "Ora hai", soldi, "Euro"
	svizzera = raw_input("Scrivi scappa e premi ok per scappare in Svizzera. Costerà 1/3 del tuo budget.: ")
	raw_input("Clicca su invio per continuare")
	turno = turno +1 
	while ordtot > evadi*6 or evadi < 10 and soldi > 10000:
		k =random.randint(1,5)
		if k == 4:
			print "Buongiorno Polizia"
			print "Sono state segnalate irregolarità nel suo negozio"
			print "Lei è stato denunziato e il suo negozio verrà chiuso"
			print nome, "è stato chiuso al turno", turno, "dalla Polizia che ha sequestrato Euro", soldi
			exit()
	if svizzera == "scappa":
		suisse = random.randint(1,6)
		if suisse == 4:
			print "Sei stato fermato al valico di Brogeda dalle autorità italiane"
			print "Sei in arresto per truffa e contrabbando"
			print "La Polizia ha chiuso", nome, "e ha sequestrato", soldi*0.66
		elif suisse == 3:
			print "C'è stato un grave problema. Perdi metà dei tuoi soldi"
			print "Sei fuggito in Svizzera con", soldi/2
			exit()
		elif suisse == 6:
			print "La Svizzera ti ha respinto, torni in Italia."
			gioco()
		else:
			print "Benvenuto in Svizzera, signore!"
			print "Sei stato ammesso in Svizzera con Euro", soldi*0.66
			exit()
	else:
		os.system("clear")
		gioco()
	

	
def gioco5():
	global turno
	while turno < 6:
		print "Turno", turno
		#global ord1
		#global ord2
		#global ord3
		global ordtot
		global soldi
		nuovo = random.randint(5,25)
		ordtot = ordtot+nuovo
		print "Hai", ordtot, "ordini"
		print "Ogni ordine ti frutta 200€. Tu per evadere un ordine ne spendi 175"
		soldi = soldi + (nuovo * 200)
		evadi = input("Quanti ordini vuoi evadere?")
		ordtot = ordtot-evadi
		soldi = soldi - (175*evadi)
		print "Ora hai", soldi, "Euro"
		raw_input("Clicca su invio per continuare")
		turno = turno +1 
		os.system("clear")
	gioco()
gioco5()		

	
	
