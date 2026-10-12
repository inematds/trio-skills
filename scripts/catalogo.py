#!/usr/bin/env python3
"""Gera catalogo/catalogo.json e catalogo/CATALOGO.md com todas as skills dos 3 pacotes, por etapa.
Uso: python3 scripts/catalogo.py"""
import json
from collections import Counter
from comum import RAIZ, PACOTES, ETAPAS, skills

NOME_ETAPA = {"definir": "Definir", "planejar": "Planejar", "construir": "Construir", "verificar": "Verificar", "revisar": "Revisar",
              "publicar": "Publicar", "depurar": "Depurar", "principios": "Princípios (pstack)", "rotina": "Rotina e meta", "outros": "Outros (novas)"}


def main():
    S = skills()
    out = RAIZ / "catalogo"
    out.mkdir(exist_ok=True)
    (out / "catalogo.json").write_text(json.dumps(S, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    por_pacote = Counter(s["pacote"] for s in S)
    L = ["# Catálogo das skills", "",
         f"{len(S)} skills: " + ", ".join(f"{k} {v}" for k, v in por_pacote.items()) + ". Gerado por `scripts/catalogo.py`.", "",
         "Legenda: **manual** = `disable-model-invocation: true` (o agente só usa quando você chama); "
         "*em construção* = pasta `in-progress` do Pocock.", ""]
    for e in ETAPAS:
        grupo = [s for s in S if s["etapa"] == e]
        if not grupo:
            continue
        L += [f"## {NOME_ETAPA[e]} ({len(grupo)})", "", "| skill | pacote | o que faz (descrição original) |", "|---|---|---|"]
        for s in sorted(grupo, key=lambda x: (x["pacote"], x["nome"])):
            marca = (" **manual**" if s["so_manual"] else "") + (" *em construção*" if s["em_construcao"] else "")
            desc = s["descricao"].replace("|", "\\|")
            if len(desc) > 180:
                desc = desc[:177].rsplit(" ", 1)[0] + "…"
            L.append(f"| `{s['nome']}`{marca} | {s['pacote']} | {desc} |")
        L.append("")
    L += ["## Como cada pacote se instala no original", ""]
    for pasta, (curto, autor, inst) in PACOTES.items():
        L.append(f"- **{curto}** ({autor}, `pacotes/{pasta}`): {inst}")
    (out / "CATALOGO.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    print(f"catálogo: {len(S)} skills ({dict(por_pacote)}) → catalogo/CATALOGO.md e catalogo/catalogo.json")
    outros = [s["nome"] for s in S if s["etapa"] == "outros"]
    if outros:
        print("sem etapa definida (ver ETAPA em scripts/comum.py):", ", ".join(outros))


if __name__ == "__main__":
    main()
