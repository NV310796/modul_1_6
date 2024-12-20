my_dict={'Ivanov':2000, 'Petrov':2001, 'Sidorov':2002, 'Pushkin':2003, 'Dantes':2004}
print(my_dict)
print(my_dict['Petrov'], my_dict.get('Lermontov'))
my_dict.update({'Tolstoy':2005, 'Griboedov':2006})
print(my_dict.pop('Sidorov'))
print(my_dict)

my_set={1,2,3,'q','w','e', 1, 'q'}
print(my_set)
my_set.add(4)
my_set.add('r')
my_set.discard('w')
print(my_set)