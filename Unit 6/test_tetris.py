test_str = '                                                                                                                                                                          #         #         #         '
def print_board(bd):
    test_count = 0
    str_1 = ""
    for ch in bd:
        str_1 += ch
        test_count += 1
        
        if(test_count % 10 == 0):
            print(str_1)
            str_1 = ""

print_board(test_str)