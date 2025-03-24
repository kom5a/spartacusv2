import React from 'react';
import Link from 'next/link';

export default function HomePage() {
  return (
    <div className="p-8 text-center bg-gray-900 text-white min-h-screen">
      <h1 className="text-5xl font-bold mb-6">Bienvenue sur KOM5A 💎</h1>
      <p className="text-xl mb-6">La plateforme des visionnaires connectés.</p>
      <div className="space-x-4">
        <Link href="/spartacus" className="bg-green-500 px-4 py-2 rounded hover:bg-green-700">Spartacus Terminal</Link>
      </div>
    </div>
  );
}
