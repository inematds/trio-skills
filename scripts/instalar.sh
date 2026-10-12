#!/usr/bin/env bash
# Atalho: scripts/instalar.sh --perfil leve|medio|pesado|pstack --destino PASTA [--dry-run] [--forcar]
exec python3 "$(dirname "$0")/instalar.py" "$@"
