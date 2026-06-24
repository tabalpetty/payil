export const REQUIRED_FIELDS = [
  "sourceName",
  "authority",
  "sourceUrl",
  "accessDate"
];

export function normalizeInput(input = {}) {
  const normalized = {
    sourceName: clean(input.sourceName),
    sourceCode: clean(input.sourceCode),
    authority: clean(input.authority),
    sourceUrl: clean(input.sourceUrl),
    localSnapshotPath: clean(input.localSnapshotPath),
    accessDate: clean(input.accessDate),
    learnerProfile: clean(input.learnerProfile),
    successTarget: clean(input.successTarget),
    duration: clean(input.duration),
    questionCount: clean(input.questionCount),
    passingScore: clean(input.passingScore),
    formats: clean(input.formats),
    domainCount: clean(input.domainCount),
    taskCount: clean(input.taskCount),
    domains: normalizeLines(input.domains),
    knownConfusions: normalizeLines(input.knownConfusions),
    notes: clean(input.notes),
    reviewerDecision: clean(input.reviewerDecision) || "needs-review",
    reviewerNote: clean(input.reviewerNote),
    verification: input.verification || null
  };

  normalized.missingRequiredFields = REQUIRED_FIELDS.filter((field) => !normalized[field]);
  return normalized;
}

export function checkpointReadiness(input = {}) {
  const data = normalizeInput(input);
  const verificationStatus = data.verification?.status || "not-run";

  if (data.reviewerDecision === "rejected") {
    return {
      status: "rejected",
      reason: "Reviewer rejected this source. Do not extract or decompose."
    };
  }

  if (data.missingRequiredFields.length > 0) {
    return {
      status: "needs-review",
      reason: `Missing required fields: ${data.missingRequiredFields.join(", ")}.`
    };
  }

  if (!["verified", "needs-review"].includes(verificationStatus)) {
    return {
      status: "needs-review",
      reason: "Server-side source verification has not produced usable evidence."
    };
  }

  if (verificationStatus !== "verified") {
    return {
      status: "needs-review",
      reason: "Server-side verification needs reviewer judgment before extraction."
    };
  }

  if (data.reviewerDecision !== "approved") {
    return {
      status: "needs-review",
      reason: "Reviewer has not approved this source identity."
    };
  }

  return {
    status: "approved",
    reason: "Approved -2 source identity checkpoint. Ready for -1 source extraction."
  };
}

export function buildCheckpoint(input = {}) {
  const data = normalizeInput(input);
  const readiness = checkpointReadiness(data);
  const generatedAt = new Date().toISOString();

  return {
    schema: "curriculum-source-identity-checkpoint-v1",
    layer: "-2",
    status: readiness.status,
    statusReason: readiness.reason,
    generatedAt,
    intendedSource: {
      sourceName: data.sourceName,
      sourceCode: data.sourceCode,
      authority: data.authority,
      sourceUrl: data.sourceUrl,
      localSnapshotPath: data.localSnapshotPath,
      accessDate: data.accessDate,
      learnerProfile: data.learnerProfile,
      successTarget: data.successTarget
    },
    officialBaseline: {
      duration: data.duration,
      questionCount: data.questionCount,
      passingScore: data.passingScore,
      formats: data.formats,
      domainCount: data.domainCount,
      taskCount: data.taskCount,
      domains: data.domains
    },
    knownConfusions: data.knownConfusions,
    notes: data.notes,
    verification: data.verification,
    reviewer: {
      decision: data.reviewerDecision,
      note: data.reviewerNote
    },
    downstreamRule:
      "Do not run -1 source extraction or 0 source-to-decomposition coverage audit until this checkpoint is approved or accepted with documented risk."
  };
}

