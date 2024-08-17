my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
separate_variable = 0
while separate_variable < len(my_list):
    number = my_list[separate_variable]
    separate_variable = separate_variable + 1
    if number == 0:
        continue
    elif number < 0:
        break
    elif number == len(my_list):
        print(number)
    else:
        print(number)