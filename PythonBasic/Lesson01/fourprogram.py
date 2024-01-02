this_is_a_string = "مسعود"
this_is_a_number = 20
this_is_another_number = 45.2


def print_a_list():
    this_is_a_list = ["مسعود", 'ali', 50.2]
    return this_is_a_list


this_is_a_dict = {'salam': 'aleyk', 'مسعود': 'کاویانی', 'ali': 'samimi'}
this_is_a_list2 = print_a_list()

for i in range(0, 100):
    print(str(i * 2))

for i in print_a_list():
    print('This is ' + str(i))
