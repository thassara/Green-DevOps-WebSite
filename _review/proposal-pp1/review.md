# Proposal and PP1 source review

Read-only review completed before website implementation. Source slide references below use actual package order, **not the sometimes incorrect displayed page number**. Reviewed every slide's XML text (29 Proposal slides, 22 PP1 slides), associated image inventory/contact sheets, all substantive diagrams at full resolution, and all six embedded spreadsheet tables. The PP1 final slide contains a 120 MB embedded video: its globe poster was inspected, but playback contents were not reviewed. No speaker notes were present.

## Files and artifacts

- Proposal original: `C:\Users\MADUSHA\Downloads\GreenDevOps (ProposalP).pptx.pptx`, 13,787,151 bytes.
- PP1 original: `C:\Users\MADUSHA\Downloads\GreenDevOpsPP1.pptx`, 127,828,358 bytes.
- Complete ordered text: `proposal/text.txt`, `pp1/text.txt`.
- Complete underlying spreadsheet text: `proposal/embedded-tables.txt`, `pp1/embedded-tables.txt`.
- Inventories include source slide association: `proposal/inventory.json`, `pp1/inventory.json`.
- All raster/vector images extracted into the respective `media` folders. Six contact sheets accompany them.

## Verified identity and portraits

Proposal slide 4 explicitly associates all four team members, IDs, and components. PP1 individual cover slides confirm the same assignments and list Software Engineering specialization.

| Name to render | Student ID | Component | Explicit PP1 slide / portrait asset |
|---|---|---|---|
| Mendis J.D.L. | IT22110084 | Release management | 7 / `pp1/media/image16.jpeg` (384×384) |
| Rathnayake D.M.B.H. | IT22149930 | Deployment | 11 / `pp1/media/image21.jpeg` (298×383) |
| Thassara M.P.M. | IT22281432 | Operations | 15 / `pp1/media/image29.jpeg` (360×360) |
| Kodithuwakku I.P. | IT22189776 | Monitoring | 18 / `pp1/media/image39.jpeg` (334×401) |

The Operations individual slides write `M.P.M Thassara`; the Proposal roster writes `Thassara M.P.M.`. These are order variants for the same verified ID. Use roster convention consistently. No supervisor, co-supervisor, team email, or phone information appears in these two decks. SLIIT and R26-SE-027 appear on their covers. The title has source typo `Pipieline`; normalize to the user's requested `Green DevOps - Energy Efficient CI/CD Pipeline`.

## Proposal stage: original direction

**Motivation (slides 2–3):** Conventional delivery emphasizes speed, triggering full builds/tests for small changes. The project proposed addressing resource waste and environmental impact across release, deployment, operations, and monitoring. Slide 2 contains external background claims (ICT 2–4% CO₂, 90% CPU waste, 35% annual cloud-cost increase) with numeric citation markers but no complete bibliography; do not present these as project results, and prefer final journal-supported background instead.

**Research gap (slide 3 embedded table):** The full table is recoverable although its preview is cropped. It contrasts cloud-level carbon monitoring with pipeline-level monitoring; carbon scheduling alone with CI/CD workflow optimization; CPU/memory HPA with predictive carbon-aware scaling; full build/test automation with change impact analysis/artifact reuse; rule-based decisions with XGBoost/LSTM; and separate optimizers with an integrated four-stage approach. These are the **Proposal's framing**, not independently verified current-market claims.

**Release (slides 5–9):** Proposed change impact analysis, artifact reuse, incremental builds, risk-based selective testing, and carbon-aware scheduling. The proposed scheduler uses XGBoost (s7). Candidate tools include Jenkins/GitHub Actions, Git commit analysis, Maven/Gradle, Nexus, Docker (s7), with GitLab, npm, Artifactory, WattTime also described as infrastructure options/dependencies (s9). Evaluation plan compares pipeline duration, rebuilt modules, and CPU use against traditional CI/CD (s8). The release architecture image (s9, image19.png) shows feedback from monitoring into change analysis and the carbon scheduler, then execution and deployment artifacts.

**Deployment (slides 10–14):** Proposed Deployment Energy Profiler and AI Green Deployment Decision Engine for timing and strategy selection. Images compare a default pipeline with profiling → AI → optimized strategy/time (s12, images22/23.png). The decision-engine architecture (s13, image24.png) accepts deployment type, urgency, target environment, time, carbon intensity, history, and OCI load. Outputs such as `42/100`, `9 hours`, `23:00`, and rolling deployment are **illustrative architecture examples**, not evaluated outcomes. It proposes profiling duration/CPU/memory, estimating energy/carbon, storing history, and evaluating ML prediction accuracy and strategy energy/carbon performance. Data sources are an Azure public dataset and experimental deployment logs (s14).

