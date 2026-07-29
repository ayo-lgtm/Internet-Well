# Product Profile: AI SaaS

## Apply when

The product provides AI-generated analysis, recommendations, content, decisions, workflows, or automation through a hosted application.

## Mandatory questions

- What user outcome does the AI improve?
- What happens when the model is wrong, unavailable, manipulated, or uncertain?
- Which data reaches model providers, memory systems, logs, analytics, and support tools?
- Are outputs high-impact, regulated, or likely to be mistaken for professional advice?
- What actions can the AI take without human approval?
- How are model, prompt, retrieval, and policy changes evaluated?

## Baseline capabilities

- critical-journey testing;
- model and prompt evaluation;
- prompt-injection and data-exfiltration controls;
- provenance and uncertainty handling;
- privacy and retention review;
- authentication, authorization, and tenant isolation;
- monitoring, cost controls, fallback, and incident response;
- accessibility and clear user communication;
- domain-expert review for high-impact outputs.

## Selection guidance

Use Inspect AI for structured research-grade evaluations where suitable. Treat promptfoo as experimental until its open verification debts are closed. Apply OWASP GenAI guidance as a standard, not as proof that the implementation is secure.

## Launch blockers

Silent failure, fabricated certainty, uncontrolled external actions, missing tenant isolation, undisclosed sensitive-data transmission, no fallback, no reproducible evaluation, or outputs that create material harm without review.
