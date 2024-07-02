from gts import gTTs
import os
mytext = ''
language = 'en'
myobj = gTTS(text=mytext, lang= language, slow = false)
myobj.save("welcome.mp3")
os.system("mpg321 welcome.mp3")
