# Updated Assessment and Feedback Report: WEB 1430

**Date:** March 16, 2026  
**Purpose:** Document what has been implemented in the assessment/feedback redesign work, identify what still remains, and clarify the next reasonable revision targets.

---

## Executive Summary

The assessment and feedback layer is meaningfully stronger than it was in the initial redesign draft. The biggest operational weakness has been fixed: assessment export is now generated from the `quizzes/*.json` sources, which makes the quiz JSON files the source of truth for the Canvas package. The quizzes and exams themselves also now include more code-reading and debugging-oriented stems, which improves signal quality even within a selected-response format.

The course feedback loop is also more operational than before. The Week 5, Week 11, and Week 13 survey question banks are now surfaced in the learner path, and the instructor workflow for monitoring and responding is documented in `course/first-delivery-monitoring-guide.md` and `course/import_to_canvas.md`.

The remaining limitations are narrower now:

- summative assessments are still entirely selected-response
- there are still no low-stakes standalone checkpoints for DevTools or persistence
- the survey response cycle still depends on manual instructor follow-through

**Current assessment/feedback verdict:** Stronger, synchronized, and usable for delivery 1, with a clear next-phase improvement path if first-delivery evidence justifies it.

---

## What Is Now Implemented

### 1. Assessment source-of-truth and package generation

This is now in place:

- `quizzes/*.json` define the live assessment content
- the Canvas assessment package is regenerated from those JSON sources
- `course/quiz-alignment.md` matches the current assessment set, point totals, and chapter coverage

This is a major improvement because it reduces silent drift between planning docs, source files, and the exported package.

### 2. Stronger item quality in existing quizzes and exams

The revised assessments now include more applied selected-response items, especially in:

- Quiz 4
- Quizzes 6-8
- Midterm Exam
- Final Exam

The improvements are mostly in code-reading, debugging judgment, safer DOM updates, storage reasoning, data-flow recognition, and accessibility/performance judgment. This does not fully solve the format ceiling, but it materially improves assessment quality inside the current tooling constraints.

### 3. Better feedback delivery path

The survey question banks for:

- Week 05 Mid-Course Check-In
- Week 11 Late-Course Check-In
- Week 13 Vue and Workload Pulse Check

are now visible in the learner path and reflected in course structure. This corrects the earlier problem where feedback instruments existed in the repo but were not meaningfully integrated into the course experience.

### 4. Instructor response workflow is documented

The feedback loop is now better operationalized through:

- `course/import_to_canvas.md`
- `course/first-delivery-monitoring-guide.md`

These documents now specify:

- when to create the live forms
- what to monitor
- what warning thresholds to watch
- how to respond using a `You said / I changed / I am watching` pattern

This is a real design improvement, even though it still depends on instructor execution.

### 5. The Final Project beta is more diagnostic than before

The Final Project Beta already asks students to explain:

- what is working well
- what is not yet done or not working correctly
- what help they need before final submission

That makes the beta a more useful diagnostic instrument than a simple status checkpoint.

---

## What Still Remains

### 1. Selected-response still dominates the formal assessment layer

All quizzes and both exams are still selected-response. The improved stems help, but the format still under-measures:

- actual troubleshooting process
- DevTools evidence
- persistence implementation logic
- longer-form design/debug explanations

This remains the main assessment limitation.

### 2. DevTools and persistence still lack standalone graded checkpoints

These topics are taught and reinforced through labs, projects, and some selected-response items, but there is still no small dedicated checkpoint for either of them.

That means some students may not discover a weak understanding until a larger artifact depends on the skill.

### 3. The feedback loop is still partly manual

The course now has:

- survey question banks
- publication in the learner path
- a monitoring guide
- an instructor response pattern

What it does not have is automatic live deployment of those surveys or automatic enforcement of the instructor follow-up routine. The design is now ready; the live delivery still depends on execution.

---

## Recommended Next-Phase Changes

### 1. Add two lightweight applied checkpoints if first delivery supports it

- **DevTools checkpoint:** one screenshot plus a brief explanation of what was inspected and what was learned
- **Persistence checkpoint:** a short state trace showing `getItem`, parse/default handling, and the stored value visible in DevTools

These should be low-friction items, not new major assignments.

### 2. Consider one deeper-response item only if operations allow it

If the Canvas workflow and grading load remain manageable, consider:

- one short-response item in the Midterm
- or one short-response item in the Final

This should be evidence-driven, not added by default.

### 3. Use first-delivery evidence before expanding assessment load

The current system is probably good enough for delivery 1. The right next move depends on what live delivery shows:

- Are students missing fragile skills too late?
- Are projects revealing the same assessment gaps repeatedly?
- Are surveys and betas producing actionable signals?

If the answer is yes, add the smallest checkpoint that fixes the real pattern.

---

## What Should Not Change Yet

- Do not replace the project milestone structure; it is one of the course's strongest features.
- Do not make quizzes longer just to increase assessment weight.
- Do not add multiple new checkpoints before first-delivery evidence exists.
- Do not weaken the code-reading/debug item improvements already in place by reverting to simple recall questions.

---

## Success Indicators to Watch in First Delivery

- fewer students reporting that Week 12 feels like a blind jump into Vue
- fewer late surprises around persistence implementation in Project 2
- stronger quality at Final Project Beta relative to the previous risk profile
- enough survey participation to make the Week 11 and Week 13 signals actionable
- evidence that the improved selected-response items better distinguish between shallow recall and usable reasoning

---

## Final Judgment

The assessment/feedback work is no longer just a redesign proposal. A substantial implementation pass is complete, and it materially improves both assessment quality and assessment maintainability.

What remains is a narrower, evidence-dependent next phase:

- add small applied checkpoints if needed
- consider limited deeper-response items if operationally feasible
- make sure instructors actually use the monitoring and response workflow during live delivery

**Final verdict:** Ready for delivery 1 with a credible next-step roadmap, rather than a draft still waiting on implementation.
