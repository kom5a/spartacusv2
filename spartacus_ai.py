import google.generativeai as genai
import time
import json
import os

# Configuration de l'API Gemini
GEMINI_API_KEY = "AIzaSyBMDLDJo8tUF9qJ6NQLY8wGQQXRkEtgFHo"  # Mets ta clé API ici
genai.configure(api_key=GEMINI_API_KEY)

# Modèle Gemini à utiliser
model = genai.GenerativeModel("gemini-1.5-pro")

# Fichier pour sauvegarder l'apprentissage
DATA_FILE = "/home/dministrateurspartaucs/kom5a/spartacus_memory.json"

# Vérifier si le fichier de mémoire existe, sinon le créer
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as f:
        json.dump({"connaissances": []}, f)

# Charger la mémoire existante
def load_memory():
    with open(DATA_FILE, "r") as f:
        return json.load(f)

# Sauvegarder la mémoire mise à jour
def save_memory(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

# Apprentissage automatique
def apprendre():
    memory = load_memory()
    
    sujets = [
        "Comment optimiser un serveur Linux pour de hautes performances ?",
        "Comment sécuriser une API avec Google Cloud ?",
        "Quelles sont les dernières tendances en IA appliquée au business ?",
        "Quelles sont les meilleures stratégies de croissance pour une startup tech ?",
        "Comment automatiser des tâches avec Python et Bash ?"
    ]
    
    for sujet in sujets:
        print(f"🔍 Spartacus apprend sur : {sujet}")
        try:
            response = model.generate_content(sujet)
            memory["connaissances"].append({"sujet": sujet, "réponse": response.text})
            save_memory(memory)
            print("✅ Apprentissage sauvegardé !")
        except Exception as e:
            print(f"❌ Erreur : {e}")
        
        time.sleep(2)  # Petite pause entre les requêtes pour éviter la surcharge

# Boucle infinie pour l'apprentissage continu
while True:
    apprendre()
    print("⏳ Pause avant le prochain cycle d'apprentissage...")
    time.sleep(3600)  # Spartacus apprend toutes les heures
