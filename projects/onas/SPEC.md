# ONAS — Product Spec v1

Status: draft for review by Dr Wale (founder and builder) · 2026-10-10
Launch market: Nigeria (Android first)
Companion documents: [`LEGAL-ISSUES.md`](LEGAL-ISSUES.md) (counsel register), [`assessment.json`](assessment.json) (machine-readable project assessment)

## 1. What ONAS is

A habit app built as a real-life RPG. Users complete real-world quests, their Hero levels up, and streaks unlock cosmetics. The long-term vision adds three money features (stakes, sponsored quests, a player marketplace). This spec deliberately ships the game **without money first**, proves retention, and adds each money feature only after counsel clears it in `LEGAL-ISSUES.md`.

## 2. Design references so far

There is no production codebase yet; `ayo-lgtm/ONAS` is an empty repository. Two design references exist:

- **Design A: first prototype (screen recording, 2026-10-10).** Dr Wale's first design, built on top of a template someone else made. It runs on Android but is a prototype, not the app. Treat its behavior and copy as a starting point, not as decisions already made.
- **Design B: Figma Make home screen** (React/Vite prototype). Brand board: ring symbol and ONAS wordmark, tagline "Healthy habits, brighter days", Iris Purple `#7C4DFF` (primary) and Pulse Teal `#00E0C6` (highlights). **Nova** (illustrated, curly hair, teal hoodie with the ONAS symbol) is the reference for the avatar art style. Only Home is designed; other tabs are placeholders.

### Design A, as observed

| Area | Observed state |
|---|---|
| Navigation | Five tabs: Hero, Quests, Earn, Social, Shop; settings gear on every screen |
| Hero | Illustrated starter Heroes ("Tide", "Nova"); level, XP bar (100 XP per level at L1), Today's Adventure card, Today 0/8, This week 0/3, Streak, Gems (labelled "Not cash") |
| Quests | 8 daily + 3 weekly; categories Health, Learning, Productivity, Mindfulness; 10–25 XP each; **all self-reported** |
| Achievements | First Quest, 7-Day Streak, Quest Explorer, Quest Champion; Founder and First Gift shown as unavailable |
| Earn | Explanatory only. Sponsored Quests, Brand Challenges, Creator Opportunities marked "not offered". No wallet, balance or cash-out |
| Social | Placeholder; no friends, chat, parties or gifts |
| Shop | No storefront; customization of starter looks only |
| Account | Email + password sign-in, verified email, display name, @username, optional profile picture (kept on device), change password, delete account |
| Storage | **Hero progress is device-only.** Clearing app data loses it; deleting the hosted account does not erase it |
| Legal & Privacy Center | Policy suite 1.0.0 effective 2026-10-09, ~24 policies tagged current / mixed / future; data requests by email to data@onas.io; public pages at onas.io not yet published |

### Issues to resolve before public launch

1. **Entity and jurisdiction.** The prototype's policy text (probably template boilerplate) states "ONAS is registered in California, United States" and "intended worldwide for adults 18+". The launch market is Nigeria. → `LEGAL-ISSUES.md` L0.
2. **Device-only progress.** Users lose streaks when they change phones, and no money feature can ever rely on device state. → Phase 1, item 1.
3. **Self-reported quests.** Acceptable for a no-money game; not acceptable as the basis for stakes. → Section 5.
4. **No selfie avatar yet.** The core differentiator is not built; the current profile photo is explicitly "not a playable Hero". → Phase 1, item 2, and L5.
5. **Policy URLs not live.** Google Play requires a reachable privacy policy URL before listing.
6. **"PLAY · GROW · EARN" tagline** appears on Earn and Shop while the app pays nothing. Counsel and Play review may read "Earn" as an earnings claim. → L7.
7. **18+ age gate** is stated in policy but was not seen in the recorded sign-up flow. Unverified.
8. **Navigation differs between designs.** A: Hero, Quests, Earn, Social, Shop. B: Home, Quests, Avatar, Social, Profile. Dr Wale to choose.
9. **Gems in Design B can be bought ("+"), earned from quests, and gifted to other users.** Purchasable value that moves between users falls under L4, not only Phase 2. Simplest fix: gifts are cosmetic items, or purchased Gems cannot be gifted.
10. **"ELEVATE TO EARN"** (Design B) raises the same L7 question as "PLAY · GROW · EARN".

### Open decisions for Dr Wale

