from Functions import ValorFinal


pagar = "Á vista sem juros"

def valordopagamento():
        global pgto, ValorFinal
        pgto = 0
        match pagar:
            case "Á vista sem juros":
                pgto == f"O pagamento será feito á vista (sem prestações) e dentro de 3 dias úteis, no valor de {ValorFinal}"
            case "Em 2x com juros de 5%":
                pgto == f"O Pagamento será feito em duas prestações iguais, sendo a primeira paga antes do inicio do projeto e a segunda em dentro de 1 mês após o inicio do mesmo, no valor de {(ValorFinal x 1.05)/2}"
    print(pgto)
