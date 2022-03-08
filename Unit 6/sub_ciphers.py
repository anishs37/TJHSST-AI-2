from audioop import cross
from math import log
import random
import operator
import sys

alphabet = "ETAOINSHRDLCUMWFGYPBVKXJQZ"
POPULATION_SIZE = 500
NUM_CLONES = 1
TOURNAMENT_SIZE = 20
TOURNAMENT_WIN_PROBABILITY = .75
CROSSOVER_LOCATIONS = 5
MUTATION_RATE = .8
ENCODED_TEXT_TO_DECODE = sys.argv[1]

with open("ngrams.txt") as f:
    ngrams = [line.strip() for line in f]

ngrams_dict = {}

for ng in ngrams:
    ng_split = ng.split(" ")
    ngrams_dict[ng_split[0]] = int(ng_split[1])

def encoder(phrase, scrambled_alpha):
    phrase = phrase.upper()
    scrambled_alpha = scrambled_alpha.upper()
    encoded = ""

    for let in phrase:
        if(let in alphabet):
            orig_loc = alphabet.index(let)
            new_enc = scrambled_alpha[orig_loc]
            encoded += new_enc
        
        else:
            encoded += let

    return encoded

def decoder(scrambled_phrase, scrambled_alpha):
    scrambled_phrase = scrambled_phrase.upper()
    scrambled_alpha = scrambled_alpha.upper()
    decoded = ""

    for let in scrambled_phrase:
        if(let in alphabet):
            orig_loc = scrambled_alpha.index(let)
            new_dec = alphabet[orig_loc]
            decoded += new_dec
        
        else:
            decoded += let
    
    return decoded

def ng_score(ng_str):
    len_ng = len(ng_str)
    count_in = 0
    
    for let in ng_str:
        if(let in alphabet):
            count_in += 1

    if(count_in != len_ng or ng_str not in ngrams_dict):
        return 0
    
    num_ng = ngrams_dict[ng_str]
    log_ret = log(num_ng, 2)
    return log_ret

def fitness(n, enc_text, scramb_alpha):
    tot_score = 0
    dec_text = decoder(enc_text, scramb_alpha)
    start = 0

    while(start <= len(dec_text) - n):
        ng_test = dec_text[start:start+n]
        tot_score += ng_score(ng_test)
        start += 1

    return tot_score

def hill_climbing(enc_text):
    high_score = 0
    scramb_alpha = ("".join(random.sample(alphabet, 26)))
    inf_count = 0
    dec_text_try = enc_text

    while(inf_count == 0):
        ft_score = fitness(4, enc_text, scramb_alpha)

        if(ft_score > high_score):
            dec_text_try = decoder(enc_text, scramb_alpha)
            high_score = ft_score
        
        rand_1 = random.randint(0, 25)
        rand_2 = random.randint(0, 25)

        holder = scramb_alpha[rand_2]
        scramb_alpha = scramb_alpha[:rand_2] + scramb_alpha[rand_1] + scramb_alpha[rand_2 + 1:]
        scramb_alpha = scramb_alpha[:rand_1] + holder + scramb_alpha[rand_1 + 1:]

        print(dec_text_try)

def pick_random():
    random_list = []
    
    while(len(random_list) != POPULATION_SIZE):
        scramb_alpha = ("".join(random.sample(alphabet, 26)))

        if(scramb_alpha not in random_list):
            random_list.append(scramb_alpha)

    return random_list

def generate_ft_dict(rand_strats):
    ft_scores = {}

    for strat in rand_strats:
        ft_sc = fitness(3, ENCODED_TEXT_TO_DECODE, strat)
        ft_scores[strat] = ft_sc

    return ft_scores

def run_tournaments(strat_list, ft_scores):
    p1, p2 = "", ""
    rand_strats = random.sample(strat_list, 2 * TOURNAMENT_SIZE)
    tourn1list, tourn2list = rand_strats[:20], rand_strats[20:]
    ftscores1, ftscores2 = [], []

    for strat in tourn1list:
        ft_sc_1 = ft_scores[strat]
        ftscores1.append((strat, ft_sc_1))
    
    for strat in tourn2list:
        ft_sc_2 = ft_scores[strat]
        ftscores2.append((strat, ft_sc_2))
    
    ftscores1.sort(key = lambda x: x[1], reverse=True)
    ftscores2.sort(key = lambda x: x[1], reverse=True)
    count1 = 0
    count2 = 0

    while(len(p1) == 0):
        elem_try = ftscores1[count1]

        if(random.random() < TOURNAMENT_WIN_PROBABILITY):
            p1 = elem_try[0]

        count1 += 1

    while(len(p2) == 0):
        elem_try = ftscores2[count2]

        if(random.random() < TOURNAMENT_WIN_PROBABILITY):
            p2 = elem_try[0]
            
        count2 += 1

    return p1, p2

def run_breed(pa1, pa2):
    final_child_list = ["-"] * 26
    crossovers = random.sample(range(0, 26), CROSSOVER_LOCATIONS)
    for cr in crossovers:
        final_child_list[cr] = pa1[cr]
    
    for ch in pa2:
        if(ch not in final_child_list):
            ind_insert = final_child_list.index('-')
            final_child_list[ind_insert] = ch
    
    if(random.random() < MUTATION_RATE):
        locs_swap = random.sample(range(0, 26), 2)
        holder = final_child_list[locs_swap[0]]
        final_child_list[locs_swap[0]] = final_child_list[locs_swap[1]]
        final_child_list[locs_swap[1]] = holder

    child = "".join(final_child_list)
    return child

