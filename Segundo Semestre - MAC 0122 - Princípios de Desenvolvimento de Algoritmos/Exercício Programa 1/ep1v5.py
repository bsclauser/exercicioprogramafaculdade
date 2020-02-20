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
		 if resultado == False:
			 print("Matriz inváldia. Há valores repetidos nos quadrados interiores da matriz. Tente novamente com uma matriz válida.")
			 return None
		 i = i + 1
    
	# fechar arquivo e retorna a matriz lida e consistida 
	arq.close()
	return mat



def TestaMatrizLida(mat):
	#consistência das linhas
	linhas = [0]*9
	for a in range(9):
		for b in range(9):
			linhas[b] = mat[a][b]
		for c in range(1,10):
			cont1 = linhas.count(c)
			if cont1 > 1:
				return False
	#consistência das colunas
	colunas = [0]*9
	for d in range(9):
		for e in range(9):
			colunas[e] = mat[e][d]
		for f in range(1,10):
			cont2 = colunas.count(f)
			if cont2 > 1:
				return False
	#consistência dos quadradrados
	quadradosn = Quadrados(mat)
	soma = 0
	for h in range(9):
		for g in range(1,10):
			j = 0
			soma = quadradosn[h][j].count(g) + quadradosn[h][j+1].count(g) + quadradosn[h][j+2].count(g)
			if soma > 1:
				return False
	return True

def Quadrados(mat):
	quadrado1, quadrado2, quadrado3, quadrado4, quadrado5, quadrado6, quadrado7, quadrado8, quadrado9 =  [[0]*3 for k in range(3)], [[0]*3 for k in range(3)], [[0]*3 for k in range(3)], [[0]*3 for k in range(3)], [[0]*3 for k in range(3)], [[0]*3 for k in range(3)], [[0]*3 for k in range(3)], [[0]*3 for k in range(3)], [[0]*3 for k in range(3)]
	for h in range (9):
		for y in range (9):
			if h >= 0 and h <=2:
			    if y >= 0 and y <= 2:
				    quadrado1[h][y] = mat[h][y]
			    if y >= 3 and y <= 5:
				    quadrado2[h][y-3] = mat[h][y]
			    if y >= 6 and y <= 8:
				    quadrado3[h][y-6] = mat[h][y]
			elif h >= 3 and h <= 5:
				if y >= 0 and y <= 2 :
					quadrado4[h-3][y] = mat[h][y]
				if y >= 3 and y <= 5:
					quadrado5[h-3][y-3] = mat[h][y]
				if y >= 6 and y <= 8:
					quadrado6[h-3][y-6] = mat[h][y]
			elif h >= 6 and h <= 8:
				if y >= 0 and y <= 2 :
					quadrado7[h-6][y] = mat[h][y]
				if y >= 3 and y <= 5:
					quadrado8[h-6][y-3] = mat[h][y]
				if y >= 6 and y <= 8:
					quadrado9[h-6][y-6] = mat[h][y]
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
	ln = (L//3)*3
	cn = (C//3)*3
	for i in range(ln,ln+3):
		for j in range(cn,cn+3):
			if Mat[i][j]== p:
				return (i,j)
	return -1

def TestaMatrizPreenchida(Matriz): 
	a = TestaMatrizLida(Matriz)
	if a:
		return True
	return False


def TemZero(matriz):
	elementoszero = 0
	for a in range(9):
		for b in range(9):
			if matriz[a][b] == 0:
				elementoszero = 1
				return [a,b,elementoszero]
	return [-1,-1]


def TestaValor(Mat, linha, coluna, val):
	col = ProcuraElementoColuna(Mat, coluna, val)
	lin = ProcuraElementoLinha(Mat, linha, val)
	qua = ProcuraElementoQuadrado(Mat, linha, coluna, val)
	if col == -1 and lin == -1 and qua == -1:
		return True
	return False


def AchouSolucao(mat):
	if TemZero(mat) == [-1,-1] and TestaMatrizPreenchida(mat) == True:
		return True
	return False

def Sudoku(Mat):
	if AchouSolucao(Mat):
		return True
	else:
		a = TemZero(Mat)
		Lin = a[0]
		Col = a[1]
		for p in range(1,10):
			if TestaValor(Mat, Lin, Col, p):
				Mat[Lin][Col] = p
				if Sudoku(Mat):
					return True
				Mat[Lin][Col] = 0
		return False


def main():
	arqentrada = str(input("Entre com o nome do arquivo:"))
	matrizsudoku = LeiaMatrizLocal(arqentrada)                                                                                                                                                                                                                                                                                                                                                              
	if matrizsudoku == None:
		main()
	elif matrizsudoku == []:
		print("[]")
	else:
		print("a")
		s = Sudoku(matrizsudoku)
		if s:
			print(matrizsudoku)


main()