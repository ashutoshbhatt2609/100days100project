from prettytable import PrettyTable
table = PrettyTable()
print(table)
table.add_column("Pokemon name",["Pikachu","Squirtle","Charmander"])
table.add_column("Type",["Electic","Water","Fire"])
table.align = 'c'
print(table)




