def main():
    narqo = str(input("Entre com o nome do arquivo origem: "))
    narqd = str(input("Entre com o nome do arquivo destino: "))
    registrosclass = int(input("Quantidade de registros a classificar: "))
    TAB = CriaTAB(narqo)
    TAB, datas, idd = CriaTAB3(TAB)
    final = ClassQuickRecursivo(TAB)
    CriaArqDest(narqd, final)
    print("Tempo para classificar a tabela:")
    print("Método Quick Recursivo:")
    print("Método Quick Não Recursivo:")
    print("Método sort() do Python:")

def CriaArqDest (nomedoarquivo, lista):
    arqdest = open(nomedoarquivo, "w")
    linhas = ""
    for a in range(len(lista)):
        for b in range(5):
            linha = lista[a][b]
            linha2 = str(linha)
            if b == 2:
                linhas = linhas + "/" + linha2
            elif b == 3:
                linhas = linhas + "/" + linha2 + ","
            elif b == 1:
                linhas = linhas + linha2
            elif b == 4:
                linhas = linhas + linha2
            else:
                linhas = linhas + linha2 + ","
        arqdest.write(linhas+"\n")
        linhas = ""
    
                 


def CriaTAB (narqo):
    arq = open(narqo, "r")
    TAB = [line.rstrip('\n') for line in arq]
    return TAB

def CriaTAB3 (TAB):
    TAB2 = []
    for k in range (len(TAB)):
        a = TAB[k].split(",")
        TAB2.append(a)
    nomes = [TAB2[i][0] for i in range (len(TAB2))]
    datas = [TAB2[j][1] for j in range (len(TAB2))]
    idd = [int(TAB2[l][2]) for l in range (len(TAB2))]
    ab = []
    for a in range(len(datas)):
        ab.append(datas[a].split("/"))
    for c in range (len(ab)):
        for d in range(3):
            ab[c][d] = int(ab[c][d])
    TAB3 = [[0,0,0,0,0] for i in range(len(TAB2))]
    for h in range (len(TAB2)):
        TAB3[h][0] = nomes[h]
        TAB3[h][1] = ab[h][0]
        TAB3[h][2] = ab[h][1]
        TAB3[h][3] = ab[h][2]
        TAB3[h][4] = idd[h]
    return TAB3, ab, idd

def ClassQuickRecursivo (TAB):
    classn = QuickSort_Index(TAB, 0)
    print(classn)
    a = 0
    while a+1 < len(classn):
        if classn[a][0] == classn[a+1][0]:
            if classn[a][3] != classn[a+1][3]:
                classndataano = QuickSort_Index([classn[a], classn[a+1]], 3)
                classn[a], classn[a+1] = classndataano[0], classndataano [1]
            elif classn[a][2] != classn[a+1][2]:
                classdatames = QuickSort_Index([classn[a], classn[a+1]], 2)
                classn[a], classn[a+1] = classdatames[0], classdatames [1]
            elif classn[a][1] != classn[a+1][1]:
                classdatadia = QuickSort_Index([classn[a], classn[a+1]], 1)
                classn[a], classn[a+1] = classdatadia[0], classdatadia [1]
            elif classn[a][4] != classn[a+1][4]:
                classid = QuickSort_Index([classn[a], classn[a+1]], 4)
                classn[a], classn[a+1] = classid[0], classid[1]
        a += 1
    return classn
    
    


    #Quick_Sort(datas, 0,len(datas)-1)
    #print(datas)

def QuickSort_Index(lst, index):
    if len(lst) == 0:
        return []
    else:
        pivot = lst[0]
        lesser = QuickSort_Index([x for x in lst[1:] if x[index] < pivot[index]], index)
        greater =  QuickSort_Index([x for x in lst[1:] if x[index] >= pivot[index]], index)
        return lesser + [pivot] + greater

def Quick_Sort(lista, inicio, fim):        
    if inicio < fim:        
        k = Particiona(lista, inicio, fim)         
        print("pivo:", lista[k])         
        Quick_Sort(lista, inicio, k - 1)         
        Quick_Sort(lista, k + 1, fim)

def Particiona(lista, inicio, fim):     
    i, j = inicio, fim     
    pivo = lista[fim]     
    while True:         
        # aumentado i         
        while i < j and lista[i] <= pivo: i = i + 1         
        if i < j:             
            lista[i], lista[j] = pivo, lista[i]         
        else: break         
        # diminuindo j         
        while i < j and lista[j] >= pivo: j = j - 1         
        if i < j: lista[i], lista[j] = lista[j], pivo
        else: break
    return i

main()
