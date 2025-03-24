# spartacus_ai.py
import json, datetime

def log(msg):
    with open("spartacus.log", "a") as f:
        f.write(f"[{datetime.datetime.now()}] {msg}\n")

def load_memory():
    try:
        with open("spartacus_memory.json", "r") as f:
            return json.load(f)
    except:
        return {}

def save_memory(memory):
    with open("spartacus_memory.json", "w") as f:
        json.dump(memory, f, indent=4)

def main():
    log("🧠 Spartacus AI lancé.")
    memory = load_memory()
    memory["last_boot"] = str(datetime.datetime.now())
    save_memory(memory)
    log("✅ Mémoire mise à jour.")

if __name__ == "__main__":
    main()
