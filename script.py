students = []
mean = 0

while True:
  name = (input('Nome: '))
  nota1 = (float(input('Nota 1: ')))
  nota2 =(float(input('Nota 2: ')))
  mean = nota1 + nota2/ 2
  students.append([name, [nota1, nota2], mean]);

  proceed = input('Deseja continuar? [S/N]').upper()

  if proceed != 'S':
    break

print('-' *26)
print(f'{"No.":<4}{"NOME":<10}{"MEDIA":>8}')

for i, a in enumerate(students):
  print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
print('-' *26)

while True:
  opc = int(input('Mostrar notas de qual aluno? (999 interrompe) '))
  if opc == 999:
    print('FINALIZANDO...')
    break
  if opc <= len(students) - 1:
    print(f'Notas de {students[opc][0]} são {students[opc][1]}')
print('<<< VOLTE SEMPRE >>>')