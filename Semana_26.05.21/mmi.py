T = int(input())
for t in range(T):
    linha = input().split(" ")

    menorNota = min([int(e) for e in linha])
    maiorNota = max([int(e) for e in linha])
    print (str(menorNota) + " " + str(maiorNota))
    if menorNota == maiorNota:
        print ("S", end = "" if t==T -1 else "\n")
    else:
        print ("N", end = "" if t==T -1 else "\n")