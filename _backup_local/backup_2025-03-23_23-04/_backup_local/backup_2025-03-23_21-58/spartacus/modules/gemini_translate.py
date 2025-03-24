#!/usr/bin/env python3
import sys

# 🧠 Dictionnaire de mots-clés mappés à des actions
INTENTIONS = {
    ("lancer", "modules", "tous"): "bash ~/kom5a/spartacus/launch_modules.sh",
    ("backup", "github", "sauvegarde"): "bash ~/kom5a/spartacus/modules/github_backup.sh",
    ("backup", "local", "sauvegarde"): "bash ~/kom5a/spartacus/modules/local_backup.sh",
    ("vérifie", "supabase", "check"): "bash ~/kom5a/spartacus/modules/connection_check.sh",
    ("auth", "db", "authentifie"): "bash ~/kom5a/spartacus/modules/db_module.sh",
    ("status", "état", "logs"): "cat ~/kom5a/logs/modules.log",
    ("redémarre", "restart", "reboot"): "bash ~/kom5a/spartacus.sh"
}

# 🗣️ Lecture de la commande
if len(sys.argv) < 2:
    print("echo '❌ Spartacus : Aucun texte reçu.'")
    sys.exit(1)

user_input = sys.argv[1].lower()
command = None

# 🔍 Match intelligent basé sur présence de mots-clés
for keywords, action in INTENTIONS.items():
    if all(word in user_input for word in keywords):
        command = action
        break

# 🎯 Résultat
print(command if command else "echo '❌ Spartacus : Désolé, je ne comprends pas encore cette commande.'")

