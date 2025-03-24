import ClerkLayout from '../components/ClerkProvider';
import '../styles/globals.css';
import { useEffect } from 'react';

export default function App({ Component, pageProps }) {
  useEffect(() => {
    console.log("🤖 Spartacus IA lancée avec Gemini en arrière-plan.");
  }, []);

  return (
    <ClerkLayout>
      <Component {...pageProps} />
    </ClerkLayout>
  );
}
