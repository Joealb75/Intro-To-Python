value_1 = -10
value_2 = -1


def secret_formula(num_1, num_2):
    n1_sum = 0
    n2_sum = 0
    total = 0

    if num_1 and num_2 > 0:
        n1_sum = num_1 * num_1
        n2_sum = num_2 * num_2
        total = (n1_sum + n2_sum) // 2
        return total

    elif num_1 or num_2 <= 0:
        t_f = bool(total)
        return t_f


return_value = secret_formula(value_1, value_2)

print(return_value)
