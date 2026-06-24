# Decision 0008: Source Identity Workbench Architecture

## Status

Accepted on June 23, 2026.

## Context

The project identified upstream layers before exam-prep production:

```text
-2 source identity -> -1 source extraction -> 0 source-to-decomposition coverage
```

Layer `-2` confirms that the curriculum is being built from the correct,
legitimate official source before extraction or decomposition. A future
interactive workbench should collect user intent, verify the official source,
supplement missing details, and produce an auditable source identity
checkpoint.

The project philosophy is to keep functionality away from the browser where
possible and avoid unnecessary browser permissions. A cautious user should not
be surprised by a curriculum tool asking for push, file-system, background
sync, persistent-storage, or clipboard permissions without a clear action.

## Decision

Use this architecture for the Source Identity Workbench PWA:

| Layer | Technology | Use |
|---|---|---|
| Hosting and edge compute | Google Cloud Run | Run the Next.js app and trusted source-verification APIs. |
| Frontend SSR and UI | React + Next.js | Provide the guided checkpoint workflow and reviewer confirmation UI. |
| Network and caching | Workbox | Cache only the app shell and non-sensitive static assets by default. |
| Client storage | IndexedDB with Dexie.js | Store minimal transparent draft state, not authoritative source truth. |
| Push and real-time sync | Firebase | Optional future layer for async job completion or cross-session sync; do not request push permission in v1. |

The browser is not the authority for source verification. Authoritative work
belongs on the server:

- fetch official source pages or PDFs;
- resolve redirects and record final URLs;
- compute source snapshot checksums;
- extract official title, code, version, domains, tasks, skills, dates, and
  baseline metadata;
- compare user-supplied claims against official evidence;
- generate the canonical source identity checkpoint;
- persist verification evidence and audit logs.

The browser should:

- collect the user's intended source identity;
- show server-produced evidence and differences;
- request human approval, rejection, or follow-up;
- allow explicit export or download of the checkpoint;
- hold only small, transparent draft state locally.

## Permission Policy

Default v1 behavior:

- no browser push notifications;
- no File System Access API;
- no background sync permission;
- no silent persistent-storage prompt;
- no clipboard access except after an explicit copy action;
- no storage of official PDFs, extracted source text, or sensitive evidence in
  IndexedDB by default;
- no service-worker caching beyond app shell and non-sensitive static assets.

Use in-app polling or server-sent events for progress before adding Firebase
push. Add Firebase push or real-time sync only when async verification jobs or
multi-device collaboration make the permission cost worthwhile.

## Consequences

- The PWA remains installable and useful without making the browser the trust
  anchor.
- Source verification can bypass browser CORS limitations through Cloud Run.
- The project can keep local/offline draft convenience while preserving a
  server-generated canonical checkpoint.
- Future implementation should not commit a browser-only verifier that claims
  source approval from client-side fetches alone.

## Implementation

V1 is implemented at:

`docs/curriculum-architecture-kit/tools/source-identity-workbench/`

It includes a Next.js UI, server-side source verification endpoint, canonical
checkpoint endpoint, Workbox-style app-shell service worker, Dexie-backed local
draft storage, Dockerfile for Cloud Run, and package-level PostCSS override for
the audited dependency tree.
