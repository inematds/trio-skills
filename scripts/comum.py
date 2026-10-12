"""Leitura dos pacotes: acha cada SKILL.md, lê o cabeçalho e classifica por etapa. Usado por catalogo.py, conflitos.py e instalar.py."""
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
PACOTES = {  # pasta em pacotes/ → (nome curto, autor, como instalar no original)
    "addy-agent-skills": ("addy", "Addy Osmani", "npx skills add addyosmani/agent-skills  |  Claude Code: /plugin marketplace add addyosmani/agent-skills e /plugin install agent-skills@addy-agent-skills"),
    "pocock-skills": ("pocock", "Matt Pocock", "claude plugin install mattpocock-skills@claude-plugins-official  |  ou cópia pelo skills.sh (nunca os dois)"),
    "pstack": ("pstack", "Lauren Tan (poteto)", "Cursor: /add-plugin pstack  (fora do Cursor só por adaptações da comunidade)"),
}
ETAPAS = ["definir", "planejar", "construir", "verificar", "revisar", "publicar", "depurar", "principios", "rotina", "outros"]

# etapa de cada skill (nome da pasta). O que não estiver aqui cai em "outros" (pacote atualizado com skill nova).
ETAPA = {
    # Addy
    "idea-refine": "definir", "interview-me": "definir", "spec-driven-development": "definir", "constraint-driven-development": "definir",
    "planning-and-task-breakdown": "planejar", "api-and-interface-design": "planejar", "documentation-and-adrs": "planejar", "context-engineering": "planejar",
    "incremental-implementation": "construir", "frontend-ui-engineering": "construir", "source-driven-development": "construir",
    "git-workflow-and-versioning": "construir", "code-simplification": "construir",
    "test-driven-development": "verificar", "browser-testing-with-devtools": "verificar", "performance-optimization": "verificar",
    "code-review-and-quality": "revisar", "doubt-driven-development": "revisar", "security-and-hardening": "revisar",
    "shipping-and-launch": "publicar", "ci-cd-and-automation": "publicar", "observability-and-instrumentation": "publicar",
    "deprecation-and-migration": "publicar", "debugging-and-error-recovery": "depurar", "using-agent-skills": "rotina",
    # Pocock
    "ask-matt": "rotina", "codebase-design": "planejar", "code-review": "revisar", "diagnosing-bugs": "depurar", "domain-modeling": "definir",
    "grill-with-docs": "definir", "implement": "construir", "implement-spec": "construir", "improve-codebase-architecture": "planejar",
    "prototype": "construir", "pr": "publicar", "research": "definir", "retro": "rotina", "setup-matt-pocock-skills": "rotina",
    "tdd": "verificar", "to-spec": "definir", "to-tickets": "planejar", "triage": "depurar", "wayfinder": "planejar", "wizard": "rotina",
    "chief-of-staff": "rotina", "claude-handoff": "rotina", "loop-me": "rotina", "setup-ts-deep-modules": "construir",
    "writing-beats": "rotina", "writing-fragments": "rotina", "writing-shape": "rotina",
    "git-guardrails-claude-code": "verificar", "migrate-to-shoehorn": "construir", "scaffold-exercises": "rotina", "setup-pre-commit": "verificar",
    "grilling": "definir", "grill-me": "definir", "handoff": "rotina", "teach": "rotina", "to-questionnaire": "definir",
    "wait-what": "rotina", "writing-for-agents": "rotina",
    # pstack
    "architect": "planejar", "arena": "construir", "automate-me": "rotina", "figure-it-out": "depurar", "how": "definir",
    "interrogate": "revisar", "poteto-mode": "rotina", "reflect": "rotina", "setup-pstack": "rotina", "show-me-your-work": "revisar",
    "typescript-best-practices": "construir", "unslop": "revisar", "why": "definir",
}


def cabecalho(md: Path) -> dict:
    """Campos simples do bloco --- ... --- (name, description, disable-model-invocation)."""
    linhas = md.read_text(encoding="utf-8").splitlines()
    if not linhas or linhas[0].strip() != "---":
        return {}
    d, chave = {}, None
    for ln in linhas[1:]:
        if ln.strip() == "---":
            break
        if ":" in ln and not ln.startswith((" ", "\t")):
            k, v = ln.split(":", 1)
            chave, v = k.strip(), v.strip()
            d[chave] = "" if v in (">", ">-", "|", "|-") else v.strip('"').strip("'")
        elif chave and ln.startswith((" ", "\t")):  # valor dobrado (name: >-) continua nas linhas recuadas
            d[chave] = (d[chave] + " " + ln.strip()).strip()
    return d


def skills():
    """Uma entrada por SKILL.md dos 3 pacotes, em ordem estável."""
    out = []
    for pasta, (curto, autor, _) in PACOTES.items():
        base = RAIZ / "pacotes" / pasta
        for md in sorted(base.rglob("SKILL.md")):
            rel = md.parent.relative_to(base)
            nome = md.parent.name
            h = cabecalho(md)
            grupo = rel.parts[1] if curto == "pocock" and len(rel.parts) > 2 else ""
            etapa = "principios" if nome.startswith("principle-") else ETAPA.get(nome, "outros")
            out.append({
                "pacote": curto, "autor": autor, "nome": h.get("name", nome), "pasta": f"{pasta}/{rel.as_posix()}",
                "descricao": h.get("description", ""), "so_manual": h.get("disable-model-invocation", "").lower() == "true",
                "etapa": etapa, "grupo": grupo, "em_construcao": grupo == "in-progress",
            })
    return out
