# PP2 source review

Source: `C:\Users\MADUSHA\Downloads\Green DevOps PP2.pptx.pptx`.
Reviewed all **12 slides**, every ordered text run, media inventory, meaningful source images, and both complete embedded Excel tables. Images on slides 3 and 5 are intrinsically cropped previews; complete table values were recovered from their embedded OLE spreadsheet packages. No source instructions were treated as website-authoring instructions.

## Primary findings for the site

- **Late-stage integration:** PP2 explicitly identifies independently optimized Green DevOps stages and disconnected carbon decisions as the gap (slide 7). Its objective is one framework with carbon-aware decisions across all four stages while preserving delivery velocity, performance and SLA compliance.
- **Lifecycle overview:** carbon-aware CI/CD in Release, AI deployment scheduling in Deploy, predictive autoscaling in Operate, and anomaly detection plus Sustainability Health Score in Monitor (slide 8). Nonfunctional focus is reliability/SLA compliance, delivery performance and environmental sustainability.
- **Problem motivation:** slide 6 describes green debt from rapid cloud-native/CI/CD growth and full builds/tests for small changes. Stakeholders are developers, DevOps/platform engineers, SREs and engineering managers. Numeric motivational claims on this slide are unsourced within the deck; **do not promote them as verified final results**.
- **Architecture/integration:** slide 10 shows Git commits feeding a Jenkins CI/CD pipeline connected to Release, Deploy, Operate and Monitor optimizers. Release change-impact analysis gates build/test execution and connects to a shared carbon-aware build/deployment scheduling layer. Deployment combines a Python energy profiler and an AI decision engine. Docker build/tag/push connects to Kubernetes. Operation consumes CPU, memory and request metrics, predicts workload, estimates carbon, prioritizes jobs and changes pod counts. Monitoring collects metrics, estimates energy/carbon and produces sustainability datasets. External carbon inputs are ElectricityMap and WattTime. History storage covers builds, deployments, server performance and sustainability measurements. Oracle Cloud/Ubuntu supplies the illustrated environment.
- **Research-history caveat:** the slide 10 diagram labels the deployment AI model **XGBoost**, which must remain historical evidence if the final journal specifies ReAct. Use the journal for final methodology.

## All-slide content map

| Slide | Content and appropriate use |
|---|---|
| 1 | Project identity: Green DevOps - Energy efficient CI/CD Pipeline, R26-SE-027, Sri Lanka Institute of Information Technology, IT4010 Progress Presentation 2. Displayed date 8/17/2026. Title contains a spelling error in “Pipeline”; use the user-approved corrected project identity on the site. |
| 2 | Agenda: problem/motivation, solution overview, system architecture/integration, commercialization, demo. Displayed date 8/17/2026. |
| 3 | Current progress and next phases. Complete PP1/PP2/Final table recovered from `ppt/embeddings/oleObject1.bin`. Footer 5/7/2026 is inconsistent with August PP2 content and likely reused, but this cannot be treated as an assessment date. Detailed table below. |
| 4 | Embedded MP4 with a server-room poster. Media has no extractable slide text. It illustrates the presentation/demo context; no unverified experimental finding should be inferred from the media. |
| 5 | PP1 comments. Complete table recovered from `oleObject2.bin`: no specific panel comments for any of the four components and implementation unchanged. Footer 5/7/2026. |
| 6 | Real-world problem and stakeholders. Discusses full-build waste and the need for carbon-aware automation throughout DevOps. Numeric claims are contextual presentation claims, not final evaluation findings. Date 8/17/2026. |
| 7 | Integrated research gap/objective and operational requirements. Date 8/16/2026. |
| 8 | Four-component integrated solution and nonfunctional focus. Date 8/16/2026. |
| 9 | Environment setup graphic: Oracle jump/bastion server, reverse SSH tunnel, local Lubuntu laptop behind NAT. Useful implementation context but not needed for main academic website architecture. Contains deployment addresses; avoid unnecessary replication on public-facing pages. |
| 10 | High-level architecture image. Original extracted at `media/image15.png` (1840 × 1348). Date 8/18/2026. Historical algorithm/ID inconsistencies noted below. |
| 11 | Academic commercialization concept: standalone modules, bundles and full suite, staged adoption and indicative subscriptions. Explicitly labels its pricing academic and contingent. Historical discussion only, **not an operating offer or subscription interface for the academic site**. |
| 12 | Thank-you slide and “Official Docs” hyperlink. Source target is `https://beliver-247.github.io/GreenDevOps_Official_docs/`; live availability was not checked. |

