inventory_names = ['Screws', 'Wheels', 'Metal parts', 'Rubber bits', 'Screw driver','Wood']
inventory_num = [43, 12, 95,21, 23, 43]
combined_list = list(zip(inventory_names, inventory_num))
#Sort the list with inventory_num
#Sort the list with inventory_names
sorted_comp_num = sorted(combined_list, key = lambda inv_tuple: inv_tuple[1])
sorted_comp_names = sorted(combined_list, key = lambda inv_tuple: len(inv_tuple[0]))
print(sorted_comp_num)
print(sorted_comp_names)
