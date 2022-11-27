from functions import get_word, display, play

print("So'z topish o'yini o'ynaymizmi? Ha(1)/ Yo'q(0)")
reply = int(input(">>>"))

if reply:
    play()
else: 
    print("Afsus, keyingi safar o'ynaymiz")

