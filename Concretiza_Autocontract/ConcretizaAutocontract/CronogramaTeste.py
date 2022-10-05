
def cronogramacompleto():
    totaldepassos = int(input("Insira o numero total de passos:\n"))
    for numero in range(0,totaldepassos):
        cronograma = str(input("Digite o cronograma do projeto"))
        print(cronograma, numero)
        if cronograma == "Fim":
            break

cronogramacompleto()
