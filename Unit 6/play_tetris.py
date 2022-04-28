from math import log
import random
import operator

POPULATION_SIZE = 500
NUM_CLONES = 100
TOURNAMENT_SIZE = 20
TOURNAMENT_WIN_PROBABILITY = .75
NUM_TRIALS = 5
MUTATION_RATE = .8

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

orientations.append((i_0, 1))
orientations.append((i_1, 1))
orientations.append((o, 2))
orientations.append((t_0, 3))
orientations.append((t_1, 3))
orientations.append((t_2, 3))
orientations.append((t_3, 3))
orientations.append((s_0, 4))
orientations.append((s_1, 4))
orientations.append((z_0, 5))
orientations.append((z_1, 5))
orientations.append((j_0, 6))
orientations.append((j_1, 6))
orientations.append((j_2, 6))
orientations.append((j_3, 6))
orientations.append((l_0, 7))
orientations.append((l_1, 7))
orientations.append((l_2, 7))
orientations.append((l_3, 7))

def make_new_board():
    orig_string = " " * 200
    return orig_string

def check_height(board):
    height_check = []
    for i in range(10):
        inter_counter = 20
        if_checked = False

        col_str = board[i:200:10]
        for j in range(20):
            if(if_checked == False):
                check_char = col_str[j]

                if(check_char == "#"):
                    if_checked = True

                else:
                    inter_counter -= 1
        
        height_check.append(inter_counter)

    return height_check

def clear_rows(bod):
    bd = "".join(bod)
    n_cl = 0
    for i in range(0, 191, 10):
        sub_str = bd[i:i+10]
        if(sub_str.count('#') == 10):
            n_cl += 1
            bd = bd[:i] + bd[i + 10:]
            for j in range(10):
                bd = " " + bd
    
    return bd, n_cl

def heuristic(board, strategy):
    a = strategy
    # a, b, c, d = strategy[0], strategy[1], strategy[2], strategy[3]
    h_to_ch = check_height(board)
    value = 0
    value += a * max(h_to_ch)
    # value += b * (perhaps deepest well depth?)
    # value += c * (perhaps number of holes in board, ie empty spaces with a filled space above?)
    # value += d * (perhaps the number of lines that were just cleared, in the move that made this board?)
    # add as many variables as you want - whatever you think might be relevant!
    return value

def place_piece(orien, board):
    num_cols = len(orien) - 1

    for pl in range(11 - num_cols):
        maxis = []
        for l in range(num_cols):
            height_check = check_height(board)
            orien_0_l_0 = orien[0][l][0]
            h_c = height_check[pl + l]
            maxis.append(orien_0_l_0 + h_c + 1)
        
        min_place = max(maxis)
        locs_to_place = []

        for j in range(num_cols):
            for to_len in range(orien[0][j][1]):
                f_row = orien[0][j][0]
                row_pl = min_place + abs(f_row) + to_len
                col_pl = pl + j
                ind_pl = ((20 - row_pl) * 10) + col_pl
                locs_to_place.append(ind_pl)
    
        count_out_of_range = 0

        for tag in locs_to_place:
            if(tag < 0):
                count_out_of_range += 1
        
        if(count_out_of_range == 0):
            for tg in locs_to_place:
                board = board[:tg] + "#" + board[tg + 1:] 
            
            board, num_clear = clear_rows(board)
            
            return board, False, num_clear
        
        if(count_out_of_range > 0):
            return board, True, 0
def print_board(bd):
    test_count = 0
    str_1 = ""
    for ch in bd:
        str_1 += ch
        test_count += 1
        
        if(test_count % 10 == 0):
            print(str_1)
            str_1 = ""
    return str_1
def play_game(strategy):
    board = make_new_board()
    highest_board = (board, 0, -1, 0, True)
    points = 0
    count_over = 0

    while(count_over == 0):
        piece_int = random.randint(1, 7)
        poss_orien_piece = []

        for orien in orientations:
            if(orien[1] == piece_int):
                poss_orien_piece.append(orien)
        
        for poss_orien in poss_orien_piece:
            board, is_over, num_clear = place_piece(poss_orien, board)
            print_board(board)
            eval_board = heuristic(board, strategy)
            if(is_over == True):
                eval_board *= -1000

            if(eval_board > highest_board[2]):
                prev_pts = highest_board[1]
                highest_board = (board, prev_pts, eval_board, num_clear, is_over)

        n_clear = highest_board[3]

        if(is_over == True):
            count_over += 1
        
        else:
            if(n_clear == 1):
                points += 40
            
            if(n_clear == 2):
                points += 100
            
            if(n_clear == 3):
                points += 300
            
            if(n_clear >= 4):
                points += 1200
            
        oldPts = highest_board[1]
        highest_board = (board, oldPts + points, -1, num_clear, is_over)
        board = highest_board[0]
    
    return highest_board[1]

def generate_random_strats():
    strategies = []
    r_ch = 1

    for j in range(POPULATION_SIZE):
        for i in range(r_ch):
            rand_ch = random.random()

            if(random.random() < 0.5):
                rand_ch *= -1
            
            strategies.append(rand_ch)
    
    return strategies

def fitness_function(strategy):
    game_scores = []
    for count in range(NUM_TRIALS):
        game_scores.append(play_game(strategy))
    return sum(game_scores) / 5

generation_num = 1
curr_gen = generate_random_strats()
next_gen = []

while(generation_num <= 3):
    st_eval = 0
    ft_scs = []

    for st in curr_gen:
        ft_sc = fitness_function(st)
        print("Evaluating Strategy " + str(st_eval) + " --> " + str(ft_sc))
        ft_scs.append((ft_sc, st))
        st_eval += 1

    ft_sorted = sorted(ft_scs, reverse = True)

    for j in range(NUM_CLONES):
        next_gen.append(next(iter(ft_scs)))

    # while(len(next_gen) != POPULATION_SIZE):
    #     p1, p2 = run_tournaments(curr_gen, ft_scs)
    #     new_child = run_breed(p1, p2)
    #     next_gen.append(new_child)
    
    curr_gen = next_gen.copy()
    next_gen.clear()
    generation_num += 1