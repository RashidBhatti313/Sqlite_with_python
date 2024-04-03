from Cs50_SQL import SQL

db = SQL("sqlite:///favorites.db")

favorite = input("Favorite: ")

rows = db.execute("SELECT * FROM favorite WHERE problem = 'MARIO'")

row = rows[0]
print(row["n"])
# for row in rows:
#     print(row["Timestamp"])

db = SQL("sqlite:///favorites.db")

favorite = input("Favorite: ")

rows = db.execute("SELECT * FROM favorite WHERE problem = ? OR %s", favorite)

print(row[0]["n"])
