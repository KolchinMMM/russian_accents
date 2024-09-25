import csv
import re


def replace_stresses(text):
    return (text.replace("а́", "+а")
            .replace("е́", "+е")
            .replace("я́", "+я")
            .replace("и́", "+и")
            .replace("о́", "+о")
            .replace("э́", "+э")
            .replace("ы́", "+ы")
            .replace("у́", "+у")
            .replace("ю́", "ю"))



with open("texts/ruscorpora_content(1).csv", "r", encoding="utf-8") as file:
    f = list(csv.reader(file, delimiter=";"))


re_end = "[^а-яА-Я◌́]+\S+$"


texts = []
huge_text = "".join(f[1][2:6])
last = ""
last_title = f[1][6]

for line in f[2:]:

    if line[6] != last_title or line[0] == "":
        last_title = line[6]
        texts.append(huge_text)
        huge_text = "".join(line[2:6])
        huge_text += line[0]
    else:
        match = re.search(re_end, line[5])
        if match:
            match = match[0]
            if match != last:
                huge_text += match

                last = match
texts.append(huge_text)
print(len(texts))
for text in texts:
    print(text)

with open("res/stress.csv", "w", encoding="utf-8") as file:
    file.write("question,answer\n")
    for text in texts:
        new_text = replace_stresses(text)
        file.write(f"{new_text.replace('+', '')},{new_text}\n")