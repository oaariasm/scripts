import os
import re


cwd = "D:\Vídeos\Curso Django - pildorasinformaticas"
list_files = os.listdir(cwd)

for file in list_files:


    orden = re.search('Vídeo\s{0,}\d{1,}', file).group()
    extension = re.search('\.\w{1,}\Z', file).group()

    name = file.replace(re.search('\.\s{0,}Vídeo\s{0,}\d{1,}', file).group(), "") # remover numero al video 
    name = name.replace(extension, "")
    # name = name.replace(re.search('\.\s{0,}$', name).group(), "") # Remove spaces at end of file
    newname = orden + ' - ' + name + extension

    file_path = os.path.join(cwd, file)
    newname_path = os.path.join(cwd, newname)
    os.rename(file_path, newname_path)
    print(f"Renmbrado {file} a {newname}")
