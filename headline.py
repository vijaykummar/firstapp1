from flask import Flask
import feedparser

myapp=Flask(__name__)

google_feed="C:\Python\feedparser-5.2.1\feedparser-5.2.1"

@myapp.route("/")
def get_news():
    feed=feedparser.parse(google_feed)
    first_article=feed('entries')[0]
    return """<html>
    <body>
     <h1> BBC HeadLines </h1>
     <b>{0} </b> <br/>
     <i>{1} </i> <br/>
     <p>{2} </p> <br/>
    </body>
    </html>""".format(first_article.get("title"),first_article.get("published"),first_article.get("summary"))



if __name__=='__main__':
    myapp.run(port=80,debug=True)


