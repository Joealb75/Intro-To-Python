value_1 = 3
value_2 = 5


def secret_formula(num_1, num_2):
    n1_sum = 0
    n2_sum = 0
    total = 0

    if num_1 and num_2 > 0:      # Why when I replace line 11 or 12 with the code below do I get 0.0 as the result?
        n1_sum = num_1 * num_1              # n1_sum *= num_1
        n2_sum = num_2 * num_2              # n2_sum *= num_2
        total = (n1_sum + n2_sum) / 2
        print(total)

    else:       # if the number is not > 0 it must be 0 or negative.
        print("Error: Numbers cannot be zero or negative.")


secret_formula(value_1, value_2)
