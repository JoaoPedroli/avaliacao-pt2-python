correct_answ = ['A', 'B', 'C', 'D', 'E', 'E', 'D', 'C', 'B', 'A']
count = soma = 0
maior = -9999
menor = 9999

while True:
  count += 1
  nota = 0
  print(f'\n=== Aluno {count} ===\n')

  for i in range(10):
    resp = None
    while True:
      resp = input(f'Resposta da questao {i+1} [A/B/C/D/E]: ').upper()
      if resp in ['A', 'B', 'C', 'D', 'E']: break
    if resp == correct_answ[i]: nota += 1

  maior = max(maior, nota)
  menor = min(menor, nota)
  soma += nota

  print(f'Nota do aluno {count}: {nota}')

  next_student = None
  while True:
    next_student = input('Outro aluno irá utilizar o sistema [S/N]? ').upper()
    if next_student in ['S', 'N']: break
  if next_student == 'N': break

print(f'Maior acerto: {maior}\nMenor acerto: {menor}')
print(f'Total de alunos que utilizaram o sistema: {count}')
print(f'Média das notas da turma: {soma / count}')
