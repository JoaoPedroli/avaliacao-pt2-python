# pedão das coxinha - ASSINADO | não copie meu nobre isso é feio Deus está vendo >:(

warn = ''
while True:
  nome = input(f'Insira seu nome {warn}: ')
  if len(nome) > 3: break
  warn = f'(O nome precisa ter mais de 3 letras)'

warn = ""
while True:
  idade = int(input(f'Insira sua idade {warn}: '))
  if idade > 0 and idade < 150: break
  warn = "(A idade precisa estar entre 0 e 150)"

warn = ""
while True:
  salario = float(input(f'Insira seu salario {warn}: '))
  if salario > 0: break
  warn = "(O salario precisa ser maior que 0)"

warn = ""
while True:
  sexo = input(f'Escolha seu sexo ["m" ou "f"] {warn}: ')
  if sexo in ['m', 'f']: break
  warn = "(O sexo precisa ser ['m' ou 'f'])"

warn = ""
while True:
  estadoCivil = input(f'''Escolha seu estado civil:
  * s = Para solteiro(a)
  * c = Para casado(a)
  * v = para viuvo(a)
  * d = para divorciado(a)
  {warn}: ''')
  if estadoCivil in ['s', 'c', 'v', 'd']: break
  warn = "(O Estado Civil precisa ser ['s' ou 'c' ou 'v' ou 'd'])"
