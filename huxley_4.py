def mostra_matriz(b):
    global N
    global M
    for linha in range(N):
        for coluna in range(M):
            print(b[linha][coluna],end=" ")
        print()   

def movimento(b):
    global N
    global M
    linha=0
    coluna=0
    existe=0
    for x in range(N):
        if(x==0):
            linha=N-1
            #coluna=y+1
        else:
            linha=x-1        
        for y in range(M):            
            if(y==M-1):
                coluna=0
            else:
                coluna=y+1                
            if(b[x][y]==1):
                #print(coluna)
                existe=1
                b[linha][coluna]=1
                b[x][y]=0
                
        

entrada=input().split()
N=int(entrada[0])
M=int(entrada[1])

#print(N,M)


b=[]

for linha in range(N):
    linha_1=[]
    for coluna in range(M):
        linha_1.append(0)
    b.append(linha_1)

K=int(input())




for x in range(K):
    entrada=input().split()
    linha=int(entrada[0])
    coluna=int(entrada[1])

    b[linha][coluna]=1
    #print(b)

entrada_2=input().split()
num_ataques=int(entrada_2[0])
num_bombas=int(entrada_2[1])



for x in range(num_ataques):
    for y in range(num_bombas):
        entrada_2=input().split()
        i=int(entrada_2[0])
        j=int(entrada_2[1])
        mostra_matriz(b)
        print("\n\n")
        movimento(b)
        mostra_matriz(b)
        
    
    

        












