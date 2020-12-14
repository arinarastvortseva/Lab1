import re
import csv

symbols = 0  # подсчёт символов
symbols_no_space = 0  # подсчёт символов без пробела
symbols_no_punct = 0  # подсчет символов без знаков препинания
words = 0  # подсчёт слов
sentences = 0  # подсчёт предложений

new_word = False

text = ''

with open('steam_description_data.csv', encoding="utf-8") as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        for i in range(len(row)):
            symbols += len(row[i])
            if i != 0:
                text += row[i]
                text += ' '

            for j in range(len(row[i]) - 1):
                symb = row[i][j]
                symb_next = row[i][j+1]

                if symb != ' ':
                    symbols_no_space += 1
                if symb.isalpha() or j == ' ':
                    symbols_no_punct += 1

                if symb.isalpha():
                    new_word = True
                elif symb in ".'-" and symb_next.isalpha() and new_word:
                    pass
                else:
                    new_word = False
                    words += 1

    #text = csv_file.read()
    #sentences += len(re.findall(r'[.!?]\s', text))
new_text = re.sub(r'[.!?]\s', r'|', text)
sentences += len(new_text.split('|'))

print('Количество символов в файле: ', symbols)
print('Количество символов в файле без пробелов: ', symbols_no_space)
print('Количество символов без знаков препинания: ', symbols_no_punct)
print('Количество слов: ', words)
print('Количество предложений: ', sentences)

