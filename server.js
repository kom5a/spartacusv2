require('dotenv').config();
const express = require('express');
const cors = require('cors');

const app = express();
const PORT = process.env.PORT || 8080;

app.use(cors());
app.use(express.json());

app.get('/', (req, res) => {
  res.send('🔥 KOM5A API is LIVE! 🚀');
});

app.get('/api/v1/test', (req, res) => {
  res.json({ message: 'API Test OK 🎯' });
});

app.listen(PORT, '0.0.0.0', () => {
  console.log(`✅ Serveur lancé sur http://localhost:${PORT}`);
});
