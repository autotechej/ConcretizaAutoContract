# Esta é a biblioteca usada para fazer a interface
import PySimpleGUI as sg

# Aqui são definidos os parâmetros do tema da interface, nesse caso foram utilizadas as cores da EJ

sg.LOOK_AND_FEEL_TABLE['MyCreatedTheme'] = {'BACKGROUND': '#87ceeb',
                                            'TEXT': '#3C3C3B',
                                            'INPUT': '#87ceeb',
                                            'TEXT_INPUT': '#3C3C3B',
                                            'SCROLL': '#EB7F00',
                                            'BUTTON': ('#3C3C3B', '#87ceeb'),
                                            'PROGRESS': ('# D1826B', '# CC8019'),
                                            'BORDER': 1, 'SLIDER_DEPTH': 0,
                                            'PROGRESS_DEPTH': 0, }
font = ("Times New Roman", 12)
FontTitle = ("Times New Roman", 40)
FontSubtitle = ("Times New Roman", 20)
font2 = ("Times New Roman", 6)
font3 = ("Times New Roman", 24)

# Essa função aplica o tema à janela

sg.theme('MyCreatedTheme')

# Aqui se definem os layouts das janelas de interface

# Layout do menu principal
MenuPrincipalLayout = [
    [sg.Image("Logotratada.png", key=1)],
    [sg.Text('Menu Principal', font=FontSubtitle)],
    [sg.Button('Preencher Novo Contrato', font=font)],
    [sg.Button('Preferências',  font=font)],
    [sg.Button('Sair', font=font)]
]

# Layout do Menu de Contratos
MenuContratosLayout = [
    [sg.Text('Menu de Seleção', font=font3)],
    [sg.Text('')],
    [sg.Button('Contrato de Prestação de Serviços')],
    [sg.Button('Sair')]
]

# Layout do Formulário
FormularioLayout1 = [
    [sg.Text('Informações do Cliente', font=font3)], 
    [sg.Text('Indique o Nome da Empresa Cliente:'), sg.InputText(), #0  
     sg.Text('Indique o CNPJ do Cliente:'), sg.InputText(), ], #1
    [sg.Text('Indique o Endereço do Cliente:'), sg.InputText(),
     sg.Text('Indique o EMAIL do Cliente:'), sg.InputText()],
    [sg.Text('Indique o CEP do Cliente:'), sg.InputText(), sg.Text(
        'Indique a Cidade e o Estado do Cliente:'), sg.InputText()],
    [sg.Text('Indique o Nome do Representante do Cliente:'), sg.InputText(
    ), sg.Text('Indique o CPF do Representante Cliente:'), sg.InputText()],
    [sg.Text('Indique o RG do Presidente Cliente:'), sg.InputText(),
     sg.Text('Indique o órgão expedidor: '), sg.InputText()],
    [sg.Text('Indique o Cargo do Representante: '), sg.InputText(),
     sg.Text('Indique o Estado Civil do Cliente: '), sg.InputText()],
    [sg.Text('Indique o telefone de contato do Cliente: '), sg.InputText()],
    [sg.Text("Testemunha 1"), sg.InputText(),
    sg.Text("Testemunha 2"), sg.InputText()],
    [sg.Text("RG Testemunha 1"), sg.InputText(),
     sg.Text("RG Testemunha 2"), sg.InputText()],
    [sg.Text("CPF Testemunha 1"), sg.InputText(),
     sg.Text("CPF Testemunha 2"), sg.InputText()],
    
    
   
    [sg.Button('Continuar'), sg.Button('Sair')]
]

FormularioLayout2 = [
    [sg.Text('Dados Financeiros', font=font3)],
    [sg.Text('Indique o Valor Final do Serviço: '), sg.InputText()],
    [sg.Text('Diga como será feito o pagamento:'),
     sg.InputText('Presencial, ...')],
    [sg.Text('Indique o Titular da Conta que o pagamento será efetuado:'),
     sg.InputText()],
    [sg.Text('Indique o CNPJ da Conta do Pagamento: '), sg.InputText()],
    [sg.Text('Inidique o Banco em que será efetuado o pagamento:'), sg.InputText()],
    [sg.Text('Indique a Agência do Banco(Com dígito):'), sg.InputText()],
    [sg.Text("Indique a Conta(Com dígito): "), sg.InputText()],
    [sg.Button('Continuar'), sg.Button('Sair')]
]

FormularioLayout3 = [
    [sg.Text('Dos Serviços e Prazos', font=font3)],
    [sg.Text('Prazo para Execução do Projeto: '),
     sg.InputText("Números"),
     sg.Text('Escreva por extenso'),
     sg.InputText("")],
    [sg.Text('Prazo para Contato após finalizar: '),
     sg.InputText("Escreva por extenso"),
     sg.Text('Escreva por extenso'),
     sg.InputText("")],
    [sg.Text('Prazo para em dias para termino do serviço: '),
     sg.InputText("Escreva por extenso"),
     sg.Text('Escreva por extenso'),
     sg.InputText("")],
    [sg.Text('Descrição do Serviço: '), sg.InputText(
        'Descreva como deve estar no contrato')],
    [sg.Text('Descrição do Serviço2: '), sg.InputText(
        'Descreva como deve estar no contrato')],    
    [sg.Text('Descrição passo-a-passo do Serviço: '),
     sg.InputText("Descrição rápida")],
    [sg.Text('Vigência do Contrato: '), sg.InputText()],
    [sg.Text('Dia de Fechamento do Contrato: '),
     sg.InputText("XX de XXXX de XXXX")],
    [sg.Button('Finalizar'), sg.Button('Sair')]
]

PagamentoWindow = [

[sg.Text('Do Pagamento', font=font3)],
[sg.Button("Á vista sem juros") , sg.Button ("Em 2x com juros de 5%") ,sg.Button ("Em 3x com juros de 10%")],


]