from flask import Flask, render_template, request
from most_played_by_beatmap_id import most_played

app = Flask(__name__)


@app.route('/', methods=['GET','POST'])
def index():
    answer = None
    if request.method == 'POST':
        username = request.form['username']
        username = str(username)
        mapid = request.form['usermap']
        mapid = int(mapid)
        answer = most_played(username_user=username,beatmap_id=mapid)
        

        
    return render_template('index.html',answer=answer)

if __name__ == '__main__':
    app.run()