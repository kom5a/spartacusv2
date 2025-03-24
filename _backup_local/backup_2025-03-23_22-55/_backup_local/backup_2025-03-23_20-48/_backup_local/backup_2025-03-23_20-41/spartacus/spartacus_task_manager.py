from config_ia import supabase_client

def verifier_nouveaux_utilisateurs():
    users = supabase_client.table('users').select("*").execute()
    for user in users.data:
        print(f"👤 Utilisateur détecté : {user['username']}")

def verifier_nouveaux_paiements():
    subs = supabase_client.table('subscriptions').select("*").execute()
    for sub in subs.data:
        print(f"💳 Abonnement actif : {sub['plan']} pour {sub['user_id']}")

# Appel automatique en boucle
if __name__ == "__main__":
    verifier_nouveaux_utilisateurs()
    verifier_nouveaux_paiements()
