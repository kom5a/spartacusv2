#!/bin/bash

DATE=$(date +%Y-%m-%d_%H-%M)
BACKUP_DIR=~/kom5a/_backup_local/backup_$DATE

echo "📦 Sauvegarde interne KOM5A → $BACKUP_DIR"

mkdir -p $BACKUP_DIR
cp -r ~/kom5a/* $BACKUP_DIR

echo "✅ Sauvegarde locale terminée à $BACKUP_DIR"
