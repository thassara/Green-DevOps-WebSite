# Source-of-truth and page plan

## Scope and source review

This repository is an academic information website, separate from the Green DevOps research system. Buildless HTML5/CSS3, with vanilla JavaScript only for accessible mobile navigation. Seven required pages. Deployable files must remain below the guideline's 20 MB limit. No runtime dependency, database, operational controls, or contact submission service.

The actual supplied files are Website.pdf and GreenDevOps_Journal_Revised_Phase1 (1).docx; the similarly named files in the brief were not separate inputs. All 16 guideline pages, 29 Proposal slides, 22 PP1 slides, 12 PP2 slides, and 282 ordered journal blocks (including all references and validity/data-availability sections) were reviewed. Embedded figure inventories/contact sheets and spreadsheet-backed progress/feedback tables supplement text extraction. Source review notes are under each source directory here.

## Authority and conflicts

- Website.pdf pp. 8–16: navigation, academic page content, expandable assessments, hosting budget and allowed technologies.
- Revised journal: final methodology, component implementation, evaluation and limitations. It is a supplied manuscript, with no confirmed publication status.
- PP2: integration and late-stage presentation history, not authority over final implementation prose.
- PP1: implemented prototypes and forward plans as presented at PP1.
- Proposal: initial component allocation, proposed methods and evaluation direction.
- Team identities: Proposal slide 4; portraits: PP1 slides 7, 11, 15, 18.
- Assessment dates remain 'To be confirmed': Proposal mixes February/March, PP1 mixes May dates and a reused March date, PP2 mixes August dates and May templates. Slide footer dates are not certified assessment dates. No marks supplied.
- Journal architecture has earlier XGBoost labels; final Deployment prose specifies ReAct. Use a semantic conceptual architecture based on final prose, with optional clearly labelled historical diagram in the journey.
- Monitor implementation says Extended Isolation Forest; reported results say Isolation Forest. Preserve distinction, without attributing detection counts to an unverified variant.
- Journal references include duplicate [31] and incomplete entries. Use selected well-described entries, retaining source numbering and avoiding invented bibliographic detail or URLs.

## Page/content map

| Page | Sections and source |
|---|---|
| Home | Exact project identity (brief, Proposal s1/s4); academic overview/motivation/gap (journal Introduction); four stages and conceptual lifecycle (journal Methodology); research journey (all decks); clearly scoped findings (journal Results); academic quick links |
| Domain | Background, literature by topic, problem/gap, verbatim RQ1–RQ4 and objectives (journal Introduction/Related Work); contribution, methodology, all four component methods/algorithms/implementation/integration (Methodology/Implementation); final conceptual architecture and LSTM source figure; verified technology groups; evaluation/results, discussion, limits, future work and selected references |
| Milestones | Native details timeline: Proposal (initial architecture, XGBoost direction); PP1 (selective Maven release, deployment profiler, prediction/scaling prototype, monitoring baseline/IF prototype, panel feedback and future plans); PP2 (integrated gap/objective, demonstration, architecture, academic commercialization); manuscript/evaluation stage (journal); separate Final Assessment and Viva placeholders. Do not infer assessment completion from file existence. |
| Documents | Stage-based archive, supplied revised journal and presentation links; Project Charter, Proposal Document, checklists, main and individual final reports/supporting documents marked Not yet added; publication status unconfirmed. |
| Presentations | Proposal, PP1, PP2 available as optimized static PDFs if export succeeds; original slide counts and source filenames in provenance; static export omits embedded video playback. Final presentation pending. |
| About Us | Four verified researchers, IDs, component contributions and source portraits; institution/faculty/project details; missing emails/supervisors explicitly pending |
| Contact Us | Institutional/project identity and genuine missing-contact placeholders; labelled name/email/subject/message form layout with disabled send control and explicit no-delivery notice |

## Result contract

- LightGBM macro F1 0.9787: five-fold time-series cross-validation, not emissions reduction.
- Release 47.7% mean wall-clock reduction: 10 paired Jenkins runs on identical commits; 39.9% median. 90.4% test skip rate = 13 of 136 possible test executions performed.
- LSTM R² 0.946 and MAPE 3.28%: unseen Bitbrains fastStorage data, not a production scaling outcome.
- Monitor: 21 Jenkins runs, 63 stage records; 8 statistical flags and 6 Isolation Forest flags, not verified anomaly accuracy. Estimated totals 0.001163 kWh and 0.000502 kgCO₂e.
- Prophet MAPE approximately 51% must accompany the forecasting limitation.
- No measured deployment percentage, integrated carbon-saving percentage, approved assessment marks, confirmed public repository, or publication claim.

## Design and delivery

Off-white paper, forest green, muted olive accents, charcoal text, serif display headings with system sans-serif body. Editorial, research-oriented layouts, substantial whitespace and modest cards. Lightweight HTML/CSS lifecycle visual, source-derived figures and portraits. Responsive grids, sticky desktop Domain contents, native details, visible focus and skip links. No remote fonts or external asset requests.

Deploy root: index.html, domain.html, milestones.html, documents.html, presentations.html, about.html, contact.html, css/, js/, assets/. Internal _review/, _content/, tools/ and packaging outputs are excluded from university deployment. A deployment ZIP will contain only the site and host instructions.
