# trio-skills

[![trio-skills](guia/assets/banner-en.jpg)](https://inematds.github.io/trio-skills/guia/en/)

**🇧🇷 [Português](README.md) · 🇺🇸 [English](README.en.md) · 🇪🇸 [Español](README.es.md)**

## What it is

trio-skills brings together in one place the three most used skill packs for coding agents: Addy Osmani's, Matt Pocock's and Lauren Tan's pstack. A skill is an instruction file that teaches the agent (Claude Code, Codex, Cursor) how to work in a certain way. The project is for people who code with agents and want to use these skills without installing everything at once. It catalogs the 97 skills by work stage, shows which ones share the same name and installs a light, medium or heavy profile. All you need is Git and Python 3.

The three most widely used engineering skill packages for AI agents, **cloned, organized, and ready to install by profile**:

| package | author | skills | focus | folder |
|---|---|---|---|---|
| agent-skills | Addy Osmani | 25 + 9 commands + 4 reviewers | the full cycle: define → plan → build → verify → review → publish | `pacotes/addy-agent-skills` |
| skills | Matt Pocock | 38 | align before building (grill-me, to-spec, tdd, diagnosing-bugs) | `pacotes/pocock-skills` |
| pstack | Lauren Tan (poteto) | 34 (20 principles) | prove it works; Cursor plugin with the poteto-mode router | `pacotes/pstack` |

Complete guide (PT/EN/ES): **https://inematds.github.io/trio-skills/guia/en/**

▶️ **Technical video (step by step, 4 min 36, in Portuguese):** https://www.youtube.com/watch?v=QiKrfsTcRi0

## Why this project

Installing all three packages in every project is the most common mistake: too many skills take up context, trigger when you don’t want them to, and **duplicate names collide** (the agent picks one, and you don’t know which). Here you can:

1. **Read** the three packages side by side, with each one’s version and license (`pacotes/*/FONTE.md`).
2. **Browse the catalog** of 97 skills by stage (`catalogo/CATALOGO.md`).
3. **See name conflicts**, including with what is already installed on your machine.
4. **Install by profile** — the ceremony matches the risk.

## Quick start

```bash
git clone https://github.com/inematds/trio-skills && cd trio-skills

python3 scripts/catalogo.py                    # generates catalogo/CATALOGO.md and catalogo.json
python3 scripts/conflitos.py --instaladas      # duplicate names: packages × your machine

scripts/instalar.sh --perfil leve --destino ./.claude/skills --dry-run   # preview first
scripts/instalar.sh --perfil leve --destino ./.claude/skills             # install
```

| profile | when | what gets included |
|---|---|---|
| `leve` | small adjustment, screen, prototype | grill-me + grilling + tdd (Pocock) |
| `medio` | new feature | grill-me + spec, planning, incremental implementation, TDD and review from Addy + /spec /plan /build /review commands |
| `pesado` | production, security, something irreversible | all 25 from Addy + 9 commands + 4 reviewers + grill-me |
| `pstack` | Cursor | explanation only: `/add-plugin pstack` in Cursor (it depends on the router and all 20 principles together) |

`--destino` is the agent’s skills folder: `./.claude/skills` (this project only) or `~/.claude/skills` (all your projects in Claude Code).

## What the installer handles

- **Addy’s checklists:** his skills point to `../../references/`. Installing a standalone skill (including with `npx skills add --skill`) loses that folder; here it goes to `<destino>/../references`, and the links work.
- **Commands outside the plugin:** Addy’s commands call `agent-skills:<skill>`, a name that only exists inside the plugin. When copied as standalone files, the installer strips the prefix.
- **Doesn’t overwrite** what you already have (use `--forcar` if you want to).

## Anatomy of a skill (summary)

```markdown
---
name: grill-me
description: A relentless interview to sharpen a plan or design.
disable-model-invocation: true
---
Call the Skill tool with "grilling".
```

- `name` and `description` are all the agent reads from each installed skill; the body is loaded only when it’s triggered. The description is the trigger.
- `disable-model-invocation: true` = runs only when you call it (the agent never triggers it on its own).
- A skill can call another (the `grill-me` skill only calls `grilling`).

## Update

```bash
scripts/atualizar.sh --conferir   # is there a new version in the originals?
scripts/atualizar.sh              # copies again (without .git/.github), rewrites FONTE.md and the catalog
bash tests/run.sh                 # 18 checks: packages, catalog, conflicts, installer
```

## Credits and licenses

The content in `pacotes/` belongs to the original authors and is licensed under MIT, maintained in each folder (`LICENSE`):
[addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) · [mattpocock/skills](https://github.com/mattpocock/skills) · [poteto/plugins (pstack)](https://github.com/poteto/plugins/tree/main/pstack).
Scripts, catalog, profiles, and guide in this repository: MIT, INEMA.CLUB.

Free AI courses: **https://inema.club**
