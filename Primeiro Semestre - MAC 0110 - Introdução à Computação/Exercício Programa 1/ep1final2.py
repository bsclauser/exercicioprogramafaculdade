def main ():

	#Estoque de notas do caixa eletrônico
	estoque100 = 5
	estoque50 = 10
	estoque20 = 15
	estoque10 = 20

	#Verifica se há estoque e deixa o programa rodar até o estoque de todas as notas acabarem
	while estoque100 or estoque50 or estoque20 or estoque10 > 0:
		#Solicita o valor do saque
		saque = int(input("Valor do saque:"))
		#Consistência
		while saque <= 0 or saque%10 != 0: 
			print("O valor do saque deve ser maior do que zero e múltiplo de 10. Tente novamente.")
			saque = int(input("Valor do saque:"))
		#Verifica se o valor do saque solicitado é maior do que o valor do estoque do caixa eletrônico
		while (estoque100*100) + (estoque50*50) + (estoque20*20) + (estoque10*10) < saque:
				print ("O valor do saque solicitado é maior do que o valor do estoque de notas no caixa eletrônico. Tente um valor menor.")
				saque = int(input("Valor do saque:"))
				#Consistência novamente, pois foi solicitado o saque
				while saque <= 0 or saque%10 != 0: 
					print("O valor do saque deve ser maior do que zero e múltiplo de 10. Tente novamente.")
					saque = int(input("Valor do saque:"))
		
	    #Cálculo das notas para o valor do saque

	    #Notas de 100
		notas100 = saque//100

		if notas100 <= estoque100:
			estoque100 -= notas100
			r100 = saque%100
		#Se a quantidade de notas de 100 necessárias para suprir o saque é maior do que o valor disponível no estoque
		#Utiliza-se todo o estoque disponível.
		else:
			notas100 = estoque100
			estoque100 = 0
			r100 = (saque - (notas100*100))

		#Notas de 50
		notas50 = r100//50

		if notas50 <= estoque50:
			estoque50 -= notas50
			r50 = r100%50
		#Se a quantidade de notas de 50  necessárias para suprir o saque é maior do que o valor disponível no estoque
		#Utiliza-se todo o estoque disponível.
		else: 
			notas50 = estoque50
			estoque50 = 0
			r50 = (r100 - (notas50*50))
			
		#Notas de 20
		notas20 = r50//20

		if notas20 <= estoque20:
			estoque20 -= notas20
			r20 = r50%20
		#Se a quantidade de notas de 20 necessárias para suprir o saque é maior do que o valor disponível no estoque
		#Utiliza-se todo o estoque disponível.
		else:
			notas20 = estoque20
			estoque20 = 0
			r20 = (r50 - (notas20*20))

		#Notas de 10
		notas10 = r20//10

		if notas10 <= estoque10:
			estoque10 -= notas10
		#Se a quantidade de notas de 10 necessárias para suprir o saque é maior do que o valor disponível no estoque
		#Utiliza-se todo o estoque disponível.
		else:
			notas10 = estoque10
			estoque10 = 0

		#Imprime a quantidade de notas de cada valor necessárias para suprir o valor do saque
		print("Notas de 100:", notas100)
		print("Notas de 50:", notas50)
		print("Notas de 20:", notas20)
		print("Notas de 10:", notas10)

	#Se todos os estoques são iguais a zero aparece a seguinte mensagem e o programa acaba
	else:
		print("O estoque de notas acabou. Espere o caixa ser reabastecido.")

main ()








