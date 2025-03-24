#!/bin/bash

echo "🔵 [KOM5A] Initialisation complète en cours..."

# 1. Lancer l’IA de Spartacus
bash ~/kom5a/spartacus/spartacus.sh

# 2. Lancer les modules (UI, DB, AUTH...)
bash ~/kom5a/spartacus/launch_modules.sh

# 3. Sauvegarde GitHub automatique
bash ~/kom5a/spartacus/modules/github_backup.sh

# 4. Affichage final
echo "✅ KOM5A est lancé avec succès. Spartacus est pleinement opérationnel."
