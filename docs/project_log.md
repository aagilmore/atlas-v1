> "Architecture tells us how Atlas works.
>
> This journal tells us why."

# Atlas Engineering Journal

## Purpose

This journal records the significant product, architectural, and implementation decisions made during the development of Atlas.

It exists to preserve engineering context rather than simply commit history.

Each entry captures:

- Purpose
- Key Decisions
- Outcome

The repository contains the code.

This journal explains why the code looks the way it does.

---

# Milestone 1 – Foundation

## Objective

Establish Atlas as a Personal Health Memory System with a stable architecture, observation model, and user workflow before expanding functionality.

## Milestone Outcomes

- Atlas product vision established.
- Dashboard specification frozen before implementation.
- Weekly observation model defined.
- Observation contract established.
- Confidence model introduced.
- Atlas architecture frozen.
- Observation repository created.
- User workflow designed.
- UI blueprint completed.
- Atlas application entry point established.

Milestone 1 concludes with Atlas transitioning from a collection of scripts into a structured software product with a stable architectural foundation.

---

## 0001 – Establish Atlas v1

### Purpose

Create the Atlas repository and establish the project foundation.

### Key Decisions

- Atlas would be developed as an independent application.
- Git history would document engineering decisions.
- Documentation would evolve alongside implementation.

### Outcome

Created the foundation for all future development.

---

## 0002 – Freeze Atlas Dashboard Specification

### Purpose

Define the Version 1 dashboard before implementation.

### Key Decisions

- Dashboard structure documented before coding.
- Dashboard layout separated from implementation.
- Dashboard became a frozen product artifact.

### Outcome

Established the implementation target for the Atlas dashboard.

---

## 0003 – Add Atlas Dashboard v1 Master

### Purpose

Add the approved dashboard design to the repository.

### Key Decisions

- Preserve the approved dashboard as the implementation reference.
- Separate visual design from application code.

### Outcome

Created the canonical dashboard reference for Version 1.

---

## 0004 – Define Weekly Observation

### Purpose

Define the structure of the weekly health observation.

### Key Decisions

- Weekly observations become the primary unit of historical record.
- Observations summarize the outcome of weekly coaching.

### Outcome

Established the initial observation model.

---

## 0005 – Add Sample Weekly Observation

### Purpose

Create representative data for dashboard development.

### Key Decisions

- Development uses sample observations.
- Sample data remains separate from production observations.

### Outcome

Enabled dashboard development without production data.

---

## 0006 – Freeze Atlas Data Dictionary

### Purpose

Define the meaning of every field used by Atlas.

### Key Decisions

- Dashboard fields documented.
- Observation fields standardized.
- Shared vocabulary established across the project.

### Outcome

Created a common language for Atlas.

---

## 0007 – Align Weekly Observation Model

### Purpose

Refine the observation model to align with the evolving dashboard and architecture.

### Key Decisions

- Observation structure updated for consistency.
- Dashboard and observation model aligned.

### Outcome

Produced a consistent observation model for Version 1.

---

## 0008 – Create Atlas Observation Loader

### Purpose

Separate observation loading from dashboard generation.

### Key Decisions

- Dashboard consumes observations through a loader.
- Dashboard no longer depends on specific files.

### Outcome

Improved separation of responsibilities.

---

## 0009 – Implement Atlas Confidence Engine

### Purpose

Introduce confidence as a first-class concept within Atlas observations.

### Key Decisions

- Missing data reduces confidence rather than eliminating coaching.
- Confidence measures observation quality.
- Coaching continues even when confidence is reduced.

### Outcome

Atlas distinguishes between incomplete information and coaching value.

---

## 0010 – Freeze Atlas Architecture

### Purpose

Define the long-term architectural responsibilities of Atlas and ChatGPT.

### Key Decisions

- ChatGPT performs coaching and reasoning.
- Atlas preserves observations and presents dashboards.
- Atlas never performs coaching.
- Atlas serves as the system of record.

### Outcome

Responsibilities were clearly separated and frozen.

---

## 0011 – Freeze Atlas Observation Contract

### Purpose

