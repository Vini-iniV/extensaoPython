x = int(input())
s1 = input()
y = int(input())
s2 = input()
z = int(input())

def calculaPartesSeparadamente(a,b,c):
    if (b == "+"):
        return a + c
    elif (b == "-"):
        return a - c
    elif (b== "/"):
        return a // c
    elif (b == "*"):
        return a * c

if(s1 == "/" and y == 0):
    print("erro", end="")
if(s2 == "/" and z == 0):
    print("erro", end="")

if (s1 == "/" or s1 == "*"):
    resParcial = calculaPartesSeparadamente(x,s1,y)
    res = calculaPartesSeparadamente(resParcial, s2, z)
elif (s2 == "/" or s2 == "*"):
    resParcial = calculaPartesSeparadamente(y,s2,z)
    res = calculaPartesSeparadamente(x, s1, resParcial)
else:
    resParcial = calculaPartesSeparadamente(x,s1,y)
    res = calculaPartesSeparadamente(resParcial, s2, z)

print(res, end="")