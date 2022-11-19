def getClient(codigo = 0, altura = 0.0, peso = 0.0):
  return {
    'codigo': codigo, 'altura': altura, 'peso': peso,
  }

count = 0
soma = { 'altura': 0.0, 'peso': 0.0 }
mais_alto = getClient(altura=-9999.9)
mais_baixo = getClient(altura=9999.9)
mais_gordo = getClient(peso=-9999.9)
mais_magro = getClient(peso=9999.9)

while True:
  count += 1
  print(f'\n=== Cliente {count} ===')
  cliente = getClient()
  cliente['codigo'] = int(input('Insira seu código: '))
  if cliente['codigo'] == 0: break

  cliente['altura'] = float(input('Insira sua altura: '))
  cliente['peso'] = float(input('Insira seu peso: '))

  soma['altura'] += cliente['altura']
  soma['peso'] += cliente['peso']

  if cliente['altura'] > mais_alto['altura']:
    mais_alto = cliente
  if cliente['altura'] < mais_baixo['altura']:
    mais_baixo = cliente
  if cliente['peso'] > mais_gordo['peso']:
    mais_gordo = cliente
  if cliente['peso'] < mais_magro['peso']:
    mais_magro = cliente

print(f'''
-- Cliente mais alto --
codigo: {mais_alto['codigo']}
altura: {mais_alto['altura']}
peso: {mais_alto['peso']}
''')
print(f'''
-- Cliente mais baixo --
codigo: {mais_baixo['codigo']}
altura: {mais_baixo['altura']}
peso: {mais_baixo['peso']}
''')
print(f'''
-- Cliente mais gordo --
codigo: {mais_gordo['codigo']}
altura: {mais_gordo['altura']}
peso: {mais_gordo['peso']}
''')
print(f'''
-- Cliente mais magro --
codigo: {mais_magro['codigo']}
altura: {mais_magro['altura']}
peso: {mais_magro['peso']}
''')

mediaa = soma['altura'] / count
mediap = soma['peso'] / count
print(f'Media das alturas dos clientes: {mediaa}')
print(f'Media dos pesos dos clientes: {mediap}')
