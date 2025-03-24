#!/bin/bash

echo "🧠 Spartacus ↔️ Gemini : Activation de l’interface..."

read -p "📝 Donne ton ordre (ex: lancer backup, vérifier db) : " user_command

# Appel simulé à Gemini (via Python)
response=$(python3 ~/kom5a/spartacus/modules/gemini_interpreter.py "$user_command")

echo "🤖 Réponse de Gemini : $response"
bash -c "$response"
