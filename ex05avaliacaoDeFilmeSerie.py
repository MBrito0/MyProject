""" print("Digite o número referente à sua avaliação do filme/série: ")
print("1.Péssimo")
print("2.Ruim")
print("3.Razoável")
print("4.Bom")
print("5.Ótimo")

avaliacao = int(input())

match avaliacao:
    case 1 :
        print("Você avaliou como: Péssimo")
        descricao= input("Por que você avaliou dessa forma?")
        print(f"Motivo: {descricao}")
    case 2 :
        print("Você avaliou como: Ruim")
        descricao= input("Por que você avaliou dessa forma?")
        print(f"Motivo: {descricao}")
    case 3 :
        print("Você avaliou como: Razoável")
        descricao= input("No que podemos melhorar?")
        print(f"Motivo: {descricao}")
    case 4 :
        print("Você avaliou como: Bom")
        descricao= input("O que falta pra ser ótimo?")
        print(f"Motivo: {descricao}")
    case 5 :
        print("Você avaliou como: Ótimo")
        print("Obrigado pela preferência!")
    case 6 :
        print("Nota inválida. Insira um valor entre 1 e 5")   
    
 """

conteudo = input("Qual filme/série preferido? ")
print("1 é Péssimo e 5 Ótimo")
avaliacao = int(input("Atribuir uma nota 1 a 5: "))

match avaliacao:
    case 1 :
        print("Você avaliou como: Péssimo")
        descricao= input("Por que você avaliou dessa forma?")
        print(f"Motivo: {descricao}")
    case 2 :
        print("Você avaliou como: Ruim")
        descricao= input("Por que você avaliou dessa forma?")
        print(f"Motivo: {descricao}")
    case 3 :
        print("Você avaliou como: Razoável")
    case 4 :
        print("Você avaliou como: Bom")
    case 5 :
        print("Você avaliou como: Ótimo")
    case _ :
        print("Nota inválida. Insira um valor entre 1 e 5") 