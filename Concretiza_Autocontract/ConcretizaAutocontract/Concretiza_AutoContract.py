#Importa a biblioteca de funções
#encoding: utf-8
# -*- coding: utf-8 -*-
import Functions as fct
import Servicos
import os
import htmlToPDF as pdf
#Executa o programa
fct.MenuPrincipal()
Servicos.escrever_contrato()
CURRENT_DIR = "C:\AUTOTECH\Desenvolvimento\ConcretizaAutocontract"
filename = os.path.join(CURRENT_DIR, f"{pdf.arquivo}.html")
pdf.html_to_pdf(filename, f"{pdf.nomeF}.pdf")