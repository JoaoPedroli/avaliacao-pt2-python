from math import sqrt

def isPrime(n):
  for i in range(2, n):
    if n % i == 0:
      return False
  return True

n = int(input('Insira um numero: '))

if n != 1 and isPrime(n): print(f'{n} eh primo')
else: print(f'{n} nao eh primo')
