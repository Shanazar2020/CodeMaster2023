import re


def get_file_content(file):
    with open(file) as f:
        return f.read()


def decode_content(content):
    return content


def decrypt_content(content, key):
    return content


page_delimiter = '~@~'
line_delimiter = '\n'
first_regex = r"F[a-zA-Z]*I"
second_regex = r"I[0-9]*N"
third_regex = r'N[^a-zA-Z0-9_]{0,5}D'
fourth_regex = r'D[ \t\n\r\f\v]+[0-9]x[0-9]'
digits_regex = r'\d+'
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


if __name__ == '__main__':
    sample = "FIND 5x3"
    f_index, i_index = return_indices(first_regex, sample)
    if f_index or i_index:
        sample = sample[i_index:]
        i_index, n_index = return_indices(second_regex, sample)

        if i_index or n_index:
            sample = sample[n_index:]
            n_index, d_index = return_indices(third_regex, sample)
            if n_index or d_index:
                sample = sample[d_index:]
                d_index, last_index = return_indices(fourth_regex, sample)
                if d_index or last_index:
                    print("Found")
                    sample = sample[d_index+1: last_index+1]
                    print(sample)
                    digits = [int(d) for d in re.findall(digits_regex, sample)]
                    print(digits)
