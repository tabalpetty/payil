import crypto from "node:crypto";

const MAX_BYTES = 5_000_000;

const SOURCE_CATALOG = [
  {
    id: "aws-aip-c01",
    sourceName: "AWS Certified Generative AI Developer - Professional",
    sourceCode: "AIP-C01",
    authority: "AWS",
    sourceUrl: "https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01.html",
    learnerProfile: "GenAI developer",
    successTarget: "Exam-ready AIP-C01 study program",
    duration: "180 minutes",
    questionCount: "75 total; 65 scored; 10 unscored",
    passingScore: "750",
    formats: "Multiple choice; multiple response",
    domainCount: "5",
    domains: [
      "Domain 1: Foundation Model Integration, Data Management, and Compliance - 31%",
      "Domain 2: Implementation and Integration - 26%",
      "Domain 3: AI Safety, Security, and Governance - 20%",
      "Domain 4: Operational Efficiency and Optimization for GenAI Applications - 12%",
      "Domain 5: Testing, Validation, and Troubleshooting - 11%"
    ],
    knownConfusions: [
      "Do not use AIF-C01 / AWS Certified AI Practitioner as the target source."
    ]
  },
  {
    id: "aws-aif-c01",
    sourceName: "AWS Certified AI Practitioner",
    sourceCode: "AIF-C01",
    authority: "AWS",
    sourceUrl: "https://docs.aws.amazon.com/aws-certification/latest/userguide/aif-c01.html",
    learnerProfile: "AI practitioner",
    successTarget: "Exam-ready AIF-C01 study program",
    knownConfusions: [
      "This is not the AIP-C01 Professional exam."
    ]
  }
];

export function discoverSourceCandidates(input = {}) {
  const sourceName = clean(input.sourceName).toLowerCase();
  const sourceCode = clean(input.sourceCode).toLowerCase();
  const authority = clean(input.authority).toLowerCase();

  if (!sourceName || !authority) {
    return {
      status: "needs-input",
      required: ["sourceName", "authority"],
      candidates: [],
      message: "Exam/course name and vendor/authority are required before discovery."
    };
  }

  const candidates = SOURCE_CATALOG
    .map((candidate) => {
      const candidateName = candidate.sourceName.toLowerCase();
      const candidateCode = candidate.sourceCode.toLowerCase();
      const candidateAuthority = candidate.authority.toLowerCase();
      let score = 0;

      if (candidateAuthority === authority) score += 40;
      if (sourceCode && candidateCode === sourceCode) score += 80;
      if (sourceCode && candidateCode.includes(sourceCode)) score += 30;
      for (const token of significantTokens(sourceName)) {
        if (candidateName.includes(token)) score += 8;
      }
      if (candidateName.includes(sourceName)) score += 30;

      return { ...candidate, confidence: Math.min(score, 100) };
    })
    .filter((candidate) => candidate.confidence >= 40)
    .sort((a, b) => b.confidence - a.confidence);

  return {
    status: candidates.length ? "candidates-found" : "needs-review",
    required: [],
    candidates,
    message: candidates.length
      ? "Select the matching official source candidate, then run server verification."
      : "No catalog candidate matched. Enter the official URL manually or add a verifier integration."
  };
}

export async function verifyOfficialSource(input = {}) {
  const sourceUrl = clean(input.sourceUrl);
  const checkedAt = new Date().toISOString();

  if (!sourceUrl) {
    return {
      status: "failed",
      checkedAt,
      requestedUrl: "",
      error: "Official source URL is required."
    };
  }

  let parsedUrl;
  try {
    parsedUrl = new URL(sourceUrl);
  } catch {
    return {
      status: "failed",
      checkedAt,
      requestedUrl: sourceUrl,
      error: "Official source URL is not a valid URL."
    };
  }

  if (!["https:", "http:"].includes(parsedUrl.protocol)) {
    return {
      status: "failed",
      checkedAt,
      requestedUrl: sourceUrl,
      error: "Official source URL must use http or https."
    };
  }

  try {
    const response = await fetch(parsedUrl, {
      redirect: "follow",
      headers: {
        "user-agent": "payil-source-identity-workbench/0.1"
      }
    });

    const contentType = response.headers.get("content-type") || "";
    const body = Buffer.from(await response.arrayBuffer());
    const limitedBody = body.subarray(0, MAX_BYTES);
    const sha256 = crypto.createHash("sha256").update(body).digest("hex");
    const text = isTextLike(contentType) ? limitedBody.toString("utf8") : "";
    const visibleText = text ? htmlToVisibleText(text) : "";
    const pageTitle = text ? extractTitle(text) : "";
    const supplements = extractSupplements(visibleText, pageTitle, input);
    const signals = sourceSignals(input);
    const matchedSignals = [];
    const missingSignals = [];

    for (const signal of signals) {
      const haystack = `${visibleText}\n${response.url}`.toLowerCase();
      if (haystack.includes(signal.value.toLowerCase())) {
        matchedSignals.push(signal.label);
      } else {
        missingSignals.push(signal.label);
      }
    }

    const notes = [];
    if (body.length > MAX_BYTES) {
      notes.push(`Only first ${MAX_BYTES} bytes inspected for text signals; checksum covers full response.`);
    }
    if (contentType.toLowerCase().includes("pdf")) {
      notes.push("PDF source fetched and checksummed; detailed PDF text extraction belongs to Layer -1.");
    }
    if (!isTextLike(contentType)) {
      notes.push("Non-text source fetched; signal matching is limited to URL and metadata.");
    }

    let status = "verified";
    if (!response.ok) status = "failed";
    else if (missingSignals.length > 0 || notes.some((note) => note.includes("Non-text") || note.includes("PDF"))) {
      status = "needs-review";
    }

    return {
      status,
      checkedAt,
      requestedUrl: sourceUrl,
      resolvedUrl: response.url,
      httpStatus: `${response.status} ${response.statusText}`.trim(),
      contentType,
      byteLength: body.length,
      sha256,
      pageTitle,
      supplements,
      matchedSignals,
      missingSignals,
      notes,
      error: response.ok ? "" : `HTTP request failed with status ${response.status}.`
    };
  } catch (error) {
    return {
      status: "failed",
      checkedAt,
      requestedUrl: sourceUrl,
      error: error instanceof Error ? error.message : "Unknown fetch error."
    };
  }
}

