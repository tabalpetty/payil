"use client";

import { useEffect, useMemo, useState } from "react";
import Dexie from "dexie";

const db = new Dexie("sourceIdentityWorkbench");
db.version(1).stores({ drafts: "id, updatedAt" });

const emptyDraft = {
  sourceName: "",
  sourceCode: "",
  authority: "",
  sourceUrl: "",
  localSnapshotPath: "",
  accessDate: new Date().toISOString().slice(0, 10),
  learnerProfile: "",
  successTarget: "",
  duration: "",
  questionCount: "",
  passingScore: "",
  formats: "",
  domainCount: "",
  taskCount: "",
  domains: "",
  knownConfusions: "",
  notes: "",
  reviewerDecision: "needs-review",
  reviewerNote: ""
};

export default function Home() {
  const [active, setActive] = useState("intent");
  const [draft, setDraft] = useState(emptyDraft);
  const [verification, setVerification] = useState(null);
  const [discovery, setDiscovery] = useState(null);
  const [selectedCandidateId, setSelectedCandidateId] = useState("");
  const [checkpoint, setCheckpoint] = useState(null);
  const [markdown, setMarkdown] = useState("");
  const [busy, setBusy] = useState("");
  const [saveState, setSaveState] = useState("draft autosave enabled");

  useEffect(() => {
    db.drafts.get("current").then((stored) => {
      if (stored?.draft) {
        setDraft({ ...emptyDraft, ...stored.draft });
        setVerification(stored.verification || null);
        setDiscovery(stored.discovery || null);
        setSelectedCandidateId(stored.selectedCandidateId || "");
      }
    });
  }, []);

  useEffect(() => {
    const handle = window.setTimeout(() => {
      db.drafts
        .put({ id: "current", draft, verification, discovery, selectedCandidateId, updatedAt: new Date().toISOString() })
        .then(() => setSaveState("draft saved locally"))
        .catch(() => setSaveState("draft save failed"));
    }, 250);
    return () => window.clearTimeout(handle);
  }, [draft, verification, discovery, selectedCandidateId]);

  useEffect(() => {
    if ("serviceWorker" in navigator) {
      navigator.serviceWorker.register("/sw.js").catch(() => {});
    }
  }, []);

  const payload = useMemo(() => ({ ...draft, verification }), [draft, verification]);

  function update(field, value) {
    setSaveState("saving draft...");
    setDraft((current) => ({ ...current, [field]: value }));
  }

  async function discoverSources() {
    if (!draft.sourceName.trim() || !draft.authority.trim()) {
      setDiscovery({
        status: "needs-input",
        message: "Exam/course name and vendor/authority are mandatory before discovery.",
        candidates: []
      });
      return;
    }
    setBusy("discover");
    setCheckpoint(null);
    setMarkdown("");
    try {
      const response = await fetch("/api/discover-source", {
        method: "POST",
        headers: { "content-type": "application/json" },
        body: JSON.stringify(draft)
      });
      const data = await response.json();
      setDiscovery(data);
      if (data.candidates?.length === 1) {
        applyCandidate(data.candidates[0]);
      }
    } finally {
      setBusy("");
    }
  }

  function applyCandidate(candidate) {
    if (!candidate) return;
    setSelectedCandidateId(candidate.id);
    setDraft((current) => ({
      ...current,
      sourceName: candidate.sourceName || current.sourceName,
      sourceCode: candidate.sourceCode || current.sourceCode,
      authority: candidate.authority || current.authority,
      sourceUrl: candidate.sourceUrl || current.sourceUrl,
      learnerProfile: candidate.learnerProfile || current.learnerProfile,
      successTarget: candidate.successTarget || current.successTarget,
      duration: candidate.duration || current.duration,
      questionCount: candidate.questionCount || current.questionCount,
      passingScore: candidate.passingScore || current.passingScore,
      formats: candidate.formats || current.formats,
      domainCount: candidate.domainCount || current.domainCount,
      domains: candidate.domains?.length ? candidate.domains.join("\n") : current.domains,
      knownConfusions: candidate.knownConfusions?.length ? candidate.knownConfusions.join("\n") : current.knownConfusions
    }));
  }

  async function verifySource() {
    if (!draft.sourceUrl.trim()) {
      await discoverSources();
      return;
    }
    setBusy("verify");
    setCheckpoint(null);
    setMarkdown("");
    try {
      const response = await fetch("/api/verify-source", {
        method: "POST",
        headers: { "content-type": "application/json" },
        body: JSON.stringify(draft)
      });
      const data = await response.json();
      setVerification(data.verification);
      applySupplements(data.verification?.supplements || {});
      setActive("verify");
    } finally {
      setBusy("");
    }
  }

  function applySupplements(supplements) {
    if (!supplements || Object.keys(supplements).length === 0) return;
    setDraft((current) => ({
      ...current,
      sourceName: current.sourceName || supplements.sourceName || "",
      sourceCode: current.sourceCode || supplements.sourceCode || "",
      learnerProfile: current.learnerProfile || supplements.learnerProfile || "",
      successTarget: current.successTarget || supplements.successTarget || "",
      duration: current.duration || supplements.duration || "",
      questionCount: current.questionCount || supplements.questionCount || "",
      passingScore: current.passingScore || supplements.passingScore || "",
      formats: current.formats || supplements.formats || "",
      domainCount: current.domainCount || supplements.domainCount || "",
      domains: current.domains || (supplements.domains || []).join("\n"),
      knownConfusions: current.knownConfusions || (supplements.knownConfusions || []).join("\n")
    }));
  }

  async function buildCheckpoint() {
    setBusy("checkpoint");
    try {
      const response = await fetch("/api/checkpoint", {
        method: "POST",
        headers: { "content-type": "application/json" },
        body: JSON.stringify(payload)
      });
      const data = await response.json();
      setCheckpoint(data.checkpoint);
      setMarkdown(data.markdown);
      setActive("checkpoint");
    } finally {
      setBusy("");
    }
  }

  async function copyMarkdown() {
    await navigator.clipboard.writeText(markdown);
    setSaveState("markdown copied");
  }

  function downloadJson() {
    const blob = new Blob([JSON.stringify(checkpoint, null, 2)], { type: "application/json" });
    const url = URL.createObjectURL(blob);
    const link = document.createElement("a");
    const slug = (draft.sourceCode || "source").toLowerCase().replace(/[^a-z0-9]+/g, "-");
    link.href = url;
    link.download = `${slug}-source-identity-checkpoint.json`;
    link.click();
    URL.revokeObjectURL(url);
  }

  function loadAipExample() {
    setDraft({
      ...emptyDraft,
      sourceName: "AWS Certified Generative AI Developer - Professional",
      sourceCode: "AIP-C01",
      authority: "AWS",
      sourceUrl: "https://docs.aws.amazon.com/aws-certification/latest/ai-professional-01/ai-professional-01.html",
      localSnapshotPath: "docs/Pilot1/aip-c01/source-material/ai-professional-01.pdf",
      accessDate: new Date().toISOString().slice(0, 10),
      learnerProfile: "GenAI developer",
      successTarget: "Exam-ready AIP-C01 study program",
      duration: "180 minutes",
      questionCount: "75 total; 65 scored; 10 unscored",
      passingScore: "750",
      formats: "Multiple choice; multiple response",
      domainCount: "5",
      domains:
        "Domain 1: Foundation Model Integration, Data Management, and Compliance - 31%\n" +
        "Domain 2: Implementation and Integration - 26%\n" +
        "Domain 3: AI Safety, Security, and Governance - 20%\n" +
        "Domain 4: Operational Efficiency and Optimization for GenAI Applications - 12%\n" +
        "Domain 5: Testing, Validation, and Troubleshooting - 11%",
      knownConfusions: "Do not use AIF-C01 / AWS Certified AI Practitioner as the target source.",
      notes: "Use the official AWS AIP-C01 guide as the source of record."
    });
    setVerification(null);
    setDiscovery(null);
    setSelectedCandidateId("aws-aip-c01");
    setCheckpoint(null);
    setMarkdown("");
  }

  return (
    <>
      <header className="appHeader">
        <div>
          <p className="eyebrow">Layer -2</p>
          <h1>Source Identity Workbench</h1>
        </div>
        <div className="status">{saveState}</div>
      </header>

      <main className="shell">
        <nav className="stepper" aria-label="Workbench sections">
          <Step active={active === "intent"} onClick={() => setActive("intent")} number="-2A" label="Intent" />
          <Step active={active === "verify"} onClick={() => setActive("verify")} number="-2B" label="Verify" />
          <Step active={active === "checkpoint"} onClick={() => setActive("checkpoint")} number="-2C" label="Checkpoint" />
        </nav>

        {active === "intent" && (
          <section className="panel">
            <PanelHead
              title="Intended official source"
              text="Enter what you know. Name and vendor are mandatory; the server can suggest and populate the rest for confirmation."
              action={<button className="secondary" onClick={loadAipExample}>Load AIP-C01 Example</button>}
            />
            <div className="grid two">
              <Field label="Exam or course name" value={draft.sourceName} onChange={(v) => update("sourceName", v)} required />
              <Field label="Code or version" value={draft.sourceCode} onChange={(v) => update("sourceCode", v)} />
              <Field label="Vendor / official authority" value={draft.authority} onChange={(v) => update("authority", v)} required />
              <Field label="Official source URL" value={draft.sourceUrl} onChange={(v) => update("sourceUrl", v)} />
              <Field label="Local snapshot path" value={draft.localSnapshotPath} onChange={(v) => update("localSnapshotPath", v)} />
              <Field label="Access date" type="date" value={draft.accessDate} onChange={(v) => update("accessDate", v)} />
              <Field label="Learner or candidate profile" value={draft.learnerProfile} onChange={(v) => update("learnerProfile", v)} />
              <Field label="Success target" value={draft.successTarget} onChange={(v) => update("successTarget", v)} />
            </div>
            <TextArea label="Known domains or sections" value={draft.domains} onChange={(v) => update("domains", v)} rows={6} />
            <TextArea label="Known confusions or exclusions" value={draft.knownConfusions} onChange={(v) => update("knownConfusions", v)} rows={3} />
            <TextArea label="Notes" value={draft.notes} onChange={(v) => update("notes", v)} rows={3} />
            <DiscoveryResult
              discovery={discovery}
              selectedCandidateId={selectedCandidateId}
              onSelect={(candidate) => applyCandidate(candidate)}
            />
            <div className="actions">
              <button className="secondary" onClick={discoverSources} disabled={busy === "discover"}>
                {busy === "discover" ? "Finding..." : "Find Official Source"}
              </button>
              <button onClick={verifySource} disabled={busy === "verify"}>{busy === "verify" ? "Verifying..." : "Run Server Verification"}</button>
            </div>
          </section>
        )}

        {active === "verify" && (
          <section className="panel">
            <PanelHead
              title="Server verification"
              text="The browser does not verify official truth. It shows what the server found."
              action={<button onClick={verifySource} disabled={busy === "verify"}>{busy === "verify" ? "Verifying..." : "Run Again"}</button>}
            />
            <VerificationSummary verification={verification} />
            <div className="grid three">
              <Field label="Duration" value={draft.duration} onChange={(v) => update("duration", v)} />
              <Field label="Question count" value={draft.questionCount} onChange={(v) => update("questionCount", v)} />
              <Field label="Passing score / standard" value={draft.passingScore} onChange={(v) => update("passingScore", v)} />
              <Field label="Question formats" value={draft.formats} onChange={(v) => update("formats", v)} />
              <Field label="Domain count" value={draft.domainCount} onChange={(v) => update("domainCount", v)} />
              <Field label="Task / objective count" value={draft.taskCount} onChange={(v) => update("taskCount", v)} />
            </div>
            <fieldset>
              <legend>Reviewer decision</legend>
              <div className="segmented">
                {["approved", "needs-review", "rejected"].map((option) => (
                  <label key={option}>
                    <input
                      type="radio"
                      name="reviewerDecision"
                      checked={draft.reviewerDecision === option}
                      onChange={() => update("reviewerDecision", option)}
                    />
                    {option}
                  </label>
                ))}
              </div>
            </fieldset>
            <TextArea label="Reviewer note" value={draft.reviewerNote} onChange={(v) => update("reviewerNote", v)} rows={4} />
            <div className="actions">
              <button className="secondary" onClick={() => window.open(draft.sourceUrl, "_blank", "noopener,noreferrer")}>Open Official URL</button>
              <button onClick={buildCheckpoint} disabled={busy === "checkpoint"}>{busy === "checkpoint" ? "Building..." : "Build Checkpoint"}</button>
            </div>
          </section>
        )}

        {active === "checkpoint" && (
          <section className="panel">
            <PanelHead
              title="Canonical -2 checkpoint"
              text="Generated by the server. Commit this output before Layer -1 extraction."
              action={
                <div className="actions compact">
                  <button className="secondary" onClick={copyMarkdown} disabled={!markdown}>Copy Markdown</button>
                  <button onClick={downloadJson} disabled={!checkpoint}>Download JSON</button>
                </div>
              }
            />
            <Readiness checkpoint={checkpoint} />
            <pre className="preview">{markdown || "Build a checkpoint to preview Markdown."}</pre>
          </section>
        )}
      </main>
    </>
  );
}

