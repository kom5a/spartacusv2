import { useState } from 'react';

export default function AskSpartacus() {
  const [question, setQuestion] = useState('');
  const [answer, setAnswer] = useState('');
  const [loading, setLoading] = useState(false);

  const askSpartacus = async () => {
    if (!question.trim()) return;
    setLoading(true);
    try {
      const res = await fetch('http://YOUR_VM_IP:5005/api/ask', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ prompt: question })
      });

      const data = await res.json();
      setAnswer(data.output || '❌ Aucune réponse');
    } catch (err) {
      setAnswer('❌ Spartacus ne répond pas...');
    }
    setLoading(false);
  };

  return (
    <div className="bg-black text-white p-4 rounded shadow-xl mt-8">
      <h2 className="text-lg mb-2 text-green-400">🤖 ASK SPARTACUS</h2>
      <input
        type="text"
        className="w-full p-2 text-black rounded mb-3"
        placeholder="Pose ta question..."
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
        onKeyDown={(e) => e.key === 'Enter' && askSpartacus()}
      />
      <button
        className="bg-green-600 hover:bg-green-700 px-4 py-2 rounded"
        onClick={askSpartacus}
        disabled={loading}
      >
        {loading ? '⏳ Réflexion en cours...' : '⚡ Demander à Spartacus'}
      </button>
      <pre className="mt-4 text-green-300 whitespace-pre-wrap">{answer}</pre>
    </div>
  );
}
