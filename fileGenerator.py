import docx
import random
import os
len, countFile = 10000, 10
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
         'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
         'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
         'z', ' ']
upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
         'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q',
         'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
         'Z', ' ']
symbol = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', ' ', '~',
          '>', '*', '(', ')', '<', '+', '-', '_', '&', '^', '!', ';', ',']
combined_list_paragraph = digits + upper + lower + symbol
combined_list_name = digits + upper + lower


def gen_paragraph(len):
    rand_digit = random.choice(digits)
    rand_upper = random.choice(upper)
    rand_lower = random.choice(lower)
    rand_symbol = random.choice(symbol)
    paragraph = rand_lower + rand_digit + rand_upper + rand_symbol
    for i in range(len):
        paragraph = paragraph + random.choice(combined_list_paragraph)
    return paragraph


def gen_file_name(len):
    rand_digit = random.choice(digits)
    rand_upper = random.choice(upper)
    rand_lower = random.choice(lower)
    paragraph = rand_lower + rand_digit + rand_upper
    for i in range(len):
        paragraph = paragraph + random.choice(combined_list_name)
    return paragraph


if not os.path.exists('docxFiles'):
    os.makedirs('docxFiles')
for x in range(countFile):
    file = docx.Document()
    file.add_paragraph(gen_paragraph(len))
    file.save(f'docxFiles/{gen_file_name(10)}.docx')
print("Done!")
choice = input(
    "Do you want to remove all docx files (delete after upload)? (y/n)")
if choice == 'y':
    os.system('rmdir /s /q docxFiles')
    print("Done!")
print("Exiting...")
