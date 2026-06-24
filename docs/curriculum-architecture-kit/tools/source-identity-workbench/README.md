# Source Identity Workbench

Layer `-2` confirms that a curriculum or exam-prep build is using the correct,
legitimate source before extraction (`-1`) or source-to-decomposition coverage
audit (`0`).

This tool follows the project trust posture:

- server-side verification is authoritative;
- the browser collects intent, shows evidence, and records human confirmation;
- local browser storage is transparent draft state only;
- no browser push, file-system, background-sync, or persistent-storage
  permission is requested in v1;
- the service worker caches only the app shell and non-sensitive static assets.

## Technology

| Layer | Choice |
|---|---|
| Hosting and edge compute | Google Cloud Run |
| Frontend SSR and UI | React + Next.js |
| Network and caching | Workbox-style service worker |
| Client storage | IndexedDB through Dexie.js |
| Push and real-time sync | Firebase later, not enabled in v1 |

## Local Development

```bash
npm install
npm run dev
```

Then open:

```text
http://localhost:3000
```

## Cloud Run

Build and run with the included `Dockerfile`. Cloud Run should set:

```text
PORT=8080
NODE_ENV=production
```

## What V1 Verifies

The user enters what they know first. `Exam or course name` and
`Vendor / official authority` are mandatory because discovery cannot be
meaningful without them. Code/version, source URL, learner profile, baseline
metadata, domains, and exclusions may be blank.

The server can then:

- suggest one or more official source candidates;
- let the UI show a dropdown when candidates are ambiguous;
- populate known fields from the selected candidate;
- fetch and verify the official URL; and
- supplement remaining fields from server-side evidence for user confirmation.

The server verification endpoint:

- fetches the official source URL from the server, avoiding browser CORS;
- records the resolved URL, HTTP status, content type, and SHA-256 checksum;
- extracts HTML page titles and visible text signals when the source is HTML;
- records PDF sources as checksumable but requiring downstream PDF extraction;
- compares user-provided name, code/version, authority, and learner profile
  against the fetched source text where possible;
- returns `verified`, `needs-review`, or `failed`.

The canonical checkpoint endpoint:

- recomputes readiness on the server;
- produces normalized JSON;
- produces Markdown suitable for committing into a pilot repo.

## Explicit Non-Goals For V1

- No client-side source authority.
- No browser-only verifier that claims approval from client fetches.
- No push notification permission.
- No local storage of official PDFs or extracted source text.
- No background sync.
