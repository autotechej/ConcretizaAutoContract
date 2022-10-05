# Importa a biblioteca de funções
#encoding: utf-8
# -*- coding: utf-8 -*-
import Functions as fct
import Servicos
import os
import htmlToPDF as pdf
# Executa o programa
fct.MenuPrincipal()
Servicos.escrever_contrato()
CURRENT_DIR = f"{str(os.getcwdb())}"    # para puxar o diretório atual
filename = os.path.join((CURRENT_DIR[2:len(CURRENT_DIR)-1]), f"{pdf.arquivo}.html")     #para juntar o diretório,tratá-lo e juntar com o arquivo, ficando diretório/arquivo.html
pdf.html_to_pdf(filename, f"{pdf.nomeF}.pdf") #chamando a função de trasnformar html em pdf     2