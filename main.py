from flask import Flask, request, render_template,redirect, url_for,session
from flask_mysqldb import MySQL
from datetime import datetime
import json


import analyze

app = Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
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
	games_played = 0
	positions = {}
	for record in player_record:
		positions[record[1]] = 1
		games_played+=record[4]
	return render_template('detail.html',data = {"player":player,"player_record":player_record,"positions":list(positions.keys()), "games_played":games_played})

@app.route("/admin")
def admin():
	return render_template('admin.html',data = {"year":str(datetime.today().year), "message":""})

@app.route("/updatePredStats", methods=['GET'])
def updatePredStats():
	a1.update_all_player_stats(int(request.args.get('year')))
	return render_template('admin.html', data =  {"year":str(datetime.today().year), "message":"successfully updated"})

@app.route("/playerDetail", methods=['POST'])
def playerDetail():
	print(request.form['player_id'])
	player, player_record = a1.get_player_details(int(request.form['player_id']))
	return json.dumps({'status':'OK','player':player,'player_record':player_record});

@app.route("/savePlayer", methods=['POST'])
def savePlayer():
	session[request.form['position']] = request.form['player_id']
	print(session)
	return json.dumps({'status':'OK'});

@app.route("/newTeam")
def newTeam():
	if "QB" not in session:
		session["QB"] = -1
	if "WR" not in session:
		session["WR"] = -1
	if "TE" not in session:
		session["TE"] = -1
	if "RB" not in session:
		session["RB"] = -1

	bestTeam = a1.pick_best_team([])
	keys = list(bestTeam.keys())
	keys.sort()
	bestQBs = bestTeam[keys[0]]
	bestRBs = bestTeam[keys[1]]
	bestTEs = bestTeam[keys[2]]
	bestWRs = bestTeam[keys[3]]
	#print(bestTeam)
	
	return render_template('newTeam.html', data = {"best_team":bestTeam, "teams":keys, "bestQBs":bestQBs, "bestRBs":bestRBs,"bestWRs":bestWRs,"bestTEs":bestTEs})

if __name__ == '__main__':
    app.run(debug=True)
