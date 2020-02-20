def main ():


	estoque100 = 5
	estoque50 = 10
	estoque20 = 15
	estoque10 = 20


	saque = int(input("Valor do saque:"))
	#Consistência
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
		nestoque100 = estoque100 - notas100
		r100 = saque%100
	else:
		notas100 = estoque100
		nestoque100 = 0
		r100 = (saque - (notas100*100))


	notas50 = r100//50

	if notas50 <= estoque50:
		nestoque50 = estoque50 - notas50
		r50 = r100%50
	else: 
		notas50 = estoque50
		nestoque50 = 0
		r50 = (r100 - (notas50*50))
		

	notas20 = r50//20

	if notas20 <= estoque20:
		nestoque20 = estoque20 - notas20
		r20 = r50%20
	else:
			notas20 = estoque20
			nestoque20 = 0
			r20 = (r50 - (notas20*20))


	notas10 = r20//10

	if notas10 <= estoque10:
		nestoque10 = estoque10 - notas10
	else:
		notas10 = estoque10
		nestoque10 = 0

	print("Notas de 100:", notas100)
	print("Notas de 50:", notas50)
	print("Notas de 20:", notas20)
	print("Notas de 10:", notas10)
	print(nestoque100, nestoque50, nestoque20, nestoque10)

	while nestoque100 or nestoque50 or nestoque20 or nestoque10 > 0:
		saque = int(input("Valor do saque:"))
		#Consistência
		while saque <= 0 or saque%10 != 0: 
			print("O valor do saque deve ser maior do que zero e múltiplo de 10. Tente novamente.")
			saque = int(input("Valor do saque:"))
			
		while (nestoque100*100) + (nestoque50*50) + (nestoque20*20) + (nestoque10*10) < saque:
			print ("O valor do saque solicitado é maior do que o valor do estoque de notas no caixa eletrônico. Tente um valor menor.")
			saque = int(input("Valor do saque:"))
			while saque <= 0 or saque%10 != 0: 
				print("O valor do saque deve ser maior do que zero e múltiplo de 10. Tente novamente.")
				saque = int(input("Valor do saque:"))
			

		if nestoque100 != 0:

			nnotas100 = saque//100

			if nnotas100 <= nestoque100:
				nestoque100 -= nnotas100
				r100 = saque%100
			else:
				nnotas100 = nestoque100
				nestoque100 = 0
				r100 = (saque - (nnotas100*100))

		else:
			nnotas100 = 0
			r100 = saque
				

		if nestoque50 != 0:

			nnotas50 = r100//50

			if nnotas50 <= nestoque50:
				nestoque50 -= nnotas50
				r50 = r100%50
			else: 
				nnotas50 = nestoque50
				nestoque50 = 0
				r50 = (r100 - (nnotas50*50))

		else: 
			nnotas50 = 0
			r50 = saque
				

		if nestoque20 != 0:

			nnotas20 = r50//20

			if nnotas20 <= nestoque20:
				nestoque20 -= nnotas20
				r20 = r50%20
			else: 
				nnotas20 = nestoque20
				nestoque20 = 0
				r20 = (r50 - (nnotas20*20))

		else: 
			nnotas20 = 0
			r20 = saque
				

		if nestoque10 != 0:

			nnotas10 = r20//10

			if nnotas10 <= nestoque10:
				nestoque10 -= nnotas10
			else:
				nnotas10 = nestoque10
				nestoque10 = 0

		else:
			nnotas10 = 0
				
		print("Notas de 100:", nnotas100)
		print("Notas de 50:", nnotas50)
		print("Notas de 20:", nnotas20)
		print("Notas de 10:", nnotas10)
		print(nestoque100, nestoque50, nestoque20, nestoque10)

	else:
		print("O estoque de notas acabou. Espere o caixa ser reabastecido.")

main ()








