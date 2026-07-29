# Playbook: AI Quality and Safety

## Purpose

Determine whether an AI feature is useful, grounded, robust, appropriately constrained, and safe for its users and decision impact.

## Inputs

Project assessment, model and provider configuration, prompts, tools, retrieval sources, memory, datasets, critical journeys, risk class, languages, and existing evaluations.

## Workflow

1. Define the user outcome and what the model must never do.
2. Separate deterministic logic, sourced facts, model inference, and autonomous action.
3. Build representative, edge, multilingual, adversarial, prompt-injection, abstention, and failure datasets.
4. Measure task success, factuality, source use, uncertainty, refusals, fairness, latency, cost, and recovery.
5. Review tool permissions, memory, data providers, output filters, model fallback, and human escalation.
6. Select evaluation and guardrail resources from the registry according to risk and compatibility.
7. Add CI gates for material regressions and production monitoring for drift and incidents.

## Outputs

AI system map, risk taxonomy, evaluation suite, baseline results, failure examples, selected resources, guardrail plan, escalation rules, and release verdict.

## Verification

Run fresh evaluations at pinned model and prompt versions; independently inspect high-impact samples; test provider failures, malformed inputs, injection, tool misuse, language paths, abstention, and recovery.

## Stop conditions

Stop before enabling high-impact autonomous action, processing new sensitive data, or claiming accuracy, fairness, legal validity, safety, or prediction performance unsupported by evidence.

## Human review

Domain experts must review high-impact datasets, scoring, legal or medical content, financial or trading outputs, safety decisions, protected-group risks, and production release criteria.
