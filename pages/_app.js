import '../styles/globals.css';
import { useEffect } from 'react';

function MyApp({ Component, pageProps }) {
  useEffect(() => {
    console.log("🤖 Spartacus AI initialisé.");
    // Activation visible
    const spartacus = document.createElement('div');
    spartacus.innerHTML = "🧠 Spartacus en ligne";
    spartacus.style.position = "fixed";
    spartacus.style.bottom = "10px";
    spartacus.style.right = "10px";
    spartacus.style.background = "#2a2a2a";
    spartacus.style.color = "white";
    spartacus.style.padding = "6px 12px";
    spartacus.style.borderRadius = "12px";
    spartacus.style.zIndex = "9999";
    document.body.appendChild(spartacus);
  }, []);

  return <Component {...pageProps} />;
}

export default MyApp;

