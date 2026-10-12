# trio-skills

[![trio-skills](guia/assets/banner.jpg)](https://inematds.github.io/trio-skills/guia/)

**🇧🇷 [Português](README.md) · 🇺🇸 [English](README.en.md) · 🇪🇸 [Español](README.es.md)**

## O que é

O trio-skills junta num só lugar os três pacotes de skills mais usados para agentes de programação: o do Addy Osmani, o do Matt Pocock e o pstack da Lauren Tan. Uma skill é um arquivo de instruções que ensina o agente (Claude Code, Codex, Cursor) a trabalhar de um jeito. O projeto serve para quem programa com agentes e quer usar essas skills sem instalar tudo de uma vez. Ele cataloga as 97 skills por etapa do trabalho, mostra quais têm o mesmo nome e instala um perfil leve, médio ou pesado. Para usar, basta Git e Python 3.

Os três pacotes de skills de engenharia mais usados com agentes de IA, **clonados, organizados e prontos para instalar por perfil**:

| pacote | autor | skills | foco | pasta |
|---|---|---|---|---|
| agent-skills | Addy Osmani | 25 + 9 comandos + 4 revisores | o ciclo completo: definir → planejar → construir → verificar → revisar → publicar | `pacotes/addy-agent-skills` |
| skills | Matt Pocock | 38 | alinhar antes de construir (grill-me, to-spec, tdd, diagnosing-bugs) | `pacotes/pocock-skills` |
| pstack | Lauren Tan (poteto) | 34 (20 de princípio) | provar que funciona; plugin do Cursor com o roteador poteto-mode | `pacotes/pstack` |

Guia completo (PT/EN/ES): **https://inematds.github.io/trio-skills/guia/**

▶️ **Vídeo técnico (passo a passo, 4 min 36):** https://www.youtube.com/watch?v=QiKrfsTcRi0

## Por que este projeto

Instalar os três inteiros em todo projeto é o erro mais comum: skill demais ocupa contexto, dispara sem você querer e **nomes repetidos colidem** (o agente escolhe uma e você não sabe qual). Aqui você:

1. **Lê** os três pacotes lado a lado, com a versão e a licença de cada um (`pacotes/*/FONTE.md`).
2. **Consulta o catálogo** das 97 skills por etapa (`catalogo/CATALOGO.md`).
3. **Vê os conflitos** de nome, inclusive com o que já está instalado na sua máquina.
4. **Instala por perfil** — a cerimônia acompanha o risco.

## Uso rápido

```bash
git clone https://github.com/inematds/trio-skills && cd trio-skills

python3 scripts/catalogo.py                    # gera catalogo/CATALOGO.md e catalogo.json
python3 scripts/conflitos.py --instaladas      # nomes repetidos: pacotes × sua máquina

scripts/instalar.sh --perfil leve --destino ./.claude/skills --dry-run   # veja antes
scripts/instalar.sh --perfil leve --destino ./.claude/skills             # instale
```

| perfil | quando | o que entra |
|---|---|---|
| `leve` | ajuste pequeno, tela, protótipo | grill-me + grilling + tdd (Pocock) |
| `medio` | recurso novo | grill-me + spec, planejamento, implementação incremental, TDD e revisão do Addy + comandos /spec /plan /build /review |
| `pesado` | produção, segurança, algo irreversível | as 25 do Addy + 9 comandos + 4 revisores + grill-me |
| `pstack` | Cursor | só explica: `/add-plugin pstack` no Cursor (ele depende do roteador e dos 20 princípios juntos) |

`--destino` é a pasta de skills do agente: `./.claude/skills` (só este projeto) ou `~/.claude/skills` (todos os seus projetos no Claude Code).

## O que o instalador resolve

- **Checklists do Addy:** as skills dele apontam para `../../references/`. Instalar uma skill avulsa (inclusive pelo `npx skills add --skill`) perde essa pasta; aqui ela vai para `<destino>/../references`, e os links funcionam.
- **Comandos fora do plugin:** os comandos do Addy chamam `agent-skills:<skill>`, nome que só existe dentro do plugin. Copiados como arquivos soltos, o instalador tira o prefixo.
- **Não sobrescreve** o que você já tem (use `--forcar` se quiser).

## Anatomia de uma skill (resumo)

```markdown
---
name: grill-me
description: A relentless interview to sharpen a plan or design.
disable-model-invocation: true
---
Call the Skill tool with "grilling".
```

- `name` e `description` são tudo o que o agente lê de cada skill instalada; o corpo só carrega quando ela é acionada. A descrição é o gatilho.
- `disable-model-invocation: true` = só roda quando você chama (o agente nunca aciona sozinho).
- Uma skill pode chamar outra (o `grill-me` só chama a `grilling`).

## Atualizar

```bash
scripts/atualizar.sh --conferir   # há versão nova nos originais?
scripts/atualizar.sh              # copia de novo (sem .git/.github), regrava FONTE.md e o catálogo
bash tests/run.sh                 # 18 verificações: pacotes, catálogo, conflitos, instalador
```

## Créditos e licenças

O conteúdo de `pacotes/` é dos autores originais, sob licença MIT, mantida em cada pasta (`LICENSE`):
[addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) · [mattpocock/skills](https://github.com/mattpocock/skills) · [poteto/plugins (pstack)](https://github.com/poteto/plugins/tree/main/pstack).
Scripts, catálogo, perfis e guia deste repositório: MIT, INEMA.CLUB.

Cursos gratuitos de IA: **https://inema.club**
