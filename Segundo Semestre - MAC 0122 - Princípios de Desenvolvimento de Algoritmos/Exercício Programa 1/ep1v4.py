import time


def LeiaMatrizLocal(NomeArquivo):
	# retorna a matriz lida se ok ou uma lista vazia senão 
	# abrir o arquivo para leitura
	try:
		arq = open(NomeArquivo, "r") 
	except:
		 return [] # retorna lista vazia se deu erro 
	# inicia matriz SudoKu a ser lida 
	mat = [9 * [0] for k in range(9)] 
	# ler cada uma das linhas do arquivo 
	i = 0 
	for linha in arq:
		 v = linha.split() 
		 # verifica se tem 9 elementos e se são todos entre '1' e '9' 
		 valorinvalido = 0
		 try:
			 for a in range(len(v)):
				 if int(v[a])>9 or int(v[a])<0:
					 valorinvalido += 1
		 except: 
			 print("Matriz inválida. Valor(es) não inteiros na matriz. Tente novamente com uma matriz válida.")
			 return None
		 if len(v) != 9 and valorinvalido != 0:
			 print("Matriz inválida. Matriz não possui 9 elementos por linha e seus valores não se encontram entre 1 e 9. Tente novamente com uma matriz válida.")
			 arq.close()
			 return None
		 elif len(v) != 9:
			 print("Matriz inválida. Há mais de nove elementos por linha da matriz. Tente novamente com uma matriz válida.")
			 arq.close()
			 return None
		 elif valorinvalido != 0:
			 print("Matriz inválida. Há valores que não se encontram entre 1 e 9 nas linhas da matriz. Tente novamente com uma matriz válida.")
			 arq.close()
			 return None
		 # transforma de texto para int 
		 for j in range(len(v)): 
			  mat[i][j] = int(v[j]) 
		 # faz as consistências iniciais da matriz dada 
		 resultado = TestaMatrizLida(mat)
		 if resultado == None:
			 return None
		 i = i + 1
    
	# fechar arquivo e retorna a matriz lida e consistida 
	arq.close()
	return mat



def Quadrados(mat):
	quadrado1 = []
	quadrado2 = []
	quadrado3 = []
	quadrado4 = []
	quadrado5 = []
	quadrado6 = []
	quadrado7 = []
	quadrado8 = []
	quadrado9 = []
	quadrado1 = mat[0:3][0:3]
	quadrado2 = mat[0:3][3:6]
	quadrado3 = mat[0:3][6:9]
	quadrado4 = mat[3:6][0:3]
	quadrado5 = mat[3:6][3:6]
	quadrado6 = mat[3:6][6:9]
	quadrado7 = mat[6:9][0:3]
	quadrado8 = mat[6:9][3:6]
	quadrado9 = mat[6:9][3:6]
	return quadrado1, quadrado2, quadrado3, quadrado4, quadrado5, quadrado6, quadrado7, quadrado8, quadrado9



def ProcuraElementoLinha (Mat, L, d):
	for s in range(9):
		if Mat[L][s] == d:
			return s
	return -1



def ProcuraElementoColuna (Mat, C, d):
	for p in range(9):
		if Mat[p][C] == d:
			return p
	return -1



def ProcuraElementoQuadrado (Mat, L, C, p):
	Ln = (L//3)*3
	Cn = (C//3)*3
	for i in range(Ln,Ln+3):
		for j in range(Cn,Cn+3):
			if Mat[i][j]== p:
				return (i,j)
	return -1



def ImprimaMatriz (Mat):
	print()
	for a in range(9):
		for b in range(9):
			if b == 8:
				print (Mat[a][b])
			else:
				print (Mat[a][b], " ", end = " ")



def TestaMatrizLida(Mat): 
	#consistência das linhas
	linhas = []
	c = 0
	h = 1
	while c < 9:
		linhas = Mat[c][:]
		c += 1
		while h < 10:
			contador1 = linhas.count(h)
			if contador1 > 1:
				print("Matriz inválida. Há números repetidos nas linhas. Tente novamente com uma matriz válida.")
				return None
			h += 1
	#consistência das colunas
	colunas = []
	w = 0
	p = 1
	while w < 0:
		colunas[w] = Mat[:][w]
		w += 1
		while p < 10:
			contador2 = colunas.count(p)
			if contador2 > 1:
				print("Matriz inválida. Há números repetidos nas colunas. Tente novamente com uma matriz válida.")
				return None
			p += 1
	#consistência dos quadrados
	quadrado1, quadrado2, quadrado3, quadrado4, quadrado5, quadrado6, quadrado7, quadrado8, quadrado9 = Quadrados(Mat)
	for g in range (1,10):
		if quadrado1.count(g) > 1 or quadrado2.count(g) > 1 or quadrado3.count(g)> 1 or quadrado4.count(g) > 1 or quadrado5.count(g) > 1 or quadrado6.count(g) > 1 or quadrado7.count(g) > 1 or quadrado8.count(g) > 1 or quadrado9.count(g) > 1:
			print("Matriz inválida. Há números repetidos no(s) quadrado(s) interno(s). Tente novamente com uma matriz válida.")
			return None
	return True



def TestaMatrizPreenchida(Matriz): 
	a = TestaMatrizLida(Matriz)
	if a:
		return True
	if a ==  None:
		return False



def TemZero(matriz):
	elemzero = 0
	for a in range(9):
		for b in range(9):
			if matriz[a][b] == 0:
				elemzero = 1
				return [a,b,elemzero]
	return [-1,-1]



def TestaValor(Mat, linha, coluna, val):
	col = ProcuraElementoColuna(Mat, coluna, val)
	lin = ProcuraElementoLinha(Mat, linha, val)
	qua = ProcuraElementoQuadrado(Mat, linha, coluna, val)
	if col == -1 and lin == -1 and qua == -1:
		return True
	return False



def AchouSolucao(mat):
	b = TestaMatrizPreenchida(mat)
	if b:
		cont = 1
		for a in range(9):
			for b in range(9):
				if mat[a][b] == 0:
					cont = cont + 1
		if cont == 1:
			return True
		
	return False



def Sudoku(Matriz): 
	if AchouSolucao(Matriz):
			return True
	else:
		ab = TemZero(Matriz)
		if ab[2] == 0:
			return True
		lin = ab[0]
		col = ab[1]
		for n in range (1,10):
			if TestaValor(Matriz, lin, col, n):
				Matriz[lin][col] = n
				Sudoku(Matriz)
				Matriz[lin][col] = 0
		if Sudoku(Matriz):
			return True
		return False


contador = 0


def main():
	tempo1 = time.clock() 
	global contador
	arqentrada = str(input("Entre com o nome do arquivo:"))
	matrizsudoku = LeiaMatrizLocal(arqentrada)  
	print("*** Matriz Inicial ***")
	ImprimaMatriz(matrizsudoku)                                                                                                                                                                                                                                                                                                                                                          
	if matrizsudoku == None:
		main()
	else:
		a = Sudoku(matrizsudoku)
		if a:
			print("***Matriz Completa***")
			ImprimaMatriz(matrizsudoku)
			g = TestaMatrizPreenchida(matrizsudoku)
			if g:
				print("*** Matriz Completa e Consistente ***")
				ImprimaMatriz(matrizsudoku)
			tempo2 = time.clock()
			tempodecorrido = tempo2 - tempo1
			print("Tempo decorrido: ", tempodecorrido, "segundos")
			contador += 1
			print(contador, "solução/soluções para esta matriz.")
		if a == False:
			print("*** Sem solução ***")
		main()

main()