## Embedded progress table (slide 3)

The slide uses terse implementation/planning phrasing. Describe its columns as the deck's recorded stages rather than asserting every item was independently completed.

| Component | PP1 column | PP2 column | Final column (planned next work) |
|---|---|---|---|
| Release | Change Impact Analyzer, Selective Build Execution, Selective Test Execution done | Implement carbon-emission-aware AI model for build scheduling | Associate Jenkins libraries to generalize the system |
| Deployment | Energy profiler and deployment comparator implemented | Implement/train AI decision engine and integrate with Release | Fine-tune profiler and AI decision engine |
| Operation | Future workload prediction and pod scaling engine implemented | Job prioritization and finish testing | Fine-tune and integrate whole system |
| Monitoring | Monitoring framework, statistical anomaly detection, Isolation Forest prototype | Finalized Isolation Forest anomaly models | Implement ML-based Sustainability Analyst Assistant |

The **Sustainability Analyst Assistant is listed as future work here**. Do not claim it exists unless the final journal independently supports it.

## Team verification and source conflicts

Slide 5's recovered feedback table confirms:

- IT22110084: Release.
- IT22149930: Deployment.
- IT22281432: Operations.
- IT22189776: Monitor.

No member names, email addresses, photographs, supervisors or contact information are supplied in this deck. The architecture image mistakenly labels Operation **IT22239198**; use **IT22281432** from the user request and slide 5, subject to the other sources' verification. The architecture also says XGBoost for Deployment, while the final journal should determine final algorithms.

## Dates and marks

The deck does **not provide one unambiguous PP2 assessment date**. It contains August 16, 17 and 18, 2026, plus reused May 7, 2026 footers. For the milestone, display “Date to be confirmed.” A historical description may safely call this the PP2 stage and note that its slides contain August 2026 dates if useful. No marks/weightings are provided. No confirmed Final Assessment or Viva dates appear.

## Commercialization and demonstration framing

Slide 11 proposes modular subscriptions and an adoption sequence: pilot one module, validate carbon/cloud cost/SLA outcomes, integrate selected modules, then adopt the complete suite. This supports one sentence about academic consideration of adoption and lifecycle support in the PP2 milestone. It does not authorize a commercial-looking website, pricing section, signup, fake operational dashboard or purchase flow. The slide itself calls the prices indicative academic pricing.

The agenda announces a demo and slide 4 contains a video. This establishes **demonstration material in the PP2 presentation**; it does not substantiate numerical outcomes. Video audio/motion was not transcribed. The informational webpage does not need this heavy media to communicate the research.

## Asset inventory and optimization

- Original PPTX: **25,857,267 bytes**, already above a 20 MB entire-site budget.
- Embedded media: 17 items totaling 22,668,528 bytes, comprising 13 raster images, 3 SVGs and 1 MP4.
- Slide 4 video: **20,129,530 bytes** (20,112,231 compressed in ZIP). It accounts for most of the deck's size.
- Large remaining image: environment setup, `image14.png`, 1,429,307 bytes.
- Best high-level source architecture: `image15.png`, 387,007 bytes; usable as **PP2 historical architecture only** with caption noting the journal supersedes final methodology and team ID.
- Embedded fonts add roughly 6 MB uncompressed; source compression reduces them.
- A separately labeled **web reading edition PDF** exported by PowerPoint is the best lightweight download while preserving slide appearance, explicitly stating that embedded video does not play in the PDF. Do not imply this is the unchanged original PPTX.
- A video-free PPTX derivative is feasible around 5.7 MB before further optimization, but should clearly state that embedded video was omitted; preserve the original outside deployable site. Avoid silently deleting media from the only archive copy.
- Original architecture extracted unchanged with provenance in this folder. A website should prefer a cleaner final-journal conceptual architecture if available, since the PP2 source is dense and includes historical discrepancies.

Review artifacts: `slides.txt`, `slides.json`, `media-inventory.json`, `media-contact-1.jpg`, `embedded-tables.json`, extracted `media/`, and recovered `oleObject1.xlsx`/`oleObject2.xlsx`. Renderer import was attempted but failed on its OLE workbook handling; this limitation does not affect the completed XML, source-image and recovered-table review. No PowerPoint COM process was started by this reviewer.
