nome = input("qual o seu nome?")
n1 = float(input("qual a sua primeira nota?"))
n2 = float(input("qual a sua segunda nota?"))
n3 = float(input("qual a sua terceira nota?"))
n4 = float(input("qual a sua quarta nota?"))
n5 = float(input("qual a sua quinta nota?"))
n6 = float(input("qual a sua sexta nota?"))
n7 = float(input("qual a sua setima nota?"))
n8 = float(input("qual a sua oitava nota?"))

media = (n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8)/8

print("ola", nome )
print("sua primeira nota foi:", n1)
print("sua segunda nota foi:", n2)
print("sua terceira nota foi:", n3)
print("sua quarta nota foi:", n4)
print("sua quinta nota foi:", n5)
print("sua sexta nota foi:", n6)
print("sua setima nota foi:", n7)
print("sua oitava nota foi:", n8)

b1 = (n1 + n2)/2
b2 = (n3 + n4)/2
b3 = (n5 + n6)/2
b4 = (n7 + n8)/2

s1 = (b1 + b2)/2
s2 = (b3 + b4)/2

print("sua nota no primeiro bimestre foi:", b1)
print("sua nota no segundo bimestre foi:", b2)
print("sua nota no terceiro bimestre foi:", b3)
print("sua nota no quarto bimestre foi:", b4)

print("sua nota no prieiro semestre foi:", s1)
print("sua nota no segundo semestre foi:", s2)

print ("sua media foi:", media)
if media > 6:
    print("aprovado")

else: ("reprovado")