export function checkpointMarkdown(checkpoint) {
  const domains = checkpoint.officialBaseline.domains?.length
    ? checkpoint.officialBaseline.domains.map((domain) => `| ${escapeCell(domain)} |`).join("\n")
    : "| None recorded |";

  const knownConfusions = checkpoint.knownConfusions?.length
    ? checkpoint.knownConfusions.map((item) => `- ${item}`).join("\n")
    : "None recorded.";

  const verification = checkpoint.verification || {};

  return `# Source Identity Checkpoint

## Status

| Field | Value |
|---|---|
| Layer | ${checkpoint.layer} Source identity |
| Status | ${checkpoint.status} |
| Status reason | ${escapeCell(checkpoint.statusReason)} |
| Generated at | ${checkpoint.generatedAt} |
| Reviewer decision | ${checkpoint.reviewer.decision || "MISSING"} |

## Intended Source

| Field | Value |
|---|---|
| Exam or course name | ${escapeCell(checkpoint.intendedSource.sourceName || "MISSING")} |
| Code or version | ${escapeCell(checkpoint.intendedSource.sourceCode || "MISSING")} |
| Official publisher | ${escapeCell(checkpoint.intendedSource.authority || "MISSING")} |
| Official source URL | ${escapeCell(checkpoint.intendedSource.sourceUrl || "MISSING")} |
| Local snapshot path | ${escapeCell(checkpoint.intendedSource.localSnapshotPath || "MISSING")} |
| Source access date | ${escapeCell(checkpoint.intendedSource.accessDate || "MISSING")} |
| Intended learner / candidate | ${escapeCell(checkpoint.intendedSource.learnerProfile || "MISSING")} |
| Success target | ${escapeCell(checkpoint.intendedSource.successTarget || "MISSING")} |

## Official Baseline

| Field | Value |
|---|---|
| Duration | ${escapeCell(checkpoint.officialBaseline.duration || "MISSING")} |
| Question count | ${escapeCell(checkpoint.officialBaseline.questionCount || "MISSING")} |
| Passing score or standard | ${escapeCell(checkpoint.officialBaseline.passingScore || "MISSING")} |
| Question formats | ${escapeCell(checkpoint.officialBaseline.formats || "MISSING")} |
| Domain count | ${escapeCell(checkpoint.officialBaseline.domainCount || "MISSING")} |
| Task or objective count | ${escapeCell(checkpoint.officialBaseline.taskCount || "MISSING")} |

## Domains Or Sections

| Domain or section |
|---|
${domains}

## Verification Evidence

| Field | Value |
|---|---|
| Verification status | ${escapeCell(verification.status || "not-run")} |
| Checked at | ${escapeCell(verification.checkedAt || "not-run")} |
| Requested URL | ${escapeCell(verification.requestedUrl || "MISSING")} |
| Resolved URL | ${escapeCell(verification.resolvedUrl || "MISSING")} |
| HTTP status | ${escapeCell(verification.httpStatus || "MISSING")} |
| Content type | ${escapeCell(verification.contentType || "MISSING")} |
| SHA-256 | ${escapeCell(verification.sha256 || "MISSING")} |
| Page title | ${escapeCell(verification.pageTitle || "MISSING")} |
| Matched signals | ${escapeCell((verification.matchedSignals || []).join(", ") || "none")} |
| Missing signals | ${escapeCell((verification.missingSignals || []).join(", ") || "none")} |
| Notes | ${escapeCell((verification.notes || []).join("; ") || "none")} |

## Known Confusions Or Exclusions

${knownConfusions}

## Notes

${checkpoint.notes || "None."}

## Reviewer Note

${checkpoint.reviewer.note || "MISSING"}

## Downstream Rule

${checkpoint.downstreamRule}
`;
}

function clean(value) {
  return typeof value === "string" ? value.trim() : "";
}

function normalizeLines(value) {
  if (Array.isArray(value)) {
    return value.map((line) => clean(String(line))).filter(Boolean);
  }
  return clean(value)
    .split("\n")
    .map((line) => line.trim())
    .filter(Boolean);
}

function escapeCell(value) {
  return String(value).replaceAll("|", "\\|").replace(/\s+/g, " ").trim();
}
