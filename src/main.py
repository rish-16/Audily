import easyocr
import gtts
from playsound import playsound

# reader = easyocr.Reader(['en'])
# result = reader.readtext("../assets/book2.jpg", detail=0)
# 
# full_text = " ".join(result)
# print (full_text)

tts = gtts.gTTS("""This module is much faster with a GPU.
THE JUNGLE BOOK 102 When the potter's donkey slipped in the man. clay-pit, Mowgli haul
ed it out by the tail, and helped to stack the pots for their journey to the market at
 Khanhiwara. That was very shock- ing, a low caste too, for the is and potter man, his
 donkey is worse. When the priest scolded him, Mowgli threatened to put him the don- o
n key, too, and told Messua's husband the priest that Mowgli had better be set to work
 as soon as possible; and the village head-man told Mow gli that he would out with the
 buf- have to go day, they grazed. and herd them while faloes next more pleased No Mow
gli; than and one was been appointed that night, because had he a village, servant of 
the as it were, he went off to evening circle that met every masonry a on a platform u
nder a great fg tree. It was the vil- lage club, and the head-man and the watchman and
 the barber (who knew all the gossip of the village village), and old Buldeo, the hunt
er, who a Tower musket, had and The smoked. met monkeys sat and talked in the upper br
anches, and there was a hole under the platform where a cobra lived, and he had his li
ttle platter of milk every night because he was sacred; and the old tree and talked, a
nd pulled sat around the men at the big huqas (the water-pipes) till far into the""")
tts.save("book2.mp3")
playsound("book2.mp3")