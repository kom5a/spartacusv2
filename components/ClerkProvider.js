import { ClerkProvider } from '@clerk/nextjs';
import { useRouter } from 'next/router';

const ClerkLayout = ({ children }) => {
  const { pathname } = useRouter();

  return (
    <ClerkProvider
      appearance={{ variables: { colorPrimary: '#00D2FF' } }}
      navigate={(to) => window.history.pushState(null, '', to)}
    >
      {children}
    </ClerkProvider>
  );
};

export default ClerkLayout;
