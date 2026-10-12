#!/usr/bin/env bash
# Testes do trio-skills: catálogo, conflitos e instalador (sempre numa pasta temporária). Uso: bash tests/run.sh
set -u
RAIZ=$(cd "$(dirname "$0")/.." && pwd); cd "$RAIZ"
T=$(mktemp -d); trap 'rm -rf "$T"' EXIT
falhas=0
ok(){ echo "  ok  $1"; }
erro(){ echo "  ERRO $1"; falhas=$((falhas+1)); }

echo "pacotes"
[ "$(ls pacotes/*/LICENSE | wc -l)" = 3 ] && ok "3 LICENSE" || erro "LICENSE faltando"
[ "$(find pacotes -name .git -o -name .github | wc -l)" = 0 ] && ok "sem .git/.github aninhado" || erro ".git/.github dentro de pacotes/"
grep -q "Commit: [0-9a-f]\{40\}" pacotes/pstack/FONTE.md && ok "FONTE.md com commit" || erro "FONTE.md sem commit"

echo "catálogo"
python3 scripts/catalogo.py >/dev/null || erro "catalogo.py falhou"
n=$(python3 -c "import json;print(len(json.load(open('catalogo/catalogo.json'))))")
m=$(find pacotes -name SKILL.md | wc -l)
[ "$n" = "$m" ] && ok "$n skills no catálogo = $m SKILL.md" || erro "catálogo $n != $m SKILL.md"
python3 -c "import json;d=json.load(open('catalogo/catalogo.json'));assert all(s['nome'] and s['descricao'] for s in d)" && ok "todas com nome e descrição" || erro "skill sem nome/descrição"
python3 -c "import json;d=json.load(open('catalogo/catalogo.json'));assert not [s for s in d if s['etapa']=='outros']" && ok "todas com etapa" || erro "skill sem etapa (scripts/comum.py ETAPA)"

echo "conflitos"
out=$(python3 scripts/conflitos.py); rc=$?
[ $rc = 0 ] && echo "$out" | grep -q "^tdd" && ok "acha tdd (pocock × pstack), sai 0" || erro "conflitos.py"
mkdir -p "$T/fake/x" && printf -- '---\nname: >-\n  spec-driven-development\ndescription: teste\n---\n' > "$T/fake/x/SKILL.md"
python3 scripts/conflitos.py --pasta "$T/fake" | grep -q "^spec-driven-development" && ok "acha conflito com pasta extra (name dobrado >-)" || erro "--pasta"

echo "instalador"
for p in leve medio pesado; do
  scripts/instalar.sh --perfil $p --destino "$T/$p/.claude/skills" --dry-run >/dev/null || erro "dry-run $p"
  [ ! -e "$T/$p" ] && ok "dry-run $p não escreve nada" || erro "dry-run $p escreveu"
  scripts/instalar.sh --perfil $p --destino "$T/$p/.claude/skills" >/dev/null || erro "instalar $p"
done
nl=$(ls "$T/leve/.claude/skills" | wc -l); nm=$(ls "$T/medio/.claude/skills" | wc -l); np=$(ls "$T/pesado/.claude/skills" | wc -l)
[ "$nl" -lt "$nm" ] && [ "$nm" -lt "$np" ] && ok "leve $nl < médio $nm < pesado $np" || erro "perfis fora de ordem ($nl $nm $np)"
[ "$(find "$T/pesado/.claude/skills" -name SKILL.md | wc -l)" -ge "$np" ] && ok "cada skill instalada tem SKILL.md" || erro "skill sem SKILL.md"
[ -f "$T/medio/.claude/skills/spec-driven-development/../../references/definition-of-done.md" ] && ok "../../references resolve" || erro "references"
! grep -rq "agent-skills:" "$T/pesado/.claude/commands" && ok "comandos sem prefixo agent-skills:" || erro "prefixo nos comandos"
[ "$(ls "$T/pesado/.claude/agents" | wc -l)" = 4 ] && ok "4 revisores no pesado" || erro "revisores"
scripts/instalar.sh --perfil leve --destino "$T/leve/.claude/skills" | grep -q "pula: já existe" && ok "não sobrescreve sem --forcar" || erro "sobrescreveu"
scripts/instalar.sh --perfil pstack --destino "$T/x" | grep -q "add-plugin pstack" && [ ! -e "$T/x" ] && ok "pstack só orienta" || erro "pstack"

echo
[ $falhas = 0 ] && echo OK || { echo "FALHOU: $falhas"; exit 1; }
