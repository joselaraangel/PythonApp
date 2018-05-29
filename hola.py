import time
import datetime
from datetime import datetime
print("¿Cómo te llamas?")
nombre = input()
print(f"Me alegro de conocerte, {nombre}")
print("¿Cuentame cual es tu edad?")
edad = input()
print(f"Entendido, tu edad es {edad}")
print("¿quieres continuar con esta conversación?")
respuesta = input()
if (respuesta == "No") or (respuesta == "no"):
	print(f"OK, Nos vemos luego!! {nombre}")
	exit()
else:
	print(f"Enhorabuena, {nombre}")
print("cual es tu ciudad de nacimiento")
ciudad = input()
tiempo = time.strftime('%H:%M:%S')
print(f"vaya a mi me gusta mucho {ciudad}, la hora aqui es {tiempo}")
print("¿Cuentame cuando cumples años?")
print("Ingresa unicamente el dia")
dia = int(input())
print("Ingresa unicamente el mes")
mes = int(input())
actual = datetime.now()  # Obtiene fecha y hora actual
#print("Día:",actual.day)  # Muestra día
#print("Mes:",actual.month)  # Muestra mes
#print("Año:",actual.year)  # Muestra año
formato_fecha = "%d-%m-%Y"
fechaInicial = str(actual.day)+"-"+str(actual.month)+"-"+str(actual.year)
fechaFinal = str(dia)+"-"+str(mes)+"-"+str(actual.year)

fecha_inicial = datetime.strptime(fechaInicial,formato_fecha)
fecha_final = datetime.strptime(fechaFinal,formato_fecha)
diferencia = fecha_final - fecha_inicial
print("Falta", diferencia.days, "dias para tu cumpleaños")

