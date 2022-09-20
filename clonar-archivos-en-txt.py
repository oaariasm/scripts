# Crea archivos vacíos con nombres de archivos de un directorio
# Útil para probar progrmas que realizan operaciones con archivos (copiar, renombrar, etc)
# de manera mas eficiente

import os

src = "D:\Vídeos\Overlord IV"  # Ruta de origen
dst = "D:\Vídeos\Overlord IV - tests"  # Ruta de destino

try:
    file_list = os.listdir(src)
except FileNotFoundError:
    print("Carpeta de origen no encontrada")

for file in file_list:
    
    if not os.path.isdir(dst):
        os.mkdir(dst)
        
    cloned_file = os.path.join(dst, file)

    if not os.path.isfile(cloned_file):
        with open(cloned_file, 'w') as f:
            f.write("")
