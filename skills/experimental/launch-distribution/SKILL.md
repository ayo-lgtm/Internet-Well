# Skill: Launch Distribution Planner

Status: **experimental**

## Purpose
Turn a product launch objective into a verified, human-reviewable distribution plan using governed Internet-Well sources. The primary seed source is the pinned `Places To Post Your Startup` record; the skill must verify destinations before recommending or using them.

## Inputs
- product name and public URL, if already public;
- launch stage: private beta, public beta, launch, major update, open source, waitlist, or relaunch;
- target user segments and relevant geographies;
- product category and business model;
- available launch assets;
- budget and founder/operator capacity;
- regulated-claim, privacy, embargo, confidentiality, and brand constraints.

## Procedure
1. Define the launch objective and the audience that must see the product.
2. Read `registry/marketing/places-to-post-your-startup.md` and use its pinned upstream source only as a candidate generator.
3. Build a candidate set across communities, product directories, review/listing sites, startup databases, editorial channels, and relevant niche communities.
4. Verify every candidate against a current primary source before selection:
   - current URL and active status;
   - submission mechanism and account requirements;
   - free/paid status and any recurring charge;
   - audience/category fit;
   - geographic scope;
   - moderation/self-promotion rules;
   - disclosure, endorsement, and content restrictions;
   - required assets and copy limits;
   - expected operator effort;
   - privacy/data-sharing implications.
5. Reject destinations that are dead, deceptive, irrelevant, prohibit the proposed promotion, or create disproportionate legal/privacy risk.
6. Rank the surviving set by **fit, reach relevance, effort, cost, trust, and measurability**. Never rank by popularity alone.
7. Produce channel-specific copy requirements and asset requirements without posting anything.
8. Identify a small first-wave launch set and a second-wave expansion set.
9. Define measurement: referral source, qualified traffic, signup/activation, conversion, retained usage, and qualitative feedback.
10. Present the plan for human approval. External submissions remain separate state-changing actions.

## Outputs
Return:
- launch objective and audience;
- verified destination matrix;
- rejected candidates and reasons;
- first-wave and second-wave channel plan;
- required copy/assets;
- tracking plan;
- risks and platform-rule notes;
- explicit approval points;
- evidence date for each destination.

## Permission boundary

This skill may research and prepare a launch plan. It cannot create accounts, submit forms, post content, purchase placement, send messages, upload assets, disclose confidential information, or otherwise act on an external platform without separate explicit authorization.

## Human review

A person must approve the destination shortlist and each external submission or account action. Legal, privacy, or brand review is required where the launch includes regulated claims, endorsements, contests, comparative advertising, personal data, or protected marks.

## Prohibited shortcuts
- No bulk posting.
- No spam, astroturfing, fake reviews, fake engagement, sockpuppets, or undisclosed paid promotion.
- No automatic account creation or submission merely because a destination appears in the source list.
- No claim that a channel is "best" without evidence tied to the product and objective.
- No reuse of outdated submission requirements without revalidation.

## Verification
A successful run proves that each selected destination was independently rechecked and that no external submission occurred without authorization. Record failed or blocked destination checks rather than silently dropping them.

## Evaluation

Pass when every selected destination has current primary-source verification, the plan separates discovery from execution, rejected candidates are explained, measurement is defined, and external actions remain approval-gated. Fail when an upstream listing is treated as current approval, destination rules are not checked, or the workflow performs bulk or unauthorized posting.