- Stack for the production app (Section 4 proposes one) and whether any Design A code is reused.
- Which design is the visual target (B recommended) and the final tab structure.
- Rights to the template used for Design A and to the Hero and Nova art: who made them, and under what license or assignment.

## 3. Phase plan

Each phase has an exit gate. Do not start a money phase until its `LEGAL-ISSUES.md` rows are marked **Cleared** by counsel.

### Phase 0 — Design (in progress)
Design A prototype and Design B home screen exist. Remaining: pick the visual target, design the other core screens, set up the production repository.

### Phase 1 — Retention MVP (no money)
1. **Server-authoritative progress.** Move XP, quests, streaks and achievements to the backend with row-level access control; device keeps an offline cache that syncs. Required for phone changes and for every later phase.
2. **Selfie → Hero.** Upload a selfie, generate a stylized Hero server-side, store only the generated Hero by default and delete the source selfie after generation (retention period set in L5). Explicit, separate consent screen before upload. Visual style decision (Afrofuturist, anime, 3D cinematic) is a design task in this phase.
3. **Verification lite.** Optional evidence per quest: in-app timer for timed quests, Health Connect step count for walks, photo proof for selected quests. Still unscored — this phase just measures how many users will provide evidence.
4. **Streak protection.** One "rest day" token per week so a single miss does not end motivation.
5. **Reminders.** Local notifications at a user-chosen time; respect quiet hours.
6. **Hide or relabel unbuilt tabs.** Either hide Earn/Social/Shop or show a single "Coming later" card each, to shorten first-run reading.
7. **Publish policies** at onas.io/terms, /privacy, /delete-account; add an 18+ (or counsel-set) age gate at sign-up.
8. **Ship to Google Play internal → closed testing** in Nigeria.

**Exit gate:** Dr Wale sets numeric targets *before* testing starts for D1, D7 and D30 retention, median streak length, and percent of quests with evidence attached. Phase 2 starts only if the targets are met.

### Phase 2 — Cosmetics shop (first revenue, lowest regulatory weight)
Gems purchasable only via Google Play Billing, spendable only on cosmetics, never withdrawable or transferable. No user-to-user trading yet. Clears L7 and the Play policy row.

### Phase 3 — Commitment stakes
Only after L0, L1, L2, L6, L8 are cleared. Structure follows counsel's chosen model (pool redistribution vs. forfeit-to-charity vs. other). Funds held by a licensed payment partner, never in an ONAS-operated balance unless counsel clears it. Requires verification tier 2 (Section 5).

### Phase 4 — Sponsored quests / offerwall
Only after L3, L8 cleared and a real network has quoted Nigerian-traffic payouts. Fraud controls (device integrity, velocity limits, KYC before payout) ship in the same release.

### Phase 5 — Player marketplace
Only after L4 cleared. Items stay off-chain.

## 4. Proposed architecture (to confirm with Dr Wale)

- **Client:** new app in `ayo-lgtm/ONAS`, for example Expo (React Native); Android first. Server-side image generation keeps low-end devices fast.
- **Backend:** managed Postgres + auth + storage + server functions (for example Supabase), with row-level security on every user table. Keep the existing auth project if it already provides these.
- **AI avatar:** an image-generation provider contracted not to train on or retain user images; cross-border transfer basis per L5.
- **Payments (Phase 2):** Google Play Billing. **(Phase 3+):** a CBN-licensed payment service provider; ONAS stores references, never card or bank credentials.
- **Analytics:** privacy-respecting product analytics for the Phase 1 retention gate; no selfie or health data in analytics events.

## 5. Quest verification tiers

| Tier | Evidence | Allowed for |
|---|---|---|
| 0 | Self-report (current) | XP, cosmetics |
| 1 | Timer, Health Connect data, photo proof (unreviewed) | XP, streak bonuses |
| 2 | Tier 1 + automated checks (GPS geofence, duplicate-photo detection, sensor consistency) + random human review | Anything with money at stake |

Stakes must never be decided by Tier 0 evidence. The pool-redistribution model gives every participant a financial reason to cheat; Tier 2 is the price of that model.

## 6. Non-goals for v1

Real-money features of any kind, user-to-user trading, chat or friend graphs, creator content, crypto/NFT items, iOS parity.

## 7. Risks

- Retention may not hold without money; Phase 1 exists to find that out cheaply.
- Selfie processing is sensitive personal data; a breach would be severe. Minimize retention.
- AI coding agents can build most of this, but anything touching money or selfies needs an independent security review before release.
- Regulatory position on stakes is unsettled at state level; see L1.
