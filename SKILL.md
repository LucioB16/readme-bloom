---
name: readme-bloom
description: "Create, redesign or audit GitHub repository READMEs with deliberate visual art direction, clear product storytelling, genuine screenshots, and verified technical documentation. Use when asked to write, beautify, improve, redesign or review README.md or related banners and diagrams."
---

# ReadmeBloom

Design memorable GitHub READMEs **with the user**. Treat each README as a product introduction and reliable technical document, not a generic template.

## Non-negotiable rules

- **Inspect before claiming.** Read the repository, current README, project manifests, entrypoints, docs and relevant assets. Distinguish verified facts, inferences and unknowns. Never invent features, commands, compatibility, testimonials, screenshots or metrics.
- **Interview selectively.** Ask about consequential preferences not answered by the repository or the user: audience, first impression, visual style, language, sections, documentation depth, real media and branding. See [references/interview.md](references/interview.md).
- **Propose before editing.** Offer 2–3 meaningfully different, context-aware directions with brief previews and tradeoffs. **STOP for explicit user approval** before modifying the README or creating final visual assets.
- **Respect technical truth.** Preserve accurate installation, usage, configuration, API, compatibility, license and warning information from an existing README. Don't quietly delete useful material.
- **Visual honesty.** Use real screenshots for a UI; label conceptual mockups. Don't fabricate product interfaces or copy other projects' brand assets.
- **Portable and accessible.** Prefer GitHub Flavored Markdown, robust relative asset paths, descriptive alt text, sensible dimensions, dark/light legibility, mobile readability and low visual noise.
- **Preserve authorization boundaries.** Do not push, create a PR, install dependencies or publish external changes without authorization. Respect repository instructions and unrelated work.

## Process

### 1. Discover and establish evidence

Decide whether the task is to **create from zero**, **improve**, or **audit only**. Inspect the project (read-only) before planning:

- Its real purpose, distinctive value and users.
- Verified install/usage commands, requirements, tests, license, maturity and limitations.
- Existing logo, brand colors, screenshots, recordings, architecture diagrams and demo URLs.
- Strengths and accuracy problems in the current README.

Record material statements as **Verified**, **Inference** or **Unconfirmed**. Resolve important unknowns before asserting them in marketing copy.

### 2. Ask targeted questions

Consult [references/interview.md](references/interview.md). Ask only what changes the design or documentation; keep questions in a small batch. If the user has already selected style, audience or scope, don't ask again.

### 3. Present 2–3 directions; wait

Each direction should include:

1. A distinctive name, design thesis and suitability to this project.
2. Proposed hierarchy, visual tone, typography, palette and use of authentic media.
3. How the first screen communicates project value.
4. One honest tradeoff or limitation.
5. A preview when tools permit: composed Markdown wireframe, screenshot placement, SVG concept or clearly labeled illustration.

Read [references/art-direction.md](references/art-direction.md). Don't force presets: elegant minimal, technical, product-first, editorial, artistic and experimental directions depend on the project. A user can reject all options.

**Approval gate:** Stop here. No README edits or final assets until the user explicitly chooses or revises a direction. For an **audit-only** request, deliver findings without this gate.

### 4. Shape the story and documentation

For an approved direction, plan:

- Hero: project name/identity, clear value proposition, strongest relevant visual/proof, useful next action.
- Fast path: legitimate installation or trying the product.
- Relevant detail: examples, features, prerequisites, configuration, usage, architecture, contribution/support, license and limitations.
- Navigation only when document length justifies it; badges only when decision-useful.

Use **real screenshots** to explain UI; **short genuine recordings** for interaction; **diagrams** for complex relationships; **illustrations** for approved branding. Don't use every format by default.

### 5. Implement

Edit only the requested README and approved assets. Reuse source images before creating anything. Avoid template-like badges, fake textured AI art, generic stock imagery and filler prose. Respect existing localization and repository conventions.

Optional deterministic helpers (Python standard library only):

- `python3 scripts/readme_audit.py README.md` — read-only Markdown and local asset checks.
- `python3 scripts/preview_concepts.py --name "Project" --tagline "Truthful message" --out-dir /tmp/readme-bloom-previews` — three **conceptual** SVGs to discuss, not product screenshots. Ask before adding them to a repo.

### 6. Validate

Check GitHub-rendered Markdown where possible, light/dark modes, narrower viewports, alt text, relative asset paths, links, command accuracy, fact preservation and the approved creative direction. Run relevant safe checks. If rendered inspection isn't possible, say so; don't claim it passed.

### 7. Hand off

Summarize changes, visuals used, verified facts, checks run and outstanding gaps. Only commit/push if requested, following the repository's Git workflow.

## Standards of taste

- Purpose understandable within seconds.
- One strong, original identity rather than decorative overload.
- Typographic hierarchy and whitespace before more assets.
- Real product demonstrations rather than marketing claims alone.
- Practical quickstart and technically accurate links.
- Accessibility and maintainability over novelty.
- Be inspired by projects such as Excalidraw, Gum, Catppuccin, VHS and n8n; **never copy their identity**.
