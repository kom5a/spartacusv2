export default async function handler(req, res) {
  if (req.method !== "POST") {
    return res.status(405).json({ error: "Méthode non autorisée" });
  }

  const { command } = req.body;

  if (!command || command.trim() === "") {
    return res.status(400).json({ error: "Commande manquante" });
  }

  try {
    const exec = require("child_process").exec;

    exec(`python3 ~/spartacus_vm/spartacus_api.py "${command}"`, (err, stdout, stderr) => {
      if (err) {
        console.error("Erreur API :", stderr);
        return res.status(500).json({ error: "Erreur d'exécution" });
      }

      return res.status(200).json({ output: stdout.trim() });
    });
  } catch (error) {
    return res.status(500).json({ error: "Erreur serveur" });
  }
}
import { exec } from 'child_process';

export default function handler(req, res) {
  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Méthode non autorisée' });
  }

  const { command } = req.body;

  if (!command || typeof command !== 'string') {
    return res.status(400).json({ error: 'Commande invalide' });
  }

  exec(`python3 ~/spartacus_vm/spartacus_engine.py "${command}"`, (error, stdout, stderr) => {
    if (error) {
      return res.status(500).json({ error: stderr || error.message });
    }
    res.status(200).json({ output: stdout.trim() });
  });
}

