import flask
from . import icsss
from flask import request

app = flask.Flask(__name__)

@app.route('/')
def main_page():
    return flask.render_template('web.html')

@app.route('/faq')
def faq_page():
    return flask.render_template('howToDinfID.html')

@app.route('/get_ics', methods = ['GET'])
def get_ics():
    data = request.args
    try:
        return flask.send_file(icsss.make_calendar(**data))
    except:
        return "Провертье правильность введённых данных"

