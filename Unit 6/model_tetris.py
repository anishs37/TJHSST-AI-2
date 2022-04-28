import sys

beginning_board = sys.argv[1]
board_list_rep = []
height_check = []

for i in range(10):
    height = 0
    inter_counter = 20
    if_checked = False

    col_str = beginning_board[i:200:10]

    for j in range(20):
        if(if_checked == False):
            check_char = col_str[j]

            if(check_char == "#"):
                if_checked = True

            else:
                inter_counter -= 1
    
    height_check.append(inter_counter)

for tag in beginning_board:
    board_list_rep.append(tag)

orig_board_list = board_list_rep[:]

orientations = []

i_0 = {
    0:(0, 1),
    1:(0, 1),
    2:(0, 1),
    3:(0, 1)
}

i_1 = {
    0:(0, 4)
}

o = {
    0:(0, 2),
    1:(0, 2)
}

t_0 = {
    0:(0, 1),
    1:(0, 2),
    2:(0, 1)
}

t_1 = {
    0:(0, 3),
    1:(-1, 1)
}

t_2 = {
    0:(-1, 1),
    1:(0, 2),
    2:(-1, 1)
}

t_3 = {
    0:(-1, 1),
    1:(0, 3)
}

s_0 = {
    0:(0, 1),
    1:(0, 2),
    2:(-1, 1)
}

s_1 = {
    0:(-1, 2),
    1:(0, 2)
}

z_0 = {
    0:(-1, 1),
    1:(0, 2),
    2:(0, 1)
}

z_1 = {
    0:(0, 2),
    1:(-1, 2)
}

j_0 = {
    0:(0, 2),
    1:(0, 1),
    2:(0, 1)
}

j_1 = {
    0:(0, 3),
    1:(-2, 1)
}

j_2 = {
    0:(-1, 1),
    1:(-1, 1),
    2:(0, 2)
}

j_3 = {
    0:(0, 1),
    1:(0, 3)
}

l_0 = {
    0:(0, 1),
    1:(0, 1),
    2:(0, 2)
}

l_1 = {
    0:(0, 3),
    1:(0, 1)
}

l_2 = {
    0:(0, 2),
    1:(-1, 1),
    2:(-1, 1)
}

l_3 = {
    0:(-2, 1),
    1:(0, 3)
}

orientations.append(i_0)
orientations.append(i_1)
orientations.append(o)
orientations.append(t_0)
orientations.append(t_1)
orientations.append(t_2)
orientations.append(t_3)
orientations.append(s_0)
orientations.append(s_1)
orientations.append(z_0)
orientations.append(z_1)
orientations.append(j_0)
orientations.append(j_1)
orientations.append(j_2)
orientations.append(j_3)
orientations.append(l_0)
orientations.append(l_1)
orientations.append(l_2)
orientations.append(l_3)

def print_board(bd):
    test_count = 0
    str_1 = ""
    for ch in bd:
        str_1 += ch
        test_count += 1
        
        if(test_count % 10 == 0):
            print(str_1)
            str_1 = ""

# print_board(beginning_board)
# print()
# print()

def clear_rows(bod):
    bd = "".join(bod)
    for i in range(0, 191, 10):
        sub_str = bd[i:i+10]
        if(sub_str.count('#') == 10):
            bd = bd[:i] + bd[i + 10:]
            for j in range(10):
                bd = " " + bd
    
    return bd

to_print = []

for orien in orientations:
    num_cols = len(orien)

    for pl in range(11 - num_cols):
        maxis = []

        for l in range(num_cols):
            maxis.append(orien[l][0] + height_check[pl + l] + 1)
        
        min_place = max(maxis)
        locs_to_place = []

        for j in range(num_cols):
            for to_len in range(orien[j][1]):
                f_row = orien[j][0]
                row_pl = min_place + abs(f_row) + to_len
                col_pl = pl + j
                ind_pl = ((20 - row_pl) * 10) + col_pl
                locs_to_place.append(ind_pl)
        
        count_out_of_range = 0

        for tag in locs_to_place:
            if(tag < 0 and count_out_of_range == 0):
                to_print.append("GAME OVER")
                count_out_of_range += 1
                
        if(count_out_of_range == 0):
            for tg in locs_to_place:
                board_list_rep[tg] = "#"
                # print_board(board_list_rep)

        if(count_out_of_range == 0):
            st_to_pt = clear_rows(board_list_rep)
            to_print.append(st_to_pt)

        board_list_rep = orig_board_list[:]
        locs_to_place = []

file_path = 'tetrisout.txt'
sys.stdout = open(file_path, "w")
for thing in to_print:
    print(thing)