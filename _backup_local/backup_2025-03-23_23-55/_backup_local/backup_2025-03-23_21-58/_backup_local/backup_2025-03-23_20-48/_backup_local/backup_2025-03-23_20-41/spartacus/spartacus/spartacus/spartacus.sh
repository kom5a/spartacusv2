#!/bin/bash
echo "🔁 Activation de Spartacus pour KOM5A..."
echo "📊 Lancement du monitoring..."
python3 monitor.py
echo "📘 Lancement du mode apprentissage..."
python3 learn_auto.py
echo "✅ Spartacus opérationnel et en mode Ultra Turbo."
