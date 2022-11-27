#from uzwords import words
import random

words = ['salom', 'assalom', 'mukammal', 'tabiiy']
def get_word():
    word = random.choice(words)
    while "-" in word or " " in word:
        word = random.choice(words)
    return word.upper()

def display(word, input_letters):
    result = ""
    for character in word:
        if character in input_letters:
            result += character
        else:
            result += "_"
    return result

def play():
    word = get_word()
    word_letters = set(word)
    input_letters = []
    count = 0

    print(f"Men {len(word)} harflik so'z o'yladim topa olasizmi? ")

    while len(word_letters) > 0:
        count += 1
        print(display(word, input_letters))
        if len(input_letters) > 0:
            print(f"Kiritilgan harflar: {input_letters}")

        letter = input("\nHarf kiriting: ").upper()
        if letter in input_letters:
            print("Bu harfni siz avval kiritgansiz. Boshqa harf kiriting")
            #print(display(word, input_letters))
            continue
        elif letter in word:
            word_letters.remove(letter)
            input_letters.append(letter)
            print(f"{letter} harfi to'g'ri")
        else:
            print(f"{letter} harfi mavjud emas. Boshqa harf kiriting:")
    print(f"Tabriklayman siz {word.lower().title()} so'zini topdingiz.")
    print(f"Kiritilgan harflar: {input_letters}")
    print(f"Urinishlar soni: {count}")
        



