entrada = input().split(" ")
a = int(entrada[0])
b = int(entrada[1])
c = int(entrada[2])

m1 = (a + b + abs(a-b)) // 2
m2 = (c + m1 + abs(m1 - c)) // 2

print (m2, end="")