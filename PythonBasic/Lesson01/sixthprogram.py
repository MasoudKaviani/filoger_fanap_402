this_is_a_string = "مسعود"
this_is_a_number = 20
this_is_another_number = 45.2

def print_a_list(gold_coin):
    golds = [100, 101, 105, 103, 103, 105, 109]
    coins = [300, 310, 302, 301, 900, 1000, 1001]
    if gold_coin == 0:
        return golds
    else:
        return coins

coins = print_a_list(1)
print(coins[2:3])
print(coins[-4:-2])