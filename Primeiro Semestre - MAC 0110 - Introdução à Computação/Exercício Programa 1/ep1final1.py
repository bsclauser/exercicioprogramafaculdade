def main ():

	#Estoque do caixa eletrônico
	estoque100 = 5
	estoque50 = 10
	estoque20 = 15
	estoque10 = 20

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
	#nestoquex = novo estoque das notas de valor x

	#Notas de 100	
	notas100 = saque//100

	if notas100 <= estoque100:
		nestoque100 = estoque100 - notas100
		r100 = saque%100
	#Se a quantidade de notas de 100 necessárias para suprir o saque é maior do que o valor disponível no estoque
	#Utiliza-se todo o estoque disponível e calcula o valor que a ainda falta ser suprido pelas outras notas.
	else:
		notas100 = estoque100
		nestoque100 = 0
		r100 = (saque - (notas100*100))

	#Notas de 50
	notas50 = r100//50

	if notas50 <= estoque50:
		nestoque50 = estoque50 - notas50
		r50 = r100%50
	#Se a quantidade de notas de 50 necessárias para suprir o saque é maior do que o valor disponível no estoque
	#Utiliza-se todo o estoque disponível e calcula o valor que a ainda falta ser suprido pelas outras notas.
	else: 
		notas50 = estoque50
		nestoque50 = 0
		r50 = (r100 - (notas50*50))
		
	#Notas de 20
	notas20 = r50//20

	if notas20 <= estoque20:
		nestoque20 = estoque20 - notas20
		r20 = r50%20
	#Se a quantidade de notas de 20 necessárias para suprir o saque é maior do que o valor disponível no estoque
	#Utiliza-se todo o estoque disponível e calcula o valor que a ainda falta ser suprido pelas outras notas.
	else:
		notas20 = estoque20
		nestoque20 = 0
		r20 = (r50 - (notas20*20))

	#Notas de 10
	notas10 = r20//10

	if notas10 <= estoque10:
		nestoque10 = estoque10 - notas10
	#Se a quantidade de notas de 10 necessárias para suprir o saque é maior do que o valor disponível no estoque
	#Utiliza-se todo o estoque disponível.
	else:
		notas10 = estoque10
		nestoque10 = 0

	#Imprime a quantidade de notas de cada valor necessárias para suprir o valor do saque
	print("Notas de 100:", notas100)
	print("Notas de 50:", notas50)
	print("Notas de 20:", notas20)
	print("Notas de 10:", notas10)

    #A partir daqui, ocorre o pedido de todos os outros saques que utilizam o "nestoque" como base, ao invés do "estoquex"
	while nestoque100 or nestoque50 or nestoque20 or nestoque10 > 0:
		saque = int(input("Valor do saque:"))
		#Consistência
		while saque <= 0 or saque%10 != 0: 
			print("O valor do saque deve ser maior do que zero e múltiplo de 10. Tente novamente.")
			saque = int(input("Valor do saque:"))
		#Verifica se o valor do saque solicitado é maior do que o valor do novo estoque do caixa eletrônico
		while (nestoque100*100) + (nestoque50*50) + (nestoque20*20) + (nestoque10*10) < saque:
			print ("O valor do saque solicitado é maior do que o valor do estoque de notas no caixa eletrônico. Tente um valor menor.")
			saque = int(input("Valor do saque:"))
			#Consistência novamente, pois foi solicitado o saque
			while saque <= 0 or saque%10 != 0: 
				print("O valor do saque deve ser maior do que zero e múltiplo de 10. Tente novamente.")
				saque = int(input("Valor do saque:"))
		
		#Cálculo das notas para o valor do saque
		#nnotasx = nova quantidade de notas de valor x

		#Notas de 100
		#Verifica se o novo estoque está zerado ou não
		if nestoque100 != 0:

			nnotas100 = saque//100

			if nnotas100 <= nestoque100:
				nestoque100 -= nnotas100
				r100 = saque%100
			#Se a quantidade de notas de 100 necessárias para suprir o saque é maior do que o valor disponível no estoque
			#Utiliza-se todo o estoque disponível.
			else:
				nnotas100 = nestoque100
				nestoque100 = 0
				r100 = (saque - (nnotas100*100))
		#Se o estoque de notas de 100 está zerado, a quantidade de notas é zero e o valor do saque não é suprido parcialmente ou totalmente
		else:
			nnotas100 = 0
			r100 = saque
				
		#Notas de 50
		#Verifica se o novo estoque está zerado ou não
		if nestoque50 != 0:

			nnotas50 = r100//50

			if nnotas50 <= nestoque50:
				nestoque50 -= nnotas50
				r50 = r100%50
			#Se a quantidade de notas de 50 necessárias para suprir o saque é maior do que o valor disponível no estoque
			#Utiliza-se todo o estoque disponível.
			else: 
				nnotas50 = nestoque50
				nestoque50 = 0
				r50 = (r100 - (nnotas50*50))
		#Se o estoque de notasd de 50 está zerado, a quantidade de notas é zero e o valor do saque não é suprido parcialmente ou totalmente
		else: 
			nnotas50 = 0
			r50 = saque
				
		#Notas de 20
		#Verifica se o novo estoque está zerado ou não
		if nestoque20 != 0:

			nnotas20 = r50//20

			if nnotas20 <= nestoque20:
				nestoque20 -= nnotas20
				r20 = r50%20
			#Se a quantidade de notas de 20  necessárias para suprir o saque é maior do que o valor disponível no estoque
			#Utiliza-se todo o estoque disponível.
			else: 
				nnotas20 = nestoque20
				nestoque20 = 0
				r20 = (r50 - (nnotas20*20))
		#Se o estoque de notas de 20 está zerado, a quantidade de notas é zero e o valor do saque não é suprido parcialmente ou totalmente
		else: 
			nnotas20 = 0
			r20 = saque
				
		#Notas de 10
		#Verifica se o novo estoque está zerado ou não
		if nestoque10 != 0:

			nnotas10 = r20//10

			if nnotas10 <= nestoque10:
				nestoque10 -= nnotas10
			#Se a quantidade de notas de 10 necessárias para suprir o saque é maior do que o valor disponível no estoque
			#Utiliza-se todo o estoque disponível.
			else:
				nnotas10 = nestoque10
				nestoque10 = 0
		#Se o estoque de notas de 10 está zerado, a quantidade de notas é zero e o valor do saque não é suprido por nenhuma nota
		else:
			nnotas10 = 0
				
		#Imprime a quantidade de notas de cada valor necessárias para suprir o valor do saque
		print("Notas de 100:", nnotas100)
		print("Notas de 50:", nnotas50)
		print("Notas de 20:", nnotas20)
		print("Notas de 10:", nnotas10)

	#Se todos os novos estoques são iguais a zero aparece a seguinte mensagem e o programa acaba
	else:
		print("O estoque de notas acabou. Espere o caixa ser reabastecido.")

main ()








