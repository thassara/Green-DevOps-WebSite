# Journal source review

Source: `C:\Users\MADUSHA\Downloads\GreenDevOps_Journal_Revised_Phase1 (1).docx`

Exact title: **An Integrated Green DevOps Framework for Sustainable Software Delivery and Operations**.

## Completeness and evidence rules

Read the entire document in its original XML order, including all references, Threats to Validity, and Data Availability after the references. Extracted all 282 body blocks (approximately 9,221 words), including headings, configuration example, and any table content (there are **no tables**). Inspected both embedded figures at native resolution. Verified footnote/endnote parts have no substantive text, footer contains page field text only, and the package has no comments part. `ordered_text.txt` contains the complete ordered transcription; stable `[NNN]` block identifiers below refer to that file, not guessed page numbers. `blocks.json` and `relations.json` preserve structure and image mapping.

No DOCX page rendering was performed: the resolved Windows dependency bundle does not provide bundled LibreOffice, and the skill prohibits use of the user's installed desktop LibreOffice. This limitation concerns page-layout QA, not content completeness. Do not claim page numbers. Both figures were visually reviewed.

Use the journal as the primary final narrative. Distinguish **reported experiment results**, **implemented/described capabilities**, and **intended/feasibility claims**. The journal's abstract/discussion contain stronger blanket claims than the numerical evaluation supports. No end-to-end measured carbon-saving percentage, independently established anomaly accuracy, deployment performance figure, quantified SLA result, or production-scale validation is present.

## Exact final research questions

Introduction → Research Questions [037–040]:

1. **RQ1 (Release):** To what extent can git-diff-based, module-level change-impact analysis, combined with a learned carbon-intensity classifier, reduce both unnecessary build/test execution and the carbon cost of necessary execution in CI/CD pipelines?
2. **RQ2 (Deploy):** How can real-time grid carbon-intensity signals and predictive analytics be incorporated into deployment scheduling to identify low-carbon deployment windows without degrading delivery performance?
3. **RQ3 (Operate):** How accurately can an LSTM-based model predict Kubernetes workload demand, and how can carbon-emission estimation and workload prioritization be integrated into scaling decisions to reduce environmental impact while preserving SLA compliance?
4. **RQ4 (Monitor):** How can sustainability monitoring be extended from measurement alone to historical baseline modelling and anomaly detection, enabling automatic identification of sustainability regressions across the Release, Deploy, and Operate stages?

## Exact final objectives

Introduction → Research Objectives [044] gives these five objectives in one paragraph:

1. Develop and empirically benchmark a module-level change-impact mechanism and a carbon-intensity classifier for Release-stage build/test scheduling.
2. Establish fine-grained deployment-stage carbon measurement and use predictive analytics to autonomously identify low-carbon deployment windows.
3. Develop an LSTM-based workload forecasting engine, a carbon-emission estimation engine, and a workload-prioritization mechanism, integrated into a runtime decision engine for sustainable Kubernetes scaling.
4. Construct historical sustainability baselines and a hybrid anomaly-detection mechanism capable of identifying sustainability regressions across Build, Test, and Deploy activity.
5. Evaluate the integrated framework's aggregate ability to reduce unnecessary compute and carbon emissions across the full delivery lifecycle while preserving delivery velocity, application performance, and SLA compliance, including identification of synergistic outcomes where environmental optimization also yields cost or performance benefits [16].

## Problem, gap, novelty

Introduction → Problem Statement [033]: repeated full builds/tests ignore change scope; immediate deployment ignores carbon intensity; reactive CPU/memory autoscaling ignores environmental impact and delay tolerance; monitoring lacks sustainability baselines and regression detection.

Introduction → Research Gap [035], Related Work → Research Gap [072–073]: research addresses selective testing, carbon timing, forecasting, scheduling, measurement, and anomaly detection separately; contribution claimed is integrated decision support and feedback throughout Release → Deploy → Operate → Monitor. Wording such as "no existing framework" is the authors' literature-review claim, not independently verified global novelty.

