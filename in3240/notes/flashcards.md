# IN4240 — Software Testing Flashcards

Format: **Q** = question, **A** = answer. Study section by section or shuffle at random.

---

## Chapter 1 — Fundamentals of Testing

---

**Q:** What is the ISTQB definition of software testing?

**A:** The process of all software life-cycle activities, both **static** and **dynamic**, concerned with planning, preparation, and evaluation of software products to determine that they satisfy specified requirements, demonstrate fitness for purpose, and detect defects.

---

**Q:** Why is exhaustive testing impossible?

**A:** The number of possible inputs, states, and paths through any non-trivial system is astronomically large. Instead, use **risk** and **priorities** to decide where to focus effort.

---

**Q:** List and briefly explain the **7 Test Principles**.

**A:**
1. **Testing shows presence of defects** — never their absence.
2. **Exhaustive testing is impossible** — use risk + priorities.
3. **Early testing saves money** — fixing a defect in design is far cheaper than in production.
4. **Defect clustering** — 80% of defects come from 20% of code (Pareto).
5. **Pesticide paradox** — the same tests stop finding new bugs; tests must evolve.
6. **Testing is context-dependent** — safety-critical ≠ a marketing website.
7. **Absence-of-errors fallacy** — bug-free software is useless if it doesn't meet user needs.

---

**Q:** What does Principle 4 (Defect Clustering) mean for test prioritisation?

**A:** Defects pile up in a small fraction of the codebase (Pareto: ~80% of issues in ~20% of code). Focus test effort on those high-risk modules rather than spreading it evenly.

---

**Q:** What is the **Pesticide Paradox** and how do you deal with it?

**A:** Running the same test suite over and over eventually stops finding new bugs because the code has been patched for those specific cases. Solution: **regularly review and add new tests**, and update the test suite to cover different areas.

---

**Q:** What is the **cost-of-defects curve** and why does it matter?

**A:** The cost of fixing a defect rises sharply the later it is found. Fixing a bug in requirements costs orders of magnitude less than fixing it in production. This is the primary motivation for **early testing**.

---

**Q:** How much testing is enough?

**A:** Depends on **risk** (technical + business) and **project constraints** (time, budget). There is no universal answer — testing should produce enough information to make good decisions.

---

**Q:** What are the **4 phases** of the fundamental test process?

**A:**
1. **Plan & control** — who, what, why, when, where; adjust as new info arrives.
2. **Analysis & design** — identify test conditions from the test basis; design test cases, data, environments.
3. **Implementation & execution** — group tests into scripts, prioritise, automate, execute, compare results, log.
4. **Test completion (closure)** — evaluate vs objectives, write test summary report, archive testware.

---

**Q:** What is the **test basis**?

**A:** The information from which tests are derived — requirements, user stories, architecture, design documents, interfaces, risk reports.

---

**Q:** What qualities does a good tester need?

**A:** Curiosity, professional pessimism, strong communication skills, skill at error guessing, and the ability to report defects constructively (fact-focused, not personal).

---

**Q:** Describe the **independence spectrum** in testing (4 levels).

**A:**
1. Programmer tests their own code. (least independent)
2. Tester in the same team as developers.
3. Dedicated test team within the organisation.
4. External test organisation. (most independent)

More independence = less bias, fresh perspective. Less independence = faster feedback, less communication overhead.

---

**Q:** What is the difference between **Error**, **Defect**, and **Failure**?

**A:**
- **Error / Mistake** — a human action that produced an incorrect result (root cause).
- **Defect / Bug / Fault** — the flaw in the code or design caused by the error.
- **Failure** — the observable incorrect behaviour when the defect is executed at runtime.

---

**Q:** What is **debugging**, and how does it differ from testing?

**A:** **Debugging** is the developer-side process of finding and removing defects after a failure is observed. **Testing** finds and reports failures. Testers don't fix; developers do.

---

## Chapter 2 — Testing Through the Software Life Cycle

---

**Q:** Draw the **V-model** and label each level.

