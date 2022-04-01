maior = -9999
for i in range(1, 6):
  n = int(input(f'Insira o {i}º numero: '))
  maior = max(maior, n)
  i += 1

print(f'O maior numero eh: {maior}')
