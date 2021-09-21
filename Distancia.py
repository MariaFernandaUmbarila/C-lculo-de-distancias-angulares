"""

Maria Fernanda Umbarila Suarez
Astronomía 2021-2
El siguiente programa es un apoyo a
las operaciones que se deben hacer
para el cálculo de distancias.

"""

import math

#Función para conocer la distancia en kilómetros entre dos puntos, conociendo sus coordenadas
def haversine(lat1, lon1, lat2, lon2):
	dlat = math.radians(lat2 - lat1)
	dlon = math.radians(lon2 - lon1)
	R = 6371
	a = (math.sin(dlat / 2)**2) + (math.cos(math.radians(lat1)) * math.cos(math.radians(lat2))) * (math.sin(dlon / 2)**2)
	distancia = 2 * R * math.asin(math.sqrt(a))
	return distancia

#Función para conocer la distancia en grados entre dos puntos, conociendo sus coordenadas
def leycoseno(lat1, lon1, lat2, lon2):
	angP = math.radians(abs(lon1 - lon2))
	ladoA = math.radians(90 - lat2)
	ladoB = math.radians(90 - lat1)
	a = ((math.cos(ladoA)) * (math.cos(ladoB))) + ((math.sin(ladoA)) * (math.sin(ladoB)) * (math.cos(angP))) 
	distancia = math.degrees(math.acos(a))
	return distancia

#Función para calcular el ángulo A dado los tres lados del triángulo
def cosenoladoA(ladoA, ladoB, ladoC):
	rad = math.pi / 180
	num = math.cos(rad * ladoA) - (math.cos(rad * ladoB) * math.cos(rad * ladoC))	
	den = math.sin(rad * ladoB) * math.sin(rad * ladoC)
	a = num / den
	anguloA = math.degrees(math.acos(a)) 
	return anguloA

#Función para calcular el ángulo B dado los tres lados del triángulo
def cosenoladoB(ladoA, ladoB, ladoC):
	rad = math.pi / 180
	num = math.cos(rad * ladoB) - (math.cos(rad * ladoA) * math.cos(rad * ladoC))	
	den = math.sin(rad * ladoA) * math.sin(rad * ladoC)
	a = num / den
	anguloB = math.degrees(math.acos(a)) 
	return anguloB

#Función para calcular el ángulo C dado los tres lados del triángulo
def cosenoladoC(ladoA, ladoB, ladoC):
	rad = math.pi / 180
	num = math.cos(rad * ladoC) - (math.cos(rad * ladoA) * math.cos(rad * ladoB))	
	den = math.sin(rad * ladoA) * math.sin(rad * ladoB)
	a = num / den
	anguloC = math.degrees(math.acos(a)) 
	return anguloC

#Función para calcular el ángulo A dados los tres lados en km del triángulo
def planocosenoA(ladoA, ladoB, ladoC):
	rad = math.pi / 180
	num = (ladoB**2) + (ladoC**2) - (ladoA**2)
	den = 2 * ladoB * ladoC
	a = num / den
	anguloA = math.degrees(math.acos(a))
	return anguloA

#Función para calcular el ángulo B dados los tres lados en km del triángulo
def planocosenoB(ladoA, ladoB, ladoC):
	rad = math.pi / 180
	num = (ladoA**2) + (ladoC**2) - (ladoB**2)
	den = 2 * ladoA * ladoC
	a = num / den
	anguloA = math.degrees(math.acos(a))
	return anguloA

#Función para calcular el ángulo C dados los tres lados en km del triángulo
def planocosenoC(ladoA, ladoB, ladoC):
	rad = math.pi / 180
	num = (ladoA**2) + (ladoB**2) - (ladoC**2)
	den = 2 * ladoA * ladoB
	a = num / den
	anguloA = math.degrees(math.acos(a))
	return anguloA

#Variables de las coordenadas en grados decimales
latMons = 4.605
longMons = -74.05527
latGua = 4.59166
longGua = -74.05416
latObs = 4.59805
longObs = -74.07694

#Valores en grados de los lados del triángulo esférico
b = leycoseno(latMons, longMons, latGua, longGua)
m = leycoseno(latGua, longGua, latObs, longObs)  
g = leycoseno(latMons, longMons, latObs, longObs)

#Valores en kilómetros de los lados del triángulo plano
kb = haversine(latMons, longMons, latGua, longGua)
km = haversine(latGua, longGua, latObs, longObs) 
kg = haversine(latObs, longObs, latMons, longMons)

#Imprime en pantalla los resulados de las funciones haversine y de trigonometría esférica
print(f"La distancia entre Guadalupe y Monserrate es: {round(leycoseno(latMons, longMons, latGua, longGua) , 5)} grados")
print(f"La distancia entre Guadalupe y Monserrate es: {round(haversine(latMons, longMons, latGua, longGua) , 5)} kilómetros")
print(f"La distancia entre Guadalupe y el Observatorio es: {round(leycoseno(latGua, longGua, latObs, longObs) , 5)} grados")
print(f"La distancia entre Guadalupe y el Observatorio es: {round(haversine(latGua, longGua, latObs, longObs) , 5)} kilómetros")
print(f"La distancia entre Monserrate y el Observatorio es: {round(leycoseno(latMons, longMons, latObs, longObs) , 5)} grados")
print(f"La distancia entre Monserrate y el Observatorio es: {round(haversine(latObs, longObs, latMons, longMons) , 5)} kilómetros")

#Imprime en pantalla el resultado de los ángulos, usando fórmulas esféricas
print(f"El ángulo A es {round(cosenoladoA(b, m, g), 5)} grados")
print(f"El ángulo B es {round(cosenoladoB(b, m, g), 5)} grados")
print(f"El ángulo C es {round(cosenoladoC(b, m, g), 5)} grados")

#Imprime en pantalla el resultado de los ángulos, usando fórmulas de geometría plana
print(f"El ángulo A es {round(planocosenoA(kb, km, kg), 5)} grados")
print(f"El ángulo B es {round(planocosenoB(kb, km, kg), 5)} grados")
print(f"El ángulo C es {round(planocosenoC(kb, km, kg), 5)} grados")

#Confirma la suma de los ángulos, las imprime en pantalla
print(f"La suma de los ángulos es : {round(cosenoladoA(m, b, g) + cosenoladoA(b, m, g) + cosenoladoA(g, m, b), 5)} grados")
print(f"La suma de los ángulos es : {round(planocosenoA(m, b, g) + planocosenoA(b, m, g) + planocosenoA(g, m, b), 5)} grados")

