#!/bin/bash

echo "🧠 Bienvenue dans le cockpit de Spartacus."
echo "🎯 Tu peux maintenant lui parler directement."

while true; do
  echo ""
  read -p "🫡 Toi 👉 " user_input

  # Quitter
  if [[ "$user_input" == "exit" || "$user_input" == "quitter" ]]; then
    echo "👋 Spartacus se replie. À très vite Chef."
    break
  fi

  # Transmettre à Gemini + exécution
  echo "🧠 Spartacus pense..."
  response=$(python3 ~/kom5a/spartacus/modules/gemini_interpreter.py "$user_input")
  
  if [[ "$response" == echo* ]]; then
    eval "$response"
  else
    echo "🚀 Exécution : $response"
    eval "$response"
  fi
done
