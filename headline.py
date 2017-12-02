from flask import Flask
myapp=Flask(__name__)
@myapp.route("/headlines")
def get_news():
    return "no news is good news"
if __name__=='__main__':
    myapp.run(port=80,debug=True)
