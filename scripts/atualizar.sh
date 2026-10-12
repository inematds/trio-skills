#!/usr/bin/env bash
# Atualiza pacotes/ a partir dos repositórios originais (cópia sem .git e .github) e regrava FONTE.md e o catálogo.
# Uso: scripts/atualizar.sh            → último commit de cada original
#      scripts/atualizar.sh --conferir → só mostra o commit atual de cada original x o que está em pacotes/
set -euo pipefail
RAIZ=$(cd "$(dirname "$0")/.." && pwd)
TMP=$(mktemp -d); trap 'rm -rf "$TMP"' EXIT
#        pasta              repositório                  subpasta
LISTA=( "addy-agent-skills  addyosmani/agent-skills      ."
        "pocock-skills      mattpocock/skills            ."
        "pstack             poteto/plugins               pstack" )
for linha in "${LISTA[@]}"; do
  read -r pasta repo sub <<<"$linha"
  git clone -q --depth 1 "https://github.com/$repo" "$TMP/$pasta"
  novo=$(git -C "$TMP/$pasta" rev-parse HEAD); data=$(git -C "$TMP/$pasta" log -1 --format=%cs)
  atual=$(grep -o 'Commit: [0-9a-f]*' "$RAIZ/pacotes/$pasta/FONTE.md" 2>/dev/null | cut -d' ' -f2 || true)
  if [ "${1:-}" = "--conferir" ]; then
    [ "$novo" = "$atual" ] && echo "$pasta: em dia (${novo:0:7})" || echo "$pasta: há versão nova ${atual:0:7} → ${novo:0:7} ($data)"
    continue
  fi
  rsync -a --delete --exclude .git --exclude .github "$TMP/$pasta/$sub/" "$RAIZ/pacotes/$pasta/"
  extra=""; [ "$sub" != "." ] && extra="- Só a pasta $sub/ do repositório $repo."
  printf '# Fonte\n\n- Origem: https://github.com/%s%s\n- Commit: %s (%s)\n- Licença: MIT (arquivo LICENSE nesta pasta, mantido sem alteração)\n- Copiado em: %s por scripts/atualizar.sh, sem .git e .github do original\n%s\n' \
    "$repo" "$([ "$sub" != "." ] && echo "/tree/main/$sub")" "$novo" "$data" "$(date +%F)" "$extra" > "$RAIZ/pacotes/$pasta/FONTE.md"
  echo "$pasta: ${atual:0:7} → ${novo:0:7} ($data)"
done
[ "${1:-}" = "--conferir" ] || python3 "$RAIZ/scripts/catalogo.py"
