# Storeless App / PWA Production Framework

This guide is the Internet Well decision and implementation path for apps that should feel installed on phones without requiring App Store or Google Play distribution.

## Quick navigation

1. [Choose distribution](#1-choose-distribution)
2. [Make the web app installable](#2-make-the-web-app-installable)
3. [Guide iPhone users to Add to Home Screen](#3-guide-iphone-users-to-add-to-home-screen)
4. [Enable Web Push notifications](#4-enable-web-push-notifications)
5. [Add badges and deep links](#5-badges-and-deep-links)
6. [Handle iOS limitations with guided fallbacks](#6-ios-capability-and-guided-fallback-layer)
7. [Offline, updates and resilience](#7-offline-updates-and-resilience)
8. [Open/free resources](#8-openfree-resources)
9. [Production verification](#9-production-verification-checklist)
10. [Agent selection rules](#10-agent-rules)

## 1. Choose distribution

Default decision order when requirements permit:

**PWA / storeless web app → PWA plus native wrapper → fully native app.**

Choose a PWA first when the product primarily needs web UI, authentication, APIs, camera/microphone/file access supported by browsers, location, offline caching, installable Home Screen presence, and Web Push.

Escalate toward native only when measured requirements need capabilities the web platform cannot adequately provide, such as deep OS integrations, extensive background execution, platform-specific health/device frameworks, advanced Bluetooth/NFC behavior, widgets/Live Activities, or other native-only APIs.

Do not submit to an app store merely to obtain an icon or notifications; installable web apps can provide those capabilities on supported platforms.

## 2. Make the web app installable

Minimum production contract:

- HTTPS in production.
- Valid Web App Manifest linked from the application.
- Stable app `id`, `name`, `short_name`, `start_url`, appropriate `scope`, `display: standalone` (or a deliberately chosen alternative), theme/background metadata, and suitable icons.
- Service worker registered at the correct scope.
- Mobile-responsive UI including iPhone safe areas/notches and touch targets.
- App routes must survive direct/deep navigation and refresh.
- Authentication/session persistence must be tested in installed mode, not only a normal browser tab.
- Icons and launch behavior must be tested on actual iOS and Android devices.

A manifest is not enough by itself. Internet Well should treat installation as a user workflow with success/failure states.

## 3. Guide iPhone users to Add to Home Screen

On iPhone/iPad, detect platform and display mode. Never make the user understand terms such as “PWA”, “service worker”, or “standalone display mode”. Explain the benefit and the next supported action.

Recommended UX state machine:

1. User opens the website.
2. App determines whether it is already running as an installed/Home Screen app.
3. If installation materially improves the requested capability, show a contextual call to action such as **Get the app on your Home Screen**.
4. On iPhone when a browser cannot expose a programmatic install prompt, show concise visual steps using the current supported browser flow: open the Share menu and choose **Add to Home Screen**, then open the new app icon.
5. Preserve the user's route/work so installation does not make them restart onboarding.
6. Once launched from the Home Screen, detect the installed state and continue setup automatically.

Do not repeatedly nag users who dismiss installation. Store a dismissal/cooldown state and surface installation again only when context makes it useful (for example, when the user asks for notifications).

## 4. Enable Web Push notifications

For standards-based Web Push, use:

**Product event → application backend/worker → Web Push sender → browser push service → service worker → visible notification → deep-linked application route.**

For iPhone/iPad, Apple supports Web Push for Home Screen web apps on iOS/iPadOS 16.4+. Apple documents Push API, Notifications API, Badging API and Service Worker support for this flow, and states that joining the Apple Developer Program is not required for Web Push.

Required implementation:

- Ask for notification permission only after a meaningful user gesture such as **Enable notifications**. Do not trigger the browser permission prompt on first page load.
- Register the service worker and create a `PushSubscription`.
- Associate subscription endpoint + encryption keys with the authenticated account/device in the backend.
- Keep VAPID private keys server-side only. Public key may be delivered to the client.
- Send pushes from a trusted server/worker using a standards-compliant Web Push library.
- Service worker handles `push` and immediately presents a visible notification where platform policy requires it.
- Handle `notificationclick` and route the user to the relevant in-app destination.
- Expire/remove subscriptions when push services return permanent invalid/unsubscribed responses.
- Support multiple subscriptions per account; a user can have multiple browsers/devices.
- Provide notification preferences by category where the product has multiple notification types.
- Rate-limit and deduplicate notifications to prevent spam.
- Do not put secrets or unnecessary sensitive information in notification payloads or lock-screen text.

Suggested user flow on iPhone:

**Want notifications? → Is this running from Home Screen? → No: guide Add to Home Screen → user launches installed app → show Enable notifications → user taps → request permission → save subscription → send a test notification → show success.**

## 5. Badges and deep links

Where supported, use the Badging API to reflect useful unread/action counts. Badge state should be derived from application state rather than becoming the only source of truth.

Notification payloads should contain an allow-listed application route or semantic object identifier. On click, the service worker focuses an existing app window when practical or opens the intended route. Validate destinations; do not accept arbitrary external URLs from untrusted payload data.

## 6. iOS capability and guided fallback layer

The objective is **supported fallback, not bypassing platform security restrictions**.

Create a small capability adapter that evaluates:

- platform/browser family;
- installed/standalone state;
- service-worker availability and registration state;
- Push API and Notifications API support;
- notification permission (`default`, `granted`, `denied`);
- Badging API support;
- online/offline state;
- camera, microphone, geolocation, share, clipboard and file capabilities when the product needs them;
- whether a requested feature depends on background execution that iOS may suspend.

Then map every unsupported state to a user-safe fallback. Examples:

| Requested capability | Preferred path | Guided fallback |
| --- | --- | --- |
| iPhone push | Installed Home Screen web app + Web Push | Guide Add to Home Screen, then resume notification setup |
| Notification permission denied | Explain how the feature is affected | Point to the relevant system/site notification setting; never repeatedly prompt |
| Background task cannot be relied on | Server-side job/queue | Notify user when server work completes instead of requiring the page to remain alive |
| Share | Web Share API | Copy/share-link UI |
| Camera/file capture | Browser media/file APIs | Standard file picker/upload |
| Offline action | Queue locally only when safe | Clearly show offline state and retry/reconcile when connected |
| Unsupported badge | In-app unread state | Do not block notification functionality |

Do not use hacks to defeat iOS lifecycle, permission, tracking, sandbox, or security restrictions. If the product truly requires an unavailable capability, the distribution decision should escalate to a native wrapper/native app rather than disguising an unsupported implementation.

## 7. Offline, updates and resilience

Service-worker caching must be deliberate:

- precache only the application shell/assets that make sense;
- define runtime caching per resource type;
- never casually cache authenticated/private API responses in a shared cache;
- provide an offline state rather than presenting stale data as current;
- version caches and delete obsolete caches;
- make app updates discoverable and avoid trapping users on an old broken service worker;
- use server-side queues for durable work rather than assuming a mobile browser can execute indefinitely in the background;
- make notification sending idempotent/retry-safe.

## 8. Open/free resources

Internet Well should treat these as resources, not mandatory dependencies.

### PWABuilder — `pwa-builder/PWABuilder`

MIT-licensed open-source PWA tooling. Useful for PWA validation, install experience, manifests, starter/reference implementations, and cross-platform guidance. The maintained monorepo includes the `<pwa-install>` component; do not point new implementations at the archived standalone `pwa-install` repository.

Use when: installation UX, PWA validation or starter/reference code saves implementation effort.

### PWABuilder PWA Starter — `pwa-builder/pwa-starter`

Open PWA starter/reference with service-worker/installability patterns. Use as a reference or starter for greenfield applications, not as a reason to rewrite an existing framework application.

### Serwist — `serwist/serwist`

Open-source service-worker/PWA tooling, particularly useful for modern JavaScript/Next.js applications that need controlled precaching/runtime caching and service-worker integration. Verify current package/license/version at adoption time.

### Web Push libraries — `web-push-libs/web-push` and language siblings

Open-source standards-based server libraries for encrypted Web Push and VAPID. For Node.js, evaluate `web-push-libs/web-push`; the organization also maintains or links implementations for other languages. Prefer the library matching the existing backend instead of adding a notification SaaS solely to send Web Push.

### Existing application backend

For projects already using Supabase/Postgres, store push subscriptions against authenticated users with RLS/server authorization and trigger notification jobs from the existing backend/worker. Do not introduce a new database merely for push subscriptions.

### Optional orchestration products

Notification workflow platforms such as Novu or ntfy may be evaluated when the product actually needs multi-channel orchestration or self-hosted topic-style notification infrastructure. They are not required for a basic PWA Web Push implementation. Recheck license, maintenance, iOS delivery architecture and operational fit before adoption.

## 9. Production verification checklist

A storeless app is not production-ready until the applicable checks pass:

- [ ] HTTPS production origin.
- [ ] Manifest validates and icons render correctly.
- [ ] Add-to-Home-Screen flow tested on a current physical iPhone/iPad.
- [ ] Installed app launches standalone and preserves auth/session.
- [ ] Deep links/routes work after cold launch.
- [ ] Service worker installs, updates and recovers from a failed/old version.
- [ ] Offline UX is explicit and does not misrepresent stale data.
- [ ] Notification permission is requested only from a meaningful user action.
- [ ] iPhone Home Screen prerequisite is detected and explained before requesting push.
- [ ] Push subscription is stored server-side with correct user/device ownership.
- [ ] VAPID private key is never exposed client-side or committed.
- [ ] Test push arrives while app is foregrounded/backgrounded/closed as supported.
- [ ] Notification click opens the intended route.
- [ ] Invalid subscriptions are removed.
- [ ] Multiple-device behavior works.
- [ ] Notification preferences/unsubscribe work.
- [ ] Badge behavior works or degrades cleanly.
- [ ] Sensitive data is not unnecessarily exposed on the lock screen.
- [ ] Android/desktop behavior is tested when those platforms are supported.
- [ ] Accessibility and reduced-motion/text-size behavior remain usable in installed mode.

## 10. Agent rules

When an Internet Well agent sees requirements such as **mobile web app**, **install on phone**, **Home Screen app**, **avoid App Store**, **avoid Google Play**, **PWA**, **web push**, or **iPhone notifications**, it should evaluate this framework before recommending native development.

The agent should:

1. inventory required device/OS capabilities;
2. choose PWA-first when all critical requirements have reliable web implementations;
3. reuse the project's existing framework/backend before adding services;
4. implement installability and a user-facing install flow, not just a manifest;
5. implement capability detection and guided fallbacks for iOS;
6. use standards-based Web Push and a maintained open library where appropriate;
7. keep notification delivery server-side and secrets out of clients;
8. test on physical iOS hardware and installed/Home Screen mode;
9. escalate to wrapper/native only for a documented capability gap;
10. never claim a PWA can bypass iOS security, permission, lifecycle or hardware restrictions.

### Definition of done

“PWA enabled” does not mean a manifest exists. Done means a normal user can discover installation, add the app to the Home Screen, reopen it without losing context, enable notifications through a clear user-initiated flow, receive a real notification, tap it into the correct screen, understand any unsupported iPhone capability, and continue through a safe fallback without developer knowledge.