function Step({ active, onClick, number, label }) {
  return (
    <button className={`step ${active ? "active" : ""}`} onClick={onClick}>
      <span>{number}</span>
      {label}
    </button>
  );
}

function PanelHead({ title, text, action }) {
  return (
    <div className="panelHead">
      <div>
        <h2>{title}</h2>
        <p>{text}</p>
      </div>
      {action}
    </div>
  );
}

function Field({ label, value, onChange, type = "text", required = false }) {
  return (
    <label>
      <span>{label}{required ? <strong className="required"> required</strong> : null}</span>
      <input required={required} type={type} value={value} onChange={(event) => onChange(event.target.value)} />
    </label>
  );
}

function TextArea({ label, value, onChange, rows }) {
  return (
    <label>
      {label}
      <textarea rows={rows} value={value} onChange={(event) => onChange(event.target.value)} />
    </label>
  );
}

function DiscoveryResult({ discovery, selectedCandidateId, onSelect }) {
  if (!discovery) return null;
  const candidates = discovery.candidates || [];

  return (
    <div className="discovery">
      <div>
        <h3>Source candidates</h3>
        <p>{discovery.message}</p>
      </div>
      {candidates.length > 0 && (
        <label>
          Select official source
          <select
            value={selectedCandidateId}
            onChange={(event) => {
              const candidate = candidates.find((item) => item.id === event.target.value);
              onSelect(candidate);
            }}
          >
            <option value="">Choose one...</option>
            {candidates.map((candidate) => (
              <option key={candidate.id} value={candidate.id}>
                {candidate.sourceCode} - {candidate.sourceName} ({candidate.confidence}%)
              </option>
            ))}
          </select>
        </label>
      )}
    </div>
  );
}

