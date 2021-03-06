import easygui

#Lector de archivox
def leerArchivo():
    archivo = easygui.fileopenbox( default="./data/*.lfp")
    data = []
    with open(archivo, "r", encoding="utf-8") as f: 
        for line in f.readlines():
            data.append(line.replace('\n', ' '))
    return data

