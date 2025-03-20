#!/bin/bash
echo "📦 Mise à jour du dépôt GitHub..."
cd /home/$(whoami)/kom5a
git pull origin main
echo "✅ Mise à jour terminée !"
