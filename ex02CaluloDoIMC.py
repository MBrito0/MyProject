nome= input("Qual é o seu nome?")
peso= float(input('Qual é seu peso em kg?'))
altura=float(input('Qual sua altura em metros?'))

imc= peso / (altura * altura)

print(imc)

if imc < 18.5:
    print("Seu estado é de Magreza leve\nPrecisa rever sua alimentação.")
elif imc < 25:
 print("Você está Saudável.\nParabéns!")
elif imc < 30:
	print("Seu estado é de Sobrepeso\nPrecisa rever sua alimentação.")
elif imc < 35:
	print("Seu estado é de Obesidade Grau I\nProcure um médico ou nutricionista.")
elif imc < 40:
	print("Seu estado é de Obesidade Grau II (severa)\nProcure um médico ou nutricionista.")
else:
	print("Seu estado é de Obesidade Grau III (mórbida)\nProcure um médico ou nutricionista.")