**A:**
```
User requirements      ◄──────►  Acceptance testing
System requirements    ◄──────►  System testing
Global design          ◄──────►  Integration testing
Detailed design        ◄──────►  Component (unit) testing
                    Implementation
```
Each test level is designed as soon as the corresponding development artefact exists.

---

**Q:** What is **Verification** vs **Validation**?

**A:**
- **Verification** — "Are we building the thing right?" Checks the product matches its specification. Happens throughout development.
- **Validation** — "Are we building the right thing?" Checks the product meets actual user needs. Happens once the user/customer is involved (acceptance testing).

---

**Q:** What is **Component (Unit) testing**?

**A:** Tests individual modules, classes, or methods **in isolation**. Done by the programmer. Uses **stubs** and **drivers** to replace missing components. TDD lives at this level.

---

**Q:** What is a **Stub**, and what is a **Driver**? (and which calls which?)

**A:**
- **Stub** — a simplified simulator **called by** the component under test (simulates a dependency called downward).
- **Driver** — a simplified simulator that **calls into** the component under test (simulates a caller from above).

Memory aid: the **driver drives** the test; the **stub stands in** for a dependency.

---

**Q:** What is **Integration testing**?

**A:** Tests the **interfaces and interactions** between components or systems. Basis: design, architecture, data flow, workflows. Tests two varieties:
- **Component integration** — interactions after unit testing.
- **System integration** — interactions with other external systems.

---

**Q:** What is **System testing**?

**A:** Tests the complete, integrated system against its specified requirements. Covers both functional and non-functional aspects. Performed in a near-production environment.

---

**Q:** What is **Acceptance testing**? Name four types.

**A:** The final level — checks the system meets user/business needs (**validation**). Types:
1. **UAT** (User Acceptance Testing)
2. **Alpha testing** — in-house, by intended users
3. **Beta testing** — real users in their real environment
4. **Operational acceptance** — operational readiness (backups, recovery)

---

**Q:** Compare **Confirmation testing** (re-testing) vs **Regression testing**.

**A:**
- **Confirmation testing** — re-runs the specific test that *failed* to confirm the defect has been fixed.
- **Regression testing** — re-runs the *previously passing* tests to confirm the fix didn't break anything else. Heavily automated.

---

**Q:** Give four examples of **non-functional testing**.

**A:** Performance (load/stress/scalability), Usability, Security, Reliability/Recoverability, Portability, Interoperability, Accessibility, Maintainability.

---

**Q:** What are the three triggers for **Maintenance testing**?

**A:**
1. **Modification** — bug fix or new feature.
2. **Migration** — moving to a new platform, data format, or infrastructure.
3. **Retirement** — archiving data and decommissioning the system.

---

**Q:** What is **Impact analysis** in maintenance testing?

**A:** Before testing a change, assess: what parts of the system are affected, what side effects the change may have, and how much regression testing is therefore needed. Hard when documentation is missing or original developers are gone.

---

**Q:** Why does agile development increase the importance of automated regression?

**A:** In agile, every iteration may change or add features. Without automated regression, re-verifying all previous functionality each sprint is too slow and expensive to be practical.

---

## Chapter 3 — Static Techniques

---

**Q:** What is the difference between **static** and **dynamic** testing?

**A:**
- **Static** — examines artefacts **without executing** them (reviews, walkthroughs, inspections, static analysis). Finds defects in requirements, design, code structure.
- **Dynamic** — executes the software to observe failures at runtime (unit tests, system tests, BVA).

---

**Q:** List the **6 phases** of a formal review.

