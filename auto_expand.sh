#!/bin/bash
set -e
echo "🔱 Ω‑AUTO‑EXPAND INITIATED..."

mkdir -p app src config logs modules public

RUNTIME="python"
echo "Runtime detected: $RUNTIME"

pip install -r requirements.txt || echo "No requirements.txt found"

echo "Generating launcher..."
chmod +x start.sh

echo "EXPANDING CONFIG..."
cat <<EOF > config/system.json
{
    "runtime": "$RUNTIME",
    "version": "Ω-AUTO-EXPAND-X",
    "deploy": "render",
    "timestamp": "$(date)"
}
EOF

echo "🔥 Ω‑AUTO‑EXPAND COMPLETE."