Novelty Statement [042] and Research Contributions [046]: joint lifecycle integration; Release empirically benchmarked selection plus carbon classification; fine-grained deployment carbon measurement and timing; LSTM + carbon estimation + SLA-aware prioritization in Kubernetes; statistical/Isolation Forest sustainability intelligence plus Sustainability Health Score.

## Release component

- **Problem:** redundant full-repository build/test work and carbon-blind timing. Introduction [033], Implementation → Release Stage [113].
- **Method:** git diff maps changed paths to owning Maven modules by longest-prefix match; Maven `-am` expands selected dependencies; documentation-only changes can bypass execution; shared/global changes trigger broader validation. Methodology → Release Phase [082–084], Implementation [113–145].
- **Algorithms:** module-level change-impact analysis; LightGBM classifier with 39 temporal/lag/rolling features from hourly national-grid data; Prophet short-horizon forecaster seeks a greener hour only when current grid is classified high-carbon. Delay is bounded to 8 hours for non-urgent builds; run now when no better window is found. [145]
- **Implementation:** self-contained Python package called from one Jenkins shell step or GitHub Actions workflow. YAML example uses `HEAD~1`→`HEAD`, shared `common-lib`, global triggers `pom.xml`, `.mvn/`, `mvnw`, `mvnw.cmd`, `settings.xml`; Maven goals `[clean, install]` and `[test]`, `also_make: true`; example carbon provider **mock**, zone `LK`, history minimum 3 hours, backfill enabled. [113–145]
- **Evaluation:** five-fold time-series cross-validation for LightGBM; 10 paired real Jenkins optimized/unoptimized runs on identical commits for CI efficiency. Results → CI/CD Optimization Performance [165–173].
- **Findings:** macro F1 0.9787; recall approximately 98%; approximately 96.2% SHAP importance from lag/rolling features; Prophet MAPE approximately 51% (weak forecast accuracy). Mean total wall-clock reduction 47.7%, median 39.9%; directly controlled build+test phases mean 66.1%, median 82.8%. Documentation/no-op average time saving 92.4%, single-module 60.4%, two-module 41.2%. 13/136 tests executed, 90.4% skipped; mean analysis overhead 1.02 s (approximately 1.2% optimized total duration).
- **Integration:** optimized artifacts, build metadata, sustainability data pass to Deployment; timing can use monitoring feedback. [084, 104]
- **Limits:** classifier baseline models are said to be outperformed but not named or quantified; classification sample sizes and class thresholds are absent. CI time reductions must not be relabelled measured energy/carbon reductions. 51% Prophet MAPE must not be hidden behind the stronger classifier metric.

## Deployment component

- **Problem:** production promotion follows build completion without considering current grid carbon. [033]
- **Method:** collect deployment CPU/memory/network telemetry; estimate energy through software power models; combine grid intensity with sustainability accounting; evaluate timing, operational stability and deployment strategy; defer non-critical releases within acceptable constraints. Methodology → Deployment Phase [086–089].
- **Algorithms:** final Implementation prose specifies an AI agent using **ReAct** (Reasoning and Acting), framed as an **MDP**, using grid conditions, system load and historical strategy performance. Select **Recreate, Rolling, Canary** using infrastructure-overlap considerations. [147,149]
- **Implementation:** Kubernetes Node Affinity, Taints and Tolerations steer workloads toward suitable infrastructure. Canary is described for reduced initial spikes in medium-carbon periods; Recreate for low-carbon maintenance windows. [149]
- **Evaluation/findings:** included in integrated implementation and monitoring data, but **no standalone numerical deployment experiment**, comparator or quantified savings is reported in Results [159–200]. Say the framework describes/implements decision support; do not claim a validated percentage or experimental superiority.
- **Integration:** receives successful builds/artifacts; passes deployment profiles, carbon estimates and recommendations into Operate. [089]
- **Diagram discrepancy:** embedded architecture still says **XGBoost AI Model / AI Decision Engine** and Deployment Energy Profiler; final prose says ReAct/MDP. Figure 2 ReAct loop is only a placeholder [148]. Use final prose for website narrative, explain diagram discrepancy in internal source notes.

## Operation component

