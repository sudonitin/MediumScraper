import requests as req
import bs4
import warnings
warnings.simplefilter('ignore') 

res = req.get('https://web.whatsapp.com/') #your link here
soup = bs4.BeautifulSoup(res.text, 'lxml')
content = ''

if soup.find('article'):
    for i in soup.select('article'):
        content += i.getText()
        #print(i.getText())
    print(content)
else:
    print("This is not a medium article link..!")

###Audio file generating###
# from gtts import gTTS
# tts = gTTS(text = content, lang = 'en')
# tts.save("read.mp3")

'''
use speechsynthesis of js to implement voice in web:
    https://devhints.io/js-speech,
    https://responsivevoice.org/,
    https://developer.mozilla.org/en-US/docs/Web/API/SpeechSynthesis
this code should be called on button click
Stop the web synthesis when new link is added****
'''

'''
CSS improvising links
https://stackoverflow.com/questions/10870564/how-to-exclude-a-class-with-all-children-in-style-definition
https://stackoverflow.com/questions/17599035/django-how-can-i-call-a-view-function-from-template/19761466#19761466
https://learn.shayhowe.com/advanced-html-css/complex-selectors/
https://stackoverflow.com/questions/15603957/css-select-all-child-elements-except-first-two-and-last-two
'''
