import sys

user_command = sys.argv[1].lower()

if "backup" in user_command:
    print("bash ~/kom5a/spartacus/modules/github_backup.sh")
elif "db" in user_command:
    print("bash ~/kom5a/spartacus/modules/db_module.sh")
elif "modules" in user_command:
    print("bash ~/kom5a/spartacus/launch_modules.sh")
elif "supabase" in user_command:
    print("bash ~/kom5a/spartacus/modules/connection_check.sh")
else:
    print("echo '❌ Commande non reconnue. Réessaie.'")