**A:**
1. **Planning** — scope, document size, assign reviewer roles.
2. **Kick-off** (optional) — entry/exit criteria, role assignment; studies show kick-offs find ~70% more major defects.
3. **Preparation** — reviewers read individually, build checklists, log defects.
4. **Review meeting** — log defects (focus: log, don't debate); aim 1–2 defects/minute.
5. **Rework** — author fixes (or argues why not).
6. **Follow-up** — moderator confirms all defects addressed; collects metrics.

---

**Q:** What are the **four types of reviews** in order of increasing formality?

**A:**
1. **Informal review** — no documentation, pair check, fast.
2. **Walkthrough** — author presents; educational; no mandatory pre-prep.
3. **Technical review** — discussion meeting; technical decisions + defect detection.
4. **Inspection** — most formal; pre-meeting prep, checklists, trained roles, metrics, formal log.

---

**Q:** What are the **roles** in a formal review?

**A:**
- **Moderator** — runs the process, distributes work, ensures quality.
- **Author** — created the document under review.
- **Scribe** — logs defects during the meeting.
- **Reviewers (checkers/inspectors)** — find defects.
- **Manager** (sometimes) — allocates resources, decides on reviews.

---

**Q:** What are the three **defect severity levels** in a review?

**A:**
- **Critical** — will damage or invalidate other documents/work products.
- **Major** — could damage other documents.
- **Minor** — cosmetic only.

---

**Q:** What is **Static Analysis** and what does it find?

**A:** Tool-based examination of code or design artefacts **without executing** them. Finds: coding standard violations, code metrics hot-spots (cyclomatic complexity, nesting depth), unreachable code, uninitialised variables, inconsistent interfaces, data flow anomalies.

---

**Q:** What is **cyclomatic complexity**?

**A:** A code metric that counts the number of **independent paths** through a piece of code. High cyclomatic complexity → hard to test, likely defect-prone. Can be used to identify hot-spots for review.

---

**Q:** What is the difference between **control flow** and **data flow** analysis?

**A:**
- **Control flow** — the sequence of execution through code. Can detect unreachable code and deep nesting.
- **Data flow** — tracks which data items are read, written, or initialised. Can detect uninitialised variables and anomalies like "written but never read."

---

**Q:** Name four defects that **static analysis finds better** than dynamic testing.

**A:** Dead/unreachable code, uninitialised variables, off-spec interfaces, cyclomatic complexity hot-spots, unused variables.

---

## Chapter 4 — Test-Driven Development (TDD)

---

**Q:** What is TDD?

**A:** A development practice where you write a **failing test first**, then write the **minimum code** to make it pass, then **refactor** — without changing behaviour. Applied mostly at the unit/component level.

---

**Q:** Describe the **Red → Green → Refactor** cycle.

**A:**
- **Red** — write a small test for behaviour that doesn't yet exist; run it; see it fail (confirms the test is testing something real).
- **Green** — write the minimum production code to make the test pass. Don't over-engineer.
- **Refactor** — improve names, remove duplication, simplify — **without changing behaviour**. All tests must still pass.

---

**Q:** What are the **advantages of TDD**?

**A:** Fast feedback (seconds to know if something broke), simpler design (only what's needed), safer changes (strong test suite catches regressions), testable code from day one, tests act as executable documentation.

---

**Q:** What are common **TDD pitfalls**?

**A:**
- Steps too big — test covers too much, hard to make pass.
- Writing production code first "to save time."
- Tests too implementation-dependent — break on any refactor.
- Insufficient refactoring — code is messy and brittle.
- "I trust that it works" — rarely true for edge cases.

---

**Q:** What do the **JUnit** annotations `@Test`, `@BeforeEach`, `@AfterEach`, `@BeforeAll`, `@AfterAll` do?

**A:**
- `@Test` — marks the method as a test case.
- `@BeforeEach` — runs before every test method.
- `@AfterEach` — runs after every test method.
- `@BeforeAll` — runs once before all tests in the class.
- `@AfterAll` — runs once after all tests in the class.

---

**Q:** What is the difference between `assertEquals` and `assertAll` in JUnit?

**A:**
- `assertEquals(expected, actual)` — fails fast on the first mismatch.
- `assertAll(...)` — groups multiple assertions; **reports all failures**, not just the first one.

---

**Q:** What are the **Leap Year rules** (used as a TDD example)?

**A:**
- Divisible by 4 → leap year.
- Divisible by 100 → **not** a leap year.
- Divisible by 400 → **is** a leap year (overrides the 100 rule).

Order of TDD: start with the smallest rule (÷4 → leap), then add exceptions one test at a time.

---

**Q:** What makes a **good JUnit test name**?

**A:** It describes the **scenario** and the **expected result**. Bad: `test1`. Good: `leapYear_DivisibleBy400_IsLeap`.

---

**Q:** Why must a test verify **only one thing**?

**A:** So that when it fails, the reason is immediately obvious. A test covering multiple behaviours can fail for multiple reasons, making diagnosis much harder.

---

## Chapter 5 — Test Design Techniques

---

**Q:** What is the difference between a **test condition**, a **test case**, and a **test procedure**?

**A:**
- **Test condition** — anything that *could* be tested (a behaviour, a rule, a value).
- **Test case** — a concrete input + expected result + preconditions + postconditions.
- **Test procedure / script** — an ordered, executable sequence of test cases.

---

**Q:** What is **traceability** in testing, and what are horizontal vs vertical traceability?

**A:** Traceability = linking a test back to the requirement or test basis item it covers.
- **Horizontal** — across documents at the same level (e.g., test case ↔ requirement at system level).
- **Vertical** — across levels (e.g., acceptance test ↔ user requirement ↔ component test).

---

**Q:** What are the three families of **test design techniques**?

**A:**
1. **Black-box (specification-based)** — test what the system should do; no knowledge of internals.
2. **White-box (structure-based)** — test using knowledge of internal code structure for coverage.
3. **Experience-based** — use tester's intuition + skill (error guessing, exploratory).

---

**Q:** Explain **Equivalence Partitioning (EP)**.

**A:** Group inputs that should be treated **the same way** by the system into partitions. Test **one value per partition**. Example: age 18–65 valid → partitions are `<18` (invalid), `18–65` (valid), `>65` (invalid). Test one value from each (e.g., 10, 30, 80).

---

**Q:** Explain **Boundary Value Analysis (BVA)**.

**A:** Defects cluster at the **edges of equivalence partitions**. For each boundary, test: the boundary value itself, one value just inside, one value just outside. For 18–65: test **17, 18, 19** (lower bound) and **64, 65, 66** (upper bound).

---

**Q:** When do you use **Decision Table Testing**?

**A:** When **combinations of input conditions** drive different outcomes (business rules). Each column is one rule (unique combination of condition T/F values), and the bottom rows show the resulting actions. Strengths: complete coverage, flushes out missing or contradictory rules.

---

**Q:** What is **State Transition Testing**?

**A:** Models the system as a **finite state machine** — states, events (transitions), guard conditions, actions. A **state table** lists all states × events; cells show the next state. Useful for finding **invalid transitions**. Coverage options: every state, every valid transition, every pair of valid transitions, every invalid transition.

---

**Q:** What is **Use Case Testing** and at which levels is it applied?

**A:** Tests **actor–system interaction flows** — each use case has preconditions, main flow, alternative flows, postconditions. Great at finding integration defects and real-world workflow issues. Mostly applied at **system** and **acceptance** levels.

---

**Q:** What is **Statement Coverage**?

**A:** Has every **executable statement** been executed at least once? Easy to achieve high numbers but does not guarantee all branch logic is tested.

---

**Q:** What is **Decision (Branch) Coverage**, and how does it compare to statement coverage?

**A:** For every `if`, `while`, `for`, `case` — has each outcome (True **and** False) been tested? **Stronger** than statement coverage. **100% decision coverage implies 100% statement coverage** (but not vice versa).

---

**Q:** What is **Error Guessing**?

**A:** An experience-based technique where the tester **predicts** where defects are likely to hide based on domain knowledge and past experience. Common targets: off-by-one errors, null inputs, empty lists, encoding issues, time zones. Best supported by maintaining a **defect/error list**.

---

**Q:** How do you **choose** which test design technique to use?

**A:** No single recipe. Consider: test basis available, risk profile and regulatory context, tester skill, time/cost, existing models (state machines, decision tables), and system complexity. Often **combine** several: BVA + decision tables + exploratory is a standard mix.

---

## Chapter 6 — Test Automation & Playwright

---

**Q:** What is **test automation**?

**A:** Use of specialised software, **separate from** the software under test, to automatically execute tests, compare results, and report outcomes.

---

**Q:** Describe the **test automation pyramid** (3 layers).

**A:**
```
        [GUI / E2E]       ← few, slow, high-level confidence
      [Integration]
   [Unit / Component]     ← many, fast, low-level confidence
```
Most tests should live at the bottom. Unit/integration tests are written by developers; GUI/E2E is owned by test automation engineers.

---

**Q:** Give 5 **benefits** of test automation.

**A:** Increased efficiency (faster, more frequent runs), improved accuracy (no human fatigue/typos), reusability across versions/browsers/environments, enables continuous testing in CI/CD, tests act as executable documentation/reports.

---

**Q:** Give 5 **risks or downsides** of test automation.

**A:** High initial investment, ongoing maintenance burden (tests rot when UI changes), technical skills required, tool licences and infrastructure costs, false alarms (flakiness lowers trust in the suite), can distract from real testing objectives.

---

**Q:** When should you **NOT** automate?

**A:** Tests that can't be automated (subjective UX/usability), tests with very low risk or that run only once, exploratory work, systems about to be retired, systems that change drastically/often. Rule of thumb: don't spend more time automating than the manual effort would cost.

---

**Q:** Compare **Capture & Playback**, **Structured Scripting**, and **Model-based Scripting**.

**A:**
| Approach | Abstraction | Skill needed | Maintenance | Example |
|---|---|---|---|---|
| Capture & Playback | None | Low | High (brittle) | Selenium IDE |
| Structured Scripting | Yes (Page Objects, functions) | Medium | Medium | Playwright, Cypress |
| Model-based | Yes (system model) | High | Low | Tosca, SpecFlow |

---

**Q:** What is **Playwright**, and what are its key features?

**A:** A Microsoft (2020) open-source, JavaScript/TypeScript end-to-end testing framework for web and API testing. Features: cross-browser (Chromium, Firefox, WebKit), multiple language bindings, parallel execution, network manipulation, built-in screenshots/video, easy CI integration.

---

**Q:** What is **synthetic test data**?

**A:** Artificially created data that **mimics real-world data**, used in non-production environments. Sources: build it yourself, fetch from other teams, fetch from external systems (e.g., Norwegian *Tenor testdata* service).

---

**Q:** What are the key **challenges** of test automation in agile?

**A:** Rapid requirement changes, maintaining speed under tight sprint cycles, balancing customer value vs adequate coverage, tests growing in complexity as features grow, cross-team collaboration, keeping the automation suite from becoming a maintenance burden.

---

## Chapter 7 — Test Management

---

**Q:** List **8 items** found in an IEEE 829 **test plan**.

**A:** Test plan identifier, Introduction/scope, Test objectives, Test items, Features to/not to be tested, Approach/strategy, Pass/fail criteria, Suspension/resumption criteria, Test deliverables, Testing tasks/schedule, Environmental needs, Responsibilities/staffing/training, **Risks and contingencies**, Approvals.

---

**Q:** What are **entry criteria** vs **exit criteria**?

**A:**
- **Entry criteria** — conditions that must be met **before** testing can start (e.g., build available, smoke test passes, environment ready).
- **Exit criteria** — conditions that must be met **before** testing can stop (e.g., coverage targets met, defect rate under threshold, time/budget exhausted).

---

**Q:** What is the difference between **project risk** and **product risk**?

**A:**
- **Project risk** — threats to the project's ability to deliver (organisational, technical, supplier issues).
- **Product risk** — threats that the product will fail to satisfy users or cause harm.

Example of project risk: staff shortages. Example of product risk: a safety-critical calculation is wrong.

---

**Q:** What are the **four responses to risk**?

**A:**
1. **Mitigate** — reduce probability or impact (e.g., extra testing, code review).
2. **Contingency** — plan what to do if it occurs.
3. **Transfer** — push the risk elsewhere (insurance, vendor contract).
4. **Ignore** — accept it if cost/impact is low.

---

**Q:** How is **risk analysis** done?

**A:** Rate each risk item 0–10 on **probability × impact**. Educated guesses, refined at project milestones. In a V-model project: at requirements phase, end of design, during implementation, and throughout testing. Produces a risk-based testing priority list.

---

**Q:** What does a **defect report** (IEEE 829) contain?

**A:** Description of the defect, steps to reproduce, impact/severity, classification (scope, severity, priority), resources involved, root cause (captured by the programmer who fixed it), conclusions and recommendations, lifecycle status.

---

**Q:** What is the **defect lifecycle**?

**A:** Opened → Assigned → Fixed → Verified → Closed. May also be: Deferred (fix later) or Rejected (not a real defect).

---

**Q:** What is **Configuration Management** and why does it matter for testing?

**A:** The process of **identifying and tracking every change** to test items and testware (code, test scripts, test data, environments). Ensures a defect found in build X can be reproduced against the **exact same version X**. Provides traceability for audits.

---

**Q:** What is the difference between **test progress monitoring** and **test control**?

**A:**
- **Monitoring** — collecting data on how testing is proceeding (tests run/passed/failed, defects found, coverage %). Provides feedback/overview.
- **Control** — **acting on** that data to adjust: re-prioritise areas, adjust schedule/scope, tighten/loosen entry/exit criteria.

---

## Chapter 8 — Tool Support for Testing

---

**Q:** List the **six tool categories** (ISTQB hexagon).

**A:**
1. Management (test mgmt, requirements mgmt, defect tracking, configuration mgmt)
2. Static testing (review tools, static analysis, modelling tools)
3. Test specification (test design tools, test data preparation)
4. Execution and logging (execution, unit testing, comparators, coverage, security)
5. Performance and monitoring (dynamic analysis, monitoring, load/stress)
6. Specific application areas (domain-specific: mobile, embedded, web)

---

**Q:** What are the **four purposes** of using test tools?

**A:**
1. Improve efficiency of test activities (automate repetitive tasks).
2. Automate things needing significant manual resources (e.g., static analysis at scale).
3. Automate what cannot be done manually (e.g., load testing thousands of users).
4. Increase reliability (consistent comparisons, simulation of complex behaviour).

---

**Q:** Name **3 benefits** and **3 risks** of test tools.

**A:**
Benefits: reduced repetitive work, greater consistency/repeatability, objective assessment (no human bias), easier access to information (dashboards).

Risks: unrealistic expectations (won't solve process problems), underestimating introduction costs (training, integration), underestimating asset maintenance (scripts rot), over-reliance replacing good manual testing.

---

**Q:** What is the **probe effect**?

**A:** The act of measuring (e.g., adding a performance monitoring probe) **changes the behaviour** being measured. An **intrusive tool** is one whose presence affects the system under test.

---

**Q:** What is the difference between the **tester's role** and the **tool user's role**?

**A:**
- **Tester** — decides *what* to test, *what* test cases to design, *how* to prioritise. Owns the testing strategy.
- **Tool user** — decides *how* to operate the tool effectively, how to extract maximum benefit, how to maintain and scale it.
Both roles are needed. A tool is only as useful as the testing strategy behind it.

---

**Q:** How should you **introduce a test tool** into an organisation?

**A:** Run a **pilot project** (small, representative scope). Define clear objectives (what does success look like). Ensure the process is in place first (automating chaos = chaos). Plan for training and ongoing support. Track ROI. Adapt usage as the team learns.

---

**Q:** Which test level is **most heavily automated**, and which is least?

**A:** **Unit testing** is most heavily automated (fast, cheap, isolated). **Acceptance testing** is least automated (often kept manual; requires user/business context).

---

## Chapter 9 — LLMs and Software Testing

---

**Q:** What are the **four ways** testers use LLMs (CT-GenAI)?

**A:**
1. **Test case generation** — from requirements, user stories, or API specs via structured prompts.
2. **Test data synthesis** — realistic edge cases, boundary values, equivalence partitions.
3. **Test script drafting** — Cypress, Playwright, pytest scaffolding from natural language.
4. **Defect prediction** — analysing code changes to prioritise where to test.

---

**Q:** Why does LLM-generated code need **extra** testing scrutiny?

**A:**
- **Non-determinism** — the same prompt may produce different code each time.
- **Subtle logic errors** — code compiles and looks right but fails on edge cases.
- **Security blind spots** — may produce injection-prone code, hardcoded secrets, weak crypto.
- **Outdated patterns** — training data may include deprecated APIs or libraries with CVEs.

---

**Q:** What is **hallucination** in the context of LLM testing?

**A:** An LLM producing **plausible but incorrect** test cases — tests that look reasonable but do not match the actual specification. The tester must always verify LLM output against the real requirements.

---

**Q:** What is the key ISTQB principle about LLM-generated output?

**A:** The **tester remains accountable** for evaluating and validating all LLM-generated output. The LLM is a tool; the human owns the quality judgement.

---

**Q:** What is the difference between **CT-AI** and **CT-GenAI**?

**A:**
- **CT-AI (2021)** — Testing **of** AI systems: data quality, bias, non-determinism, ML metrics (how to test an AI product).
- **CT-GenAI (2025)** — Testing **with** generative AI: prompt engineering, LLM evaluation, RAG, integration (how to use GenAI as a testing tool).

---

**Q:** What did the **HumanEval TDD study** show about LLMs?

**A:** Three pipelines (Iterative TDD, Batch, NoTDD) were tested on 164 Python tasks. **Iterative TDD** (write one test → run → implement → next test) usually **outperformed NoTDD** (direct prompting without tests). Conclusion: test-first feedback loops are useful even for LLMs.

---

**Q:** What is the difference between **SAST** and **DAST**?

**A:**
- **SAST** — Static Application Security Testing: analyses source code/binaries without running the app.
- **DAST** — Dynamic Application Security Testing: attacks the running application to find vulnerabilities.

---

**Q:** How do classic testing techniques map to **vulnerability research**?

**A:**
- Boundary Value Analysis → finds **buffer overflows**.
- Equivalence Partitioning → finds **input-validation gaps**.
- Control-flow testing → reveals **authentication bypasses**.
Same foundational techniques, different stakes.

---

## Chapter 10 — Exploratory Testing

---

**Q:** Define **exploratory testing**.

**A:** Simultaneous **learning**, **test design**, and **test execution** — guided by the tester, not a script. It focuses on **discovery** and relies on the tester's domain knowledge and curiosity.

---

**Q:** What is the difference between **Wrong** and **Weird** in testing?

**A:**
- **Wrong** — violates a specified rule or contract (caught by scripted tests).
- **Weird** — violates an unstated expectation, taste, or rhythm (only a human is likely to notice).

Both matter. Examples of "weird": an error message that is technically correct but sounds condescending; a button in an unexpected location.

---

**Q:** Why is exploratory testing classified as both **dynamic** and **experience-based**?

**A:** Dynamic because it **executes** the software. Experience-based because it relies on the **tester's intuition and domain knowledge** to guide what to explore.

---

**Q:** What is the **COUNT heuristic**?

**A:** Test with zero, one, many, too many, and too few items. Example: search returning no results (0), one result (1), many results (n), an overloaded result set (too many), a system that should show results but shows none (too few).

---

**Q:** What is the **Goldilocks heuristic**?

**A:** Test with too big, too small, and just right inputs.
- Too big: overload a text field.
- Too small: leave it empty.
- Just right: the happy-case input.

---

**Q:** What is the **CRUD heuristic**?

**A:** For any entity, test: **Create** (new + duplicate), **Read** (existing + non-existent), **Update** (existing + non-existent), **Delete** (existing + non-existent). Covers the full lifecycle of data.

---

**Q:** What does **RCRCRC** stand for, and when is it used?

**A:** A regression scoping mnemonic:
- **R**ecent — newly added code
- **C**ore — key functionality that must always work
- **R**isky — areas relying on other services
- **C**onfig — areas affected by configuration/environment
- **R**epaired — code changed during a recent bug fix
- **C**hronic — areas that frequently break

---

**Q:** What are **trigger heuristics** in exploratory testing?

**A:** Use your own emotional reactions as signals:
- **Impatience** → investigate delays.
- **Confusion** → investigate counterintuitive behaviour.
- **Surprise** → an assumption has been violated.
- **Discomfort** → something feels off — investigate it.

---

**Q:** What is the difference between a **mnemonic** and a **heuristic**?

**A:**
- **Mnemonic** — a memory aid (e.g., CRUD, RCRCRC).
- **Heuristic** — a problem-solving rule of thumb that often works but is **not guaranteed** to work in all cases.

---

**Q:** What is a **test charter** in exploratory testing?

**A:** A short mission statement for an exploratory session:
- **Target** — what is being explored
- **Resources** — tools, data, time budget (typically time-boxed, e.g., 90 minutes)
- **Information goals** — what you hope to learn

---

**Q:** What are the **5 steps** for doing exploratory testing?

**A:**
1. Develop a **bug classification** (taxonomy from past projects + root cause analysis).
2. **Understand** the system under test (type, functionality, users).
3. **Choose a heuristic** (CRUD, COUNT, Goldilocks, RCRCRC, trigger emotions, etc.).
4. Create a **test charter** (target, resources, goals).
5. **Continuously assess** findings: take notes, adapt next session, file bugs, update charter.

---

**Q:** Name the **9 bug taxonomy categories**.

**A:** Input validation, Boundary, Calculation, Usability, Security, Logic, Compatibility, Syntax, Performance.

---

**Q:** When does exploratory testing **shine** (best-fit scenarios)?

**A:** Poor or missing documentation, limited time, unfamiliar/new product, areas where scripted tests pass but users still complain, high-risk usability/UX flows, after an automated regression run to find what scripted tests missed.

---

**Q:** Why does context matter so much in exploratory testing?

**A:** The same behaviour can produce very different user experiences depending on who the user is. Example: a 200ms delay is trivial for one user but unacceptable for a nurse on night shift under time pressure. Context is **lived**, not declared in a doc.

---

## Key Terms Quick-Fire

---

**Q:** **Test coverage** — definition.

**A:** The percentage of identified test items (statements, branches, partitions, etc.) that have been exercised by the test suite. 100% does not mean fully tested.

---

**Q:** **Testware** — definition.

**A:** All artefacts produced during testing: test cases, test scripts, test data, test environments, test plans, test reports.

---

**Q:** **Test strategy** — definition.

**A:** A high-level description of the test levels and techniques to be used on a project; derived from the test policy or from risk analysis.

---

**Q:** **Incident** — definition.

**A:** An event during testing that requires investigation (may or may not turn out to be a defect).

---

**Q:** **Severity vs Priority** (defect management).

**A:**
- **Severity** — the technical impact of the defect on the system.
- **Priority** — the business urgency of fixing the defect.
A cosmetic bug on a login page may have low severity but high priority (high visibility). A catastrophic crash in a rarely used feature may have high severity but lower priority.

---

**Q:** What is **COTS**?

**A:** Commercial Off-the-Shelf software — pre-built software products bought rather than developed in-house. Needs its own acceptance and integration testing.

---

**Q:** What is the risk formula?

**A:** **Risk = Probability × Impact** (both rated 0–10).

---

*End of flashcards. Good luck on the exam!*
