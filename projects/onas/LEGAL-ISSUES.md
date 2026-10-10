# ONAS — Legal Issues Register

Status: open · prepared 2026-10-10 for review by the founder (licensed Nigerian counsel)
Scope: Nigeria launch, Android first. This register describes product flows precisely and lists the questions they raise. It contains no legal conclusions; the **Counsel conclusion** fields are for counsel to complete.

Background facts gathered (verify before relying on them):
- Supreme Court of Nigeria (2024) held lotteries and gaming to be residual matters for states; NLRC's remit is now limited to the FCT. The Central Gaming Bill had not received assent as of the latest source found; Lagos has challenged it.
- Google Play lists Nigeria as a market for licensed real-money gambling apps; a May 2025 report says Play now recognizes only Lagos State-issued licenses.
- NDPA 2023 and GAID 2025 treat biometric data as sensitive personal data.
- PayPal receiving for Nigerian users launched January 2026 via Paga.

Status values: **Open** · **In analysis** · **Cleared** (feature may be built as described) · **Cleared with conditions** · **Blocked** (redesign required).

---

## L0 — Entity, governing law, and in-app statements
**Status:** Open · **Blocks:** public launch

**Facts:** The in-app policy suite (v1.0.0, effective 2026-10-09) states "ONAS is registered in California, United States" and "intended worldwide for adults 18+, California registration". The launch market is Nigeria, and the founder is in Nigeria.

**Questions:**
1. Which entity operates ONAS for Nigerian users (CAC-registered Nigerian company, US parent, or both)?
2. Governing law and dispute forum for Nigerian users.
3. Do the in-app policies need to be reissued before Play listing to reflect the operating entity and NDPA?
4. Should "worldwide" availability be narrowed to Nigeria until each market is reviewed?

**Counsel conclusion:**

**Build impact:** Policy text, store listing entity, payment partner onboarding (partners contract with the operating entity).

---

## L1 — Commitment stakes ("cash betting pool")
**Status:** Open · **Blocks:** Phase 3

**Flow (as envisioned):**
1. User pays an entry stake (for example ₦1,000) to join a 7-day routine.
2. Stake is held for 7 days.
3. Users who complete the routine receive their stake back plus a share of the stakes forfeited by users who did not complete.
4. ONAS deducts a platform fee from forfeited stakes.
5. Completion is decided by quest evidence (see SPEC §5).

**Alternative structures for comparison:**
- **A. Pool redistribution** (as above).
- **B. Forfeit-to-charity:** forfeited stakes go to a named charity; completers receive their stake back plus non-cash rewards. ONAS fee is a fixed entry fee, not a cut of forfeits.
- **C. Forfeit-to-platform:** forfeited stakes become ONAS revenue; completers receive their stake back plus non-cash rewards.
- **D. Sponsor-funded prize:** no user stake; a sponsor funds prizes for completers (see also L3).

