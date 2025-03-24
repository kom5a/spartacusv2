import sys

command = sys.argv[1].lower()

if "lancer les modules" in command:
    print("bash ~/kom5a/spartacus/launch_modules.sh")

elif "backup" in command:
    print("bash ~/kom5a/spartacus/modules/github_backup.sh")

elif "vérifier supabase" in command or "connection" in command:
    print("bash ~/kom5a/spartacus/modules/connection_check.sh")

else:
    print("echo '❌ Commande non reconnue. Réessaie.'")

