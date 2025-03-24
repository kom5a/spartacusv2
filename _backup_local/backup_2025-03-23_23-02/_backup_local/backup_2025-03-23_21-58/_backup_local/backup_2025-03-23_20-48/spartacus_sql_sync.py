# spartacus_sql_sync.py

import requests, psycopg2, json

# Charger config Supabase
with open('config/supabase_config.json') as f:
    config = json.load(f)

# Connexion à Supabase
conn = psycopg2.connect(
    host=config["host"],
    port=config["port"],
    user=config["user"],
    password=config["password"],
    dbname=config["database"]
)

# Récupérer le fichier SQL depuis GitHub
url_sql = "https://raw.githubusercontent.com/kom5a/spartacusv2/main/supabase/functions/init_db.sql"
r = requests.get(url_sql)
sql_code = r.text

# Exécution SQL
with conn.cursor() as cur:
    cur.execute(sql_code)
    conn.commit()

print("✅ Spartacus : SQL synchronisé et exécuté avec succès.")
