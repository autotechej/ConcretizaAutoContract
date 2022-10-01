# Este arquivo armazena as funções da interface, caso queira rodar a interface só é necessário a função MenuPrincipal()

# Aqui são importados a biblioteca da interface gráfica e a biblioteca criada por mim que contem os Layouts das janelas
from optparse import Values
import PySimpleGUI as sg
import Layouts as lyt


# Essa função capta e armazena os dados de pagamento
def Formulario3():
    global FormularioWindow3, event6, values6, Prazo1,Prazo3, Prazo2, DescricaoServico,DescricaoServico2, DescricaoPassoAPasso, Vigencia, DataFechamento,extenso1, extenso2, extenso3
    FormularioWindow3 = sg.Window("Autotech AutoContract", lyt.FormularioLayout3)
    event6, values6 = FormularioWindow3.read()
    Prazo1 = values6[0]  # usado
    extenso1= values6[1]
    Prazo2 = values6[2]  # usado
    extenso2 = values6[3]
    Prazo3 = values6[4]
    extenso3 = values6[5]
    DescricaoServico = values6[6]  # usado
    DescricaoServico2 = values6[7]
    DescricaoPassoAPasso = values6[8]  # usado
    Vigencia = values6[9]  # usado
    DataFechamento = values6[10]  # usado
    if event6 == 'Finalizar':
        FormularioWindow3.close()
    elif event6 == 'Sair' or event6 == sg.WIN_CLOSED:
        FormularioWindow3.close()


# Essa função capta e armazena os dados da EJ
def Formulario2():
    global FormularioWindow2, event5, values5, ValorFinal, DescricaoPagamento, Titular, CNPJPagamento, Banco, Agencia, Conta
    FormularioWindow2 = sg.Window(
        "Concretiza AutoContract", lyt.FormularioLayout2)
    event5, values5 = FormularioWindow2.read()
    ValorFinal = values5[0]  # usado
    DescricaoPagamento = values5[1]  # usado
    Titular = values5[2]  # usado
    CNPJPagamento = values5[3]
    Banco = values5[4]  # usado
    Agencia = values5[5]  # usado
    Conta = values5[6]  # usado

    if event5 == 'Continuar':
        FormularioWindow2.close()
        PagamentoWindow()
    elif event5 == 'Sair' or event5 == sg.WIN_CLOSED:
        FormularioWindow2.close()

# Essa função capta e armazena os dados do cliente


def Formulario():
    # Declara as variáveis de forma global para serem usadas em outras funções e locais
    global FormularioWindow, event4, values4, NomeCliente, Testemunha1, Testemunha2, TelefoneRepresentante, EstadoCivilRepresentante, CargoRepresentante, NomeEmpresa, CNPJCliente, OrgaoExpedidor, RGRepresentante, EnderecoCliente, CPFRepresentante, CEPcliente, CidadeEstadoCliente, NomeRepresentante, EMAILCliente,  CPFTestemunha1, CPFTestemunha2, RGtestemunha1, RGtestemunha2
    # A função Window cria a janela com o layout especificado
    FormularioWindow = sg.Window(
        "Concretiza AutoContract", lyt.FormularioLayout1)
    # event armazena as informações passadas pelos botões em strings
    # values armazena as informações passadas pelas caixas de texto em strings de um dicionário
    # A função read lê os dados da janela(Botões e caixas de texto)
    event4, values4 = FormularioWindow.read()
    NomeEmpresa = values4[0]  # usado
    CNPJCliente = values4[1]  # usado
    EnderecoCliente = values4[2]  # usado
    EMAILCliente = values4[3]  # usado
    CEPcliente = values4[4]  # usado
    CidadeEstadoCliente = values4[5]  # usado
    NomeRepresentante = values4[6]  # usado
    CPFRepresentante = values4[7]  # usado
    RGRepresentante = values4[8]  # usado
    OrgaoExpedidor = values4[9]  # usado
    CargoRepresentante = values4[10]  # usado
    EstadoCivilRepresentante = values4[11]  # usado
    TelefoneRepresentante = values4[12]  # usado
    Testemunha1 = values4[13]  # usado
    Testemunha2 = values4[14]  # usado
    RGtestemunha1 = values4[15]
    RGtestemunha2 = values4[16]
    CPFTestemunha1 = values4[17]  # usado
    CPFTestemunha2 = values4[18]  # usado
    
   

    if event4 == 'Continuar':
        FormularioWindow.close()
        Formulario2()

    elif event4 == 'Sair' or event4 == sg.WIN_CLOSED:
        FormularioWindow.close()

# A função que executa a janela do Menu de Contratos


def MenuPreencherContratos():
    global ContratosWindow, event2, values2, TipoContrato
    ContratosWindow = sg.Window("Concretiza AutoContract", lyt.MenuContratosLayout, size=(
        350, 200), element_justification='c')
    event2, values2 = ContratosWindow.read()
    # Caso clique em continuar o programa verifica qual o contrato desejado
    if event2 == 'Contrato de Prestação de Serviços':
        ContratosWindow.close()
        Formulario()
    # Caso clique sair o programa encerra
    elif event2 == 'Sair' or event2 == sg.WIN_CLOSED:
        ContratosWindow.close()

# A função que executa a janela do Menu Principal, dentro dela são executadas as outras


def MenuPrincipal():
    global MenuWindow, event1, values1, PagamentoWindow
    MenuWindow = sg.Window("Concretiza AutoContract", lyt.MenuPrincipalLayout, size=(
        400, 350), element_justification='c')
    event1, values1 = MenuWindow.read()
    # Caso clique Preencher Novo Contrato ele abre o menu de contratos
    if event1 == 'Preencher Novo Contrato':
        MenuWindow.close()
        MenuPreencherContratos()
    # Caso clique Sair ele encerra o programa
    elif event1 == 'Sair' or event1 == sg.WIN_CLOSED:
        MenuWindow.close()


def PagamentoWindow():
    global event7, values7, pgto, Pagamento
    PagamentosWindow = sg.Window(
        "Concretiza AutoContract", lyt.PagamentoWindow)
    event7, values7 = PagamentosWindow.read()
    if event7 == "Á vista sem juros" or "Em 2x com juros de 5%" or "Em 3x com juros de 10%":
        pgto = event7
        valordopagamento()
        PagamentosWindow.close
        Formulario3()


def valordopagamento():

    global Pagamento, pgto

    match pgto:
        case "Á vista sem juros":
            Pagamento = f"O pagamento será feito á vista (sem prestações) e dentro de 3 dias úteis, no valor de R${ValorFinal}"
        case "Em 2x com juros de 5%":
            Pagamento = f"O Pagamento será feito em duas prestações iguais, sendo a primeira paga antes do inicio do serviço e a segunda em dentro de 1 mês após o inicio do mesmo, no valor de R${round((float(ValorFinal)*1.05)/2,2)}"
        case "Em 3x com juros de 10%":
            Pagamento = f"O pagamento será feito em três prestações iguais, sendo a primeira paga antes do inicio do serviço e as seguintes com até um mês passados o pagamento anterior com parcelas de 3x R${round((float(ValorFinal)*1.1)/3,2)}"

            