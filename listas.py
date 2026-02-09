#lista = ['a', 'b', 'c']



progs = ['Yes', 'Genesis', 'Pink Floyd', 'ELP']

# Varrendo a lista
for prog in progs:
    print(prog)
    
# Trocando o ultimo elemento
progs[-1] = 'King Crimson'
print(progs)

# Incluindo um item na lista
progs.append('Led Zeppelin')
print(progs)

# Removendo um item da lista
progs.remove('Genesis')
print(progs)

# Ordenando a lista
progs.sort()
print(progs)

# Invertendo a lista
progs.reverse()
print(progs)

