sal_inicial = int(input('Digite o salario inicial do funcionario: '))
sal_atual = sal_inicial
por_inicial = 1.5

for i in range(1996, 2023):
  sal_atual += (sal_inicial * (por_inicial / 100))
  por_inicial *= 2

print(sal_atual)
