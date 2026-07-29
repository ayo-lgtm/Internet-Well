# Product Profile: AI SaaS

## Applies to

Products providing AI-generated analysis, recommendations, content, decisions, workflows, or automation through a hosted application.

## Required capabilities

Critical-journey testing, model and prompt evaluation, prompt-injection and data-exfiltration controls, provenance, uncertainty, abstention, privacy, retention, authentication, authorization, tenant isolation, monitoring, cost controls, provider fallback, incident response, accessibility, and domain review.

## Risk model

Primary risks are fabricated certainty, hallucination, prompt injection, hidden provider data flows, model or prompt drift, discriminatory output, sensitive-data leakage, uncontrolled external action, silent failure, runaway cost, and users mistaking AI output for qualified professional advice.

## Mandatory questions

- What user outcome does the AI improve?
- What happens when the model is wrong, unavailable, manipulated, or uncertain?
- Which data reaches providers, memory, logs, analytics, and support tools?
- Are outputs high-impact, regulated, or likely to be mistaken for professional advice?
- What actions can the AI take without human approval?
- How are model, prompt, retrieval, provider, and policy changes evaluated?

## Selection guidance

Use registry evidence and current pins. Inspect AI may support structured evaluations where suitable. Treat promptfoo as experimental until its open verification debts are closed. Apply OWASP GenAI guidance as a standard, not as proof that implementation is secure. Prefer deterministic logic for rights, eligibility, money, deadlines, safety, or other high-impact conclusions.

## Completion evidence

Critical journeys and representative failure paths pass; evaluation datasets cover expected, edge, multilingual, adversarial, injection, abstention, and provider-failure cases; tenant isolation and data flows are verified; model and prompt versions are recorded; monitoring and fallback work; high-impact outputs are constrained and escalated.

## Human review

Domain experts, security, privacy, legal, accessibility, and operations reviewers must approve high-impact output criteria, sensitive-data providers, regulated use, autonomous actions, public claims, and production release.

## Launch blockers

Silent failure, fabricated certainty, uncontrolled external actions, missing tenant isolation, undisclosed sensitive-data transmission, no fallback, no reproducible evaluation, unsupported professional-advice behavior, or outputs that create material harm without review.
