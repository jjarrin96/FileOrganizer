import glob 
import os
import shutil

descargas_folder = os.path.expanduser("~") + "/Downloads/"

archivos = glob.glob(descargas_folder + "*")

carpetas_nombres = ["Carpetas",
                    "Musica",
                    "Excels", 
                    "Presentaciones", 
                    "Words", 
                    "Imagenes",
                    "PDFs",
                    "Archivo_comprimidos",
                    "Otros_archivos"]

extension_unicas = set([i.split(".")[-1].lower() for i in archivos])

ubicaciones = []
for nombre in carpetas_nombres:
    ubicaciones.append(descargas_folder + nombre)

archivos_agrupados = {}
for ext in extension_unicas:
    if len(ext) > 5:
        archivos_agrupados[ext] = ubicaciones[0]
    elif ext in ["mp3", "mp4"]:
        archivos_agrupados[ext] = ubicaciones[1]
    elif ext in ["csv", "xls", "xlsx"]:
        archivos_agrupados[ext] = ubicaciones[2]
    elif ext in ["ppt", "pptx"]:
        archivos_agrupados[ext] = ubicaciones[3]
    elif ext in ["docx", "doc", "docm"]:
        archivos_agrupados[ext] = ubicaciones[4]
    elif ext in ["jpeg", "jpg", "png"]:
        archivos_agrupados[ext] = ubicaciones[5]
    elif ext == "pdf":
        archivos_agrupados[ext] = ubicaciones[6]
    elif ext in ["zip", "rar"]:
        archivos_agrupados[ext] = ubicaciones[7]
    else:
        archivos_agrupados[ext] = ubicaciones[8]

# Comprueba si la carpeta ya existe antes de intentar crearla
for ubicacion in ubicaciones:
    if not os.path.exists(ubicacion):
        os.makedirs(ubicacion)
        print(f"La carpeta '{ubicacion}' se ha creado con éxito.")
    else:
        print(f"La carpeta '{ubicacion}' ya existe.")

for archivo in archivos:
    ext_file = archivo.split(".")[-1].lower()
    carpeta = archivos_agrupados[ext_file]
    shutil.move(archivo, carpeta)


