from flask import Flask, request, render_template,redirect, url_for,session

from flask_mysqldb import MySQL
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
		return []

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
		sql = "SELECT player_id, pos, team, year, games_played, rush, rush_yards, rush_td, target, catch, catch_yards, catch_td, pass, complete, pass_yards, pass_td, interceptions, fumbles FROM player_year_stats WHERE player_id = %s"
		#print(val)
		mycursor.execute(sql, [int(player_id)])
		myresult = mycursor.fetchall()
		final_result = []

		for result in myresult:
			final_result.append(result)


		mycursor = self.mysql.connection.cursor()
		sql = "SELECT id,firstname,lastname FROM players"
		#print(val)
		mycursor.execute(sql)
		myresult = mycursor.fetchone()
		player_detail = myresult


		return player_detail,final_result
