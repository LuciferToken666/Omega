#!/bin/bash
echo "🌀 Starting Ω‑Auto Service (PRODUCTION MODE)..."
gunicorn main:app --bind 0.0.0.0:$PORT --workers 1
