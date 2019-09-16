import requests as req
import bs4
import warnings
warnings.simplefilter('ignore') 

res = req.get('Article Link Here')
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

'''
CSS improvising links
https://stackoverflow.com/questions/10870564/how-to-exclude-a-class-with-all-children-in-style-definition
https://stackoverflow.com/questions/17599035/django-how-can-i-call-a-view-function-from-template/19761466#19761466
https://learn.shayhowe.com/advanced-html-css/complex-selectors/
https://stackoverflow.com/questions/15603957/css-select-all-child-elements-except-first-two-and-last-two
'''
