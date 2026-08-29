# App Design Style Catalog

A user-facing and agent-facing vocabulary for choosing an application's visual direction before implementation. The goal is to translate vague requests such as “make it modern” into an explicit design brief.

## Core styles

| Style | Visual language | Strong fits | Watch-outs |
|---|---|---|---|
| Minimalism | restrained palette, whitespace, few focal elements | productivity, legal, finance, health, utilities | can become generic or under-signposted |
| Maximalism | dense composition, expressive type, layered color/pattern | culture, media, campaigns, creator products | accessibility and cognitive load |
| Futuristic | technical geometry, luminous surfaces, motion, high contrast | AI, developer tools, emerging-tech products | avoid sci-fi decoration that hurts usability |
| Vector art | scalable illustration and geometric forms | onboarding, education, friendly SaaS | illustration must support rather than replace hierarchy |
| Collage art | cutouts, layered imagery, mixed media | editorial, culture, campaigns | can become visually noisy |
| Retro | period-specific typography, palettes and motifs | entertainment, lifestyle, nostalgia-led brands | distinguish intentional period design from dated UI |
| Cyberpunk | dark surfaces, neon accents, dense technical motifs | games, experimental developer/AI experiences | poor fit for trust-heavy products unless used sparingly |
| Pop art | bold primary forms, repetition, graphic contrast | creator, entertainment, campaigns | high visual intensity |
| Glassmorphism | translucent surfaces, blur, layered depth | dashboards, premium utilities, modern consumer UI | contrast/performance; always provide readable fallbacks |
| Clay style | soft 3D forms, rounded objects, playful depth | onboarding, education, family/consumer apps | asset weight and excessive ornament |
| Pixel art | deliberately low-resolution visual language | games, retro communities, playful products | limited fit for dense professional workflows |
| Editorial | typography-led layouts, strong grids, image/text rhythm | publishing, knowledge, portfolios, research | long-form patterns need adaptation for transactional UI |
| Y2K | early-digital motifs, chrome, gradients, playful typography | fashion, music, creator products | trend-sensitive and easy to overdo |
| Swiss design | grid discipline, typography, whitespace, objective hierarchy | enterprise, legal, finance, information-heavy apps | can feel austere without brand character |
| Surreal design | unexpected scale/composition and dreamlike imagery | campaigns, art, creative products | do not sacrifice navigation predictability |
| Bohemian | organic textures, warm eclectic patterns, handmade feel | lifestyle, wellness, travel, craft | consistency and contrast |
| Victorian style | ornamental typography, borders, historical motifs | storytelling, heritage, themed experiences | unsuitable as literal UI chrome for most workflows |
| Graffiti | expressive lettering, street-art texture and irregular composition | music, youth culture, creative communities | readability and accessibility |
| Aurora | luminous gradient fields and atmospheric color | AI, premium SaaS, onboarding/marketing surfaces | gradients should not obscure controls/text |
| Handwritten | hand-rendered typography/marks and human imperfection | personal, education, creative and friendly brands | use as accent; body/interface text must remain readable |

## Selection framework

Choose a **primary style**, optional **secondary influence**, and explicit usability constraints. Do not combine styles merely because they are available.

A design brief should capture:

- product category and audience;
- desired emotional qualities (trusted, energetic, calm, premium, playful, technical, etc.);
- primary style and optional secondary influence;
- typography direction;
- density and information hierarchy;
- motion tolerance;
- accessibility requirements;
- device targets and PWA/native constraints;
- reference products/screens the user likes;
- patterns the user explicitly dislikes.

## Agent rule

When a user has not chosen a style, recommend 2–3 candidates based on product purpose and explain the trade-off in plain language. For trust-sensitive products, prioritize usability, accessibility and established interaction patterns over visual novelty. Never infer that a visual style changes the product's security, legal, privacy or accessibility requirements.
