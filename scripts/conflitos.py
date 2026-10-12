#!/usr/bin/env python3
"""Mostra skills com o mesmo nome: entre os 3 pacotes e, com --instaladas, contra o que já está na sua máquina.
Mesmo nome = o agente escolhe uma e você não sabe qual.
Uso: python3 scripts/conflitos.py [--instaladas] [--pasta DIR ...]
  --instaladas  varre ~/.claude/skills, ~/.agents/skills, ~/.codex/skills, ./.claude/skills e os plugins
                instalados no Claude Code (~/.claude/plugins/installed_plugins.json)
  --pasta DIR   varre outra pasta (pode repetir)
  --todas       mostra também repetições que não envolvem os 3 pacotes
Sempre sai com código 0: é um relatório, não um bloqueio."""
import json
import sys
from collections import defaultdict
from pathlib import Path
from comum import cabecalho, skills

PADRAO = ["~/.claude/skills", "~/.agents/skills", "~/.codex/skills", "./.claude/skills"]


def plugins_instalados():
    f = Path("~/.claude/plugins/installed_plugins.json").expanduser()
    if not f.exists():
        return []
    d = json.loads(f.read_text())
    return [i["installPath"] for v in d.get("plugins", d).values() for i in v if i.get("installPath")]


def instaladas(pastas):
    vistos = {}
    for p in pastas:
        base = Path(p).expanduser()
        if not base.is_dir():
            continue
        for md in base.rglob("SKILL.md"):
            real = md.resolve()
            if real in vistos:  # symlink para a mesma skill conta uma vez
                continue
            nome = cabecalho(md).get("name") or md.parent.name
            vistos[real] = (nome, str(md.parent).replace(str(Path.home()), "~"))
    return list(vistos.values())


def main(argv):
    pastas = []
    if "--instaladas" in argv:
        pastas += PADRAO + plugins_instalados()
    pastas += [argv[i + 1] for i, a in enumerate(argv) if a == "--pasta" and i + 1 < len(argv)]
    por_nome = defaultdict(list)
    for s in skills():
        por_nome[s["nome"]].append(f"{s['pacote']}: pacotes/{s['pasta']}")
    for nome, onde in instaladas(pastas):
        por_nome[nome].append(f"instalada: {onde}")
    dup = {n: v for n, v in sorted(por_nome.items()) if len(v) > 1}
    entre_pacotes = {n: v for n, v in dup.items() if sum(not x.startswith("instalada") for x in v) > 1}
    if "--todas" not in argv:  # só o que envolve pelo menos uma skill dos pacotes
        dup = {n: v for n, v in dup.items() if any(not x.startswith("instalada") for x in v)}
    print(f"{len(dup)} nome(s) repetido(s)" + (f" (pacotes + {len(pastas)} pasta(s) da máquina)" if pastas else " entre os 3 pacotes"))
    for n, v in dup.items():
        marca = "  ← nos pacotes" if n in entre_pacotes else ""
        print(f"\n{n}{marca}")
        for x in v:
            print(f"  - {x}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
