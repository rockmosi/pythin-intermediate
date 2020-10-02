# since 2020,10.02
# 어제의 점프 투 플라스크와 오늘의 점프 투 플라스크는 다르다!!! - 박응용
# source code site: https://github.com/pahkey/flaskbook
## check source by chapter: https://wikidocs.net/81088

# Flask made by Armin Ronacher on 2004
# Thanks Armin!!

from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


if __name__ == "__main__":
    app.run()

