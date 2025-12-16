#!/bin/bash
set -e

echo "🔱 Ω‑AUTO‑EXPAND INITIATED..."

# 1) สร้างโฟลเดอร์มาตรฐาน
mkdir -p app src config logs modules public

# 2) Auto detect ภาษา
if ls *.py > /dev/null 2>&1; then
    RUNTIME="python"
elif ls *.js > /dev/null 2>&1; then
    RUNTIME="node"
elif ls *.go > /dev/null 2>&1; then
    RUNTIME="go"
else
    RUNTIME="unknown"
fi
echo "Runtime detected: $RUNTIME"

# 3) Auto install dependencies
case $RUNTIME in
    "python")
        pip install -r requirements.txt 2>/dev/null || echo "No requirements.txt"
        ;;
    "node")
        npm install || yarn install || pnpm install
        ;;
    "go")
        go mod tidy
        ;;
esac

# 4) Generate launcher
echo "Generating launcher..."
cat <<EOF > start.sh
#!/bin/bash
echo '🌀 Starting Ω‑Auto Service...'
case $RUNTIME in
    "python") python main.py ;;
    "node")   node index.js ;;
    "go")     go run main.go ;;
    *)        echo "Runtime not recognized." ;;
esac
EOF
chmod +x start.sh

# 5) Auto‑expand config
echo "EXPANDING CONFIG..."
cat <<EOF > config/system.json
{
    "runtime": "$RUNTIME",
    "version": "Ω-AUTO-EXPAND",
    "expand_mode": true,
    "timestamp": "$(date)"
}
EOF

echo "🔥 Ω‑AUTO‑EXPAND COMPLETE."
