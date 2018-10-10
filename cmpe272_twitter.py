from flask import jsonify, render_template, request
from flask import Flask
import json
from cmpe272_twitter_api import Cmpe272_Twitter_API as twitter
import api_key as t
# Jia Ma Start
app = Flask(__name__)

@app.route('/')
@app.route('/index.html')
def index():
    return app.send_static_file('cmpe272_twitter.html')

@app.route('/timeline', methods=['POST'])
def timeline():
    screen_name = request.form.get('screenname', 'SanJoseTrails')
    tapi = twitter(t.CONSUMER_KEY, t.CONSUMER_SECRET, t.ACCESS_KEY, t.ACCESS_SECRET)
    timeline = tapi.GetUserTimeline(screen_name=screen_name)
    return jsonify([t['text'] for t in timeline])

@app.route('/poststatus', methods=['POST'])
def poststatus():
    text = request.form.get('text', '')
    status = {'status': 'error'}
    if text:
        tapi = twitter(t.CONSUMER_KEY, t.CONSUMER_SECRET, t.ACCESS_KEY, t.ACCESS_SECRET)
        if tapi.PostUpdate(status=text):
            status = {'status': 'ok'}
    return jsonify(status)
# Jia Ma End