- **Problem:** reactive Kubernetes autoscaling acts after threshold breaches and ignores carbon and workload urgency. [033]
- **Method:** gather CPU, memory, request rates, pods and latency; forecast demand; estimate carbon of candidate actions; classify job urgency; combine in Runtime Decision Engine. Methodology → Operation Phase [091–096].
- **Algorithms:** **LSTM** short-term forecasting; **Carbon Estimation Engine**; **Job Priority Engine**; **Runtime Decision Engine** produces Scale Up, Scale Down, Maintain, Delay Jobs. High priority executes immediately; medium may defer only if service quality remains unaffected; low-priority batch/maintenance can shift to cleaner windows. [095,151,153]
- **Implementation figure:** `image2.png` at [152], embedded caption **Figure 4. LSTM Workload Prediction Architecture**. Inputs CPU%, memory%, requests/s, active pods, historical metrics; sequence length **12**, sampling **30 s**, history **6 min**, prediction **next 30 s**. LSTM → dropout → three fully connected layers (ReLU, ReLU, Linear) → predicted CPU utilization, load level Low/Medium/High, recommended pods. Figure shows dropout range **0.2–0.5** (not a verified selected optimal hyperparameter).
- **Evaluation:** Bitbrains **fastStorage** dataset; unseen test data; no train/test sample sizes stated. Results → Runtime Workload Prediction and Operational Intelligence [175–179].
- **Findings:** **R² = 0.946**, **MAPE = 3.28%**, plus successful operational recommendation generation. HPA comparison is **functional**, showing forecasting/carbon/priority/SLA awareness; no quantitative scaling, response latency, energy reduction or SLA violation comparison is reported.
- **Integration:** inputs deployment profiles and telemetry; outputs predictions, workload classes and carbon-aware recommendations to Monitoring. [096,104]
- **Limits:** model accuracy on a trace is evidence of forecast feasibility, not measured emissions or production SLA preservation. Implementation simplifies priorities to Immediate/Delayable while methodology spells out High/Medium/Low; describe these as urgency classes rather than claim a precise fixed interface.

## Monitoring component

- **Problem:** observability reports performance/utilization but lacks historical sustainability context and regression detection. [033]
- **Method:** central historical repository ingests metrics across stages; estimate energy/carbon; separate Build/Test/Deploy baselines; statistical Z-scores and multidimensional Isolation Forest; aggregate **Sustainability Health Score (SHS)**. Methodology → Monitoring Phase [098–101].
- **Algorithms:** resource-based/CPU power estimation; energy × regional carbon intensity with **PUE** adjustment; statistical deviations/Z-score; stage-specific unsupervised **Isolation Forest**. Implementation [157] says **Extended Isolation Forest**; Results [191–193] says **Isolation Forest**. Use "Isolation Forest-based" unless resolving implementation variant from another source. SHS has scale **0–100**, but formula/weights are absent. [155,157]
- **Implementation:** Prometheus and Grafana dashboards described; no dashboard screenshot embedded (placeholder [158]); anomaly-process Figure 4 is also a placeholder [156]. Features include CPU utilization, duration, infrastructure overhead, estimated energy/emissions and carbon intensity. [191]
- **Evaluation:** **21** real Jenkins executions → **63** stage records (Build, Test, Deploy). Data fields include duration, processor use, overhead, energy, carbon, intensity, status, timestamp. Results → Sustainability Monitoring and Anomaly Detection [181–193].
- **Findings:** Deploy highest mean CPU/energy/carbon, Build lowest, Test intermediate. Total **estimated** energy **0.001163 kWh**, emissions **0.000502 kgCO₂e** over that monitoring period. **8 statistical flags** (Build 4, Test 3, Deploy 1), **6 Isolation Forest flags** (stage distribution not supplied). These are anomaly counts, not validated recall/precision or unique combined flags.
- **Integration:** SHS, carbon-efficiency assessments and alerts feed future release scheduling, deployment timing, scaling and priorities. Feedback Loop [103–105].
- **Limits:** no labelled anomaly ground truth or comparative detection accuracy; no SHS benchmark value/formula. Do not present IF's 6 vs Z-score's 8 as a measured superiority result or sum them to 14 distinct anomalies.

## Architecture and data flow

Methodology → Integrated Green DevOps Architecture [079–080], Feedback Loop [103–105], Implementation → Integrated Architecture Overview [110–111]:

