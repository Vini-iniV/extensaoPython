n = int(input())
notasDe100 = 0
notasDe50 = 0
notasDe20 = 0
notasDe10 = 0
notasDe5 = 0
notasDe2 = 0
notasDe1 = 0

while n >= 100:
    n -= 100
    notasDe100 += 1
while n >= 50:
    n -= 50
    notasDe50 += 1
while(n >= 20):
    n -= 20
    notasDe20 += 1
while(n >= 10):
    n -= 10
    notasDe10 += 1
while(n >= 5):
    n -= 5
    notasDe5 += 1
while(n >= 2):
    n -= 2
    notasDe2 += 1
while(n >= 1):
    n -= 1
    notasDe1 += 1

print(str(notasDe100) + " nota(s) de R$ 100")
print(str(notasDe50) + " nota(s) de R$ 50")
print(str(notasDe20) + " nota(s) de R$ 20")
print(str(notasDe10) + " nota(s) de R$ 10")
print(str(notasDe5) + " nota(s) de R$ 5")
print(str(notasDe2) + " nota(s) de R$ 2")
print(str(notasDe1) + " nota(s) de R$ 1", end="")