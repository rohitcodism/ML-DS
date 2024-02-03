def is_cube_equal(num):
    num_str = str(num)
    sum_cube = sum(int(num)**3 for num in num_str)
    return num == sum_cube

def max_min(num_arr):
    max_num = max(num_arr)
    min_num = min(num_arr)
    return max_num,min_num

def all_validator(num_arr):

    equal_cube_num = []

    for num in num_arr:
        if is_cube_equal(num):
            equal_cube_num.append(num)
    print(equal_cube_num)

    order_arr = max_min(num_arr=equal_cube_num)
    print("max : ",order_arr[0])
    print("min: ", order_arr[1])

all_validator([123, 371, 407, 153, 370])


