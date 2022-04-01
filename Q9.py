from math import sqrt

# acabei usando função de novo pq tava com preguiça, perdão senhor
def isPrime(n):
  for i in range(2, int(sqrt(n)) + 1):
    if n % i == 0:
      return False
  return True

n = int(input('Insira um numero: '))

if n != 1 and isPrime(n): print(f'{n} eh primo')
else: print(f'{n} nao eh primo')