function VerificationSummary({ verification }) {
  if (!verification) {
    return <div className="notice">No server verification has run yet.</div>;
  }

  const rows = [
    ["Status", verification.status],
    ["Checked", verification.checkedAt],
    ["Requested URL", verification.requestedUrl],
    ["Resolved URL", verification.resolvedUrl],
    ["HTTP", verification.httpStatus],
    ["Content type", verification.contentType],
    ["SHA-256", verification.sha256],
    ["Title", verification.pageTitle],
    ["Supplements", summarizeSupplements(verification.supplements)],
    ["Matched", verification.matchedSignals?.join(", ") || "none"],
    ["Missing", verification.missingSignals?.join(", ") || "none"],
    ["Notes", verification.notes?.join("; ") || "none"],
    ["Error", verification.error || "none"]
  ];

  return (
    <dl className="summary">
      {rows.map(([key, value]) => (
        <div key={key}>
          <dt>{key}</dt>
          <dd>{value || "none"}</dd>
        </div>
      ))}
    </dl>
  );
}

function summarizeSupplements(supplements) {
  if (!supplements || Object.keys(supplements).length === 0) return "none";
  return Object.entries(supplements)
    .map(([key, value]) => `${key}: ${Array.isArray(value) ? value.length + " values" : value}`)
    .join("; ");
}

function Readiness({ checkpoint }) {
  if (!checkpoint) return <div className="notice">No checkpoint generated.</div>;
  return <div className={`banner ${checkpoint.status}`}>{checkpoint.status}: {checkpoint.statusReason}</div>;
}
