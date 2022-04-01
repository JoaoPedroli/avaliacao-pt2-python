# pedão das coxinha - ASSINADO | não copie meu nobre isso é feio Deus está vendo >:(

pop_pais_A = 80000
tax_cres_A = 3.0

pop_pais_B = 200000
tax_cres_B = 1.5

anos = 0
while pop_pais_A < pop_pais_B:
  anos += 1
  pop_pais_A += (pop_pais_A * (tax_cres_A / 100))
  pop_pais_B += (pop_pais_B * (tax_cres_B / 100))
  print(pop_pais_A, pop_pais_B)

print(f'''Levaria {anos} anos para que a populacao do pais A ultrapasse ou iguale a populacao do pais B,
mantidas as taxas de crescimento.''')