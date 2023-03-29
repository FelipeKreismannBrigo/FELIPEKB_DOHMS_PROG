print("Digite um número:")
a=float(input())
print("Qual operação você quer fazer?")
c=input()

c=c.lower()

if c=="²":
    print(a**2)
    quit()

print("Digite o número a multiplicar o outro")
b=float(input())

if c=="*":
    print(a*b)

elif c=="/":
    print(a/b)

elif c=="+":
    print(a+b)

elif c=="-":
    print(a-b)    