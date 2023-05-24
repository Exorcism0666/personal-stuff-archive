import re

def find_telegram_links(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        text = f.read()
    links = re.findall(r'http[s]?://t(?:elegram)?.me/(?!joinchat|share)\S+', text)
    with open(output_file, 'w', encoding='utf-8') as f:
        for link in links:
            f.write(link + '\n')

find_telegram_links('input.txt', 'output.txt')
