import Head from "next/head";
import SpartacusUI from "../components/SpartacusUI";

export default function Home() {
  return (
    <div className="min-h-screen bg-gray-100 text-black p-8">
      <Head>
        <title>KOM5A - Contrôle IA</title>
      </Head>

      <h1 className="text-3xl font-bold mb-6">👑 Bienvenue sur KOM5A</h1>
      <p className="mb-4">Contrôle Spartacus via l’interface ci-dessous :</p>

      <SpartacusUI />
    </div>
  );
}
