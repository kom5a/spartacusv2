from supabase import create_client
import os

# Configuration projet
CONFIG = {
    "project": "KOM5A",
    "mode": "ultra_turbo",
    "learning_enabled": True,
    "monitoring_enabled": True,
    "logs_path": "./logs/",
    "errors_path": "./errors/"
}

# Clé Gemini
GEMINI_API_KEY = "AIzaSyDdk_310_N31ISRJHTqkVkP7w1LA6aTFZg"

# Lecture config Supabase depuis fichier JSON
import json

config_path = "/home/ahmedabdelli141106/kom5a/config/config_supabase.json"

if os.path.exists(config_path):
    with open(config_path, "r") as f:
        supa_conf = json.load(f)
        SUPABASE_URL = supa_conf["SUPABASE_URL"]
        SUPABASE_KEY = supa_conf["SUPABASE_KEY"]
        supabase_client = create_client(SUPABASE_URL, SUPABASE_KEY)
else:
    supabase_client = None
    print("❌ Fichier de configuration Supabase introuvable.")

