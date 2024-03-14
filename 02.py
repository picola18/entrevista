termo = int(input("Qual número? "))

n1, n2 = 0, 1
contador = 1000
termo_na_fibonacci = False

for _ in range(contador):
    if termo == n1 or termo == n2:
        termo_na_fibonacci = True
        break
    nth = n1 + n2
    n1 = n2
    n2 = nth

if termo_na_fibonacci:
    print('Seu número está na sequência de Fibonacci.')
else:
    print('Seu número não está na sequência de Fibonacci.')