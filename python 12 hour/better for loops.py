inventiry_names = ['screws', 'wheels', 'Metal parts', 'Rubber bits', 'screw driver', 'wood']
inventory_num = [23, 45, 78, 49, 50, 36]
print(list(zip(inventiry_names, inventory_num)))


for thing in zip(inventory_num, inventory_names):
    print(thing)
    print(thing[0]


  for name, number in zip(inventory_names, inventory_num):
    print(f"{name} current inventory is: {number}")
