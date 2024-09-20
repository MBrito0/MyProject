print("Digite o número referente ao estado da moeda: ")
print("1.Flor de Cunho")
print("2.Soberba")
print("3.Muita bem conservada")
print("4.Bem conservada")
print("5.outros estados")

estado = int(input())

match estado:
    case 1 :
        print("Perfeita!Vou pagar R$1.000.000.00!")
    case 2 :
        print("Quase perfeita!Ofereço R$250.000.00!")
    case 3 :
        print("Que ótimo posso dar uns R$100.000.00!")
    case 4 :
        print("Que bom. Aceitaria R$30.000.00!")
    case 5 :
        print("Desculpe,não aceito neste estado.")
