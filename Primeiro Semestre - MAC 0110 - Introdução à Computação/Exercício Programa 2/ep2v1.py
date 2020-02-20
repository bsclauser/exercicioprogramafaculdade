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


def main():
	a, b = map(float, input("Entre com o intervalo:").split())
	#while  b == a or a > b:
		#a, b = map(float, input("O intervalo deve ser entre dois números diferentes sendo o primeiro menor que o segundo. \nEntre com o intervalo:").split())
	n = int(input("Entre com a quantidade de elementos na amostra:"))
	while n <= 0: 
		n = int(input("A quantidade de elementos na amostra deve ser um número positivo diferente de zero. Tente novamente. \nEntre com a quantidade de elementos na amostra:"))
	while (b-a)/n < 0.001:
		print("Os valores que você inseriu para o intervalo são inválidos. \nOs valores do intervalo devem ser diferentes e o segundo deve ser maior que o primeiro. \nTente novamente.")
		main()
	ga = GeraAmostra(a, b, n)
	length = len(ga) + 1
	print("Amostra:")
	for i in range (1, length):

		if i == 0 or (i%10) != 0:
			print ("%10.4f" %ga[i-1], end="")

		else:
			print ("%10.4f" %ga[i-1])
	print()
	while True:
		nintervalo = int(input("Entre com o número de intervalos:"))
		if nintervalo <= 0:
			main()
		valorint = (b-a)/nintervalo
		print (valorint)
		inter = 0.000
		ii = []*(nintervalo+1)
	
		for i in range (nintervalo):
			ninter = inter + valorint
			ii.append(ninter)
			inter += valorint
		
			

		
			




main()


