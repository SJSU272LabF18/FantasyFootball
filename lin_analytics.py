import csv
import mysql.connector
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from math import sqrt

import numpy as np

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="!@)59380",
  database="footballStats"
)
def evaluate_prediction(year):
	highest_score = 0
	lowest_score = 0
	player_dict = {}
	total_mse = 0
	mycursor = mydb.cursor(buffered=True)
	sql = "SELECT player_id, year, points FROM player_year_stats"

	#print(val)
	mycursor.execute(sql)
	myresult = mycursor.fetchall()
	final_result = []
	for result in myresult:
		print(result)
		if result[0] in player_dict and result[1] != 2017:
			player_dict[result[0]]["train"].append(list(result))
		elif result[1] != 2017:
			player_dict[result[0]] = {"train":[]}
			player_dict[result[0]]["train"] = [result]
		elif result[0] in player_dict  and result[1] == 2017:
			player_dict[result[0]]["actual"] = [result]
		elif result[1] == 2017:
			player_dict[result[0]] = {"train":[],"actual":[]}
			player_dict[result[0]]["actual"] = [result]

	for key, value in player_dict.items():
		scores = []
		years = []
		prediction = 0
		if len(value["train"]) > 0:
			for year_stat in value["train"]:
				years.append([year_stat[1]])
				scores.append([float(year_stat[2])])
				if highest_score <float(year_stat[2]):
					highest_score = float(year_stat[2])
				if lowest_score >float(year_stat[2]):
					lowest_score = float(year_stat[2])
		#print(scores)
		#print(years)
			reg = LinearRegression().fit(years, scores)
			prediction = reg.predict(np.array([year]).reshape(-1, 1))
		
		if "actual" in value:
			
			#print(float(value["actual"][0][2]))
			total_mse += mean_squared_error(np.array([float(value["actual"][0][2])]).reshape(-1, 1), np.array([float(prediction)]).reshape(-1, 1))
	
	print(sqrt(total_mse/len(player_dict)))
	print(highest_score)
	print(lowest_score)


evaluate_prediction(2017)