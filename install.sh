#!/bin/bash
echo "[*] checking basic requirements..."

if ! [ -x "$(command -v python3)" ]; then
  echo 'Error: python3 is not installed.' >&2
  exit 1
fi

if ! [ -x "$(command -v npm)" ]; then
  echo 'Error: npm is not installed.' >&2
  exit 1
fi

if ! [ -x "$(command -v pip)" ]; then
  echo 'Error: pip is not installed.' >&2
  exit 1
fi
echo "[OK] Base requirements satisfied"

echo "[*] setting up venv..."
python3 -m venv venv
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    source venv/bin/activate
elif [[ "$OSTYPE" == "msys" ]]; then
    source venv/Scripts/activate
fi

echo "[OK] venv setup complete"

echo "[*] installing root npm packages..."
npm install
echo "[OK] npm install complete"

echo "[*] installing packages dependencies.."
npx nx run-many --target=install --all
echo "[OK] nx install complete"


echo "[*] setting up default server .env variables"
npx nx run djangolic:setup-env
echo "[OK] env variables set ! you may want to change them in .env file"


echo "[*] setting up server database.."
npx nx run djangolic:db-init
echo "[OK] database setup complete"

echo "[*] building tailwind css.."
npx nx run djangolic:build