Define the permanent interface between ChatGPT and Atlas.

### Key Decisions

- Atlas stores finalized observations.
- Historical observations are immutable.
- Observation structure is preserved exactly as produced.

### Outcome

Established the permanent contract between coaching and storage.

---

## 0012 – Create Atlas Observation Repository

### Purpose

Create a permanent repository for Atlas observations.

### Key Decisions

- Production observations stored separately from sample data.
- Repository becomes the source of historical observations.

### Outcome

Established the foundation for long-term health memory.

---

## 0013 – Add Observation Repository Manager

### Purpose

Centralize observation access.

### Key Decisions

- Dashboard requests observations through the repository manager.
- Dashboard no longer references filenames directly.

### Outcome

Observation management became independent from dashboard implementation.

---

## 0014 – Design Atlas User Workflow

### Purpose

Define how users interact with ChatGPT and Atlas.

### Key Decisions

- Weekly coaching begins in ChatGPT.
- Coaching remains conversational.
- Atlas Observation is created only after coaching concludes.
- Atlas imports finalized observations.
- Atlas exports history for longitudinal analysis.
- Atlas never interrupts coaching.

### Outcome

Established the complete user workflow.

---

## 0015 – Define Atlas UI Blueprint

### Purpose

Define the Version 1 screen structure.

### Key Decisions

Home screen contains:

- View Dashboard
- Import Observation from ChatGPT
- Export History for ChatGPT

Additional decisions:

- Home becomes the navigation hub.
- Dashboard specification remains independently maintained.
- Observation History removed from Version 1 to maintain simplicity.

### Outcome

Established the Version 1 navigation model.

---

## 0016 – Define Atlas Product Vision

### Purpose

Define the long-term identity and principles of Atlas.

### Key Decisions

- Atlas is a Personal Health Memory System.
- Atlas preserves coaching outcomes rather than conversations.
- Atlas complements ChatGPT rather than replacing it.
- Responsibilities remain stable while implementation may evolve.
- Version 1 uses manual import/export while allowing future automated synchronization.

### Outcome

Established the long-term vision that will guide future development.

---

## 0017 – Create Atlas Application Entry Point

### Purpose

Transition Atlas from individual scripts into an application.

### Key Decisions

- Introduced the `app` package.
- `atlas.py` became the application launcher.
- Application startup separated from application logic.

### Outcome

Created the architectural foundation for Atlas as an application.

---

# Major Engineering Discoveries

The following discoveries significantly influenced the design of Atlas.

## Atlas is a Personal Health Memory System

Atlas preserves the long-term story of a person's health rather than attempting to replace health coaching.

---

## ChatGPT Coaches. Atlas Preserves.

Responsibilities are intentionally separated.

ChatGPT provides conversation, reasoning, education, and coaching.

Atlas preserves the outcomes of those conversations.

---

## Preserve Outcomes, Not Conversations

Atlas stores finalized observations rather than complete coaching transcripts.

This preserves the important information while keeping the historical record concise and portable.

---

## Freeze Responsibilities, Not Implementation

Architectural responsibilities remain stable even as implementation evolves.

Manual import/export may eventually become seamless synchronization without changing the underlying architecture.

---

## The Repository Is the Source of Truth

Engineering decisions are based on the current state of the repository rather than memory.

Repository inventory is performed before significant development sessions.

---

# Looking Ahead

Milestone 1 established the architectural and product foundation for Atlas.

Milestone 2 shifts the focus from defining Atlas to building Atlas.

Future development will prioritize:

- Interactive application workflows.
- Dashboard experience.
- Observation import and export.
- Longitudinal health memory.
- Continued alignment with the Product Vision.

## 0018 – Implement Interactive Home Menu

### Purpose

Introduce the first interactive user interface for Atlas by separating menu presentation from application control.

### Key Decisions

- Created a dedicated `menu.py` module.
- Separated menu presentation from application logic.
- Application controller now requests user input rather than displaying the menu directly.
- Established the pattern of one responsibility per module.

### Outcome

Atlas became an interactive application capable of accepting user input through a modular home menu, establishing the foundation for future navigation.