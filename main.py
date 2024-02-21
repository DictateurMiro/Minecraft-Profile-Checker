import os 
import requests
import time
import re

os.system("cls")

def print_rgb(r, g, b, texte):
    print(f"\x1b[38;2;{r};{g};{b}m{texte}\x1b[0m")

def clear_lines(lines):
    # Remove accent
    lines = re.sub(r'[éèêë]', 'e', lines)
    return lines

liness_modifiees = []

with open('name.txt', 'r', encoding='utf-8') as file:
    for lines in file:
        lines = lines.strip()
        if 3 <= len(lines) <= 16:
            lines = clear_lines(lines)
            liness_modifiees.append(lines)

with open('name.txt', 'w', encoding='utf-8') as file:
    for lines in liness_modifiees:
        file.write(lines + '\n') 

liness = 0
mtn = 0

with open('name.txt', 'r') as f:
    for l in f:
        liness += 1

print("Nombre de liness dans le file : " + str(liness) + "\n\n")

with open('name.txt', 'r') as f:
    for l in f:
        mtn += 1
        lp = l.strip()
        url = "https://api.mojang.com/users/profiles/minecraft/" + lp
        time.sleep(1)
        os.system("title Pseudo : " + lp + " (" + str(mtn) + "/" + str(liness) + ")")
        r = requests.get(url)
        d = r.status_code
        if d == 200:
            print_rgb(255, 50, 50, "(" + str(mtn) + "/" + str(liness) + ") [-] " + lp)
        elif d == 404:
            print_rgb(50, 255, 50, "(" + str(mtn) + "/" + str(liness) + ") [+] " + lp)

