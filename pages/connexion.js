import { SignIn } from "@clerk/nextjs";

export default function Connexion() {
  return (
    <div className="fade-in">
      <SignIn path="/connexion" routing="path" signUpUrl="/inscription" />
    </div>
  );
}
