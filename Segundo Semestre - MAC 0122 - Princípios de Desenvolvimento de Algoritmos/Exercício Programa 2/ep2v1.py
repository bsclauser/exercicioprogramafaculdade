from classe.pilha import PilhaNot

def TraduzPosFixa(expn):
    global num
    global letras
    prior = {}
    prior["#"] = 5
    prior["_"] = 5
    prior["**"] = 4
    prior["*"] = 3
    prior["/"] = 3
    prior["+"] = 2
    prior["-"] = 2
    prior["("] = 1
    prior[")"] = 1
    prior["="] = 0
    novalista = []
    pilha = PilhaNot()
    for token in expn:
        if len(token)>1 and token != "**":
            cont = 0
            for a in range (len(token)):
                if token[a] in letras or token[a] in num:
                    cont += 1
                elif "-" in token[a] or "+" in token[a]:
                    novalista.append(token[1])
                    if token[0] == "-":
                        pilha.push("_")
                    elif token [0] == "+":
                        pilha.push("#")
            if cont == len(token):
                novalista.append(token)
        elif token in letras or token in num:
            novalista.append(token)
        elif token == "(":
            pilha.push(token)
        elif token == ")":
            toptoken = pilha.pop()
            while toptoken != "(":
                novalista.append(toptoken)
                toptoken = pilha.pop()
        else:
            while (not pilha.is_empty()) and (prior[str(pilha.top())] >= prior[str(token)]):
                novalista.append(pilha.pop())
            pilha.push(token)
    
    while not pilha.is_empty():
        novalista.append(pilha.pop())
    return " ".join(novalista)


tabvar = []
tabval = []


def main():
    global notnum
    global num
    global letras
    global tabvar
    global tabval
    while True:
        prompts()
        exp = input()
        for b in range (len(exp)):
            if (exp[b] not in notnum) and (exp[b] not in num) and (exp[b] not in letras) and (exp[b] != " "):
                print("Há caracteres inválidos na expressão. Tente novamente.")
                main()
        expre = BlankSpaces(exp)
        contvar = 0
        contnum = 0
        indvar = 0
        indval = 0
        for a in range (len(expre)):
            if len(expre[a]) == 1:
                if expre[a] in num:
                    contnum += 1
                    indval = a
                elif expre[a] in letras:
                    contvar += 1
                    indvar = a
            elif len(expre[a])>1:
                contl = 0
                contn = 0
                for c in range (len(expre[a])):
                    if expre[a][c] in letras:
                        contl += 1
                    elif expre[a][c] in num:
                        contn += 1
                if contn == len(expre[a]):
                    contnum += 1
                    indval = a
                elif contl == len(expre[a]):
                    contvar += 1
                    indvar = a
        if contvar == 1 and contnum == 1 and "=" in expre:
            #Temos uma atribuição
            if expre[indval-1] == "_":
                val = "-"+expre[indval]
            elif expre[indval-1] == "#":
                val = "+"+expre[indval]
            else:
                val = expre[indval]
            tabval.append(val)
            tabvar.append(expre[indvar])
            print(tabval, tabvar)
        else: 
            print(tabval != [], tabvar != [])
            if tabval != [] and tabvar != []:
                for e in range (len(expre)):
                    for f in range (len(tabvar)):
                        print(expre[e], tabvar[f])
                        if expre[e] == tabvar[f]:
                            expre[e] = tabval[f]
            print(expre)
            expposfix = TraduzPosFixa(expre)
            print(expposfix)
            print(CalcPosFixa(expposfix))




notnum = ["**", "*", "/", "+", "-", "=", "(", ")", "_", "#"]
num = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
letras = ["A", "B", "C", "D", "E", "F","G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y","z"]


def BlankSpaces(exp):
    global notnum
    global num
    global letras
    listafinal = []
    for i in range (len(exp)):
        if exp[i] in letras:
            if i != 0 and exp[i-1] in letras:
                pass
            else:
                mesmotipo = []
                while i < (len(exp)) and exp[i] in letras:
                    mesmotipo.append(exp[i])
                    i += 1
                mesmotipo2 = "".join(mesmotipo)
                listafinal.append(mesmotipo2)
        elif exp[i] in num:
            if i != 0 and exp[i-1] in num:
                pass
            else:
                mesmotipo3 = []
                while i < (len(exp)) and exp[i] in num:
                    mesmotipo3.append(exp[i])
                    i += 1
                mesmotipo4 = "".join(mesmotipo3)
                listafinal.append(mesmotipo4)
        elif exp[i] in notnum:
            if exp[i-1] in notnum:
                print(exp[i-1])
                if exp[i-1] == ")" and exp[i] == "+":
                    listafinal.append("+")
                elif exp[i-1] == ")" and exp[i] == "-":
                    listafinal.append("-")
                elif exp[i] == "-": 
                    listafinal.append("_")
                elif exp[i] == "+": 
                    listafinal.append("#")
                elif exp[i] == "*" and exp[i-1] == "*":
                    listafinal.append("**")
                elif exp[i] == "(" or exp[i] == ")":
                    listafinal.append(exp[i])
                elif exp[i] == "/":
                    listafinal.append(exp[i])
            elif ((exp[i-1] in num) or (exp[i-1] in letras)) and exp[i] != "*":
                listafinal.append(exp[i])
            elif exp[i+1] not in notnum:
                listafinal.append(exp[i])
            elif exp[i] == "=":
                listafinal.append(exp[i])
            elif exp[i] == "/":
                listafinal.append(exp[i])
                print(exp[i]=="/")
        print(listafinal)
        listafinal = ChecarLista(listafinal)
    return listafinal
                
def ChecarLista(lista):
    global notnum
    if lista[0] in notnum:
        if lista[0] == "-": lista[0] = "_"
        elif lista[0] == "+": lista[0] = "#"
    for a in range (1, len(lista)):
        if lista[a] in notnum:
            if lista[a-1] in notnum and lista[a-1] != "(" and lista[a-1] != ")":
                if lista[a] == "-": lista [a] = "_"
                elif lista [a] == "+": lista [a] = "#"

    return lista



def prompts():
    print(">>> ", end=" ")


def CalcPosFixa(listaexp):
    pilha2 = PilhaNot()
    
    for t in range(len(listaexp)):
        print(listaexp)
        if listaexp[t] == "+":
            pilha2.push(pilha2.pop() + pilha2.pop())
        elif listaexp[t] == "-":
            oper = pilha2.pop()
            pilha2.push(pilha2.pop() - oper)
        elif listaexp[t] == "*":
            if t+1 < len(listaexp) and listaexp[t+1] == "*":
                oper3 = pilha2.pop()
                oper4 = pilha2.pop()
                pilha2.push(pow(oper4, oper3))
            if (t+1 < len(listaexp) and listaexp[t+1] != "*") or t == (len(listaexp)-1):
                pilha2.push(pilha2.pop() * pilha2.pop())
        elif listaexp[t] == '/':
            oper2 = pilha2.pop()
            if oper2 != 0:
                pilha2.push(pilha2.pop() / oper2)
            else:
                raise ValueError("Divisão por zero!")
        elif (pilha2.is_number(listaexp[t])):
            pilha2.push(float(listaexp[t]))
        elif listaexp[t] == "_":
            pilha2.push((-1)*pilha2.pop())
        elif listaexp[t] == "#":
            pilha2.push((+1)*pilha2.pop())

    return pilha2.pop()



main()