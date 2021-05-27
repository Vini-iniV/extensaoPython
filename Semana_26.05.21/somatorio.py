T = int(input())
for t in range(T):
    linha = input().split(";")
    somatorio = sum([int(e) for e in linha])
    print (somatorio, end = "" if t==T -1 else "\n")