import os
import htmlToPDF as pdf
caminho = str(os.getcwdb())
print(os.path.join(caminho ,"/pasta",'teste.py'))


CURRENT_DIR = f"{str(os.getcwdb())}"
diretorio = CURRENT_DIR
filename = os.path.join((diretorio[2:len(CURRENT_DIR)-1]), f"{pdf.arquivo}.html")


print(filename)