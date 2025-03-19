#!/bin/bash

### === CONFIGURATION GLOBALE === ###
LOG_FILE="$HOME/spartacus-log.txt"
ERROR_LOG="$HOME/spartacus-error.log"
SPARTACUS_DIR="$HOME/kom5a/"
GITHUB_REPO="https://github.com/Ahmed022025/kom5a"
GCLOUD_PROJECT_ID="kom5a-waooo-2025"
INSTANCE_NAME="kom5a-instance"
ZONE="europe-west1-b"
DOMAIN_NAME="kom5a.org"

log() {
    echo "$(date +'%Y-%m-%d %H:%M:%S') - $1" | tee -a "$LOG_FILE"
}

error_log() {
    echo "$(date +'%Y-%m-%d %H:%M:%S') - ERROR: $1" | tee -a "$ERROR_LOG"
}

check_command() {
    if [ $? -ne 0 ]; then
        error_log "Erreur lors de l'exécution : $1"
        exit 1
    fi
}

install_dependencies() {
    log "🛠 Installation des dépendances..."
    sudo apt update && sudo apt install -y git curl docker docker-compose nginx python3-pip mailutils htop
    check_command "Installation des dépendances"
}

configure_gcloud() {
    log "🔧 Configuration de Google Cloud..."
    gcloud config set project "$GCLOUD_PROJECT_ID"
    check_command "Configuration GCloud"
    gcloud services enable compute.googleapis.com cloudbuild.googleapis.com
    check_command "Activation des services"
}

deploy_instance() {
    log "🚀 Déploiement de l'instance GCloud..."
    INSTANCE_EXIST=$(gcloud compute instances list --filter="name=$INSTANCE_NAME" --format="value(name)")
    if [ -z "$INSTANCE_EXIST" ]; then
        gcloud compute instances create "$INSTANCE_NAME" --zone="$ZONE" --machine-type=e2-medium --image-family=debian-11 --image-project=debian-cloud --boot-disk-size=20GB
        check_command "Création de l'instance"
    else
        log "⚡ Instance déjà existante : $INSTANCE_NAME"
    fi
}

configure_gemini() {
    log "🤖 Configuration de Gemini AI..."
    export GEMINI_API_KEY="AIzaSyBMDLDJo8tUF9qJ6NQLY8wGQQXRkEtgFHo"
    echo "export GEMINI_API_KEY=\"$GEMINI_API_KEY\"" >> ~/.bashrc
    source ~/.bashrc
    log "✅ Gemini API Configuré."
}

test_gemini() {
    log "🧪 Test de connexion avec Gemini..."
    python3 - <<EOF
import google.generativeai as genai
import os
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-pro")
response = model.generate_content("Test de connexion avec Spartacus")
print(response.text)
EOF
}

configure_nginx() {
    log "🌍 Configuration de Nginx..."
    sudo tee /etc/nginx/sites-available/default > /dev/null <<EOL
server {
    listen 80;
    server_name $DOMAIN_NAME;
    root /var/www/html;
    index index.html;
    location / {
        try_files \$uri \$uri/ =404;
    }
}
EOL
    sudo systemctl restart nginx
    check_command "Redémarrage de Nginx"
}

backup_project() {
    log "💾 Sauvegarde du projet sur Google Cloud Storage..."
    gcloud storage cp -r /var/www/html gs://kom5a-backups/
    check_command "Sauvegarde sur Cloud Storage"
}

auto_update() {
    log "🔄 Mise à jour automatique..."
    cd "$SPARTACUS_DIR" || exit
    git pull origin main
    check_command "Mise à jour du projet"
    sudo systemctl restart nginx
    check_command "Redémarrage Nginx"
}

setup_cron() {
    log "📅 Configuration des tâches planifiées..."
    (crontab -l 2>/dev/null; echo "0 * * * * $SPARTACUS_DIR/spartacus.sh backup_project") | crontab -
    check_command "Tâches cron configurées"
}

### === MENU INTERACTIF === ###
while true; do
    clear
    echo "🔹 SPARTACUS - Gestion et Automatisation KOM5A 🔹"
    echo "1) Installer les dépendances"
    echo "2) Configurer Google Cloud"
    echo "3) Déployer sur Google Cloud"
    echo "4) Configurer Gemini AI"
    echo "5) Tester connexion avec Gemini"
    echo "6) Configurer Nginx"
    echo "7) Sauvegarde Cloud"
    echo "8) Mise à jour automatique"
    echo "9) Configuration Cron"
    echo "10) Quitter"
    
    if [ -t 0 ]; then
        read -p "Votre choix : " CHOIX
    else
        CHOIX=10  # Quitter si non interactif
    fi

    case $CHOIX in
        1) install_dependencies ;;
        2) configure_gcloud ;;
        3) deploy_instance ;;
        4) configure_gemini ;;
        5) test_gemini ;;
        6) configure_nginx ;;
        7) backup_project ;;
        8) auto_update ;;
        9) setup_cron ;;
        10) exit 0 ;;
        *) echo "⛔ Choix invalide !" ;;
    esac
    sleep 2
done

