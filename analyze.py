from flask import Flask, request, render_template,redirect, url_for,session
from sklearn.linear_model import LinearRegression
from flask_mysqldb import MySQL
import numpy as np

class Analyze:
	def __init__(self, app):
		self.app = app
		self.app.config['MYSQL_USER'] = 'root'
		self.app.config['MYSQL_PASSWORD'] = '!@)59380'
		self.app.config['MYSQL_DB'] = 'footballStats'
		self.app.config['MYSQL_HOST'] = 'localhost'
		self.mysql = MySQL()
		self.mysql = MySQL(app)



	def pick_best_team(self, excluded_player_ids):
		pos_dict = {}
		mycursor = self.mysql.connection.cursor()
		sql = "SELECT players.id, pos, firstname, lastname, predicted_score FROM players JOIN player_year_stats ON players.id = player_year_stats.player_id group by pos,players.id"
		mycursor.execute(sql)
		myresult = mycursor.fetchall()

		for result in myresult:
			if result[1] in pos_dict:
				pos_dict[result[1]].append(list(result))
			else:
				pos_dict[result[1]] = [list(result)]
			#print(result)
		#print(val)
		for key, value in pos_dict.items():
			pos_dict[key].sort(key=lambda x:-x[4])
			
		return pos_dict

	def get_sorted_players(self, sort_by = "pos"):
		mycursor = self.mysql.connection.cursor()
		sql = "SELECT id,firstname,lastname FROM players"
		#print(val)
		mycursor.execute(sql)
		myresult = mycursor.fetchall()
		final_result = []

		for result in myresult:
			final_result.append(result)

		return final_result

	def get_player_details(self, player_id):
		mycursor = self.mysql.connection.cursor()
		sql = "SELECT player_id, pos, team, year, games_played, rush, rush_yards, rush_td, target, catch, catch_yards, catch_td, pass, complete, pass_yards, pass_td, interceptions, fumbles,points FROM player_year_stats WHERE player_id = %s"
		print(player_id)
		mycursor.execute(sql, [int(player_id)])
		myresult = mycursor.fetchall()
		final_result = []

		for result in myresult:
			result = list(result)
			result[18] = float(result[18])
			final_result.append(result)


		mycursor = self.mysql.connection.cursor()
		sql = "SELECT id,firstname,lastname, predicted_score FROM players WHERE id = %s"
		#print(val)
		mycursor.execute(sql, [int(player_id)])
		myresult = mycursor.fetchone()
		player_detail = myresult
		player_detail = list(player_detail)
		print(player_detail)
		player_detail[3] = float(player_detail[3])
		return player_detail,final_result

	def update_all_player_stats(self,year):

		player_dict = {}

		mycursor = self.mysql.connection.cursor()
		sql = "SELECT player_id, year, points FROM player_year_stats"
		
		#print(val)
		mycursor.execute(sql)
		myresult = mycursor.fetchall()
		final_result = []
		for result in myresult:
			if result[0] in player_dict:
				player_dict[result[0]].append(list(result))
			else:
				player_dict[result[0]] = [result]
		for key, value in player_dict.items():
			scores = []
			years = []
			for year_stat in value:
				years.append([year_stat[1]])
				scores.append([float(year_stat[2])])
			#print(scores)
			#print(years)
			reg = LinearRegression().fit(years, scores)
			prediction = reg.predict(np.array([year]).reshape(-1, 1))
			print(prediction)

			mycursor = self.mysql.connection.cursor()
			sql = "UPDATE players SET predicted_score = %s WHERE id = %s"
			mycursor.execute(sql,[float(prediction[0][0]), key])

		self.mysql.connection.commit()

		return final_result