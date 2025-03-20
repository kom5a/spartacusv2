#!/bin/bash
echo "🚀 Déploiement sur Google Cloud en cours..."
gcloud config set project KOM5A_PROJECT_ID
gcloud app deploy --quiet
echo "✅ Déploiement terminé !"
