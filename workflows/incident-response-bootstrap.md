# Workflow: Incident Response Bootstrap (solo founder)

Minimal IR capability before launch — adapted from the PagerDuty
Incident Response documentation
([record](../registry/operations/pagerduty-incident-response.md)), scaled
to one person. Do this once; drill it quarterly.

1. **Severity definitions** (write them down, 3 levels are enough):
   SEV1 = product down or data at risk; SEV2 = major feature broken;
   SEV3 = degraded/cosmetic. Pre-decide what each level interrupts
   (SEV1: everything, including sleep; SEV3: next workday).
2. **Detection**: alerting from Prometheus rules
   ([record](../registry/operations/prometheus.md)) and external checks +
   public status page via Uptime Kuma
   ([record](../registry/operations/uptime-kuma.md)) hosted **off** your
   production infrastructure.
3. **Communication template** (pre-written): what happened, impact, what
   we're doing, next update time. Post to the status page; update on a
   fixed cadence even when there's nothing new.
4. **During an incident**: stabilize first, root-cause later; keep a
   timestamped scratch log (it becomes the postmortem timeline); never
   debug on the only copy of data — snapshot/backup first (restic:
   [record](../registry/operations/restic.md)).
5. **Blameless postmortem** within a week for SEV1/SEV2: timeline,
   contributing causes, what detection missed, 1–3 concrete follow-ups
   with dates. Store in-repo next to ADRs.
6. **Agent role**: agents may draft timelines from logs, prepare comms
   drafts, and open follow-up issues. Declaring/resolving incidents and
   all external communication are human actions.
