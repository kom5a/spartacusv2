#!/usr/bin/env python3
import sys
import os

# 🔐 Clé API Gemini (utilisée plus tard)
with open(os.path.expanduser("~/kom5a/spartacus/config/gemini_api_key.txt")) as f:
    api_key = f.read().strip()

# 🧠 Commande utilisateur reçue
try:
    user_message = sys.argv[1].strip().lower()
except IndexError:
    print("echo '❌ Aucun texte reçu par Gemini.'")
    sys.exit(1)

# 📚 Dictionnaire intelligent
translations = {
    "lance tous les modules": "bash ~/kom5a/spartacus/launch_modules.sh",
    "sauvegarde github": "bash ~/kom5a/spartacus/modules/github_backup.sh",
    "sauvegarde locale": "bash ~/kom5a/spartacus/modules/local_backup.sh",
    "vérifie supabase": "bash ~/kom5a/spartacus/modules/connection_check.sh",
    "authentifie db": "bash ~/kom5a/spartacus/modules/db_module.sh",
    "status": "cat ~/kom5a/logs/modules.log",
    "redémarre spartacus": "bash ~/kom5a/spartacus/shutdown.sh"
}

# 🔍 Analyse de la commande
command = None
for key in translations:
    if key in user_message:
        command = translations[key]
        break

# 🧾 Résultat final
if command:
    print(command)
else:
    print(f"echo '❌ Spartacus : Désolé, je ne comprends pas encore cette commande.'")