generation_num = 1
curr_gen = pick_random()
next_gen = []

while(generation_num <= 500):
    ft_dict = generate_ft_dict(curr_gen)
    ft_dict_sorted = dict(sorted(ft_dict.items(), key=operator.itemgetter(1), reverse=True))
    next_gen.append(next(iter(ft_dict_sorted)))
    print(decoder(ENCODED_TEXT_TO_DECODE, next_gen[0]))
    while(len(next_gen) != POPULATION_SIZE):
        p1, p2 = run_tournaments(curr_gen, ft_dict)
        new_child = run_breed(p1, p2)
        next_gen.append(new_child)
    
    curr_gen = next_gen.copy()
    next_gen.clear()
    generation_num += 1

final_ft_dict = generate_ft_dict(curr_gen)
final_ft_dict_sorted = dict(sorted(final_ft_dict.items(), key=operator.itemgetter(1), reverse=True))
best_cipher = next(iter(ft_dict))
print(decoder(ENCODED_TEXT_TO_DECODE, best_cipher))

#print(fitness(4, "XMTP CGPQR BWEKNJB GQ OTGRB EL BEQX BWEKNJB, G RFGLI. GR GQ BEQX ABSETQB RFGQ QBLRBLSB TQBQ EJJ RBL KMQR SMKKML VMPYQ GL BLDJGQF: 'G FEUB RM AB E DMMY QRTYBLR GL RFER SJEQQ GL RFB PMMK MC RFER RBESFBP.'", "XRPHIWGSONFQDZEYVJKMATUCLB"))
#hill_climbing("XMTP CGPQR BWEKNJB GQ OTGRB EL BEQX BWEKNJB, G RFGLI. GR GQ BEQX ABSETQB RFGQ QBLRBLSB TQBQ EJJ RBL KMQR SMKKML VMPYQ GL BLDJGQF: 'G FEUB RM AB E DMMY QRTYBLR GL RFER SJEQQ GL RFB PMMK MC RFER RBESFBP.'")
#hill_climbing("PF HACYHTTRQ VF N PBYYRPGVBA BS SERR YRNEAVAT NPGVIVGVRF GUNGGRNPU PBZCHGRE FPVRAPR GUEBHTU RATNTVAT TNZRF NAQ CHMMYRF GUNGHFR PNEQF, FGEVAT, PENLBAF NAQ YBGF BS EHAAVAT NEBHAQ. JRBEVTVANYYL QRIRYBCRQ GUVF FB GUNG LBHAT FGHQRAGF PBHYQ QVIR URNQ-SVEFG VAGB PBZCHGRE FPVRAPR, RKCREVRAPVAT GUR XVAQF BS DHRFGVBAFNAQ PUNYYRATRF GUNG PBZCHGRE FPVRAGVFGF RKCREVRAPR, OHG JVGUBHGUNIVAT GB YRNEA CEBTENZZVAT SVEFG. GUR PBYYRPGVBA JNF BEVTVANYYLVAGRAQRQ NF N ERFBHEPR SBE BHGERNPU NAQ RKGRAFVBA, OHG JVGU GURNQBCGVBA BS PBZCHGVAT NAQ PBZCHGNGVBANY GUVAXVAT VAGB ZNALPYNFFEBBZF NEBHAQ GUR JBEYQ, VG VF ABJ JVQRYL HFRQ SBE GRNPUVAT.GUR ZNGREVNY UNF ORRA HFRQ VA ZNAL PBAGRKGF BHGFVQR GUR PYNFFEBBZNF JRYY, VAPYHQVAT FPVRAPR FUBJF, GNYXF SBE FRAVBE PVGVMRAF, NAQFCRPVNY RIRAGF. GUNAXF GB TRAREBHF FCBAFBEFUVCF JR UNIR ORRANOYR GB PERNGR NFFBPVNGRQ ERFBHEPRF FHPU NF GUR IVQRBF, JUVPU NERVAGRAQRQ GB URYC GRNPUREF FRR UBJ GUR NPGVIVGVRF JBEX (CYRNFRQBA’G FUBJ GURZ GB LBHE PYNFFRF – YRG GURZ RKCREVRAPR GURNPGVIVGVRF GURZFRYIRF!). NYY BS GUR NPGVIVGVRF GUNG JR CEBIVQRNER BCRA FBHEPR – GURL NER ERYRNFRQ HAQRE N PERNGVIR PBZZBAFNGGEVOHGVBA-FUNERNYVXR YVPRAPR, FB LBH PNA PBCL, FUNER NAQ ZBQVSLGUR ZNGREVNY. SBE NA RKCYNANGVBA BA GUR PBAARPGVBAF ORGJRRA PFHACYHTTRQ NAQ PBZCHGNGVBANY GUVAXVAT FXVYYF, FRR BHEPBZCHGNGVBANY GUVAXVAT NAQ PF HACYHTTRQ CNTR. GB IVRJ GUR GRNZBS PBAGEVOHGBEF JUB JBEX BA GUVF CEBWRPG, FRR BHE CRBCYR CNTR.SBE QRGNVYF BA UBJ GB PBAGNPG HF, FRR BHE PBAGNPG HF CNTR. SBEZBER VASBEZNGVBA NOBHG GUR CEVAPVCYRF ORUVAQ PF HACYHTTRQ, FRRBHE CEVAPVCYRF CNTR.")