**Operations (slides 15–19):** Proposed AI workload prediction plus energy/carbon-aware scaling and job prioritization. LSTM appears in the s17 embedded table and s19 architecture (image37.png). Pipeline: collect Kubernetes CPU/memory/request rate, clean/normalize, predict, estimate energy/carbon, delay low-priority background tasks, select scaling. Candidate platform: Kubernetes, Prometheus, Oracle Cloud, Python. Validation plan compares prediction accuracy, energy, resource utilization, response time, and Kubernetes HPA (s18). S15 uses past-tense contribution wording, but this is a proposal-stage account; do not turn it into final verified implementation/results.

**Monitoring (slides 20–24):** Proposed pipeline-level sustainability metrics and datasets. Design Science Research: problem identification, artifact design, implementation, evaluation (s22). Python, psutil, Jenkins/GitHub Actions, ElectricityMaps, OCI. Pipeline metrics → energy estimate → carbon estimate → dataset (s23). Evaluation plan: per-stage energy, estimated carbon, utilization, monitoring overhead. Monitoring architecture (s24, image44.png) provides feedback to release, deployment, operations. This stage does not yet describe the later LLM analyst assistant in its text.

**Academic commercialization/planning (slides 25–28):** Proposed audience: cloud-native companies, large CI/CD enterprises, DevOps/SRE engineers, sustainability officers (s25). Embedded budget is an estimate: development LKR 1,200,000, infrastructure/hardware LKR 500,000, maintenance/marketing LKR 750,000, total LKR 2,450,000. No realized cost, customers, or commercial readiness is established. Planned WBS includes literature, gap, architecture, model development, integration, evaluation, reporting and publication submission. These are plans, not completed publication evidence.

## PP1 stage: implementation and feedback

**Panel feedback (slide 2 embedded table):**

- Release: improve time management; component is fine. Response: implementation unchanged, found a suitable ML dataset, practiced with a timer.
- Deployment: component is fine; implementation unchanged.
- Operations: component is fine; implementation unchanged.
- Monitoring: clarify ML technique. Response identifies Isolation Forest (`Isolation Forrest` typo in source).

**Implementation-to-next-phase table (slide 3 embedded table):**

| Component | PP1 recorded progress | Planned PP2 work at that time | Planned final work at that time |
|---|---|---|---|
| Release | Change impact analyzer, selective build execution, selective test execution done | Carbon-aware AI model for build-location suggestion | Fine-tune system |
| Deployment | Energy profiler and deployment comparator implemented | Train/implement AI decision engine and integrate release | Fine-tune profiler/AI engine |
| Operations | Future workload prediction and pod scaling engine implemented | Job prioritization, finish testing | Fine-tune and integrate system |
| Monitoring | Monitoring framework, statistical anomaly detection, Isolation Forest prototype | LLM Sustainability Analyst Assistant | Fine-tune LLM and integrate system |

This table is important source evidence unavailable from normal slide text extraction; the in-slide preview is cropped on its right and lower edges.

**Infrastructure/integration (slides 5–6):** PP1 depicts an OCI jump server/reverse SSH connection to a local Ubuntu laptop (s5 image14.png), then Jenkins release/deploy/operate/monitor flow integrated with Docker, Kubernetes, database history, and ElectricityMaps/WattTime (s6 image15.png). S6 labels the deployment AI as XGBoost and includes Azure deployment data. Its architecture is useful historical evidence but combines current implementation and intended modules; s3 clarifies actual completion. Infrastructure diagrams contain specific IP/port details which add little academic value on the website; an accessible content summary is preferable to reproducing environment administration instructions.

**Release (slides 7–10):** Focus becomes a Jenkins plugin/pipeline performing commit impact analysis, selective builds/tests, and proposing greener time/region suggestions (s8). By s10 the implemented stack is Jenkins Pipeline/Groovy/Maven/GitHub; Git diff + Python optimizer for changed Maven modules; `-pl`/`-am` and Surefire for selection; REST JSON into a Flask/SQLite research dashboard. The s9 diagram (image17.png) specifically shows Python DAG analysis, repository POM dependency trees, dynamic Maven commands, Docker outputs, and metrics. The carbon-aware location model remains future PP2 work per s3.

