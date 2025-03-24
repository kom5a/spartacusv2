import Head from "next/head";
import dynamic from "next/dynamic";

const SpartacusUI = dynamic(() => import("../components/SpartacusUI"), { ssr: false });

export default function Dashboard() {
  return (
    <div className="min-h-screen bg-gray-900 text-white p-6">
      <Head>
        <title>KOM5A - Tableau de Bord</title>
      </Head>

      <header className="mb-8">
        <h1 className="text-3xl font-bold">👑 Tableau de Bord KOM5A</h1>
        <p className="text-gray-400">Bienvenue, visionnaire. Spartacus est prêt.</p>
      </header>

      <section className="mb-10">
        <SpartacusUI />
      </section>

      <footer className="text-gray-500 mt-10 text-sm">
        © 2025 KOM5A. Powered by Spartacus 🛡️
      </footer>
    </div>
  );
}
