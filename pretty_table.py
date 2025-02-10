from prettytable import PrettyTable 

table = PrettyTable()

table.add_column("Name", ["Hitesh", "Monali", "Abhimanyu"])
table.add_column("Age", [41, 38, 12])
table.align = 'l'

print(table)