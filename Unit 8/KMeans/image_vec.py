import sys
import urllib.request
import io
from PIL import Image
import random
# URL = 'https://i.pinimg.com/originals/95/2a/04/952a04ea85a8d1b0134516c52198745e.jpg'
# f = io.BytesIO(urllib.request.urlopen(URL).read()) # Download the picture at the url as a file object
# img = Image.open(f) # You can also use this on a local file; just put the local filename in quotes in place of f.
# # img.show() # Send the image to your OS to be displayed as a temporary file
# dims = img.size # A tuple. Note: width first THEN height. PIL goes [x, y] with y counting from the top of the frame.
# pix = img.load() # Pix is a pixel manipulation object; we can assign pixel values and img will change as we do so.
# # print(pix[2,5]) # Access the color at a specific location; note [x, y] NOT [row, column].
# pix[2,5] = (255, 255, 255) # Set the pixel to white. Note this is called on “pix”, but it modifies “img”.
# # img.show() # Now, you should see a single white pixel near the upper left corner
# img.save("puppy.png") # Save the resulting image. Alter your filename as necessary.

# img = Image.open("/Users/anish/Documents/TJHSST-AI-2/Unit 8/KMeans/puppy.png")
URL = sys.argv[1]
f = io.BytesIO(urllib.request.urlopen(URL).read())
img = Image.open(f)
dims = img.size
pix = img.load()
orig_pix_vals = []

for x in range(0, dims[0]):
    for y in range(0, dims[1]):
        pix_vals = pix[x,y]
        orig_pix_vals.append(pix_vals)

#Naive 8
# for x in range(0, dims[0]):
#     for y in range(0, dims[1]):
#         upd_pix_vals = []
#         pix_vals = pix[x,y]
#         for val in pix_vals:
#             if(val < 128):
#                 upd_pix_vals.append(0)           
#             else:
#                 upd_pix_vals.append(255)
#         tup_app = tuple(upd_pix_vals)
#         pix[x,y] = tup_app

# naive_8 = img.save('naive8.png')

# Naive 27
# for x in range(0, dims[0]):
#     for y in range(0, dims[1]):
#         upd_pix_vals = []
#         pix_vals = pix[x,y]
#         for val in pix_vals:
#             if(val < (255/3)):
#                 upd_pix_vals.append(0)           
#             elif(val > 510/3):
#                 upd_pix_vals.append(255)
#             else:
#                 upd_pix_vals.append(127)
#         tup_app = tuple(upd_pix_vals)
#         pix[x,y] = tup_app

# naive_27 = img.save('naive27.png')

k = int(sys.argv[2])
dict_colors = dict()
rand_pts = []
orig_rgb = []

for i in range(k):
    rand_x, rand_y = random.randint(0, dims[0]), random.randint(0, dims[1])
    rgb_vals = pix[rand_x,rand_y]
    if(rgb_vals not in orig_rgb):
        rand_pts.append((rand_x, rand_y))
        orig_rgb.append(rgb_vals)

def find_rgb_dict(sets):
    rgb_dict = dict()
    for i in range(k):
        rgb_dict[i] = list()
    for s in orig_pix_vals:
        sq_errors = []
        for o_s in orig_rgb:
            sq_er = (s[0] - o_s[0]) ** 2 + (s[1] - o_s[1]) ** 2 + (s[2] - o_s[2]) ** 2
            sq_errors.append(sq_er)
        
        min_loc = 0
        min_err = max(sq_errors)
        for ct, sq in enumerate(sq_errors):
            if(sq < min_err):
                min_loc = ct
                min_err = sq
        rgb_dict[min_loc].append(s)
    
    return rgb_dict

def get_results(prev_dict, rgb_dict, prevError):
    list_diff = []
    for i in range(k):
        val_prev, val_curr = len(prev_dict[i]), len(rgb_dict[i])
        val_diff = val_curr - val_prev
        list_diff.append(val_diff)
    sq_err = 0
    for val in list_diff:
        sq_err += (val ** 2)
    num_0 = list_diff.count(0)
    err_ratio = sq_err / prevError
    if(num_0 == k or (err_ratio >= 0.97 and err_ratio <= 1.03)):
        return (True, sq_err)
    else:
        return (False, sq_err)

to_cont = False
prevError = float('inf')
while(to_cont == False):
    rgb_dict = find_rgb_dict(orig_rgb)
    for l in rgb_dict:
        list_check = rgb_dict[l]
        list_means = list()

        for i in range(3):
            list_i = [x[i] for x in list_check]
            list_means.append(sum(list_i) / len(list_i))

        tuple_means = tuple(list_means)
        orig_rgb[l] = tuple_means
    
    prev_dict = rgb_dict
    rgb_dict = find_rgb_dict(orig_rgb)
    to_cont, prevError = get_results(prev_dict, rgb_dict, prevError)

def return_lowest_error(x, y):
    sq_errors = []
    s = pix[x,y]

    for o_s in orig_rgb:
        sq_er = (s[0] - o_s[0]) ** 2 + (s[1] - o_s[1]) ** 2 + (s[2] - o_s[2]) ** 2
        sq_errors.append(sq_er)

    min_loc = 0
    min_err = max(sq_errors)
    for ct, sq in enumerate(sq_errors):
        if(sq < min_err):
            min_loc = ct
            min_err = sq
    
    return min_loc

for x in range(0, dims[0]):
    for y in range(0, dims[1]):
        num_loc = return_lowest_error(x, y)
        mean_to_use = orig_rgb[num_loc]
        pix[x,y] = (round(mean_to_use[0]), round(mean_to_use[1]), round(mean_to_use[2]))

final_img = img.save("kmeansout.png")