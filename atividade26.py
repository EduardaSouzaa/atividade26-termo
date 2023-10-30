t1 = int(input("Digite o primeiro termo da PA: "))
r = int(input("Digite a razão da PA: "))

for i in range(10):
    print(i)
    termo = t1 + i * r
    print(f'Termo {i+1}: {termo}')