import re
from crypto.Cipher import AES
import base64


def get_file_content(file):
    with open(file) as f:
        return f.read()


def decode_base64(content):
    return base64.b64decode(content)


def decrypt_content(content, key):
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.decrypt(content)


page_delimiter = '~@~'
line_delimiter = '\n'


# regex = ''
# c = ""
# content = decrypt_content(c, 1)
# pages = content.split(page_delimiter)
#
# for page in pages:
#     pass

def return_indices(regex, text):
    match = re.match(regex, text)
    if match:
        first, second = match.span()
        return first, second - 1
    return 0, 0


def extract_digits(text):
    digits_regex = r'\d+'
    result = re.findall(digits_regex, text)
    return result if result else []


def extract_numbers(text):
    first_regex = r"F[a-zA-Z]*I"
    second_regex = r"I[0-9]*N"
    third_regex = r'N[^a-zA-Z0-9_]{0,5}D'
    fourth_regex = r'D[ \t]+[0-9]x[0-9]'
    new_line_regex = r'\n'
    original_text = text + ''

    f_index, i_index = return_indices(first_regex, text)
    if f_index or i_index:
        original_i = i_index
        text = text[i_index:]
        i_index, n_index = return_indices(second_regex, text)

        if i_index or n_index:
            original_n = original_i + n_index
            text = text[n_index:]
            n_index, d_index = return_indices(third_regex, text)
            if n_index or d_index:
                original_d = original_n + d_index
                text = text[d_index:]
                d_index, last_index = return_indices(fourth_regex, text)

                if d_index or last_index:
                    new_l1, new_l2 = return_indices(new_line_regex, original_text[f_index: original_d + 1])
                    if new_l2 == 0 and new_l1 == 0:
                        text = text[d_index + 1: last_index + 1]
                        digits = [int(d) for d in extract_digits(text)]
                        return digits


if __name__ == '__main__':
    content = "FaabDAWsqqI12N~@D 5x3"
    result = ''
    pages = content.split(page_delimiter)
    for page in pages:
        numbers = extract_numbers(page)
        if numbers and len(numbers) > 1:
            page_n, line_n = numbers
            indexed_page = pages[page_n - 1]

            lines = [line for line in indexed_page.split(line_delimiter) if line]
            if len(lines) > line_n - 1:
                indexed_line = lines[line_n]
                numbers = extract_numbers(indexed_line)
                if numbers:
                    result += ''.join(numbers)

        print(extract_numbers(content))
