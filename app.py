from flask import Flask, render_template, request
from most_played_by_beatmap_id import most_played

app = Flask(__name__)


@app.route('/', methods=['GET','POST'])
def index():
    answer = None
    if request.method == 'POST':
        username = request.form['username']
        mapid = request.form['usermap']
        if len(username) > 1 and len(mapid) > 1:
            username = str(username)
            mapid = int(mapid)
            answer = most_played(username_user=username,beatmap_id=mapid)
        else:
            answer = 'Error either Username or Beatmap ID is invalid!'

    
    return render_template('index.html',answer=answer)
        

        


if __name__ == '__main__':
    app.run(debug=True)