import json
import requests
import psycopg2

# Chemin vers la configuration Supabase
with open('/home/ahmedabdelli141106/kom5a/config/supabase_config.json') as f:
    config = json.load(f)

# Connexion à la base Supabase
conn = psycopg2.connect(
    host=config['host'],
    port=config['port'],
    user=config['user'],
    password=config['password'],
    dbname=config['database']
)

# Récupération du fichier SQL depuis GitHub
sql_url = "https://raw.githubusercontent.com/kom5a/spartacusv2/main/supabase/functions/init_db.sql"
print(f"📦 Téléchargement de : {sql_url}")
sql = requests.get(sql_url).text

# Exécution SQL
try:
    with conn.cursor() as cur:
        cur.execute(sql)
        conn.commit()
        print("✅ Tables Supabase créées avec succès via GitHub.")
except Exception as e:
    print("❌ Erreur pendant l’exécution SQL :", e)
finally:
    conn.close()

