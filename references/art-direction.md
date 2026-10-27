# Art-direction principles for exceptional READMEs

The README is simultaneously a five-second pitch, an honest demonstration, and a technical entry point. Optimize for *taste, comprehension, personality, structure, and correctness* in roughly that order—never trade technical truth for appearance.

## Visual selection

| Project type | Often effective | Avoid |
| --- | --- | --- |
| App with UI | Real hero screenshot with concise message, 1–3 feature visuals | Fake UI composites presented as product captures |
| CLI or developer tool | Short authentic terminal demo, simple logo, clear command examples | Endless GIFs and walls of badges |
| Library/framework | Crisp proposition, small working snippet, conceptual diagram if complex | Generic stock illustration unrelated to API |
| Creative product | Purpose-built mark, restrained but distinctive graphic system | Generic AI brush marks, fake handmade texture |
| Backend/service | Clear audience/use case, lightweight architecture diagram, verified quickstart | Beauty-only content that hides prerequisites |

### First screen

Typically contains one dominant identity element (wordmark, icon or well-chosen image), a plain-language positioning statement, direct product evidence and one action. A cluster of decorative badges rarely substitutes for an explanation.

### Typography and composition

- GitHub controls base typography. SVG lettering and wordmarks can give personality, but body copy must remain selectable and accessible.
- Plan dark-mode contrast for transparent logos and images. Avoid giant fixed-size assets that overflow mobile.
- Use hierarchy and negative space. No need for decorative horizontal rules between every section.
- Prefer coherent graphic decisions to complicated artwork. Limit the number of competing font styles, effects and palettes.

### Media ethics

- A screenshot must depict the real software. If it shows an unfinished prototype, label it.
- Generate concept art only when approved and useful. Never pass artistic approximation as evidence of a working feature.
- Avoid generic AI artifact patterns: indistinct pseudo-text, implausibly perfect hand-drawn marks, unrelated glass cards, texture overlays, arbitrary glowing gradients or bland 3D shapes.
- Keep assets local to the repo where licensing permits. Give them descriptive names and alt text.
- GIFs are valuable for interaction but expensive to load: prefer short loops and a static fallback.

## Structural practice

- Say **what it is** before lengthy technical detail.
- Get the reader to a working first action quickly.
- Group related features and link to deeper docs rather than overwhelming the README.
- Retain troubleshooting, compatibility and known limitations when they prevent failures.
- Link to contribution, support, license and security policies when relevant.

## Reference projects (inspiration, not templates)

- [Excalidraw](https://github.com/excalidraw/excalidraw): friendly recognizability and rapid explanation.
- [Gum](https://github.com/charmbracelet/gum): an unusual but coherent CLI personality.
- [Catppuccin](https://github.com/catppuccin/catppuccin): exceptionally consistent visual system.
- [VHS](https://github.com/charmbracelet/vhs): the real product demo supports technical understanding.
- [n8n](https://github.com/n8n-io/n8n): clearer product positioning and action hierarchy.

Extract general principles, not artwork, layout clones or proprietary brand assets. Match the project you have.

## Quality checklist

- [ ] Project purpose understandable in seconds.
- [ ] Authentic proof accompanies big claims.
- [ ] Visual identity is distinctive *and* restrained.
- [ ] Headings and sections follow user questions naturally.
- [ ] Quickstart really works with documented prerequisites.
- [ ] Paths, links, image sizes and alt text validated.
- [ ] Works in GitHub's light and dark themes where tested.
- [ ] No fabricated features, screenshots or unverified performance claims.
- [ ] Previous accurate README information preserved or intentionally relocated.
- [ ] User approved the direction before implementation.
