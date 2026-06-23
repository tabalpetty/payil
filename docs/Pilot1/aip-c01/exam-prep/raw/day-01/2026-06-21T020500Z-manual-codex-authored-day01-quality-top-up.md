# Raw Day 1 Question Generation Response

## Metadata

```json
{
  "provider": "manual",
  "model": "codex-authored",
  "run_id": "quality-top-up",
  "created_utc": "2026-06-21T020500Z",
  "status": "raw-draft",
  "prompt_pack": "docs/Pilot1/aip-c01/exam-prep/day-01-question-generation-prompts.md",
  "note": "Manual top-up candidate set authored in-repo because OPENAI_API_KEY was unavailable in the execution environment. These are not previously rejected questions and were still passed through the same review script."
}
```

## Raw Response Text

```json
[
  {
    "status": "draft",
    "official_exam_code": "AIP-C01",
    "accelerated_day": "Day 1",
    "curriculum_order": "Day01-order001",
    "topic": "Foundation models and GenAI fundamentals",
    "knowledge_category": "Knowledge",
    "knowledge_type": "Declarative; Conceptual",
    "question_format": "multiple-choice",
    "difficulty": "hard",
    "cognitive_demand": "judge",
    "stem": "A product team wants a GenAI assistant to draft support replies, but leadership expects the model itself to enforce refund policy, check customer entitlements, and open tickets. Which design decision best separates foundation-model capability from application responsibility?",
    "options": [
      "Use the foundation model for language generation while the application retrieves policy, verifies entitlements, and performs ticket actions through controlled services.",
      "Fine-tune the model on refund policies so the model can become the system of record for entitlement decisions.",
      "Increase the model context window so all policies fit into the prompt and no application controls are needed.",
      "Move ticket creation into the prompt instructions so the model can decide when operational actions are valid."
    ],
    "correct_answer": "A",
    "rationale_correct": "The model can generate and reason over text, but application code and trusted services should enforce policy, authorization, state changes, and workflow actions.",
    "rationale_distractors": {
      "B": "Fine-tuning may improve task behavior but does not make the model a trusted authority for entitlement or policy enforcement.",
      "C": "A larger context window does not replace deterministic application controls.",
      "D": "Prompt instructions cannot safely perform or authorize operational side effects by themselves."
    },
    "misconception_tags": ["model-vs-application-confusion", "prompt-as-control-plane"],
    "source_trace_needed": "AIP-C01 Task 1.1 and Day 1 study guide foundation-model/application-boundary section.",
    "remediation_target": "docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day01-order001-foundation-models-genai-fundamentals.md"
  },
  {
    "status": "draft",
    "official_exam_code": "AIP-C01",
    "accelerated_day": "Day 1",
    "curriculum_order": "Day01-order001",
    "topic": "Foundation models and GenAI fundamentals",
    "knowledge_category": "Knowledge",
    "knowledge_type": "Declarative; Conceptual",
    "question_format": "multiple-choice",
    "difficulty": "hard",
    "cognitive_demand": "diagnose",
    "stem": "A company deploys a summarization feature using a foundation model. Users report fluent summaries that occasionally introduce claims not present in the source documents. What is the best initial interpretation of this failure?",
    "options": [
      "The system is seeing a generative behavior risk and needs grounding, evaluation, and output controls around the model.",
      "The model endpoint is unavailable and the application is falling back to cached summaries.",
      "The model has been trained from scratch incorrectly and must be rebuilt before any mitigation is possible.",
      "The token limit is always the root cause whenever a summary contains unsupported claims."
    ],
    "correct_answer": "A",
    "rationale_correct": "Fluent unsupported claims are a known GenAI output risk; the application should add grounding, checks, and evaluation rather than assuming infrastructure outage or retraining from scratch.",
    "rationale_distractors": {
      "B": "Endpoint failure would usually present as invocation errors or fallback behavior, not necessarily fluent new claims.",
      "C": "Most teams use existing foundation models; rebuilding from scratch is not the first response.",
      "D": "Truncation can cause omissions, but unsupported claims are broader than token limits alone."
    },
    "misconception_tags": ["hallucination-as-infrastructure-failure", "training-from-scratch-default"],
    "source_trace_needed": "AIP-C01 Task 1.1 and Day 1 study guide GenAI behavior risks.",
    "remediation_target": "docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day01-order001-foundation-models-genai-fundamentals.md"
  },
  {
    "status": "draft",
    "official_exam_code": "AIP-C01",
    "accelerated_day": "Day 1",
    "curriculum_order": "Day01-order001",
    "topic": "Foundation models and GenAI fundamentals",
    "knowledge_category": "Knowledge",
    "knowledge_type": "Declarative; Conceptual",
    "question_format": "multiple-response",
    "difficulty": "exam-plus",
    "cognitive_demand": "compare",
    "stem": "A team is deciding whether a planned feature should be treated as a GenAI use case or a conventional rules-and-search workflow. Which two signals most strongly indicate that a foundation model is appropriate? (Select TWO.)",
    "options": [
      "The output must be synthesized in natural language from variable user input and contextual evidence.",
      "The workflow requires deterministic arithmetic on a fixed schema with no language ambiguity.",
      "The feature needs flexible interpretation of messy text, intent, or semantic similarity.",
      "The main requirement is to copy an exact stored value from one database field to another.",
      "The business wants to remove all validation and authorization code from the application."
    ],
    "correct_answer": ["A", "C"],
    "rationale_correct": "Foundation models are well suited when the task requires language synthesis, semantic interpretation, or flexible handling of unstructured input.",
    "rationale_distractors": {
      "B": "Deterministic arithmetic over fixed schemas is usually better handled with conventional code.",
      "D": "Exact data movement is not a GenAI capability need.",
      "E": "Using a model does not remove the need for validation or authorization."
    },
    "misconception_tags": ["genai-for-everything", "model-vs-application-confusion"],
    "source_trace_needed": "AIP-C01 Task 1.1 and Day 1 study guide GenAI fit criteria.",
    "remediation_target": "docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day01-order001-foundation-models-genai-fundamentals.md"
  },
  {
    "status": "draft",
    "official_exam_code": "AIP-C01",
    "accelerated_day": "Day 1",
    "curriculum_order": "Day01-order001",
    "topic": "Foundation models and GenAI fundamentals",
    "knowledge_category": "Knowledge",
    "knowledge_type": "Declarative; Conceptual",
    "question_format": "multiple-choice",
    "difficulty": "hard",
    "cognitive_demand": "select",
    "stem": "An enterprise architecture review finds that a proposed GenAI service sends user prompts directly to a model and returns the raw response to the user. Which addition most directly turns the model call into a governed application workflow?",
    "options": [
      "Add retrieval, input validation, authorization checks, output validation, logging, and human escalation paths around the model invocation.",
      "Raise temperature so responses cover a wider range of user intents.",
      "Store prompts in a larger object store before sending them to the model.",
      "Replace all application code with a longer system prompt that describes company policy."
    ],
    "correct_answer": "A",
    "rationale_correct": "A governed GenAI application wraps model inference with controls, context, validation, observability, and operational handling.",
    "rationale_distractors": {
      "B": "Temperature affects output variability, not governance.",
      "C": "Storage alone does not create controls or workflow.",
      "D": "Prompts help steer behavior but do not replace application controls."
    },
    "misconception_tags": ["raw-model-call-as-application", "security-afterthought"],
    "source_trace_needed": "AIP-C01 Task 1.1 and Day 1 study guide system map.",
    "remediation_target": "docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day01-order001-foundation-models-genai-fundamentals.md"
  },
  {
    "status": "draft",
    "official_exam_code": "AIP-C01",
    "accelerated_day": "Day 1",
    "curriculum_order": "Day01-order002",
    "topic": "Tokens, context windows, inference, temperature, top-k, and top-p",
    "knowledge_category": "Knowledge",
    "knowledge_type": "Declarative; Conceptual; Causal",
    "question_format": "multiple-choice",
    "difficulty": "hard",
    "cognitive_demand": "diagnose",
    "stem": "A team adds long policy documents to every prompt for a chatbot. Latency and cost rise sharply, and some late-document rules appear to be ignored. Which explanation best connects the symptoms?",
    "options": [
      "The prompt is consuming more tokens, increasing inference work and risking context-window truncation or reduced attention to later content.",
      "The model has switched from inference mode to training mode because the prompt contains policy documents.",
      "Lowering top-p will automatically reduce token usage while preserving all policy context.",
      "The application must raise temperature because long prompts always make outputs deterministic."
    ],
    "correct_answer": "A",
    "rationale_correct": "Longer prompts consume more tokens, increase processing cost and latency, and can stress context-window limits.",
    "rationale_distractors": {
      "B": "Including documents in a prompt does not train the model.",
      "C": "Top-p affects sampling, not how many input tokens are sent.",
      "D": "Temperature controls randomness, not whether long prompts are fully represented."
    },
    "misconception_tags": ["bigger-context-is-always-better", "prompt-is-training"],
    "source_trace_needed": "Day 1 study guide tokens/context/inference parameters.",
    "remediation_target": "docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day01-order002-tokens-context-inference-parameters.md"
  },
  {
    "status": "draft",
    "official_exam_code": "AIP-C01",
    "accelerated_day": "Day 1",
    "curriculum_order": "Day01-order002",
    "topic": "Tokens, context windows, inference, temperature, top-k, and top-p",
    "knowledge_category": "Knowledge",
    "knowledge_type": "Declarative; Conceptual; Causal",
    "question_format": "multiple-choice",
    "difficulty": "hard",
    "cognitive_demand": "select",
    "stem": "A customer-support assistant must answer policy questions consistently and avoid creative wording in regulated responses. Which inference-parameter strategy is the best starting point?",
    "options": [
      "Use a lower temperature and constrain sampling so the model favors more predictable completions.",
      "Use a higher temperature so the model explores more unusual response paths.",
      "Maximize top-k so every possible token is equally likely.",
      "Increase the context window and leave sampling unconstrained because consistency comes only from more context."
    ],
    "correct_answer": "A",
    "rationale_correct": "Lower-temperature and constrained sampling settings are a reasonable starting point when consistency matters more than creative variation.",
    "rationale_distractors": {
      "B": "Higher temperature tends to increase variation.",
      "C": "Broad sampling does not improve consistency.",
      "D": "More context can help grounding but does not by itself control output variability."
    },
    "misconception_tags": ["temperature-means-quality", "context-window-as-control"],
    "source_trace_needed": "Day 1 study guide inference parameter behavior.",
    "remediation_target": "docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day01-order002-tokens-context-inference-parameters.md"
  },
  {
    "status": "draft",
    "official_exam_code": "AIP-C01",
    "accelerated_day": "Day 1",
    "curriculum_order": "Day01-order002",
    "topic": "Tokens, context windows, inference, temperature, top-k, and top-p",
    "knowledge_category": "Knowledge",
    "knowledge_type": "Declarative; Conceptual; Causal",
    "question_format": "multiple-response",
    "difficulty": "exam-plus",
    "cognitive_demand": "judge",
    "stem": "A team is tuning a model-backed code-review assistant. They want concise comments, stable formatting, and enough room for a pull-request diff. Which two changes address different parts of the problem? (Select TWO.)",
    "options": [
      "Set explicit output-length and formatting instructions in the prompt.",
      "Choose a context window large enough for the diff and required review instructions.",
      "Raise temperature to make the assistant less likely to vary its formatting.",
      "Assume top-k controls how many input files can be included in the request.",
      "Remove all examples from the prompt because examples always waste context."
    ],
    "correct_answer": ["A", "B"],
    "rationale_correct": "Formatting and output length are prompt-design concerns; fitting the diff and instructions is a context-window/token-budget concern.",
    "rationale_distractors": {
      "C": "Higher temperature generally increases variation.",
      "D": "Top-k affects sampling over output tokens, not the number of input files.",
      "E": "Examples can be valuable when used deliberately within the token budget."
    },
    "misconception_tags": ["sampling-vs-context-confusion", "examples-are-always-bad"],
    "source_trace_needed": "Day 1 study guide tokens, context windows, and inference controls.",
    "remediation_target": "docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day01-order002-tokens-context-inference-parameters.md"
  },
  {
    "status": "draft",
    "official_exam_code": "AIP-C01",
    "accelerated_day": "Day 1",
    "curriculum_order": "Day01-order002",
    "topic": "Tokens, context windows, inference, temperature, top-k, and top-p",
    "knowledge_category": "Knowledge",
    "knowledge_type": "Declarative; Conceptual; Causal",
    "question_format": "multiple-choice",
    "difficulty": "hard",
    "cognitive_demand": "diagnose",
    "stem": "An application passes a retrieved contract excerpt plus a user question to a model. The response omits a clause that appears near the end of the excerpt. Which first investigation is most appropriate?",
    "options": [
      "Check token counts, truncation behavior, prompt ordering, and whether the relevant clause is within the effective context sent to the model.",
      "Assume the model permanently learned an incorrect version of the contract and fine-tune immediately.",
      "Increase temperature so the model is more likely to mention unusual clauses.",
      "Remove retrieval and ask the model to rely on pretraining for contract terms."
    ],
    "correct_answer": "A",
    "rationale_correct": "The symptom may come from token budget, truncation, prompt structure, or retrieval packaging, so those should be checked first.",
    "rationale_distractors": {
      "B": "Prompted context is not permanent training data, and fine-tuning is not the first diagnostic step.",
      "C": "Temperature does not guarantee attention to omitted context.",
      "D": "Pretraining is not reliable for specific contract clauses."
    },
    "misconception_tags": ["prompt-is-training", "temperature-fixes-grounding"],
    "source_trace_needed": "Day 1 study guide context window and retrieval packaging discussion.",
    "remediation_target": "docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day01-order002-tokens-context-inference-parameters.md"
  },
  {
    "status": "draft",
    "official_exam_code": "AIP-C01",
    "accelerated_day": "Day 1",
    "curriculum_order": "Day01-order003",
    "topic": "AWS GenAI service landscape",
    "knowledge_category": "Representation / Location",
    "knowledge_type": "Declarative; Conceptual; Embedded",
    "question_format": "multiple-choice",
    "difficulty": "hard",
    "cognitive_demand": "select",
    "stem": "A team needs managed access to multiple foundation models, embeddings, and guardrail features without operating model-serving infrastructure. Which service role should they place at the model-access layer of their architecture?",
    "options": [
      "Amazon Bedrock for managed foundation-model access and related GenAI capabilities.",
      "Amazon CloudWatch as the primary model runtime because it stores operational metrics.",
      "AWS CloudFormation as the runtime inference endpoint because it provisions stacks.",
      "Amazon S3 as the model reasoning layer because it stores prompt and document files."
    ],
    "correct_answer": "A",
    "rationale_correct": "Amazon Bedrock belongs at the managed foundation-model access layer for invoking models and related GenAI capabilities.",
    "rationale_distractors": {
      "B": "CloudWatch observes systems but is not the model runtime.",
      "C": "CloudFormation provisions infrastructure but does not perform inference.",
      "D": "S3 stores data but does not provide model reasoning."
    },
    "misconception_tags": ["service-role-confusion", "storage-as-runtime"],
    "source_trace_needed": "AWS Bedrock User Guide and Day 1 AWS service landscape.",
    "remediation_target": "docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day01-order003-aws-genai-service-landscape.md"
  },
  {
    "status": "draft",
    "official_exam_code": "AIP-C01",
    "accelerated_day": "Day 1",
    "curriculum_order": "Day01-order003",
    "topic": "AWS GenAI service landscape",
    "knowledge_category": "Representation / Location",
    "knowledge_type": "Declarative; Conceptual; Embedded",
    "question_format": "multiple-response",
    "difficulty": "hard",
    "cognitive_demand": "compare",
    "stem": "A company is drawing a Day 1 GenAI system map for a retrieval-augmented assistant. Which two components are correctly placed outside the foundation model itself? (Select TWO.)",
    "options": [
      "A vector or document retrieval layer that selects grounding context.",
      "An IAM role that grants the application permission to call required AWS APIs.",
      "The model's learned parameters inside the managed model provider.",
      "The model's token sampling process during generation.",
      "The pretraining corpus originally used to build the foundation model."
    ],
    "correct_answer": ["A", "B"],
    "rationale_correct": "Retrieval and IAM permissions are application/platform components around the model, not the model internals.",
    "rationale_distractors": {
      "C": "Model parameters are part of the model.",
      "D": "Sampling is part of inference behavior.",
      "E": "The pretraining corpus is not an application component the team places in the runtime architecture."
    },
    "misconception_tags": ["model-vs-application-confusion", "service-role-confusion"],
    "source_trace_needed": "AIP-C01 Task 1.1 and Day 1 system map.",
    "remediation_target": "docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day01-order003-aws-genai-service-landscape.md"
  },
  {
    "status": "draft",
    "official_exam_code": "AIP-C01",
    "accelerated_day": "Day 1",
    "curriculum_order": "Day01-order003",
    "topic": "AWS GenAI service landscape",
    "knowledge_category": "Representation / Location",
    "knowledge_type": "Declarative; Conceptual; Embedded",
    "question_format": "multiple-choice",
    "difficulty": "hard",
    "cognitive_demand": "diagnose",
    "stem": "An application team says their GenAI workload needs monitoring, but their diagram sends CloudWatch logs into the prompt as the primary control for model safety. What correction best clarifies the service role?",
    "options": [
      "Use observability data to monitor and investigate the application, while safety controls and prompt/context design remain explicit application and Bedrock-layer concerns.",
      "Use CloudWatch metrics as the only grounding source because metrics are more reliable than documents.",
      "Remove application logging because model outputs are enough to reconstruct every failure.",
      "Put IAM policies inside the model prompt so CloudWatch can enforce data access."
    ],
    "correct_answer": "A",
    "rationale_correct": "CloudWatch supports observability and investigation; it does not replace safety controls, grounding design, or IAM enforcement.",
    "rationale_distractors": {
      "B": "Metrics are not a general grounding source for user answers.",
      "C": "Logging is necessary for operations and auditability.",
      "D": "IAM policies are enforced by AWS, not by prompt text."
    },
    "misconception_tags": ["observability-as-safety-control", "iam-in-prompt"],
    "source_trace_needed": "Amazon CloudWatch User Guide, IAM User Guide, and Day 1 service landscape.",
    "remediation_target": "docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day01-order003-aws-genai-service-landscape.md"
  },
  {
    "status": "draft",
    "official_exam_code": "AIP-C01",
    "accelerated_day": "Day 1",
    "curriculum_order": "Day01-order004",
    "topic": "API, event-driven, serverless, container, and workflow fundamentals",
    "knowledge_category": "Knowledge",
    "knowledge_type": "Conceptual; Conditional",
    "question_format": "multiple-choice",
    "difficulty": "hard",
    "cognitive_demand": "select",
    "stem": "A team is building a GenAI document-analysis feature where a user uploads a file, the system extracts text, invokes a model, stores results, and notifies the user minutes later. Which integration pattern best fits the end-to-end workflow?",
    "options": [
      "Asynchronous event-driven processing with a queue or workflow orchestrator coordinating the long-running steps.",
      "A single synchronous browser request that blocks until every document page has been analyzed.",
      "A static website call directly to the model endpoint using the user's browser credentials.",
      "A scheduled batch job that ignores the upload event and scans the bucket once per month."
    ],
    "correct_answer": "A",
    "rationale_correct": "Long-running multi-step processing after an upload fits asynchronous event-driven or workflow orchestration patterns.",
    "rationale_distractors": {
      "B": "Blocking a browser request is brittle for long-running work.",
      "C": "Direct browser-to-model calls create credential and control problems.",
      "D": "Monthly scanning fails the user-triggered workflow requirement."
    },
    "misconception_tags": ["sync-for-everything", "client-direct-model-call"],
    "source_trace_needed": "AIP-C01 Task 2.5, AWS Step Functions docs, and Amazon SQS docs.",
    "remediation_target": "docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day01-order004-application-integration-patterns.md"
  },
  {
    "status": "draft",
    "official_exam_code": "AIP-C01",
    "accelerated_day": "Day 1",
    "curriculum_order": "Day01-order005",
    "topic": "IAM, trust boundaries, least privilege, networking, and data protection",
    "knowledge_category": "Knowledge; Skill",
    "knowledge_type": "Conceptual; Conditional; Normative",
    "question_format": "multiple-choice",
    "difficulty": "hard",
    "cognitive_demand": "judge",
    "stem": "A regulated team is designing a GenAI assistant that retrieves internal HR documents. The first design gives the model invocation role broad read access to every HR bucket because the prompt promises to ignore restricted records. What is the best review finding?",
    "options": [
      "The design violates least privilege because access controls must be enforced by IAM and retrieval filtering, not only by prompt instructions.",
      "The design is acceptable because the model can decide which records the user should see.",
      "The design only needs a higher temperature so restricted documents are less likely to be repeated.",
      "The design should remove logging to reduce the chance of sensitive data appearing in audit trails."
    ],
    "correct_answer": "A",
    "rationale_correct": "Least privilege and retrieval authorization must be enforced outside the prompt using IAM, data access controls, and filtering.",
    "rationale_distractors": {
      "B": "The model should not be trusted as the authorization boundary.",
      "C": "Sampling settings do not enforce data access.",
      "D": "Logging needs careful handling, not removal as a security strategy."
    },
    "misconception_tags": ["prompt-as-access-control", "security-afterthought"],
    "source_trace_needed": "AWS IAM User Guide and Day 1 trust-boundary artifact.",
    "remediation_target": "docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day01-order005-trust-boundaries-iam-data-protection.md"
  },
  {
    "status": "draft",
    "official_exam_code": "AIP-C01",
    "accelerated_day": "Day 1",
    "curriculum_order": "Day01-order005",
    "topic": "IAM, trust boundaries, least privilege, networking, and data protection",
    "knowledge_category": "Knowledge; Skill",
    "knowledge_type": "Conceptual; Conditional; Normative",
    "question_format": "multiple-response",
    "difficulty": "exam-plus",
    "cognitive_demand": "configure",
    "stem": "A company is preparing a baseline security review for a new Bedrock-backed application that handles confidential customer text. Which two controls belong in the initial trust-boundary design? (Select TWO.)",
    "options": [
      "Grant the application role only the model invocation and data access permissions needed for its workflow.",
      "Log model requests and responses according to the organization's sensitive-data handling policy.",
      "Let users pass arbitrary AWS role ARNs in prompts so the model can choose its own permissions.",
      "Use one shared administrator role for development, test, and production model access.",
      "Disable all output checks because IAM already controls every model response."
    ],
    "correct_answer": ["A", "B"],
    "rationale_correct": "Least-privilege roles and policy-aligned observability are basic trust-boundary controls for a confidential GenAI workload.",
    "rationale_distractors": {
      "C": "Prompts must not select AWS permissions.",
      "D": "Shared administrator roles violate least privilege and environment separation.",
      "E": "IAM does not validate model-output content."
    },
    "misconception_tags": ["iam-in-prompt", "iam-solves-output-safety"],
    "source_trace_needed": "AWS IAM User Guide, Bedrock guardrails documentation, and Day 1 trust-boundary artifact.",
    "remediation_target": "docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day01-order005-trust-boundaries-iam-data-protection.md"
  },
  {
    "status": "draft",
    "official_exam_code": "AIP-C01",
    "accelerated_day": "Day 1",
    "curriculum_order": "Day01-order006",
    "topic": "GenAI requirements analysis and basic solution architecture",
    "knowledge_category": "Skill",
    "knowledge_type": "Conceptual; Conditional; Strategic",
    "question_format": "multiple-choice",
    "difficulty": "hard",
    "cognitive_demand": "select",
    "stem": "A business sponsor asks for a GenAI assistant for field technicians. Requirements include offline capture, later synchronization, retrieval from repair manuals, and human approval before warranty decisions. Which architecture decision best reflects those requirements?",
    "options": [
      "Separate capture/sync, retrieval grounding, model assistance, and human approval into distinct components with explicit control points.",
      "Send technician notes directly to a model and automatically approve warranty claims from the response.",
      "Train a new foundation model so offline capture and approval workflow are unnecessary.",
      "Use only a prompt template because retrieval and workflow controls are implementation details that can wait."
    ],
    "correct_answer": "A",
    "rationale_correct": "The architecture should translate requirements into components and controls: data capture, retrieval, inference, and approval workflow.",
    "rationale_distractors": {
      "B": "Automatic approval violates the human-approval requirement.",
      "C": "Training a model does not remove application workflow needs.",
      "D": "Retrieval and workflow controls are core requirements, not optional details."
    },
    "misconception_tags": ["requirements-to-architecture-gap", "model-replaces-workflow"],
    "source_trace_needed": "AIP-C01 Task 1.1 and AWS Well-Architected Framework.",
    "remediation_target": "docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day01-order006-requirements-basic-solution-architecture.md"
  },
  {
    "status": "draft",
    "official_exam_code": "AIP-C01",
    "accelerated_day": "Day 1",
    "curriculum_order": "Day01-order006",
    "topic": "GenAI requirements analysis and basic solution architecture",
    "knowledge_category": "Skill",
    "knowledge_type": "Conceptual; Conditional; Strategic",
    "question_format": "multiple-response",
    "difficulty": "exam-plus",
    "cognitive_demand": "judge",
    "stem": "A team is reviewing requirements for a GenAI claims triage system. Which two requirements most directly affect the first architecture sketch rather than only the final prompt wording? (Select TWO.)",
    "options": [
      "Claims with low confidence must route to a human reviewer before customer notification.",
      "The system must retrieve policy and claim history from approved internal sources before model invocation.",
      "The assistant should use a friendly tone in its customer-facing explanation.",
      "The response should avoid contractions when writing status summaries.",
      "The prompt should call the model a claims expert."
    ],
    "correct_answer": ["A", "B"],
    "rationale_correct": "Human routing and retrieval from approved systems define components, data flows, and control placement in the architecture.",
    "rationale_distractors": {
      "C": "Tone matters, but it is primarily prompt/output guidance.",
      "D": "Style constraints are prompt-level details.",
      "E": "Role framing is a prompt tactic, not a system architecture requirement."
    },
    "misconception_tags": ["prompt-vs-architecture", "human-review-omitted"],
    "source_trace_needed": "AIP-C01 Task 1.1 and Day 1 architecture artifact.",
    "remediation_target": "docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day01-order006-requirements-basic-solution-architecture.md"
  },
  {
    "status": "draft",
    "official_exam_code": "AIP-C01",
    "accelerated_day": "Day 1",
    "curriculum_order": "Day01-order007",
    "topic": "Foundation-model capabilities, limitations, and basic model selection",
    "knowledge_category": "Knowledge; Skill",
    "knowledge_type": "Declarative; Conditional; Strategic",
    "question_format": "multiple-choice",
    "difficulty": "hard",
    "cognitive_demand": "select",
    "stem": "A team must choose a model for a customer chat feature that needs low latency, strong instruction following, moderate reasoning, and predictable cost at high request volume. What is the best selection approach?",
    "options": [
      "Compare candidate models against task-specific quality, latency, context, safety, and cost criteria before selecting.",
      "Select the largest available model because model size always dominates latency and cost concerns.",
      "Select the cheapest model without evaluation because chat quality can be fixed entirely with prompts.",
      "Select a model based only on whether it supports the longest context window."
    ],
    "correct_answer": "A",
    "rationale_correct": "Model selection should weigh the actual use case across quality, latency, context, safety, and cost constraints.",
    "rationale_distractors": {
      "B": "Larger models may increase latency and cost and are not always necessary.",
      "C": "Prompts cannot compensate for every model capability gap.",
      "D": "Context length is only one selection dimension."
    },
    "misconception_tags": ["largest-model-is-best", "prompt-fixes-all-model-gaps"],
    "source_trace_needed": "AIP-C01 Task 1.2 and Amazon Bedrock model evaluation docs.",
    "remediation_target": "docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day01-order007-model-capabilities-limitations-selection.md"
  },
  {
    "status": "draft",
    "official_exam_code": "AIP-C01",
    "accelerated_day": "Day 1",
    "curriculum_order": "Day01-order008",
    "topic": "Basic Amazon Bedrock model invocation",
    "knowledge_category": "Skill; Representation / Location",
    "knowledge_type": "Procedural; Embedded",
    "question_format": "multiple-choice",
    "difficulty": "hard",
    "cognitive_demand": "diagnose",
    "stem": "A developer invokes a Bedrock model from a Lambda function and receives an authorization error before any model response is returned. Which first check best matches the invocation path?",
    "options": [
      "Verify the Lambda execution role has permission for the Bedrock runtime action and the selected model resource or allowed model scope.",
      "Increase model temperature because authorization errors often occur when outputs are too deterministic.",
      "Add more examples to the prompt so the model can infer the missing AWS permission.",
      "Reduce max output tokens because Bedrock rejects all long requests as authorization failures."
    ],
    "correct_answer": "A",
    "rationale_correct": "Authorization errors occur before model generation and should be investigated through IAM permissions for the runtime invocation path.",
    "rationale_distractors": {
      "B": "Temperature has no bearing on AWS authorization.",
      "C": "Prompt examples cannot grant IAM permissions.",
      "D": "Token limits and authorization failures are different classes of errors."
    },
    "misconception_tags": ["iam-in-prompt", "sampling-fixes-api-error"],
    "source_trace_needed": "AWS Bedrock InvokeModel/Converse API references and IAM documentation.",
    "remediation_target": "docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day01-order008-basic-bedrock-model-invocation.md"
  },
  {
    "status": "draft",
    "official_exam_code": "AIP-C01",
    "accelerated_day": "Day 1",
    "curriculum_order": "Day01-order008",
    "topic": "Basic Amazon Bedrock model invocation",
    "knowledge_category": "Skill; Representation / Location",
    "knowledge_type": "Procedural; Embedded",
    "question_format": "multiple-response",
    "difficulty": "hard",
    "cognitive_demand": "configure",
    "stem": "A team is writing a minimal Bedrock invocation runbook for a new service. Which two details must the runbook capture so another developer can reproduce the call shape? (Select TWO.)",
    "options": [
      "The runtime API or SDK method being used and the model identifier selected for the request.",
      "The request body structure, including messages or prompt fields and inference parameters required by that model/API.",
      "The exact model weights used during provider pretraining.",
      "A promise that the model will never produce unexpected content.",
      "A user password embedded in the prompt so the model can authenticate itself."
    ],
    "correct_answer": ["A", "B"],
    "rationale_correct": "A reproducible invocation needs the API/method, model identifier, and request payload shape including relevant inference parameters.",
    "rationale_distractors": {
      "C": "Pretraining weights are not part of a basic invocation runbook.",
      "D": "A runbook cannot guarantee all model behavior.",
      "E": "Credentials must not be embedded in prompts."
    },
    "misconception_tags": ["missing-request-shape", "credentials-in-prompt"],
    "source_trace_needed": "AWS Bedrock InvokeModel and Converse API references.",
    "remediation_target": "docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day01-order008-basic-bedrock-model-invocation.md"
  },
  {
    "status": "draft",
    "official_exam_code": "AIP-C01",
    "accelerated_day": "Day 1",
    "curriculum_order": "Day01-order009",
    "topic": "Prompt fundamentals, instructions, templates, and structured outputs",
    "knowledge_category": "Knowledge; Skill",
    "knowledge_type": "Conceptual; Procedural; Causal",
    "question_format": "multiple-choice",
    "difficulty": "hard",
    "cognitive_demand": "select",
    "stem": "A team wants a model to return incident summaries that downstream code can parse reliably. The current prompt asks for a helpful summary, and parsing fails when headings vary. Which prompt change best targets the failure?",
    "options": [
      "Specify a strict output schema with required fields, formatting constraints, and examples of valid output.",
      "Raise temperature so the model explores more heading styles and one may match the parser.",
      "Remove all role and task instructions so the model is not constrained.",
      "Ask the model to decide the best structure for each incident because flexibility improves parsing."
    ],
    "correct_answer": "A",
    "rationale_correct": "Structured-output requirements and examples reduce variation and align the response with downstream parsing needs.",
    "rationale_distractors": {
      "B": "More variation worsens parser reliability.",
      "C": "Removing instructions makes the output less predictable.",
      "D": "Flexible structure conflicts with reliable parsing."
    },
    "misconception_tags": ["structured-output-afterthought", "temperature-fixes-format"],
    "source_trace_needed": "AIP-C01 Task 1.6 and Bedrock Prompt Management docs.",
    "remediation_target": "docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day01-order009-prompt-fundamentals-structured-output.md"
  },
  {
    "status": "draft",
    "official_exam_code": "AIP-C01",
    "accelerated_day": "Day 1",
    "curriculum_order": "Day01-order009",
    "topic": "Prompt fundamentals, instructions, templates, and structured outputs",
    "knowledge_category": "Knowledge; Skill",
    "knowledge_type": "Conceptual; Procedural; Causal",
    "question_format": "multiple-response",
    "difficulty": "hard",
    "cognitive_demand": "judge",
    "stem": "A company is creating a reusable prompt template for customer-email classification. Which two prompt elements most directly reduce ambiguity for the model? (Select TWO.)",
    "options": [
      "A clear task instruction with the allowed classification labels.",
      "Definitions or examples that distinguish similar labels.",
      "A note that the model should use any label it finds creative.",
      "A hidden assumption that downstream code will infer missing fields.",
      "An instruction to ignore all customer text if it is difficult."
    ],
    "correct_answer": ["A", "B"],
    "rationale_correct": "Explicit task framing, label set, definitions, and examples reduce ambiguity and make outputs easier to evaluate.",
    "rationale_distractors": {
      "C": "Invented labels break classification consistency.",
      "D": "Downstream code should not guess missing output structure.",
      "E": "Ignoring difficult inputs is not a valid classification strategy."
    },
    "misconception_tags": ["ambiguous-labels", "downstream-parser-will-fix-it"],
    "source_trace_needed": "AIP-C01 Task 1.6 and Day 1 prompt fundamentals artifact.",
    "remediation_target": "docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day01-order009-prompt-fundamentals-structured-output.md"
  },
  {
    "status": "draft",
    "official_exam_code": "AIP-C01",
    "accelerated_day": "Day 1",
    "curriculum_order": "Day01-order009",
    "topic": "Prompt fundamentals, instructions, templates, and structured outputs",
    "knowledge_category": "Knowledge; Skill",
    "knowledge_type": "Conceptual; Procedural; Causal",
    "question_format": "multiple-choice",
    "difficulty": "hard",
    "cognitive_demand": "diagnose",
    "stem": "An application uses the same prompt template for refund, fraud, and shipping questions. The model often answers outside the intended domain and mixes policies. Which prompt-design issue should be addressed first?",
    "options": [
      "The prompt lacks domain boundaries, task-specific instructions, and routing or context rules for different request types.",
      "The prompt is too structured; removing constraints will make the model infer the correct policy domain.",
      "The model needs a higher top-p value because policy mixing is caused only by narrow sampling.",
      "The application should stop using templates because every prompt must be handwritten by an operator."
    ],
    "correct_answer": "A",
    "rationale_correct": "Domain boundaries, routing/context rules, and task-specific instructions are needed when one application handles different policy areas.",
    "rationale_distractors": {
      "B": "Fewer constraints would likely increase mixing.",
      "C": "Sampling settings do not define policy routing.",
      "D": "Reusable templates are useful when designed with the right variables and constraints."
    },
    "misconception_tags": ["one-prompt-for-all-domains", "sampling-fixes-policy-routing"],
    "source_trace_needed": "AIP-C01 Task 1.6 and Day 1 prompt fundamentals artifact.",
    "remediation_target": "docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day01-order009-prompt-fundamentals-structured-output.md"
  },
  {
    "status": "draft",
    "official_exam_code": "AIP-C01",
    "accelerated_day": "Day 1",
    "curriculum_order": "Day01-order010",
    "topic": "Basic GenAI evaluation concepts and golden datasets",
    "knowledge_category": "Knowledge; Skill",
    "knowledge_type": "Conceptual; Procedural",
    "question_format": "multiple-choice",
    "difficulty": "hard",
    "cognitive_demand": "select",
    "stem": "A team wants to evaluate a GenAI assistant before changing its prompt template. They have only three examples that all represent happy-path customer questions. What is the best next step for the golden dataset?",
    "options": [
      "Add representative edge cases, failure modes, ambiguous inputs, and expected evaluation notes before using it as a regression signal.",
      "Use the three examples because a golden dataset should be as small as possible.",
      "Replace the examples with one long prompt that asks the model whether it is accurate.",
      "Evaluate only average response length because shorter answers are always better."
    ],
    "correct_answer": "A",
    "rationale_correct": "A useful golden dataset should cover representative success cases, edge cases, and known failure modes with expected behavior.",
    "rationale_distractors": {
      "B": "A tiny happy-path set is not enough for regression confidence.",
      "C": "Self-judgment is not a substitute for defined test cases.",
      "D": "Response length alone is not a quality metric."
    },
    "misconception_tags": ["happy-path-only-evaluation", "self-evaluation-as-proof"],
    "source_trace_needed": "AIP-C01 Task 5.1 and Amazon Bedrock model evaluation docs.",
    "remediation_target": "docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day01-order010-basic-evaluation-golden-datasets.md"
  },
  {
    "status": "draft",
    "official_exam_code": "AIP-C01",
    "accelerated_day": "Day 1",
    "curriculum_order": "Day01-order010",
    "topic": "Basic GenAI evaluation concepts and golden datasets",
    "knowledge_category": "Knowledge; Skill",
    "knowledge_type": "Conceptual; Procedural",
    "question_format": "multiple-response",
    "difficulty": "exam-plus",
    "cognitive_demand": "judge",
    "stem": "After a prompt update, a GenAI assistant scores the same on broad human preference ratings but fails more often on refund-policy questions. Which two evaluation changes would make this regression easier to detect next time? (Select TWO.)",
    "options": [
      "Tag golden-dataset cases by policy area or capability so regressions can be segmented.",
      "Include expected-answer criteria for refund-policy cases rather than only general preference scores.",
      "Remove domain tags because aggregate scores are easier to read.",
      "Use only one evaluator comment for the entire dataset to keep review fast.",
      "Increase temperature during evaluation so the model has more chances to answer correctly."
    ],
    "correct_answer": ["A", "B"],
    "rationale_correct": "Segmentation and explicit expected criteria help reveal focused regressions that aggregate preference ratings can hide.",
    "rationale_distractors": {
      "C": "Removing tags makes localized regressions harder to find.",
      "D": "One broad comment is not enough diagnostic evidence.",
      "E": "Changing sampling during evaluation can obscure comparison rather than isolate regression."
    },
    "misconception_tags": ["aggregate-score-hides-regression", "evaluation-after-deployment"],
    "source_trace_needed": "AIP-C01 Task 5.1 and Day 1 golden dataset artifact.",
    "remediation_target": "docs/Pilot1/aip-c01/student-kit/accelerated-7-day/day-01-artifacts/day01-order010-basic-evaluation-golden-datasets.md"
  }
]
```
