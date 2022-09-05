#Este arquivo armazena as funções da interface, caso queira rodar a interface só é necessário a função MenuPrincipal()

#Aqui são importados a biblioteca da interface gráfica e a biblioteca criada por mim que contem os Layouts das janelas
import PySimpleGUI as sg
import Layouts as lyt



#Essa função capta e armazena os dados de pagamento
def Formulario3():
    global FormularioWindow3, event6, values6, Prazo1, Prazo2, DescricaoSistema, DescricaoPassoAPasso, Vigencia, DataFechamento
    FormularioWindow3 = sg.Window("Autotech AutoContract", lyt.FormularioLayout3)
    event6, values6 = FormularioWindow3.read()
    Prazo1 = values6[0]
    Prazo2 = values6[1]
    DescricaoSistema = values6[2]
    DescricaoPassoAPasso = values6[3]
    Vigencia = values6[4]
    DataFechamento = values6[5]
    if event6 == 'Finalizar':
        FormularioWindow3.close()
    elif event6 == 'Sair' or event6 == sg.WIN_CLOSED:
        FormularioWindow3.close()


#Essa função capta e armazena os dados da EJ
def Formulario2():
    global FormularioWindow2, event5, values5, ValorFinal, DescricaoPagamento, Titular, CNPJPagamento, Banco, Agencia, Conta
    FormularioWindow2 = sg.Window("Concretiza AutoContract", lyt.FormularioLayout2)
    event5, values5 = FormularioWindow2.read()
    ValorFinal = values5[0]
    DescricaoPagamento = values5[1]
    Titular = values5[2]
    CNPJPagamento = values5[3]
    Banco = values5[4]
    Agencia = values5[5]
    Conta = values5[6]
    if event5 == 'Continuar':
        FormularioWindow2.close()
        Formulario3()
    elif event5 == 'Sair' or event5 == sg.WIN_CLOSED:
        FormularioWindow2.close()

#Essa função capta e armazena os dados do cliente
def Formulario():
    #Declara as variáveis de forma global para serem usadas em outras funções e locais
    global FormularioWindow, event4, values4, NomeCliente, TelefoneRepresentante, EstadoCivilRepresentante, CargoRepresentante, NomeEmpresa, CNPJCliente, OrgaoExpedidor, RGRepresentante, EnderecoCliente,CPFRepresentante, CEPcliente, CidadeEstadoCliente, NomeRepresentante, EMAILCliente
    #A função Window cria a janela com o layout especificado
    FormularioWindow = sg.Window("Concretiza AutoContract", lyt.FormularioLayout1)
    #event armazena as informações passadas pelos botões em strings
    #values armazena as informações passadas pelas caixas de texto em strings de um dicionário
    #A função read lê os dados da janela(Botões e caixas de texto)
    event4, values4 = FormularioWindow.read()
    NomeEmpresa=values4[0]
    CNPJCliente=values4[1]
    EnderecoCliente=values4[2]
    EMAILCliente=values4[3]
    CEPcliente=values4[4]
    CidadeEstadoCliente=values4[5]
    NomeRepresentante=values4[6]
    CPFRepresentante=values4[7]
    RGRepresentante=values4[8]
    OrgaoExpedidor=values4[9]
    CargoRepresentante=values4[10]
    EstadoCivilRepresentante=values4[11]
    TelefoneRepresentante=values4[12]

    if event4 == 'Continuar':
        FormularioWindow.close()
        Formulario2()
        
    elif event4 =='Sair' or event4 == sg.WIN_CLOSED:
        FormularioWindow.close()

#A função que executa a janela do Menu de Contratos
def MenuPreencherContratos():
    global ContratosWindow, event2, values2, TipoContrato
    ContratosWindow = sg.Window("Concretiza AutoContract", lyt.MenuContratosLayout, size=(350,200), element_justification='c')
    event2, values2 = ContratosWindow.read()
    #Caso clique em continuar o programa verifica qual o contrato desejado
    if event2 == 'Contrato de Prestação de Serviços':
        ContratosWindow.close()
        Formulario()
    #Caso clique sair o programa encerra
    elif event2 == 'Sair' or event2 == sg.WIN_CLOSED:
        ContratosWindow.close()

#A função que executa a janela do Menu Principal, dentro dela são executadas as outras
def MenuPrincipal():
    global MenuWindow, event1, values1
    MenuWindow = sg.Window("Concretiza AutoContract", lyt.MenuPrincipalLayout, size=(400,350), element_justification='c')
    event1, values1 = MenuWindow.read()
    #Caso clique Preencher Novo Contrato ele abre o menu de contratos
    if event1 == 'Preencher Novo Contrato':
        MenuWindow.close()
        MenuPreencherContratos()
    #Caso clique Sair ele encerra o programa
    elif event1 == 'Sair' or event1 == sg.WIN_CLOSED:
        MenuWindow.close()
