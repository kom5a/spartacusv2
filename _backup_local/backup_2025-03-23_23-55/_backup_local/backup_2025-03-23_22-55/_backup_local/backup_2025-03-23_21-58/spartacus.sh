#!/bin/bash

echo "🔥 SPARTACUS ACTIVÉ – KOM5A AUTOMATION ⚙️"

# Ajouter le footer signature
if [[ "$1" == "--footer" ]]; then
  echo "<footer style='text-align:right; font-size:12px; margin-top:50px;'>Made by Spartacus – © KOM5A2025</footer>" >> index.html
  echo "✅ Footer ajouté à index.html"
fi

# Git Push auto
if [[ "$1" == "--push" ]]; then
  git add .
  git commit -m "🤖 Auto update by Spartacus"
  git push
  echo "✅ Pushed to GitHub automatiquement."
fi

