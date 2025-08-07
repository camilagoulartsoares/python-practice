# Lista: estrutura mutável (pode alterar os valores)
materias = ["Lógica", "Funções", "Tuplas", "Listas"]

print("Lista de matérias:")
print(materias)

# Adicionando um item na lista
materias.append("Dicionários")
print("Depois de adicionar:")
print(materias)

# Removendo um item
materias.remove("Tuplas")
print("Depois de remover:")
print(materias)

# Tupla: estrutura imutável (não pode alterar os valores)
dias_da_semana = ("Segunda", "Terça", "Quarta", "Quinta", "Sexta")

print("Tupla de dias da semana:")
print(dias_da_semana)

# Acessando elementos
print("Primeira matéria:", materias[0])
print("Último dia da semana:", dias_da_semana[-1])
