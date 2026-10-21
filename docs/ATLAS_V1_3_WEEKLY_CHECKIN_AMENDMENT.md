# ATLAS V1.3 — Weekly Check-In and History Amendment

**Status:** Active with the V1.3 production release. Supplements the canonical Weekly Check-in V2.1 and locked V1.2 Performance Score amendment; replaces neither.

## Nutrition inputs — every Saturday
In the existing Nutrition section, collect average daily **saturated fat (g)** and **total fiber (g)** with calories, protein, fat, and carbohydrates. Use Garmin Nutrition weekly averages. Garmin total fiber already includes logged psyllium; **do not double count psyllium**. Include both measures in Wilson's nutrition/cardiovascular coaching. Do not alter Performance Score pillars or weights.

Add these optional properties under `weekly_execution_scorecard.nutrition`:
```json
"saturated_fat": {"actual": 18, "unit": "g"},
"fiber": {"actual": 32, "unit": "g"}
```
Values are examples, not actual measurements. Missing values are absent/null, **not zero**. Do not invent historical measurements.

## Workflow and roles
Keep the normal Saturday, one-category-at-a-time check-in, Wilson coaching, locked scoring, and full ATLAS JSON. Wilson owns scoring, coaching, projections and confidence; ATLAS only stores and displays supplied JSON. V1.2 scoring and Metabolic Health remain unchanged.

## Weekly archive
V1.3 preserves the complete original weekly JSON in `atlas_weekly_history_v1_3.json`, keyed by `week.date_range`. Re-uploading the same period replaces that record without duplication. Historical imports must not change the active displayed week. Never recalculate historical scores.

## Import/export
Import original weekly JSON files or a ZIP via **Import Historical Check-Ins**; exclude synthetic test records. **Download History** exports `atlas_history_export.json` containing `weekly_checkins` and `metabolic_history`. Attach the export to ChatGPT for longitudinal coaching; Mac mini history is not automatically available to Wilson.

## Compatibility
Older weekly JSON without saturated fat/fiber remains valid. Preserve the separate production metabolic history. No new dashboard card, scoring change, historical backfill, or change to Saturday cadence.
