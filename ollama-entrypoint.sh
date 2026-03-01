#!/bin/bash
# ollama-entrypoint.sh — starts ollama and pulls the model if not present
ollama serve &
OLLAMA_PID=$!

# Wait for ollama to be ready
until ollama list >/dev/null 2>&1; do sleep 1; done

# Pull model if not already downloaded
if ! ollama list | grep -q 'mistral:7b-instruct-v0.3-q4_K_M'; then
  echo "Pulling mistral:7b-instruct-v0.3-q4_K_M..."
  ollama pull mistral:7b-instruct-v0.3-q4_K_M
fi

# Keep ollama running in foreground
wait $OLLAMA_PID
