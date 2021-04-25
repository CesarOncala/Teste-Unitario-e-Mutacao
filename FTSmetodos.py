
####################################################
def numeroPerfeito(n):
    div=0
    for i in range(1,n+1):
        div=0 
        for j in range(1,i):
            if i%j==0:
                div+=j
        if div==i:
            if i == n:
                return True
    return False 

def mediaIntersecao(m,n,vetor1,vetor2):
    media = 0.0
    cont = 0

    for x in range(n):
        for i in range(m):
            if vetor1[x] == vetor2[i]:
                media += vetor1[x]
                cont = cont + 1

    if cont == 0:
        return 0
	
    return media/cont
####################################################