**Source commit → selective Release and bounded carbon timing → carbon-aware Deployment → predictive Operation → historical Monitoring → feedback to prior decisions.**

Common infrastructure: Oracle VM, Ubuntu, **K3s Kubernetes**, Jenkins, Python, Docker; ElectricityMap/Maps and WattTime named as live carbon-signal API sources, with historical heuristic fallbacks for outages. [110]. Do not imply the YAML mock provider demonstrates live API use in every experiment.

`image1.png` (1429×982) is the actual integrated architecture figure embedded after Implementation overview, linked as `rId8`. A convenience exact copy is `architecture-source.png`. The original contains a public-looking IP/Jenkins endpoint; do not add such infrastructure endpoints to a website. It has transparent/black background and small labels; a readable code-native redraw is preferable. It includes legacy XGBoost deployment labels and dataset labels; redraw using final prose and retain an internal provenance note. `image2.png` (1430×814) is the LSTM architecture.

## Numeric claims ledger

| Value | Verified scope and comparator | Source |
|---|---|---|
| 0.9787 macro F1; ~98% recall | Tuned LightGBM carbon classification, 5-fold time-series CV; unspecified baseline models | Results → Carbon-Intensity Classification [165] |
| ~96.2% | SHAP importance attributable to lag and rolling-window features | [166] |
| ~51% MAPE | Supplementary Prophet forecast; acknowledged weakness | [167] |
| 47.7% mean; 39.9% median | Total pipeline wall-clock reduction, 10 paired Jenkins runs on identical commits, optimized vs unoptimized | [169–170] |
| 66.1% mean; 82.8% median | Build/test phase time savings only | [170] |
| 92.4%; 60.4%; 41.2% | Average execution-time savings for doc/no-op, one-module, two-module change scopes respectively | [171] |
| 13/136; 90.4% | Tests executed / possible; test-skip rate across benchmarks | [172] |
| 1.02 s; ~1.2% | Mean optimization analysis overhead and share of optimized total duration | [172] |
| 0.946 R²; 3.28% MAPE | LSTM prediction on unseen Bitbrains fastStorage test data | [175–176] |
| 21 runs; 63 records | Jenkins monitoring sample across Build/Test/Deploy | [181] |
| 0.001163 kWh; 0.000502 kgCO₂e | Total **estimated** monitored energy/emissions, not reductions | [185] |
| 8 (4/3/1) | Statistical anomaly flags (Build/Test/Deploy) | [188] |
| 6 | Isolation Forest anomaly flags; overlap and validation unknown | [192] |
| 39; 8 h | Release feature count; maximum permitted build delay | Implementation [145] |
| 12; 30 s; 6 min | LSTM sequence length; sampling/prediction horizon; history | Embedded Figure 4 [152] |
| 0–100 | SHS scale; no observed SHS result or formula | Implementation [157] |

The introduction's **2–4% global emissions**, **70 billion kWh**, literature's **10–30%**, **2–15%**, **30–45%** are background claims from cited literature [031,063,068], **not this project's results**. Omit unless independently checked and clearly attributed.

## Limitations and future work

Discussion [209–210]: utilization-based energy estimates can err; dependence on external carbon API availability/accuracy; evolving workloads require retraining; broader industrial validation needed. Future work: improved carbon forecasting, reinforcement-learning optimization, embodied carbon/infrastructure lifecycle metrics, diverse cloud environments and production-scale evaluation.

Threats to Validity [279]: internal validity affected by energy estimation/workload variability; external validity limited to one experimental environment; construct validity depends on sustainability metric and SHS selection; small samples constrain conclusion validity. Interpret unvalidated areas as **feasibility evidence**.

Data Availability [281]: Bitbrains public; code/configuration/models/experimental artifacts **can be made available on reasonable request or through a public repository in final publication**. This does not establish an existing public repository URL, model download, dataset link, or published journal status. Do not invent links.

## Literature groupings

Follow the journal's actual Related Work headings [050–073], not a generic article list:

