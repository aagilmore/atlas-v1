# Atlas UI Blueprint

The Atlas interface is intentionally simple.

Atlas is not a coaching application.

Atlas is a dashboard and historical health system.

Every screen exists to help the user understand long-term progress.

# Atlas Version 1 Screen Map

Atlas Version 1 contains four primary screens.

## Home

Purpose:

Provide the primary entry point into Atlas.

Actions:

- View Dashboard
- Import Observation from ChatGPT
- Export History for ChatGPT

Reference:

- user_workflow.md

---

## Dashboard

Purpose:

Present the user's current health dashboard.

Reference:

- dashboard_specification.md

---

## Import Observation

Purpose:

Import and validate a finalized Atlas Observation from ChatGPT.

Reference:

- observation_contract.md
- user_workflow.md

---

## Export History

Purpose:

Generate an Atlas History package for longitudinal analysis in ChatGPT.

Reference:

- user_workflow.md

---

# Navigation Flow

Atlas Version 1 uses a simple navigation model.

Home
├── View Dashboard
├── Import Observation
└── Export History

Dashboard
└── Return Home

Import Observation
└── Return Home

Export History
└── Return Home

The Home screen is the primary navigation hub.

All workflows begin and end at Home.