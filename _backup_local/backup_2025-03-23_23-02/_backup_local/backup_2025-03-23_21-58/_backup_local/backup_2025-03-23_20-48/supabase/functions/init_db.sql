-- 👤 Utilisateurs
create table if not exists users (
  id uuid primary key default gen_random_uuid(),
  email text not null unique,
  username text,
  created_at timestamp default now()
);

-- 📝 Publications
create table if not exists posts (
  id uuid primary key default gen_random_uuid(),
  user_id uuid references users(id),
  content text,
  type text default 'text',
  created_at timestamp default now()
);

-- 👥 Abonnements
create table if not exists abonnements (
  id uuid primary key default gen_random_uuid(),
  follower uuid references users(id),
  following uuid references users(id),
  created_at timestamp default now()
);

-- 💰 Transactions KOM5A Coins
create table if not exists transactions (
  id uuid primary key default gen_random_uuid(),
  user_id uuid references users(id),
  montant integer,
  type text,
  created_at timestamp default now()
);