1. **Sustainable Software Engineering and Green DevOps:** Karlskrona sustainability design [47]; GREENSOFT lifecycle assessment [48]; Green DevOps/SusDevOps [49,50,20]; governance/objectives [54]; sustainability review [51].
2. **Energy Measurement, Carbon Accounting, and Sustainability Monitoring:** resource-based energy [17,60]; SCI [52, also 6]; Cloud Carbon Footprint [53]; PUE/CUE and environmental metrics [16]; anomaly/baseline context [57–59].
3. **Sustainability Challenges in CI/CD:** regression selection [1], selection/minimization/prioritization survey [2]; Maven [3]; CI caching [22]; computational overhead [56,17].
4. **Carbon-Aware Computing, Workload Scheduling and Sustainable Deployment:** datacenter carbon timing [4]; bounded workload shifts [5]; regional carbon signals [18,23]; cloud intensity [24]; FREEDA [25]; continuous delivery [26]; Kubernetes deployment [31].
5. **AI-Driven Resource Management, Runtime Monitoring, and Sustainability Intelligence:** workload forecasting/resource management [41,42]; multi-objective AI [19]; sustainable cloud engineering [43]; anomaly survey [57]; Isolation Forest [58]; Extended IF [59].
6. **Integrated research gap:** lifecycle integration combining measurement, monitoring, anomaly detection, scheduling, prediction, and autonomous decisions [072–073].

`references.txt` retains **all 62 reference entries exactly as supplied**, with original numbering. There is a duplicated [31] and abbreviated/duplicated entries. Reference validity has **not** been independently web-verified. Do not fabricate DOI/URLs or silently "fix" author names by guessing.

## Source inconsistencies and missing content

1. **Deploy algorithm:** integrated image says XGBoost; final Implementation says ReAct/MDP. Prefer the latter in final narrative.
2. **Monitor algorithm:** Implementation says Extended IF; Results says IF. Use generic Isolation Forest-based phrasing.
3. **Carbon calculations:** implementation calls modeled emissions "exact" [155], but Discussion/Threats explicitly acknowledge estimation errors. Always say **estimated**.
4. **Evidence strength:** abstract/discussion claim preserved velocity/performance/SLA; evaluation supplies no end-to-end causal carbon reduction or quantified SLA comparison. Present goals/capabilities separately from measured results.
5. **Missing figures:** ReAct loop, multidimensional anomaly process and Grafana dashboard are literal placeholders [148,156,158]. Do not pretend they are supplied artifacts.
6. **Figure numbering:** actual LSTM image caption is Figure 4, while anomaly placeholder also says Figure 4; integrated image is referred to as Fig. 1 but no surrounding caption paragraph exists.
7. **Reference numbering/quality:** [31] appears twice (Canary paper and Poojary Kubernetes paper). ReAct [29]/[32], Kubernetes [31]/[42], carbon scheduling [18]/[39], AI resource management [19]/[41], cloud engineering [23]/[43], systematic review [17]/[45], SCI [6]/[52] appear overlapping/duplicate. Several Methodology citations appear misaligned with reference topics (e.g. energy models cite XGBoost/Optuna).
8. **No contacts/team:** no author roster, student IDs, emails, supervisors, institution, or project URL in body/figures, apart from an infrastructure IP. Obtain people/contact data from the supplied presentations if present.
9. **No tables:** numbers occur in narrative; do not cite nonexistent table numbers.
10. **Publication status:** title/structure show a manuscript; no journal acceptance/publication/date evidence. Do not label as published/peer-reviewed from this file alone.

## Suggested website-safe results prose

"Across ten paired Jenkins benchmarks, selective execution reduced mean pipeline wall-clock time by 47.7% and skipped 90.4% of possible test executions. The carbon-intensity classifier achieved macro F1 0.9787 in five-fold time-series validation. On unseen Bitbrains fastStorage data, the LSTM workload model achieved R² 0.946 and MAPE 3.28%. Monitoring covered 21 Jenkins runs and 63 stage records, demonstrating stage-specific baselines and anomaly detection. Broader production validation and direct energy measurement remain future work."

The weak Prophet forecast (~51% MAPE), small monitoring sample, estimated emissions and missing Deployment quantitative evaluation should be available in component/evaluation detail rather than omitted from research limitations.
