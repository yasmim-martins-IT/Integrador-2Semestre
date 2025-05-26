import sqlite3
import pandas as pd

conn = sqlite3.connect("db.sqlite3")

df = pd.read_sql_query("SELECT * FROM app_historico", conn)

df.to_excel("planilhaImportada.xlsx", index=False)  

df.to_csv("PlanilhaImportada.csv", index=False)


conn.close()

