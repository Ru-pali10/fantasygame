import sqlite3
db=sqlite3.connect('players.db')
curplay=db.cursor()
sql="SELECT * FROM match JOIN stats ON match.player=stats.player;"
result=curplay.execute(sql)
for record in result:
    print(record)

