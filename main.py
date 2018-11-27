from flask import Flask, request, render_template,redirect, url_for,session
from flask_mysqldb import MySQL
from datetime import datetime
import analyze

app = Flask(__name__)
a1 = analyze.Analyze(app)

@app.route('/')
def index():
    return render_template('index.html',data = '')

@app.route("/homePage")
def homePage():
    return render_template('homePage.html',data = '')

@app.route("/playerPool")
def playerPool():
	players = a1.get_sorted_players()
	return render_template('playerPool.html',data = players)

@app.route("/detail/<player_id>")
def detail(player_id):
	player, player_record = a1.get_player_details(player_id)
	return render_template('detail.html',data = {"player":player,"player_record":player_record})

@app.route("/admin")
def admin():
	return render_template('admin.html',data = str(datetime.today().year))

@app.route("/updatePredStats", methods=['GET'])
def updatePredStats():
	a1.update_all_player_stats(int(request.args.get('year')))
	return render_template('admin.html', data = str(datetime.today().year))

@app.route("/newTeam")
def newTeam():
	bestTeam = a1.pick_best_team([])
	return render_template('newTeam.html', data = str(datetime.today().year))

if __name__ == '__main__':
    app.run(debug=True)
