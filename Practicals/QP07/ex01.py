def switch_dict(my_dict):
    my_dict_aux = {}
    for k, v in my_dict.items():
        if v in my_dict_aux:
            my_dict_aux[v].append(k)
        else:
            my_dict_aux[v] = [k]
    return (my_dict_aux)


print(switch_dict({"jan": "winter", "feb": "winter", "may": "spring", "july": "summer", "august": "summer"}))
# {'winter': ['jan', 'feb'], 'spring': ['may'], 'summer': ['july', 'august']}
print(switch_dict({1: 2, 2: 1, 3: 1, 4: 2}))
# {2: [1, 4], 1: [2, 3]}
print(switch_dict({"Ice": "Cream", "Heavy": "Cream", "Light": "Cream", "Double": "Cream"}))
# {'Cream': ['Ice', 'Heavy', 'Light', 'Double']}
print(switch_dict({}))
# {}