function sourceSignals(input) {
  return [
    ["source name", input.sourceName],
    ["source code/version", input.sourceCode],
    ["authority", input.authority],
    ["learner profile", input.learnerProfile]
  ]
    .map(([label, value]) => ({ label, value: clean(value) }))
    .filter((signal) => signal.value);
}

function extractSupplements(visibleText, pageTitle, input) {
  const joined = `${pageTitle}\n${visibleText}`;
  const supplements = {};
  const codeMatch = joined.match(/\b[A-Z]{2,4}-C\d{2}\b/);
  const durationMatch = joined.match(/(\d{2,3})\s+minutes/i);
  const passingScoreMatch = joined.match(/(?:passing score|minimum passing score)[^\d]*(\d{3,4})/i);
  const questionCountMatch = joined.match(/(\d{2,3})\s+(?:questions|question exam)/i);
  const scoredMatch = joined.match(/(\d{2,3})\s+scored questions/i);
  const unscoredMatch = joined.match(/(\d{1,3})\s+unscored questions/i);
  const domains = extractDomains(joined);

  if (pageTitle) supplements.sourceName = pageTitle.replace(/\s+-\s+AWS Certified.*$/i, "").trim();
  if (codeMatch) supplements.sourceCode = codeMatch[0];
  if (durationMatch) supplements.duration = `${durationMatch[1]} minutes`;
  if (passingScoreMatch) supplements.passingScore = passingScoreMatch[1];
  if (questionCountMatch) {
    supplements.questionCount = questionCountMatch[1];
    if (scoredMatch && unscoredMatch) {
      supplements.questionCount = `${questionCountMatch[1]} total; ${scoredMatch[1]} scored; ${unscoredMatch[1]} unscored`;
    }
  }
  if (/multiple choice/i.test(joined) && /multiple response/i.test(joined)) {
    supplements.formats = "Multiple choice; multiple response";
  }
  if (domains.length) {
    supplements.domains = domains;
    supplements.domainCount = String(domains.length);
  }

  const catalogMatch = SOURCE_CATALOG.find((candidate) => {
    return (
      clean(input.sourceCode).toLowerCase() === candidate.sourceCode.toLowerCase() ||
      clean(input.sourceUrl) === candidate.sourceUrl
    );
  });
  if (catalogMatch) {
    for (const key of ["learnerProfile", "successTarget", "duration", "questionCount", "passingScore", "formats", "domainCount"]) {
      if (catalogMatch[key]) supplements[key] = catalogMatch[key];
    }
    if (catalogMatch.domains) supplements.domains = catalogMatch.domains;
    if (catalogMatch.knownConfusions) supplements.knownConfusions = catalogMatch.knownConfusions;
  }

  return supplements;
}

function extractDomains(text) {
  const domains = [];
  const pattern = /Domain\s+\d+:\s+([^0-9|]+?)\s+(\d{1,2})%/gi;
  let match;
  while ((match = pattern.exec(text)) !== null) {
    domains.push(`Domain ${domains.length + 1}: ${collapseWhitespace(match[1])} - ${match[2]}%`);
  }
  return domains;
}

function significantTokens(value) {
  return value
    .split(/[^a-z0-9]+/i)
    .map((token) => token.toLowerCase())
    .filter((token) => token.length >= 3 && !["aws", "the", "and", "for", "exam", "certified"].includes(token));
}

function clean(value) {
  return typeof value === "string" ? value.trim() : "";
}

function isTextLike(contentType) {
  const lowered = contentType.toLowerCase();
  return lowered.includes("text/") || lowered.includes("html") || lowered.includes("json") || lowered.includes("xml");
}

function extractTitle(html) {
  const match = html.match(/<title[^>]*>([\s\S]*?)<\/title>/i);
  return match ? collapseWhitespace(stripTags(match[1])) : "";
}

function htmlToVisibleText(html) {
  return collapseWhitespace(
    html
      .replace(/<script[\s\S]*?<\/script>/gi, " ")
      .replace(/<style[\s\S]*?<\/style>/gi, " ")
      .replace(/<noscript[\s\S]*?<\/noscript>/gi, " ")
      .replace(/<[^>]+>/g, " ")
  );
}

function stripTags(text) {
  return text.replace(/<[^>]*>/g, "");
}

function collapseWhitespace(text) {
  return text.replace(/\s+/g, " ").trim();
}
