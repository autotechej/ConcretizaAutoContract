# Importa a biblioteca de funções
#encoding: utf-8
# -*- coding: utf-8 -*-
import Functions as fct
import Servicos
import os
import htmlToPDF as pdf
print(os.getcwdb())
# Executa o programa
fct.MenuPrincipal()
Servicos.escrever_contrato()
CURRENT_DIR = f"{str(os.getcwdb())}"
filename = os.path.join((CURRENT_DIR[2:len(CURRENT_DIR)-1]), f"{pdf.arquivo}.html")
pdf.html_to_pdf(filename, f"{pdf.nomeF}.pdf")