**Deployment (slides 11–14):** Energy profiler is concrete progress: profiler.py measures CPU/memory; energy_calculator.py estimates kWh; carbon_api.py retrieves intensity; carbon_calculator.py estimates CO₂; db_sync.py stores it (s14). Screenshot image27.png adds every-10-second sampling, SQLite sync, ElectricityMaps then WattTime fallback, and a Sri Lankan time-of-day heuristic (peak ~550/off-peak ~420 gCO₂/kWh). The screenshot's one-run figures (3.4 minutes, 5.6% average CPU, 24 samples) describe a displayed PP1 demonstration and are not final evaluation claims. The source's phrase “real CO₂ number” should be rendered as **estimated emissions** because the method is a model. AI timing/strategy diagram is still the earlier proposed design (s13).

**Operations (slides 15–17):** Same LSTM prediction/carbon optimization/job-priority concept, now with recorded implemented prediction and pod scaling per s3. The s16 emphasis is proactive rather than reactive scaling while maintaining SLA performance. The s17 diagram (image37.png) connects LSTM forecasting and energy/carbon estimation to resource control and pod scaling. Job prioritization is explicitly next-phase work in s3.

**Monitoring (slides 18–20):** Expands beyond energy/carbon collection into statistical anomaly detection and the Isolation Forest prototype (s3), with the LLM analyst assistant planned next. S19 lists stage-level visibility, abnormal behavior, history analytics, and explanatory insights. S20 diagram (image40.jpeg) adds MongoDB Atlas, CPU proxy energy estimation, energy × carbon intensity, historical baselines, deviation/Z-score detection, Isolation Forest, a 0–100 sustainability health score, analyst assistant, and analytics dashboard. Do not describe every box as implemented at PP1; distinguish s3's progress from the broader architecture.

**End matter:** s21 thanks; s22 video poster. No final integrated evaluation results in the text of this deck.

## Dates and ambiguity

- Proposal s1/s4 and end slides show `2/24/2026` while many content slides show `17/03/2026`. These are slide labels, not a single verified assessment date.
- Proposal s26 Gantt image plans proposal presentation in **April 2026**, PP1 in **June 2026**, PP2 in **September 2026**, final presentation/viva in **November 2026**.
- Proposal s27 embedded WBS assigns proposal presentation to **March 2026**, conflicting with s26's plan. Excel date serials were decoded and indicate month starts (e.g. 46082 = 2026-03-01), not actual assessment days.
- PP1 cover and most slides show `5/7/2026`, individual covers `5/8/2026`, release content `5/10/2026`, and Operations cover retains `17/03/2026`. Month/day and day/month interpretation is not established. Do not select a precise PP1 milestone date.
- Both packages have template-like creation/modification metadata in **2006/2011**, which is irrelevant to project assessment dates.
- No allocated assessment marks are present. Use “Date to be confirmed” and “Marks to be confirmed” for milestone details; stage order remains clear.

## Recommended useful assets

- Team portraits: four verified paths above; existing small JPEGs already total about 159 KB and can be served at natural size or modestly optimized.
- Proposal release architecture: `proposal/media/image19.png`, 1736×1436, ~327 KB (s9).
- Proposal deployment decision architecture: `proposal/media/image24.png`, 1873×706, ~83 KB (s13); label it **proposed** and avoid elevating example numeric outputs.
- Proposal monitoring architecture: `proposal/media/image44.png`, 640×706, ~301 KB (s24).
- PP1 release flow: `pp1/media/image17.png`, 1252×500, ~78 KB (s9).
- PP1 operations flow: `pp1/media/image37.png`, 2043×753, ~126 KB (s17).
- PP1 monitoring flow: `pp1/media/image40.jpeg`, 2061×482, ~199 KB (s20).
- PP1 integrated architecture: `pp1/media/image15.png`, 2146×1475, ~415 KB (s6), with historical/current-progress caveat and environment addresses present.
- Use a small number of these, converted to optimized WebP or lossless PNG where readability requires it, with captions linking the stage/source. The final journal/PP2 architecture should supersede PP1 in final-methodology sections.
- Omit decorative backgrounds, technology-logo collages, duplicated cloud backgrounds, clipped table preview images, and the PP1 video from the deployable site. Reproduce table content as semantic HTML instead.

## Download feasibility

PP1 media `ppt/media/VAHEAi8gP4s.mp4` is **120,075,754 bytes**, nearly all the deck's size, leaving approximately 7.75 MB for package content (not an exported file-size guarantee). A PDF export without video should be far smaller and works for academic browsing, while the unmodified 127.8 MB PPTX cannot fit 20 MB hosting. The Proposal is 13.8 MB itself, largely due to oversized decorative raster backgrounds; exporting static PDF or preparing a clearly labeled optimized viewing copy can preserve research content far more economically. Do not silently alter original source presentations. Parent is coordinating PowerPoint PDF export. No website code was written by this review task.
