from PIL import Image
import pytesseract
import os

# Getting text/string from image.
puzzle_Image = Image.open(os.getcwd() + '/file.png')
text = pytesseract.image_to_string(puzzle_Image)
with open('result.txt', 'w') as result_file:
    result_file.write(text)

# Opening text file for reading lines.
with open('result.txt', 'r') as file:
    read_file = file.readlines()

# Formatting text in the same format given in image.
size = len(read_file)
index_list = [idx + 1 for idx, val in enumerate(read_file) if val == '\n']
result_list = [read_file[i: j] for i, j in zip([0] + index_list, index_list + ([size] if index_list[-1] != size else []))]

for i in range(19):
    lst = [item[i].strip('\n') for item in result_list]
    final_result = " ".join(lst)
    print(final_result)
