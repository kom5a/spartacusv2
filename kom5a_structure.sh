#!/bin/bash
echo "🔧 Création de la structure complète KOM5A..."

mkdir -p ~/ahmed2025/KOM5A/{frontend,backend,ai,auth,db,modules,design,affiliation,users,logs,api,analytics}

touch ~/ahmed2025/KOM5A/db/{users.db,json.db,settings.db}
touch ~/ahmed2025/KOM5A/auth/{clerk_config.json,auth_keys.env}
touch ~/ahmed2025/KOM5A/modules/{chatbot.py,bot_affiliate.py,db_sync.py}
touch ~/ahmed2025/KOM5A/frontend/{index.html,style.css,app.js}
touch ~/ahmed2025/KOM5A/backend/{server.js,config.js}
touch ~/ahmed2025/KOM5A/api/routes.js
touch ~/ahmed2025/KOM5A/analytics/{track.js,logs.csv}
touch ~/ahmed2025/KOM5A/logs/spartacus.log

echo "✅ Structure KOM5A créée avec succès."
