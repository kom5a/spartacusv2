#!/bin/bash

### === INIT TITAN MODE === ###
LOG_FILE="$HOME/kom5a/spartacus/spartacus.log"
ERROR_LOG="$HOME/kom5a/spartacus/spartacus-error.log"
PROJECT_DIR="$HOME/kom5a"
SPARTACUS_NAME="SPARTACUS VM"
TIMESTAMP=$(date +'%Y-%m-%d %H:%M:%S')

# === IMPORTATION DE LA CLE GEMINI ===
source "$PROJECT_DIR/spartacus/config_ia.sh"

# === CONFIGURATION PYTHON DE GEMINI ===
echo "⚙️ Configuration de Gemini..."
python3 - <<EOF
import google.generativeai as genai
from config_ia import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-pro")
response = model.generate_content("Spartacus, es-tu prêt ?")
print("🤖 Réponse Gemini : ", response.text)
EOF

# === LOGGING SIMPLE ===
log() {
    echo "$TIMESTAMP - $1" | tee -a "$LOG_FILE"
}
error_log() {
    echo "$TIMESTAMP - ERREUR : $1" | tee -a "$ERROR_LOG"
}

# === MONITORING DE BASE ===
monitor_project() {
    log "🔎 Monitoring des fichiers critiques de KOM5A..."
    FILES=("index.html" "style.css" "script.js" "pages" "components")
    for file in "${FILES[@]}"; do
        if [ -e "$PROJECT_DIR/$file" ]; then
            log "✅ Présent : $file"
        else
            error_log "❌ Fichier ou dossier manquant : $file"
        fi
    done
}

# === CONNECTION À SUPABASE ===
connect_supabase() {
    if [ -f "$PROJECT_DIR/config/supabase_config.json" ]; then
        log "🔗 Fichier de config Supabase trouvé."
    else
        error_log "❌ Supabase config manquant !"
    fi
}

# === DÉCLENCHEMENT FINAL ===
lancer_spartacus() {
    log "🚀 Lancement de SPARTACUS..."
    monitor_project
    connect_supabase
    log "🧠 SPARTACUS EST EN ROUTE, CHEF !"
}

# === EXECUTION ===
clear
echo "💥 BIENVENUE DANS LE CENTRE DE COMMANDE DE SPARTACUS 💥"
lancer_spartacus
