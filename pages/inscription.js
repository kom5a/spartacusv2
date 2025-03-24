import { SignUp } from "@clerk/nextjs";

export default function Inscription() {
  return (
    <div className="fade-in">
      <SignUp path="/inscription" routing="path" signInUrl="/connexion" />
    </div>
  );
}
