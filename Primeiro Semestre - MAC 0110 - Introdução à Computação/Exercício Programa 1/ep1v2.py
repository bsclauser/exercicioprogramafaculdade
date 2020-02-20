def main ():

	estoque100 = 5
	estoque50 = 10
	estoque20 = 15
	estoque10 = 20

	while estoque100 or estoque50 or estoque20 or estoque10 > 0:
		saque = int(input("Valor do saque:"))
		while saque <= 0 or saque%10 != 0: 
			print("O valor do saque deve ser maior do que zero e múltiplo de 10. Tente novamente.")
			saque = int(input("Valor do saque:"))
		while (estoque100*100) + (estoque50*50) + (estoque20*20) + (estoque10*10) < saque:
				print ("O valor do saque solicitado é maior do que o valor do estoque de notas no caixa eletrônico. Tente um valor menor.")
				saque = int(input("Valor do saque:"))
				while saque <= 0 or saque%10 != 0: 
					print("O valor do saque deve ser maior do que zero e múltiplo de 10. Tente novamente.")
					saque = int(input("Valor do saque:"))
		
		notas100 = saque//100

		if notas100 <= estoque100:
			estoque100 -= notas100
			r100 = saque%100
		else:
			notas100 = estoque100
			estoque100 = 0
			r100 = (saque - (notas100*100))

		notas50 = r100//50

		if notas50 <= estoque50:
			estoque50 -= notas50
			r50 = r100%50
		else: 
			notas50 = estoque50
			estoque50 = 0
			r50 = (r100 - (notas50*50))
			
		notas20 = r50//20

		if notas20 <= estoque20:
			estoque20 -= notas20
			r20 = r50%20
		else:
			notas20 = estoque20
			estoque20 = 0
			r20 = (r50 - (notas20*20))

		notas10 = r20//10

		if notas10 <= estoque10:
			estoque10 -= notas10
		else:
			notas10 = estoque10
			estoque10 = 0

		print("Notas de 100:", notas100)
		print("Notas de 50:", notas50)
		print("Notas de 20:", notas20)
		print("Notas de 10:", notas10)
		print(estoque100, estoque50, estoque20, estoque10)

	else:
		print("O estoque de notas acabou. Espere o caixa ser reabastecido.")

main ()








