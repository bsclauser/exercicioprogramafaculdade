
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
	quadrado1 = [[0,0,0],[0,0,0],[0,0,0]]
	quadrado2 = [[0,0,0],[0,0,0],[0,0,0]]
	quadrado3 = [[0,0,0],[0,0,0],[0,0,0]]
	quadrado4 = [[0,0,0],[0,0,0],[0,0,0]]
	quadrado5 = [[0,0,0],[0,0,0],[0,0,0]]
	quadrado6 = [[0,0,0],[0,0,0],[0,0,0]]
	quadrado7 = [[0,0,0],[0,0,0],[0,0,0]]
	quadrado8 = [[0,0,0],[0,0,0],[0,0,0]]
	quadrado9 = [[0,0,0],[0,0,0],[0,0,0]]
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
	


def QuadradosRetornaEspecifico(matriz, numquadrado):
	quadrado1, quadrado2, quadrado3, quadrado4, quadrado5, quadrado6, quadrado7, quadrado8, quadrado9 = Quadrados(matriz)
	todosquadrados = [quadrado1,quadrado2,quadrado3,quadrado4,quadrado5,quadrado6,quadrado7,quadrado8,quadrado9]
	for a in range(9):
		if numquadrado == a:
			quadf = todosquadrados[a]
			return quadf
	print("Quadrado não encontrado.")
	return -1
	 
	
	
	
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
	if L >= 0 and L <= 2:
		if C >= 0 and C <= 2:
			quad = QuadradosRetornaEspecifico(Mat, 0)
			for f in range(3):
				for j in range(3):
					if quad[f][j] == p:
						return (f,j)
			return -1
		elif C >= 3 and C <= 5:
			quad = QuadradosRetornaEspecifico(Mat, 1)
			for f in range(3):
				for j in range(3):
					if quad[f][j] == p:
						return (f,j)
			return -1
		elif C >= 6 and C <= 8:
			quad = QuadradosRetornaEspecifico(Mat, 2)
			for f in range(3):
				for j in range(3):
					if quad[f][j] == p:
						return (f,j)
			return -1
	if L >= 3 and L <= 5:
	    if C >= 0 and C <= 2:
		    quad = QuadradosRetornaEspecifico(Mat, 3)
		    for f in range(3):
			    for j in range(3):
			        if quad[f][j] == p:
				        return(f,j)
		    return -1
	    elif C >= 3 and C <= 5:
		    quad = QuadradosRetornaEspecifico(Mat, 4)
		    for f in range(3):
			    for j in range(3):
				    if quad[f][j] == p:
					    return (f,j)
		    return -1
	    elif C >= 6 and C <= 8:
		    quad = QuadradosRetornaEspecifico(Mat, 5)
		    for f in range(3):
			    for j in range(3):
				    if quad[f][j] == p:
					    return (f,j)
		    return -1
	if L >= 6 and L <= 8:
		if C >= 0 and C <= 2:
			quad = QuadradosRetornaEspecifico(Mat, 6)
			for f in range(3):
				for j in range(3):
					if quad[f][j] == p:
						return (f,j)
			return -1
		elif C >= 3 and C <= 5:
			quad = QuadradosRetornaEspecifico(Mat, 7)
			for f in range(3):
				for j in range(3):
					if quad[f][j] == p:
						return(f,j)
			return -1
		elif C >= 6 and C <= 8:
			quad = QuadradosRetornaEspecifico(Mat, 8)
			for f in range(3):
				for j in range(3):
					
					if quad[f][j] == p:
						return (f,j)
			return -1
	
	
			 
def ImprimaMatriz (Mat):
	print()
	for a in range(9):
		for b in range(9):
			cont = 1
			if b == 8:
				print (Mat[a][b])
			else:
			    print (Mat[a][b], " ", end = " ")					



def TestaMatrizLida(Mat): 
	#consistência das linhas
	linhas = [0]*9
	for t in range(9):
		for y in range(9):
			linhas[y] = Mat[t][y]
		for h in range(1,10):
			contador1 = linhas.count(h)
			if contador1 > 1:
				print("Matriz inválida. Há números repetidos nas linhas. Tente novamente com uma matriz válida.")
				return None
	#consistência das colunas
	colunas = [0]*9
	for p in range(9):
		for w in range(9):
			colunas[w] = Mat[w][p]
		for b in range(1,10):
			contador2 = colunas.count(b)
			if contador2 > 1:
				print("Matriz inválida. Há números repetidos nas colunas. Tente novamente com uma matriz válida.")
				return None
	#consistência dos quadrados
	quadrado1, quadrado2, quadrado3, quadrado4, quadrado5, quadrado6, quadrado7, quadrado8, quadrado9 = Quadrados(Mat)
	contadorquad = 0
	for g in range (1,10):
		if quadrado1.count(g) > 1 or quadrado2.count(g) > 1 or quadrado3.count(g)> 1 or quadrado4.count(g) > 1 or quadrado5.count(g) > 1 or quadrado6.count(g) > 1 or quadrado7.count(g) > 1 or quadrado8.count(g) > 1 or quadrado9.count(g) > 1:
			print("Matriz inválida. Há números repetidos no(s) quadrado(s) interno(s). Tente novamente com uma matriz válida.")
			return None
	return True


def TestaMatrizPreenchida(Mat): 
	a = TestaMatrizLida(Mat)
	if a:
		return True
	if a ==  None:
		return False

def TemZero(Mat):
	elemzero = 0
	for a in range(9):
		for b in range(9):
			if Mat[a][b] == 0:
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



def AchouSolucao(Mat):
	b = TestaMatrizPreenchida(Mat)
	if b:
		cont = 1
		for a in range(9):
			for b in range(9):
				if Mat[a][b] == 0:
					cont = cont + 1
		if cont == 1:
			return True
		
	return False



def Sudoku(Mat): 
	if AchouSolucao(Mat):
		if Mat not in solucoes:
			return True
	else:
		ab = TemZero(Mat)
		if ab[2] == 0:
			return True
		lin = ab[0]
		col = ab[1]
		for n in range (1,10):
			if TestaValor(Mat, lin, col, n):
				Mat[lin][col] = n
				Sudoku(Mat)
				Mat[lin][col] = 0
		if Sudoku(Mat):
			return True
		return False
	

contador = 0
solucoes = []



def main():
		global contador
		global solucoes
		arqentrada = str(input("Entre com o nome do arquivo:"))
		matrizsudoku = LeiaMatrizLocal(arqentrada)                                                                                                                                                                                                                                                                                                                                                              
		if matrizsudoku == None:
			main()
		else:
			print(solucoes)
			print(contador)
			a = Sudoku(matrizsudoku)
			print(a)
			if a == True:
				ImprimaMatriz(matrizsudoku)
				solucoes.append(matrizsudoku)
				contador += 1
				Sudoku(matrizsudoku)
			if a == False:
				print("***Fim***")
main()
