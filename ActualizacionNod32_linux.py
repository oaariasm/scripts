#!/usr/bin/env python3

# Copia la actualización de Nod32 desde un directorio remoto a donde se encuentre el script

import os
import shutil
import time
import hashlib

origin = '/run/user/1000/kio-fuse-kEhlvE/smb/192.168.0.10/htdocs/Nod32Update/ActualizacionNod32.rar' #Ruta de origen de la actualización. Cambiar esto.
dest = os.getcwd()


def copiar():
    print(f"Copiando Actualización...")
    shutil.copy(origin, dest)
    print("Listo!")
    time.sleep(1)

def get_file_size(file):
    return os.path.getsize(file)

def calc_hash(path, size):
    m = hashlib.md5()
    with open(path, 'rb') as f:
        b = f.read(size)
        while len(b) > 0:
            m.update(b)
            b = f.read(size)
    print(f"Calculando hash de {path}, tamaño: {size} bytes ")
    print(f"La suma MD5 es: {m.hexdigest()}")


def main():
    if os.path.isfile(origin) and os.path.isfile(os.path.join(dest, 'ActualizacionNod32.rar')):
        if calc_hash(origin, get_file_size(origin)) == calc_hash(os.path.join(dest, 'ActualizacionNod32.rar'), get_file_size(os.path.join(dest, 'ActualizacionNod32.rar'))):
            print("Los arhivos son iguales")
        else:
            copiar()

    elif os.path.isfile(origin) and not os.path.isfile(os.path.join(dest, 'ActualizacionNod32.rar')):
        copiar()
    elif not os.path.isfile(origin):
        print("No se encuentra la actualización en el servidor...")
        time.sleep(1)


if __name__ == "__main__":
    main()
