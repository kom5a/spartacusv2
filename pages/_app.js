import '../styles/globals.css';
import { ClerkProvider, RedirectToSignIn, SignedIn, SignedOut } from '@clerk/nextjs';
import { useEffect } from 'react';

function MyApp({ Component, pageProps }) {
  useEffect(() => {
    console.log("🤖 Spartacus AI initialisé.");
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

  return (
    <ClerkProvider {...pageProps}>
      <SignedIn>
        <Component {...pageProps} />
      </SignedIn>
      <SignedOut>
        <RedirectToSignIn />
      </SignedOut>
    </ClerkProvider>
  );
}

export default MyApp;

