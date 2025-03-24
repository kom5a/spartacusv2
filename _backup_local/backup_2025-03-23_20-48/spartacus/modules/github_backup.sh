#!/bin/bash
cd ~/kom5a
git add .
git commit -m "🧠 Backup automatique - $(date '+%Y-%m-%d %H:%M:%S')"
git push origin main
