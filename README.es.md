# trio-skills

[![trio-skills](guia/assets/banner-es.jpg)](https://inematds.github.io/trio-skills/guia/es/)

**🇧🇷 [Português](README.md) · 🇺🇸 [English](README.en.md) · 🇪🇸 [Español](README.es.md)**

## Qué es

trio-skills reúne en un solo lugar los tres paquetes de skills más usados para agentes de programación: el de Addy Osmani, el de Matt Pocock y el pstack de Lauren Tan. Una skill es un archivo de instrucciones que le enseña al agente (Claude Code, Codex, Cursor) a trabajar de cierta manera. El proyecto es para quien programa con agentes y quiere usar estas skills sin instalar todo de una vez. Cataloga las 97 skills por etapa del trabajo, muestra cuáles tienen el mismo nombre e instala un perfil ligero, medio o pesado. Solo necesitas Git y Python 3.

Los tres paquetes de skills de ingeniería más usados con agentes de IA, **clonados, organizados y listos para instalar por perfil**:

| paquete | autor | skills | enfoque | carpeta |
|---|---|---|---|---|
| agent-skills | Addy Osmani | 25 + 9 comandos + 4 revisores | el ciclo completo: definir → planificar → construir → verificar → revisar → publicar | `pacotes/addy-agent-skills` |
| skills | Matt Pocock | 38 | alinearse antes de construir (grill-me, to-spec, tdd, diagnosing-bugs) | `pacotes/pocock-skills` |
| pstack | Lauren Tan (poteto) | 34 (20 de principio) | demostrar que funciona; plugin de Cursor con el enrutador poteto-mode | `pacotes/pstack` |

Guía completa (PT/EN/ES): **https://inematds.github.io/trio-skills/guia/es/**

▶️ **Video técnico (paso a paso, 4 min 36, en portugués):** https://www.youtube.com/watch?v=QiKrfsTcRi0

## Por qué existe este proyecto

Instalar los tres paquetes completos en cada proyecto es el error más común: demasiadas skills ocupan contexto, se activan sin que lo quieras y **los nombres repetidos entran en conflicto** (el agente elige una y no sabes cuál). Aquí puedes:

1. **Leer** los tres paquetes lado a lado, con la versión y la licencia de cada uno (`pacotes/*/FONTE.md`).
2. **Consultar el catálogo** de las 97 skills por etapa (`catalogo/CATALOGO.md`).
3. **Ver los conflictos** de nombres, incluso con lo que ya está instalado en tu máquina.
4. **Instalar por perfil** — el nivel de rigor acompaña al riesgo.

## Uso rápido

```bash
git clone https://github.com/inematds/trio-skills && cd trio-skills

python3 scripts/catalogo.py                    # genera catalogo/CATALOGO.md y catalogo.json
python3 scripts/conflitos.py --instaladas      # nombres repetidos: paquetes × tu máquina

scripts/instalar.sh --perfil leve --destino ./.claude/skills --dry-run   # revisa antes
scripts/instalar.sh --perfil leve --destino ./.claude/skills             # instala
```

| perfil | cuándo | qué se incluye |
|---|---|---|
| `leve` | ajuste pequeño, pantalla, prototipo | grill-me + grilling + tdd (Pocock) |
| `medio` | función nueva | grill-me + spec, planificación, implementación incremental, TDD y revisión de Addy + comandos /spec /plan /build /review |
| `pesado` | producción, seguridad, algo irreversible | las 25 de Addy + 9 comandos + 4 revisores + grill-me |
| `pstack` | Cursor | solo explica: `/add-plugin pstack` en Cursor (depende del enrutador y de los 20 principios juntos) |

`--destino` es la carpeta de skills del agente: `./.claude/skills` (solo este proyecto) o `~/.claude/skills` (todos tus proyectos en Claude Code).

## Qué resuelve el instalador

- **Listas de verificación de Addy:** sus skills apuntan a `../../references/`. Instalar una skill por separado (incluso con `npx skills add --skill`) hace que se pierda esa carpeta; aquí se copia a `<destino>/../references` y los enlaces funcionan.
- **Comandos fuera del plugin:** los comandos de Addy llaman a `agent-skills:<skill>`, un nombre que solo existe dentro del plugin. Al copiarlos como archivos sueltos, el instalador elimina el prefijo.
- **No sobrescribe** lo que ya tienes (usa `--forcar` si quieres).

## Anatomía de una skill (resumen)

```markdown
---
name: grill-me
description: A relentless interview to sharpen a plan or design.
disable-model-invocation: true
---
Call the Skill tool with "grilling".
```

- `name` y `description` son todo lo que el agente lee de cada skill instalada; el cuerpo solo se carga cuando se activa. La descripción es el disparador.
- `disable-model-invocation: true` = solo se ejecuta cuando la llamas (el agente nunca la activa por su cuenta).
- Una skill puede llamar a otra (`grill-me` solo llama a `grilling`).

## Actualizar

```bash
scripts/atualizar.sh --conferir   # ¿hay una versión nueva en los originales?
scripts/atualizar.sh              # vuelve a copiar (sin .git/.github), vuelve a escribir FONTE.md y el catálogo
bash tests/run.sh                 # 18 verificaciones: paquetes, catálogo, conflictos, instalador
```

## Créditos y licencias

El contenido de `pacotes/` pertenece a los autores originales, bajo licencia MIT, conservada en cada carpeta (`LICENSE`):
[addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) · [mattpocock/skills](https://github.com/mattpocock/skills) · [poteto/plugins (pstack)](https://github.com/poteto/plugins/tree/main/pstack).
Scripts, catálogo, perfiles y guía de este repositorio: MIT, INEMA.CLUB.

Cursos gratuitos de IA: **https://inema.club**
