#Luis A. Gonzalez
#Module 1.3 Assignment
#10/25/26

Bottles = input("Enter the amount of bottles: ")
print(Bottles)


Lyrics1 = f"3 bottles of beer on the wall, 3 bottles of beer. Take one down and pass it around, 2 bottle (s) of beer on the wall."
Lyrics2 = f"2 bottles of beer on the wall, 2 bottles of beer. Take one down and pass it around, 1 bottle (s) of beer on the wall."
Lyrics3 = f"1 bottle of beer on the wall, 1 bottle of beer.Take one down and pass it around, 0 bottle (s) of beer on the wall."
Lyrics4 = f"Time to buy more bear"

import time
lyric_countdown = [Lyrics1, Lyrics2, Lyrics3, Lyrics4]

for word in lyric_countdown:
    print(word)
    time.sleep(1)
