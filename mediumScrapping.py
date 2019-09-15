import requests as req
import bs4
import warnings
warnings.simplefilter('ignore') 

res = req.get('https://forge.medium.com/why-trying-harder-can-sometimes-backfire-4185eae26f45')
soup = bs4.BeautifulSoup(res.text, 'lxml')
content = ''
for i in soup.select('article'):
    content += i.getText()
    #print(i.getText())
#print(content)

###Audio file generating###
from gtts import gTTS
tts = gTTS(text = content, lang = 'en')
tts.save("read.mp3")

'''
use speechsynthesis of js to implement voice in web:
    https://devhints.io/js-speech,
    https://responsivevoice.org/,
    https://developer.mozilla.org/en-US/docs/Web/API/SpeechSynthesis
this code should be called on button click
'''
