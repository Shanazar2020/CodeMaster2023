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
regex = ''
c = ""
content = decrypt_content(c, 1)
pages = content.split(page_delimiter)

for page in pages:
    pass
