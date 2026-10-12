# Catálogo das skills

97 skills: addy 25, pocock 38, pstack 34. Gerado por `scripts/catalogo.py`.

Legenda: **manual** = `disable-model-invocation: true` (o agente só usa quando você chama); *em construção* = pasta `in-progress` do Pocock.

## Definir (13)

| skill | pacote | o que faz (descrição original) |
|---|---|---|
| `constraint-driven-development` | addy | Establishes a project's quality bar as a written contract and stops agents quietly lowering it. Interviews the user on which dimensions matter, supplies sane default thresholds… |
| `idea-refine` | addy | Refines raw ideas into sharp, actionable concepts through structured divergent and convergent thinking. Use when an idea is still vague, when you need to stress-test… |
| `interview-me` | addy | Extracts what the user actually wants instead of what they think they should want. Achieves this through one-question-at-a-time interview until ~95% confidence about the… |
| `spec-driven-development` | addy | Creates specs before coding. Use when starting a new project, feature, or significant change and no specification exists yet. Use when drafting a PRD or requirements document… |
| `domain-modeling` | pocock | Build and sharpen a project's domain model. Use when discussing codebase terminology, writing or editing a GLOSSARY.md, or recording or editing an ADR. |
| `grill-me` **manual** | pocock | A relentless interview to sharpen a plan or design. |
| `grill-with-docs` **manual** | pocock | A relentless interview to sharpen a plan or design, which also creates docs (ADR's and glossary) as we go. |
| `grilling` | pocock | Grill the user relentlessly about a plan, decision, or idea. Use when the user wants to stress-test their thinking, or uses any 'grill' trigger phrases. |
| `research` | pocock | Investigate a question against high-trust primary sources and capture the findings as a Markdown file in the repo. Use when the user wants a topic researched, docs or API facts… |
| `to-questionnaire` **manual** | pocock | Turn a decision you can't fully answer into a questionnaire for someone else to fill in. |
| `to-spec` **manual** | pocock | Turn the current conversation into a spec and publish it to the project issue tracker: no interview, just synthesis of what you've already discussed. |
| `how` | pstack | Use for \"how does X work\", code walkthroughs before changing something, and placement / ownership / layering questions (\"where should this live\", \"which package owns… |
| `why` | pstack | Use for 'why does X work this way', 'why we picked Y', design rationale, regressions, postmortems, or data-backed thresholds. Discovers available MCPs and queries each evidence… |

## Planejar (9)

| skill | pacote | o que faz (descrição original) |
|---|---|---|
| `api-and-interface-design` | addy | Guides stable API and interface design. Use when designing APIs, module boundaries, or any public interface. Use when creating REST or GraphQL endpoints, defining type… |
| `context-engineering` | addy | Optimizes agent context setup. Use when starting a new session, when agent output quality degrades, when switching between tasks, or when you need to configure rules files and… |
| `documentation-and-adrs` | addy | Records decisions and documentation. Use when you need to document an architecture decision (ADR) or the reasoning behind a design choice, when changing public APIs, shipping… |
| `planning-and-task-breakdown` | addy | Breaks work into ordered tasks. Use when you have a spec or clear requirements and need to break work into implementable tasks. Use when a task feels too large to start, when… |
| `codebase-design` | pocock | Shared vocabulary for designing deep modules. Use when the user wants to design or improve a module's interface, find deepening opportunities, decide where a seam goes, make… |
| `improve-codebase-architecture` **manual** | pocock | Scan a codebase for deepening opportunities, present them as a visual HTML report, then grill through whichever one you pick. |
| `to-tickets` **manual** | pocock | Break a plan, spec, or the current conversation into a set of tracer-bullet tickets, each declaring its blocking edges, published to the configured tracker (edges as text in… |
| `wayfinder` **manual** | pocock | Plan a huge chunk of work (more than one agent session can hold) as a shared map of decision tickets on your issue tracker, and resolve them one at a time until the way to the… |
| `architect` **manual** | pstack | Sketch types, signatures, and module structure before code, then stay in the loop while implementation fills in. Use for /architect, 'architect this', 'design this', or… |

## Construir (12)

| skill | pacote | o que faz (descrição original) |
|---|---|---|
| `code-simplification` | addy | Simplifies code for clarity. Use when refactoring code for clarity without changing behavior. Use when code works but is harder to read, maintain, or extend than it should be.… |
| `frontend-ui-engineering` | addy | Builds production-quality, accessible, responsive user-facing UIs. Use when building or modifying interfaces and pages, creating components, implementing layouts, meeting WCAG… |
| `git-workflow-and-versioning` | addy | Structures git workflow practices. Use when making any code change. Use when committing, branching, resolving conflicts, splitting uncommitted work in a messy working tree into… |
| `incremental-implementation` | addy | Delivers changes incrementally in thin, verifiable slices. Use when implementing any feature or change that touches more than one file, or when picking up the next task from a… |
| `source-driven-development` | addy | Grounds every implementation decision in official documentation. Use when you want to verify an approach against the official docs before implementing it, or when you want… |
| `implement` **manual** | pocock | Implement a piece of work based on a spec or set of tickets. |
| `implement-spec` **manual** | pocock | Implement the result of /to-spec and /to-tickets in code. |
| `migrate-to-shoehorn` | pocock | Migrate test files from `as` type assertions to @total-typescript/shoehorn. Use when user mentions shoehorn, wants to replace `as` in tests, or needs partial test data. |
| `prototype` | pocock | Build a throwaway prototype to answer a design question. Use when the user wants to sanity-check whether a state model or logic feels right, or explore what a UI should look like. |
| `setup-ts-deep-modules` **manual** *em construção* | pocock | Wire dependency-cruiser into a TypeScript repo so each package is a deep module, with implementation hidden in subfolders and reachable only through its entry-point files.… |
| `arena` **manual** | pstack | Spawn N parallel candidates at the same task, pick a base, graft the strongest parts of the losers into it. Use for /arena, 'arena this', 'throw it in the arena', or when one… |
| `typescript-best-practices` | pstack | TypeScript best practices. Use when reading or editing any .ts or .tsx file. |

## Verificar (7)

| skill | pacote | o que faz (descrição original) |
|---|---|---|
| `browser-testing-with-devtools` | addy | Tests in real browsers via Chrome DevTools MCP. Use when building or debugging anything that runs in a browser. Use when you need to inspect the DOM, capture console errors,… |
| `performance-optimization` | addy | Optimizes application performance across frontend, backend, queries, and databases. Use when performance requirements exist, when you suspect performance regressions, when Core… |
| `test-driven-development` | addy | Drives development with tests using the red-green-refactor loop. Use when implementing any logic, fixing any bug, or changing any behavior. Use when you need to prove that code… |
| `git-guardrails-claude-code` | pocock | Set up Claude Code hooks to block dangerous git commands (push, reset --hard, clean, branch -D, etc.) before they execute. Use when user wants to prevent destructive git… |
| `setup-pre-commit` | pocock | Set up Husky pre-commit hooks with lint-staged (Prettier), type checking, and tests in the current repo. Use when user wants to add pre-commit hooks, set up Husky, configure… |
| `tdd` | pocock | Test-driven development. Use when the user wants to build features or fix bugs test-first, mentions "red-green-refactor", or wants integration tests. |
| `tdd` **manual** | pstack | Use only when the user explicitly asks for TDD, a failing test, or a regression test, OR when the bug has an obvious cheap local test target. Skip when the test path is… |

## Revisar (7)

| skill | pacote | o que faz (descrição original) |
|---|---|---|
| `code-review-and-quality` | addy | Conducts multi-axis code review. Use before merging any change. Use when reviewing code written by yourself, another agent, or a human. Use when you need to assess code quality… |
| `doubt-driven-development` | addy | Subjects every non-trivial decision to a fresh-context adversarial review before it stands. Use when you want every assumption cross-examined before proceeding, when… |
| `security-and-hardening` | addy | Hardens code against vulnerabilities. Use when auditing an input handler for vulnerabilities, when handling user input, authentication, data storage, or external integrations,… |
| `code-review` | pocock | Review the changes since a fixed point (commit, branch, tag, or merge-base) along two axes: Standards (does the code follow this repo's documented coding standards?) and Spec… |
| `interrogate` **manual** | pstack | Use for \"interrogate\", \"adversarial review\", \"multi-model review\", \"challenge this\", \"stress test this code\", \"find blind spots\", or \"tear this apart\". Multiple… |
| `show-me-your-work` **manual** | pstack | Keep a reviewable decision trail for long-running or unattended work: a TSV log with one row per decision (what, why, evidence, result). Local by default; commit it when a… |
| `unslop` | pstack | Cut AI tells from any writing. Must always apply. |

## Publicar (5)

| skill | pacote | o que faz (descrição original) |
|---|---|---|
| `ci-cd-and-automation` | addy | Automates CI/CD pipeline setup. Use when setting up or modifying build and deployment pipelines. Use when you need to automate quality gates, configure test runners in CI, or… |
| `deprecation-and-migration` | addy | Manages deprecation and migration. Use when removing old systems, APIs, or features. Use when migrating users from one implementation to another. Use when migrating a database… |
| `observability-and-instrumentation` | addy | Instruments code so production behavior is visible and diagnosable. Use when adding logging, metrics, tracing, or alerting. Use when shipping any feature that runs in… |
| `shipping-and-launch` | addy | Prepares production launches. Use when preparing to deploy to production, or when asking what needs to be in place before shipping. Use when you need a pre-launch checklist,… |
| `pr` | pocock | Use when writing a PR body. |

## Depurar (4)

| skill | pacote | o que faz (descrição original) |
|---|---|---|
| `debugging-and-error-recovery` | addy | Guides systematic root-cause debugging. Use when tests fail, builds break, something that worked yesterday broke, behavior doesn't match expectations, or you encounter any… |
| `diagnosing-bugs` | pocock | Diagnosis loop for hard bugs and performance regressions. Use when the user says "diagnose"/"debug this", or reports something broken/throwing/failing/slow. |
| `triage` **manual** | pocock | Move issues and external PRs through a state machine of triage roles, categorise, verify, grill if needed, and write agent-ready briefs. |
| `figure-it-out` **manual** | pstack | Design an auditable playbook when no narrower one fits: a large migration, an ambitious multi-part change, or work a human reviews after stepping away. Scales rigor to the… |

## Princípios (pstack) (20)

| skill | pacote | o que faz (descrição original) |
|---|---|---|
| `principle-boundary-discipline` **manual** | pstack | Apply when wiring validation, error handling, or framework adapters. Concentrate guards at system boundaries (CLI, config, network, external APIs); trust internal types and… |
| `principle-build-the-lever` **manual** | pstack | Apply to any non-trivial work, not just bulk work: edits, migrations, analyses, checks. Build the tool that does it or proves it (codemod, script, generator, or a skill your… |
| `principle-encode-lessons-in-structure` **manual** | pstack | Apply when you catch yourself writing the same instruction a second time, or notice a recurring correction. Encode the rule as a lint, metadata flag, runtime check, or script… |
| `principle-exhaust-the-design-space` **manual** | pstack | Apply when facing a novel UI interaction or architectural decision with no precedent in the codebase. Build 2-3 competing prototypes and compare side by side before committing. |
| `principle-experience-first` **manual** | pstack | Apply when product, UX, or feature-scope tradeoffs come up. Choose user delight over implementation convenience; ship fewer polished features over more rough ones. |
| `principle-fix-root-causes` **manual** | pstack | Apply when debugging. Trace each symptom to its root cause and fix it there; reproduce first, ask why until you reach it, resist nil-check guards that silence crashes. |
| `principle-foundational-thinking` **manual** | pstack | Apply before writing logic: choosing core types and data structures, sequencing scaffold-vs-feature work, asking what concurrent actors share. Get the data structures right so… |
| `principle-guard-the-context-window` **manual** | pstack | Apply when context is filling up: large outputs, long files, repeated reads, fan-out planning. Route bulk to subagents; keep summaries in the main thread, not raw payloads. |
| `principle-laziness-protocol` **manual** | pstack | Apply when refactoring, evaluating diff size, or tempted to add abstractions, layers, or signal threading. Bias toward deletion and the smallest change that solves the problem. |
| `principle-make-operations-idempotent` **manual** | pstack | Apply when designing commands, lifecycle steps, or processing loops that run amid crashes, restarts, and retries. Converge to the same end state regardless of partial prior runs. |
| `principle-migrate-callers-then-delete-legacy-apis` **manual** | pstack | Apply when introducing a new internal API while old callers still exist. Migrate callers and delete the old API in the same wave instead of preserving compatibility layers. |
| `principle-minimize-reader-load` **manual** | pstack | Apply when reviewing or shaping code that's hard to trace. Count layers between question and answer, and hidden state in the reader's head; collapse one-caller wrappers and… |
| `principle-never-block-on-the-human` **manual** | pstack | Apply when tempted to ask 'should I do X?' on reversible work. Proceed, present the result, let the human course-correct after the fact; reserve confirmation for irreversible… |
| `principle-outcome-oriented-execution` **manual** | pstack | Apply during planned rewrites and migrations with explicit phase boundaries. Converge on the target architecture; don't preserve smooth intermediate states with throwaway… |
| `principle-prove-it-works` **manual** | pstack | Apply after completing a task, before declaring done. Verify against the real artifact (run the feature, read the actual value, inspect the diff), not a proxy, self-report, or… |
| `principle-redesign-from-first-principles` **manual** | pstack | Apply when integrating a new requirement into an existing design. Redesign as if the requirement had been a foundational assumption from day one, instead of bolting it on. |
| `principle-separate-before-serializing-shared-state` **manual** | pstack | Apply when concurrent actors might write to the same file, branch, key, or state object. Eliminate the sharing first; serialize structurally only when one shared writer is a… |
| `principle-sequence-verifiable-units` **manual** | pstack | Apply to multi-step work (sweeps, migrations, runs of similar edits) and to how you stack commits and PRs. Break work into small units that each end in a verifiable state,… |
| `principle-subtract-before-you-add` **manual** | pstack | Apply when sequencing an addition, refactor, or rewrite. Remove dead weight, redundant validators, and stub references first, then build on the simpler base. |
| `principle-type-system-discipline` **manual** | pstack | Apply when designing types, reviewing a function signature, or writing code in any statically-typed language. Make illegal states unrepresentable, brand semantic primitives,… |

## Rotina e meta (20)

| skill | pacote | o que faz (descrição original) |
|---|---|---|
| `using-agent-skills` | addy | Discovers and invokes agent skills. Use when starting a session, or when you need to decide which skill or workflow applies to the piece of work at hand. This is the meta-skill… |
| `ask-matt` **manual** | pocock | Ask which skill or flow fits your situation. A router over the skills in this repo. |
| `chief-of-staff` **manual** *em construção* | pocock | Pursue a long-running goal in a single session by co-ordinating subagents. |
| `claude-handoff` **manual** *em construção* | pocock | Hand the current conversation off to a fresh background agent that picks up the work immediately. |
| `handoff` **manual** | pocock | Compact the current conversation into a handoff document for another agent to pick up. |
| `loop-me` **manual** *em construção* | pocock | Grill me about specs for the workflows I want to build, within this workspace. |
| `retro` **manual** | pocock | Conduct a retrospective on a coding session. |
| `scaffold-exercises` | pocock | Create exercise directory structures with sections, problems, solutions, and explainers that pass linting. Use when user wants to scaffold exercises, create exercise stubs, or… |
| `setup-matt-pocock-skills` **manual** | pocock | Configure this repo for the engineering skills: set up its issue tracker, triage label vocabulary, and domain doc layout. Run once before first use of the other engineering skills. |
| `teach` **manual** | pocock | Teach the user a new skill or concept, within this workspace. |
| `wait-what` **manual** | pocock | Stop. That last message did not land: re-pitch it. |
| `wizard` | pocock | Generate an interactive bash wizard that walks a human through steps only they can perform. Use when provisioning infrastructure, setting up credentials or CI secrets, walking… |
| `writing-beats` **manual** *em construção* | pocock | Writing, exploit; assemble raw material into a journey of beats, grounding each term before a beat leans on it. |
| `writing-for-agents` | pocock | Writing documents for agents. Use when creating or editing skills, or modifying AGENTS.md or CLAUDE.md. |
| `writing-fragments` **manual** *em construção* | pocock | Writing, explore: mine raw fragments, no structure yet. |
| `writing-shape` **manual** *em construção* | pocock | Writing, exploit: shape raw material into an article, paragraph by paragraph. |
| `automate-me` **manual** | pstack | Use for \"automate me\", \"create/update/refresh my -mode skill\", \"turn/capture my preferences or working style into a skill\", or wanting agents to follow how the user… |
| `poteto-mode` **manual** | pstack | poteto's agent style for concise, detailed responses, deliberate subagents, unslopped prose, simple code, and verified work. Use for poteto, /poteto-mode, or requests to work… |
| `reflect` **manual** | pstack | Spawn three parallel review subagents over the active transcript, surface learnings, and route each to a concrete edit on an existing skill. Use when the user says reflect. |
| `setup-pstack` | pstack | Configure which models pstack uses per role. Detects your available models and writes an always-applied rule that overrides the skill defaults. Use for /setup-pstack,… |

## Como cada pacote se instala no original

- **addy** (Addy Osmani, `pacotes/addy-agent-skills`): npx skills add addyosmani/agent-skills  |  Claude Code: /plugin marketplace add addyosmani/agent-skills e /plugin install agent-skills@addy-agent-skills
- **pocock** (Matt Pocock, `pacotes/pocock-skills`): claude plugin install mattpocock-skills@claude-plugins-official  |  ou cópia pelo skills.sh (nunca os dois)
- **pstack** (Lauren Tan (poteto), `pacotes/pstack`): Cursor: /add-plugin pstack  (fora do Cursor só por adaptações da comunidade)
