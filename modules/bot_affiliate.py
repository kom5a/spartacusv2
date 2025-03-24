def enregistrer_affiliation(user_id, lien):
    with open("affiliates.json", "a") as f:
        f.write(f"{user_id} → {lien}\n")

print("🤝 Module d'affiliation actif. Chaque utilisateur est un ambassadeur.")
