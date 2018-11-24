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


