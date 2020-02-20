from random import seed, randrange 
# Gera n números aleatórios no intervalo [a, b) 
def GeraAmostra(a, b, n): 
	# Use o seu NUSP como semente      
	NUSP = 11221230
	seed(NUSP)     
	amostra = n * [0] 
	for k in range(n):         
	 	amostra[k] = a + float(randrange(1000000)) * (b - a)/1000000.0 

	return amostra


def PrintAmostra(a, b, length, ga):
	print("Amostra:")
	novoa = len(str(a)) + 2
	novob = len(str(b)) + 2
	difcar = novob - novoa
	for i in range (1, length):
		if i == 0 or (i%10) != 0:
			print (" "*difcar, "%10.3f" %ga[i-1], end="")
		else:
			 print (" "*difcar ,"%10.3f" %ga[i-1])
	print()


def main():
	a, b = map(float, input("Entre com o intervalo:").split())
	n = int(input("Entre com a quantidade de elementos na amostra:"))
	while n <= 0: 
		n = int(input("A quantidade de elementos na amostra deve ser um número positivo diferente de zero. Tente novamente. \nEntre com a quantidade de elementos na amostra:"))
	while (b-a)/n < 0.001:
		print("Os valores que você inseriu para o intervalo são inválidos. \nOs valores do intervalo devem ser diferentes e o segundo deve ser maior que o primeiro. \nTente novamente.")
		main()
	ga = GeraAmostra(a, b, n)
	length = len(ga) + 1
	PrintAmostra(a, b, length, ga)
	while True:
		nintervalo = int(input("Entre com o número de intervalos:"))
		if nintervalo <= 0:
			main()
		valorint = (b-a)/nintervalo
		inter = a
		inter2 = 0.000
		cont = [0]*nintervalo
		for i in range (nintervalo):
			inter2 = inter 
			inter += valorint
			for j in range (len(ga)):
				if ga[j] < inter and ga[j] >= inter2:
					cont[i] += 1
		print ("          Intervalo     ", "         Frequência     ", "     Gráfico     ")
		inter = a
		inter2 = 0.000
		for j in range (nintervalo):
			inter2 = inter 
			inter += valorint
			novointer = len(str(inter))
			novointer2 = len(str(inter2))
			novafreq = len(str(cont[j]))
			dif = novointer2 - novointer
			print(" "*dif , "%12.3f" %inter2, "A", " "*dif  ,"%12.3f" %inter, end="")
			print("%12d" %cont[j], end="")
			for u in range (cont[j]):
				print("\u25a0", end="")
			print()
main()