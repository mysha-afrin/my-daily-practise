for thing in zip(inventory_names, inventory_num):
    print(f'{thing}')

#Exercise
#combine zip and enumerate to get 'screw [id:0] - inventory: 43'
for index, inventory_tuple in enumerate(zip(inventory_num, inventory_names)):
    print(f"{inventory_tuple[0]} [id: {index}] - inventory: {inventory_tuple[1]}")