**Questions:**
1. Under Lagos law (and any other target state), does A, B, C or D constitute a lottery, betting, gaming, or a promotional competition?
2. Is the outcome "skill" (the user's own effort) or "chance" for these purposes, and does that distinction matter under the applicable state law?
3. If licensing is required, which licence class, from which authority, and does reciprocity extend it to other states?
4. Does the platform fee structure change the classification?
5. Consumer-protection obligations (FCCPC) for the terms, refund rules, and dispute process when evidence is contested.

**Counsel conclusion:**

**Build impact:** Determines whether ONAS needs an LSLGA licence, which structure is built, Play listing category, and whether geo-fencing to specific states is required.

---

## L2 — Custody of user funds
**Status:** Open · **Blocks:** Phase 3, Phase 4

**Flow:** Stakes (L1) and sponsored-quest earnings (L3) would sit somewhere between collection and payout.

**Questions:**
1. May ONAS hold user balances itself, or must all funds sit with a CBN-licensed partner?
2. Would an in-app balance that can be withdrawn constitute e-money or a payment service requiring a CBN licence?
3. Required KYC tier (BVN/NIN) at deposit vs. at withdrawal.
4. Treatment of unclaimed balances and dormant accounts.

**Counsel conclusion:**

**Build impact:** Whether ONAS builds a wallet ledger or only stores references to a licensed partner's balances.

---

## L3 — Sponsored quests and offerwall payouts
**Status:** Open · **Blocks:** Phase 4

**Flow:**
1. Advertiser or offerwall network pays ONAS for a user completing a sponsored task (survey, app trial).
2. ONAS credits the user a share.
3. User either withdraws (bank transfer, mobile wallet, or PayPal via Paga) or uses the credit as a free stake entry (L1).

**Questions:**
1. Is a user paid for sponsored tasks an independent contractor, a promotion participant, or something else, and what follows for tax and consumer law?
2. Disclosure and advertising-standards obligations for sponsored content (ARCON and related rules).
3. Does using sponsored credit as a stake entry change the classification of L1 (for example, creating a free-entry route)?
4. Restrictions on minors and on data collected by third-party survey providers.

**Counsel conclusion:**

**Build impact:** Payout flow, KYC trigger point, disclosure copy, whether credit can enter stakes.

---

## L4 — Player marketplace for digital items
**Status:** Open · **Blocks:** Phase 5

**Flow:** Users earn rare cosmetics through streaks and sell them to other users; ONAS takes a fee per trade. Items are database records, not blockchain tokens.

**Questions:**
1. If proceeds can be withdrawn as cash, does the marketplace trigger payment-service or money-transmission regulation?
2. Could tradeable items be "digital assets" under the Investments and Securities Act 2025 even if off-chain?
3. Consumer-protection position on refunds and on items that lose value.
4. Does Google Play's billing policy require Play Billing for item purchases between users?

**Counsel conclusion:**

**Build impact:** Whether proceeds are cash-withdrawable or Gems-only, and whether the marketplace ships at all.

---

## L5 — Selfies and AI avatar generation
**Status:** Open · **Blocks:** Phase 1 item 2

**Flow:**
1. User uploads a selfie after a dedicated consent screen.
2. Selfie is sent to an AI image provider (likely outside Nigeria) that returns a stylized Hero.
3. ONAS stores the generated Hero; the source selfie is deleted after N days (N to be set).
4. No face recognition, matching, or identity verification is performed on the selfie.

**Questions:**
1. Is a selfie used only for stylization "biometric data" under NDPA/GAID when no biometric template or identification is performed?
2. Required lawful basis and consent wording; whether a DPIA is mandatory before launch.
3. NDPC registration tier and Compliance Audit Return obligations at ONAS's expected scale.
4. Cross-border transfer basis for sending selfies to a foreign provider; required contract terms (no training, no retention, deletion SLA).
5. Retention period for source selfies and for generated Heroes after account deletion.

**Counsel conclusion:**

**Build impact:** Consent screen copy, retention timers, provider selection, DPIA as a release gate.

---

## L6 — Age restrictions
**Status:** Open · **Blocks:** public launch (and Phase 3 strictly)

**Facts:** Policy states 18+. No age gate was seen in the recorded sign-up flow.

**Questions:**
1. Minimum age for the no-money app vs. for any money feature.
2. Required strength of age verification for money features (self-declaration vs. BVN/NIN-based).
3. Obligations under the Child's Rights Act and NDPA for any users under 18.

**Counsel conclusion:**

**Build impact:** Sign-up flow, KYC sequencing.

---

## L7 — Marketing claims and store policy
**Status:** Open · **Blocks:** Play listing

**Facts:** The tagline "PLAY · GROW · EARN" appears in-app while the app pays nothing. Phase 2 sells cosmetics via Play Billing.

**Questions:**
1. Is "Earn" an earnings claim under consumer-protection and advertising rules while no cash rewards exist?
2. Required disclosures for virtual currency (Gems) purchases, including that Gems have no cash value.
3. Any Nigerian rules on in-app purchases by consumers (refunds, pricing in naira, VAT).

**Counsel conclusion:**

**Build impact:** Tagline, store listing copy, shop disclosures.

---

## L8 — Tax on user payouts and platform revenue
**Status:** Open · **Blocks:** Phase 3, Phase 4

**Questions:**
1. Withholding or reporting obligations when ONAS pays users (stake winnings, sponsored-task earnings, marketplace proceeds).
2. VAT on the platform fee, cosmetics sales, and marketplace fees.
3. Any gaming-specific tax if L1 is classified as gaming.

**Counsel conclusion:**

**Build impact:** Payout records, tax fields collected at KYC, receipts.

---

## Sign-off

| Item | Status | Counsel | Date |
|---|---|---|---|
| L0 | Open | | |
| L1 | Open | | |
| L2 | Open | | |
| L3 | Open | | |
| L4 | Open | | |
| L5 | Open | | |
| L6 | Open | | |
| L7 | Open | | |
| L8 | Open | | |

Recommended outside input despite in-house counsel: a gaming-licensing specialist (or informal LSLGA engagement) on L1, and an independent technical security review before any money or selfie feature ships.
