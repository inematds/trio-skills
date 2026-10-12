#!/usr/bin/env python3
"""Instala um perfil de skills numa pasta de skills (projeto ou usuário), copiando de pacotes/.
Uso: scripts/instalar.sh --perfil leve|medio|pesado|pstack --destino PASTA [--dry-run] [--forcar]
  --destino  a pasta de skills do agente, por exemplo ./.claude/skills (projeto) ou ~/.claude/skills (você)
  --dry-run  só mostra o que entraria; não escreve nada (rode isto primeiro)
  --forcar   sobrescreve skill que já existe no destino (sem isso, pula e avisa)
O que ele faz além de copiar:
  - pasta references/ do Addy vai para <destino>/../references, porque as skills dele apontam para ../../references
    (instalar uma skill avulsa perde esses checklists; ver README do agent-skills)
  - comandos do Addy vão para <destino>/../commands sem o prefixo "agent-skills:" (que só existe dentro do plugin)
  - revisores do Addy (perfil pesado) vão para <destino>/../agents
  - perfil pstack só explica como instalar: é plugin do Cursor (/add-plugin pstack)"""
import shutil
import sys
from pathlib import Path
from comum import RAIZ, cabecalho

PASTA = {"addy": "addy-agent-skills", "pocock": "pocock-skills", "pstack": "pstack"}
ADDY = RAIZ / "pacotes" / "addy-agent-skills"


def args(argv):
    a = {"perfil": None, "destino": None, "dry": "--dry-run" in argv, "forcar": "--forcar" in argv}
    for i, x in enumerate(argv):
        if x in ("--perfil", "--destino") and i + 1 < len(argv):
            a[x[2:]] = argv[i + 1]
    return a


def itens(perfil):
    f = RAIZ / "perfis" / f"{perfil}.txt"
    if not f.exists():
        sys.exit(f"perfil desconhecido: {perfil} (há: {', '.join(p.stem for p in (RAIZ / 'perfis').glob('*.txt'))}, pstack)")
    return [l.strip() for l in f.read_text().splitlines() if l.strip() and not l.startswith("#")]


def main(argv):
    a = args(argv)
    if a["perfil"] == "pstack":
        print("pstack é plugin do Cursor e depende do roteador poteto-mode e das 20 skills de princípio juntas.\n"
              "No Cursor: /add-plugin pstack   ·   depois /setup-pstack (modelos por papel) e /poteto-mode no início da tarefa.\n"
              "Os arquivos estão em pacotes/pstack para leitura. Este instalador não copia o pstack avulso.")
        return 0
    if not a["perfil"] or not a["destino"]:
        print(__doc__)
        return 2
    dest = Path(a["destino"]).expanduser().resolve()
    base = dest.parent
    plano, refs = [], False
    for it in itens(a["perfil"]):
        if it.startswith("cmd:"):
            plano.append(("comando", ADDY / ".claude" / "commands" / it[4:], base / "commands" / it[4:]))
        elif it.startswith("agente:"):
            plano.append(("revisor", ADDY / "agents" / it[7:], base / "agents" / it[7:]))
        else:
            pac, rel = it.split("/", 1)
            src = RAIZ / "pacotes" / PASTA[pac] / rel
            nome = cabecalho(src / "SKILL.md").get("name") or src.name
            plano.append(("skill", src, dest / nome))
            refs |= pac == "addy"
    if refs:
        plano.append(("checklists", ADDY / "references", base / "references"))
    nomes = [d.name for t, s, d in plano if t == "skill"]
    rep = {n for n in nomes if nomes.count(n) > 1}
    if rep:
        sys.exit(f"perfil {a['perfil']} tem nome repetido: {', '.join(sorted(rep))}")

    print(f"perfil {a['perfil']} → {dest}" + ("   (dry-run: nada será escrito)" if a["dry"] else ""))
    feitos = pulados = 0
    for tipo, src, dst in plano:
        if not src.exists():
            sys.exit(f"não achei {src} (rode scripts/atualizar.sh?)")
        existe = dst.exists()
        acao = "sobrescreve" if existe and a["forcar"] else ("pula: já existe" if existe else "instala")
        print(f"  {tipo:<10} {dst.relative_to(base) if dst.is_relative_to(base) else dst}   [{acao}]")
        if a["dry"] or (existe and not a["forcar"]):
            pulados += existe and not a["forcar"]
            continue
        if existe:
            shutil.rmtree(dst) if dst.is_dir() else dst.unlink()
        dst.parent.mkdir(parents=True, exist_ok=True)
        if src.is_dir():
            shutil.copytree(src, dst)
        elif tipo == "comando":
            dst.write_text(src.read_text(encoding="utf-8").replace("agent-skills:", ""), encoding="utf-8")
        else:
            shutil.copy2(src, dst)
        feitos += 1
    if a["dry"]:
        print(f"{len(plano)} item(ns) no plano. Tire o --dry-run para instalar.")
    else:
        print(f"instalados {feitos}, pulados {pulados}. Reinicie o agente para ele ler as skills novas.")
        print("Dica: python3 scripts/conflitos.py --instaladas mostra nomes repetidos com o que você já tinha.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
