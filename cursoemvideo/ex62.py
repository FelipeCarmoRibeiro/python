print("="*30)
print("10 TERMOS DE UMA PA". center(30))
print("="*30)

t = int(input("Primeiro termo: "))
r = int(input("Razao: "))


for c in range(0, 10):
    print(t + r*c, end="-> ")
print("Acabou")    


