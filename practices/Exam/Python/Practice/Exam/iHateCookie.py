# one box -> 24 cookies
# one container -> 75 boxes

def calculate_hate_for_cookie(num_cookie):
    left_cookie = 0
    left_box = 0

    box = 0
    container = 0

    if num_cookie != 0 and num_cookie <=24:
        box = 1
        container = 1
        left_box = 0
        left_cookie = 0
    else:
        box = num_cookie // 24
        left_cookie = num_cookie % 24

    if 75 > box > 0:
        container = 1
    else:
        container = num_cookie // 75
        left_box = box % 75
    print(f'number of boxes : {box}')
    print(f'number of containers : {container}')
    print(f'number of left out boxes : {left_box}')
    print(f'number of left out cookies : {left_cookie}')

calculate_hate_for_cookie(70665)



