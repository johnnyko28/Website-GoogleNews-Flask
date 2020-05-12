from flask import Flask, jsonify, json
from newsapi import NewsApiClient


# EB looks for an 'application' callable by default.
application = Flask(__name__, static_folder='static')

# Init
newsapi = NewsApiClient(api_key='ac90537702d7468da86ffe236b33c0f6')

# /v2/top-headlines
top_headlines = newsapi.get_top_headlines(language='en', country='us')

# /v2/everything
all_articles = newsapi.get_everything(q='coronavirus',
                                      sources='bbc-news,the-verge',
                                      from_param='2020-03-01',
                                      to='2020-03-09',
                                      language='en',
                                      page=2)

# /v2/everything CNN
all_articles_cnn = newsapi.get_everything(language='en', sources='cnn')

# /v2/everything FOX-News
all_articles_fox_news = newsapi.get_everything(language='en', sources='fox-news')

# /v2/sources
sources = newsapi.get_sources(language='en', country='us')

@application.route('/top_headlines', methods=['GET'])
def get_top_headlines():
    return jsonify(top_headlines)

@application.route('/cnn', methods=['GET'])
def get_cnn_news():
    return jsonify(all_articles_cnn)

@application.route('/foxnews', methods=['GET'])
def get_fox_news():
    return jsonify(all_articles_fox_news)

@application.route('/sources', methods=['GET'])
def get_sources():
    return jsonify(sources)

@application.route('/everything', methods=['GET'])
def get_everything():
    return jsonify(all_articles)


@application.route('/')
def homepage():
    return application.send_static_file("index.html")


# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run()

