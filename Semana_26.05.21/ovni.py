T = int(input())
for t in range(T):
    linha = input().split(" ")

    raio1 = int((linha[0]))
    raio2 = int((linha[1]))
    raio3 = int((linha[2]))
    
    if raio1 + raio2 <= raio3:
        print ("CABE!", end = "" if t==T -1 else "\n")
    else:
        print ("NAO CABE!", end = "" if t==T -1 else "\n")