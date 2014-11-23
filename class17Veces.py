Disponibles=[True,True,True,True,True,True]

J1=[0,0,0,0,0,0]
J2=[0,0,0,0,0,0]
J3=[0,0,0,0,0,0]
J4=[0,0,0,0,0,0]

#class DiesisieteVeces:

def Jugadores(self,Numero):
	if Numero == 0:
		return J1
	else:
		if Numero == 1:
			return J2
		else:
			if Numero == 2:
				return J3
			else:
				if Numero == 3:
					return J4

def NuevaPartida(self,):
	""" Metodo que reinicia el contador de booleanos. """
	""" Numeros Disponibles """
	Disponibles[0] = True
	Disponibles[1] = True
	Disponibles[2] = True
	Disponibles[3] = True
	Disponibles[4] = True
	Disponibles[5] = True
	""" Jugador Uno """
	J1[0] = 0
	J1[1] = 0
	J1[2] = 0
	J1[3] = 0
	J1[4] = 0
	J1[5] = 0
	""" Jugador Dos """
	J2[0] = 0
	J2[1] = 0
	J2[2] = 0
	J2[3] = 0
	J2[4] = 0
	J2[5] = 0
	""" Jugador Tres """
	J3[0] = 0
	J3[1] = 0
	J3[2] = 0
	J3[3] = 0
	J3[4] = 0
	J3[5] = 0
	""" Jugador Cuatro """
	J4[0] = 0
	J4[1] = 0
	J4[2] = 0
	J4[3] = 0
	J4[4] = 0
	J4[5] = 0

def LanzarDado():
	""" Metodo que devuelve un numero al azar en un rango
	del 1 al 7 (tomando en cuenta que en ningun momento
	regresara el numero 7). """

	import random
	Cara = random.randrange(1,7)
	return Cara

def AgregarCara(Cara,*J):
	""" Metodo que agregara el numero de caras que saque el jugador
	de acuerdo al metodo de 'LanzarDados', se tomara la variable
	que almacene 'Cara' y la lista de numeros del jugador. Esperara
	de parametros un valor Int y una lista de con la sumatoria
	de caras  de un jugador. """
	Jugador=[]
	for x in J:
	    Jugador.append(x)
	
	if Cara == 1 and Disponibles[0] == True:
		Jugador[0] = Jugador[0] + 1
		#e=Jugador[0]
		#Jugador[0]=e+1
	else:
		if Cara == 2 and Disponibles[1] == True:
			Jugador[1] = Jugador[1] + 1
			#e=Jugador[1]
			#Jugador[1]=e + 1
		else:
			if Cara == 3 and Disponibles[2] == True:
				Jugador[2] = Jugador[2] + 1
				#e=Jugador[2]
				#Jugador[2]=e + 1
			else:
				if Cara == 4 and Disponibles[3] == True:
					Jugador[3] = Jugador[3] + 1
					#e=Jugador[3]
					#Jugador[3]=e + 1
				else:
					if Cara == 5 and Disponibles[4] == True:
						Jugador[4] = Jugador[4] + 1
						#e=Jugador[4]
						#Jugador[4]=e + 1
					else:
						if Cara == 6 and Disponibles[5] == True:
							Jugador[5] = Jugador[5] + 1
							#e=Jugador[5]
							#Jugador[5]=e + 1
	return Jugador

def BloquearNumero(self,Jugador):
	""" Metodo que bloquea un numero con la condicion de que el
	mismo numero sobrepase a 17. """

	if Jugador[0] > 17:
		Disponibles[0] = False
	else:
		if Jugador[1] > 17:
			Disponibles[1] = False
		else:
			if Jugador[2] > 17:
				Disponibles[2] = False
			else:
				if Jugador[3] > 17:
					Disponibles[3] = False
				else:
					if Jugador[4] > 17:
						Disponibles[4] = False
					else:
						if Jugador[5] > 17:
							Disponibles[5] = False

def VerfGanador(self,Jugador,N):
	""" Metodo que devuelve un ganador. """

	if Jugador[0] == 17:
		Ganador = N
	else:
		if Jugador[1] == 17:
			Ganador = N
		else:
			if Jugador[2] == 17:
				Ganador = N
			else:
				if Jugador[3] == 17:
					Ganador = N
				else:
					if Jugador[4] == 17:
						Ganador = N
					else:
						if Jugador[5] == 17:
							Ganador = N
						else:
							if Jugador[0] == False and Jugador[1] == False and Jugador[2] == False and Jugador[3] == False and Jugador[4] == False and Jugador[5] == False:
								Ganador = "Empate"
							else:
								Ganador = "Siguiente Turno"
	return Ganador