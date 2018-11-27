import csv
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="!@)59380",
  database="footballStats"
)
def load_data(filename):
	with open(filename, newline='') as csvfile:
		header = {}
		spamreader = csv.reader(csvfile, delimiter=',')
		for i,row in enumerate(spamreader):
			# create header dictionary with col num as values
			for y,col in enumerate(row):
				if i == 0:
					header[col] = y
			
			if i == 0:
				print(row)
				continue

			# check if player exists
			mycursor = mydb.cursor(buffered=True)
			name = row[header['Name']]
			sql = "SELECT id FROM players WHERE firstname = %s AND lastname = %s"
			val = name.replace(',','').rsplit(' ',1)

			#print(val)
			if ',' in name:
				mycursor.execute(sql, [val[1], val[0]])
			else:
				mycursor.execute(sql, val)

			# myresult = (player_id,)
			myresult = mycursor.fetchone()
			player_id = -1
			if myresult != None:
				player_id = myresult[0]
			# if the player doesn't exist in database, add player
			if myresult == None or len(myresult) == 0:
				mycursor = mydb.cursor()

				sql = "INSERT INTO players (firstname, lastname) VALUES (%s, %s)"
				
				if ',' in name:
					mycursor.execute(sql, [val[1], val[0]])
				else:
					mycursor.execute(sql, val)


				mydb.commit()
				player_id = mycursor.lastrowid

			# check if player game record already exists

			mycursor = mydb.cursor(buffered=True)
			sql = "SELECT id FROM player_year_stats WHERE player_id = %s AND year = %s"
			val = [str(player_id), row[header["Year"]]]

			#print(val)
			mycursor.execute(sql, val)

			# myresult = (player_id,)
			myresult = mycursor.fetchone()

			if myresult == None:

				mycursor = mydb.cursor(buffered=True)
				print(row)
				row_with_zeros = []
				for g, col in enumerate(row):
					if col == '':
						row_with_zeros.append(0)
					elif g > 2:
						row_with_zeros.append(int(col))
					else:
						row_with_zeros.append(col)
				print(row_with_zeros)
				points = 0
				if row[header["Pass Yards"]] != "":
					points += float(int(row[header["Pass Yards"]])/25)
				if row[header["Pass TD"]] != "":
					points += float(int(row[header["Pass TD"]])*4)
				if row[header["Int"]] != "":
					points -= float(int(row[header["Int"]])*2)
				if row[header["Rush Yards"]] != "":
					points += float(int(row[header["Rush Yards"]])/10)
				if row[header["Rush TD"]] != "":
					points += float(int(row[header["Rush TD"]])*6)
				if row[header["Catch"]] != "":
					points += float(int(row[header["Catch"]]))
				if row[header["Catch yards"]] != "":
					points += float(int(row[header["Catch yards"]])/10)
				if row[header["Catch TD"]] != "":
					points += float(int(row[header["Catch TD"]])*6)
				if row[header["Fum"]] != "":
					points -= float(int(row[header["Fum"]])*2)
				points /= float(int(row[header["Games Plyd"]]))
				print(points)
				sql = "INSERT INTO player_year_stats (player_id, pos, team, year, games_played, rush, rush_yards, rush_td, target, catch, catch_yards, catch_td, pass, complete, pass_yards, pass_td, interceptions, fumbles, points) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, "+str(points)+") "
				mycursor.execute(sql, [player_id]+row_with_zeros[1:])


				mydb.commit()

load_data('data/dlstats_2015_2017.csv')
load_data('data/dlstats_2014_2016.csv')
load_data('data/dlstats_2013_2015.csv')
load_data('data/dlstats_2012_2014.csv')
load_data('data/dlstats_2011_2013.csv')
load_data('data/dlstats_2010_2012.csv')
load_data('data/dlstats_2009_2011.csv')
load_data('data/dlstats_2008_2010.csv')
load_data('data/dlstats_2007_2009.csv')
load_data('data/dlstats_2006_2008.csv')
load_data('data/dlstats_2005_2007.csv')
load_data('data/dlstats_2004_2006.csv')
load_data('data/dlstats_2003_2005.csv')
