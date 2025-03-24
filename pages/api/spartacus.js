// /pages/api/spartacus.js

import { exec } from 'child_process';

export default function handler(req, res) {
  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Méthode non autorisée' });
  }

  const { prompt } = req.body;

  if (!prompt || prompt.trim() === '') {
    return res.status(400).json({ error: 'Prompt requis' });
  }

  const command = `python3 ~/ahmed2025/KOM5A/ai/spartacus_engine.py "${prompt.replace(/"/g, '\"')}"`;

  exec(command, (error, stdout, stderr) => {
    if (error) {
      console.error('Erreur d\'exécution :', error);
      return res.status(500).json({ error: stderr || error.message });
    }

    return res.status(200).json({ result: stdout });
  });
}

