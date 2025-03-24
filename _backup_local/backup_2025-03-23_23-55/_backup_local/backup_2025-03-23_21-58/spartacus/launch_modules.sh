#!/bin/bash

echo "🚀 [Spartacus] Lancement intelligent des modules KOM5A..."
LOG_FILE=~/kom5a/logs/modules.log
MODULES_DIR=~/kom5a/spartacus/modules

mkdir -p ~/kom5a/logs
echo "🕒 $(date) | Lancement des modules" > $LOG_FILE

for module in "$MODULES_DIR"/*.sh; do
    MODULE_NAME=$(basename "$module")
    echo "🔧 Activation de $MODULE_NAME ..."
    bash "$module"
    
    if [ $? -eq 0 ]; then
        echo "✅ $MODULE_NAME lancé avec succès." | tee -a $LOG_FILE
    else
        echo "❌ Échec de $MODULE_NAME !" | tee -a $LOG_FILE
    fi
done

echo "🎯 Tous les modules traités. Vérifie le log : $LOG_FILE"

