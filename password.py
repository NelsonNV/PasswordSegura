import hashlib
import csv
import pendulum
import os


def evaluar_seguridad(passwd):
  # Puntuación inicial
  score = 0
  
  # Puntuar por longitud
  if len(passwd) >= 8:
    score += 1
 
  # Puntuar por números
  score += sum(char.isdigit() for char in passwd)
  
  # Puntuar por símbolos
  score += sum(not char.isalnum() for char in passwd)
  
  # Puntuar si tiene mayúsculas y minúsculas
  if any(char.isupper() for char in passwd) and any(char.islower() for char in passwd):
    score += 1
  
  # Leer palabras comunes
  lstWordlist = []
  strFileNames = os.listdir('wordlist/')

  for archivo in strFileNames:
    if archivo.endswith('.txt'):
    #Leer archivo wordlist
      with open(f'wordlist/{archivo}', 'r') as file:
        for palabra in file:
          lstWordlist.append(palabra.strip())

    lstWordlist = list(set(lstWordlist))

  if passwd in lstWordlist:
    score -= 1

  # Calcular fortaleza
  strength = hashlib.sha256(passwd.encode()).hexdigest()
  
  # Calcular tiempo de decodificación
  decode_time = 10 ** (score - 1)
  
  return score, strength, decode_time
  
  
strPassWord = input('contraseña ->')  

puntuacion, fortaleza, tiempo = evaluar_seguridad(strPassWord)

tiempo = pendulum.Duration(seconds=tiempo)

# Imprimimos los resultados
if puntuacion == 0:
    print("Puntuación de seguridad: Muy insegura")
elif puntuacion == 1:
    print("Puntuación de seguridad: Insegura")
elif puntuacion == 2:
    print("Puntuación de seguridad: Moderadamente insegura")
elif puntuacion == 3:
    print("Puntuación de seguridad: Moderada")
elif puntuacion == 4:
    print("Puntuación de seguridad: Moderadamente segura")
elif puntuacion == 5:
    print("Puntuación de seguridad: Segura")
else:
    print("Puntuación de seguridad: Muy segura")
print(f"Fortaleza: {fortaleza}")
print(f"Tiempo de decodificación: {tiempo.in_words()}")

