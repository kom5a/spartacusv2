#!/bin/bash

echo "🔍 Vérification de la connexion GITHUB et SUPABASE..."

# Vérifie GitHub
if git ls-remote https://github.com/kom5a/spartacusv2.git &> /dev/null; then
  echo "✅ Connexion GITHUB : OK"
else
  echo "❌ Connexion GITHUB : Échec"
fi

# Vérifie Supabase
if ping -c 1 db.nkzizwmwgshrkjajcvvr.supabase.co &> /dev/null; then
  echo "✅ Connexion SUPABASE : OK"
else
  echo "❌ Connexion SUPABASE : Échec"
fi

echo "📦 Vérification terminée."
