import { useState } from 'react';

export default function SpartacusUI() {
  const [input, setInput] = useState('');
  const [response, setResponse] = useState('');
  const [loading, setLoading] = useState(false);

  const sendCommand = async () => {
    if (!input.trim()) return;
    setLoading(true);
    try {
      const res = await fetch('http://YOUR_VM_IP:5005/api/command', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ command: input })
      });

      const data = await res.json();
      setResponse(data.output || '🛑 Aucune réponse reçue.');
    } catch (err) {
      setResponse('🚨 Erreur de connexion à Spartacus API');
    }
    setLoading(false);
  };

  return (
    <div className="bg-gray-900 p-4 rounded shadow-lg w-full max-w-xl">
      <input
        className="w-full p-2 bg-black text-green-400 border border-green-500 rounded mb-4"
        placeholder="Tape ta commande..."
        value={input}
        onChange={e => setInput(e.target.value)}
        onKeyDown={e => e.key === 'Enter' && sendCommand()}
      />
      <button
        className="bg-green-600 hover:bg-green-700 text-white px-4 py-2 rounded"
        onClick={sendCommand}
        disabled={loading}
      >
        {loading ? '⏳ Envoi...' : '⚡ Exécuter'}
      </button>
      <pre className="mt-4 text-green-300 whitespace-pre-wrap">{response}</pre>
    </div>
  );
}

