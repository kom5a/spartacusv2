import json
from datetime import datetime

with open("spartacus_memory.json", "r+") as file:
    memory = json.load(file)
    memory["last_boot"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file.seek(0)
    json.dump(memory, file, indent=4)
    file.truncate()

print("🧠 Spartacus AI lancé.")
print("✅ Mémoire mise à jour.")
