import json
import subprocess
import os
import threading

CONFIG_FILE = "config.json"
with open(CONFIG_FILE, "r") as file:
    config = json.load(file)

LOG_FILE = "logs/orchestrator.log"
ERROR_FILE = "logs/errors.log"

def log(message):
    with open(LOG_FILE, "a") as log_file:
        log_file.write(message + "\n")
    print(message)

def log_error(message):
    with open(ERROR_FILE, "a") as error_file:
        error_file.write(message + "\n")
    print(f"❌ {message}")

def check_dependencies(script):
    for dep in script.get("dependencies", []):
        result = subprocess.run(["which", dep], capture_output=True, text=True)
        if result.returncode != 0:
            log_error(f"Dépendance manquante : {dep} (nécessaire pour {script['file']})")
            return False
    return True

def run_script(script):
    script_path = os.path.join("scripts", script["file"])
    
    if not os.path.exists(script_path):
        log_error(f"Script introuvable : {script_path}")
        return
    
    if not check_dependencies(script):
        return
    
    log(f"🚀 Exécution : {script['file']}")
    try:
        if script["file"].endswith(".py"):
            subprocess.run(["python3", script_path])
        elif script["file"].endswith(".sh"):
            subprocess.run(["bash", script_path])
        elif script["file"].endswith(".js"):
            subprocess.run(["node", script_path])
        else:
            log_error(f"Format non supporté : {script['file']}")
    except Exception as e:
        log_error(f"Erreur lors de l'exécution de {script['file']}: {str(e)}")

def update_github(repo_name, repo_info):
    log(f"📦 Mise à jour de {repo_name} depuis {repo_info['git_repo']}")
    os.chdir(repo_info["path"])
    subprocess.run(["git", "pull"])

def deploy_gcloud():
    log("🚀 Déploiement sur Google Cloud en cours...")
    subprocess.run(["bash", "scripts/deploy_gcloud.sh"])

def main():
    threads = []

    for repo_name, repo_info in config["projects"].items():
        t = threading.Thread(target=update_github, args=(repo_name, repo_info))
        threads.append(t)
        t.start()

    for script in sorted(config["scripts"], key=lambda x: x["priority"]):
        t = threading.Thread(target=run_script, args=(script,))
        threads.append(t)
        t.start()

    t = threading.Thread(target=deploy_gcloud)
    threads.append(t)
    t.start()

    for t in threads:
        t.join()

if __name__ == "__main__":
    main()
