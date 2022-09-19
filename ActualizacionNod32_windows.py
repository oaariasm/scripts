#!/usr/bin/env python3

import os
import shutil
import time
import hashlib

origin = 'Z:/Nod32Update/ActualizacionNod32.rar'
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
