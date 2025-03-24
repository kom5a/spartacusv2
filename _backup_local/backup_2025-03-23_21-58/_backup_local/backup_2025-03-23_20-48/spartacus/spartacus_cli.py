import json
from config_ia import supabase_client

def afficher_utilisateurs():
    users = supabase_client.table("users").select("*").execute()
    for u in users.data:
        print(f"👤 {u['username']} | ID: {u['id']} | Email: {u.get('email', 'N/A')}")

def afficher_abonnements():
    subs = supabase_client.table("subscriptions").select("*").execute()
    for s in subs.data:
        print(f"💳 Plan: {s['plan']} | Utilisateur: {s['user_id']} | Statut: {s['status']}")

def menu_principal():
    while True:
        print("\n🔥 TERMINAL DE COMMANDE - SPARTACUS 🔥")
        print("1. Afficher les utilisateurs")
        print("2. Afficher les abonnements")
        print("3. Quitter")

        choix = input("🧠 Que veux-tu faire ? : ")

        if choix == "1":
            afficher_utilisateurs()
        elif choix == "2":
            afficher_abonnements()
        elif choix == "3":
            print("⛔ Fin de session Spartacus.")
            break
        else:
            print("❌ Option invalide. Réessaie.")

if __name__ == "__main__":
    menu_principal()
