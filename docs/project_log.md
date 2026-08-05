# Atlas Project Log

## August 4, 2026 – Atlas v1 Reset

Today we intentionally restarted Atlas with a new repository.

### Background

The original repository was created for two purposes:

1. To learn AI-assisted software development using GitHub, Codespaces, and ChatGPT.
2. To explore whether Atlas should be a standalone health application.

That exploration was successful. We learned how to work together, developed an effective workflow, and identified the product we actually wanted to build.

### Key Realizations

During development, it became clear that the weekly health check-in would continue to be entered manually. There was no desire to build integrations with Garmin, WHOOP, Apple Health, or other external systems.

It also became apparent that ChatGPT already provided the strongest part of the experience:

- Health analysis
- Coaching
- Trend interpretation
- Question answering

As a result, Atlas no longer needed to replicate those capabilities.

### Product Pivot

Atlas was redefined as a companion to ChatGPT rather than a replacement.

Atlas is responsible for:

- Maintaining a structured health journal
- Generating the Weekly Snapshot Dashboard
- Calculating historical trends
- Producing the Atlas Health Score

ChatGPT remains responsible for:

- Weekly conversations
- Coaching
- Longitudinal analysis
- Recommendations
- Natural language interaction

### Outcome

This decision dramatically simplified the project.

The approved Atlas Dashboard v1.0 became the product specification, and all future development will be measured by one question:

**Does this improve the dashboard or the journal?**

If not, it does not belong in Atlas v1. 
The purpose of Atlas is not to replace ChatGPT. The purpose of Atlas is to make every health conversation with ChatGPT more informed, more visual, and more consistent over time.

0012 – Create Atlas Observation Repository

• Added production observations repository.
• Separated development sample data from production observations.
• Updated dashboard loader to read production observations.
• Verified identical dashboard output after migration.