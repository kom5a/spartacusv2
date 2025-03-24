import React from 'react';
import SpartacusUI from '../components/SpartacusUI';
import AskSpartacus from '../components/AskSpartacus'; // 🧠 IA intégrée (Gemini)

export default function SpartacusPage() {
  return (
    <div className="p-6 min-h-screen bg-black text-white font-mono">
      <h1 className="text-4xl font-bold mb-6">⚙️ Terminal Spartacus</h1>
      <SpartacusUI />
      <AskSpartacus />
    </div>
  );
}

