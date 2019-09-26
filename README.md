# ArticleScraping

**NOTE: This project is developed for educational purpose only and does not try to imitate any legit application.**

This project scrapes the content of any medium article and also allows the user to get an audio version of that article.
User has to provide the link of the medium article in the user interface and submit it. In case user wants to generate an *mp3* file 
of that article, they should run the `mediumScraping.py` file, changing the url link inside the script. 

## How to run
Open terminal/cmd and run the following commands :

```git
git clone https://github.com/globefire/ArticleScraping.git
cd ArticleScraping
pip install -r requirements.txt
```

To run the python script run this command ([Change the link inside the file](https://github.com/globefire/ArticleScraping/blob/76ddf728769d562b8fbe2e7eadd02e5495bd20c5/mediumScraping.py#L6))

```git
python mediumScraping.py
```

To launch the web interface run the following commands

```git
cd mediumscraper
python manage.py runserver
```

UI:

