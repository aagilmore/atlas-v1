# Atlas Dashboard Specification v1

## Purpose

The Atlas Dashboard is the primary view of a user's current health state.

It is generated from the latest Atlas Observation and presents the most important information at a glance.

The dashboard is intentionally concise. It is a summary, not a report.

---

# Header

## Week
Observation.week

Display:
Week 32, 2026

Required:
Yes

---

## Overall Status

Observation.assessment.overall_status

Examples:

- On Track
- Watch
- Recovery
- Off Track

Required:
Yes

---

## Confidence

Confidence Engine

Display:
High / Medium / Low

Required:
Yes

---

# Scale

## Today's Weight

Observation.scale.today_weight

Required:
Yes

---

## Average Weight

Observation.scale.average_weight

Required:
Yes

---

# Recovery

## Average Daily Calorie Burn

Observation.recovery.average_daily_calorie_burn

Required:
Yes

---

# Activity

## Strength Sessions

Observation.activity.strength_sessions

Required:
Yes

---

## Weekly Strength Volume

Observation.activity.weekly_strength_volume

Required:
Yes

---

## Average Strength Volume per Session

Observation.activity.average_strength_volume_per_session

Required:
Yes

---

# Nutrition

## Average Daily Calories

Observation.nutrition.average_daily_calories

Required:
Yes

---

## Average Daily Protein

Observation.nutrition.average_daily_protein

Required:
Yes

---

# Assessment

## Overall Assessment

Observation.assessment.summary

Required:
No

Future Enhancement

---

## Focus Areas

Observation.assessment.focus_areas

Required:
No

Future Enhancement

---

## Wins

Observation.assessment.wins

Required:
No

Future Enhancement

---

## Risks

Observation.assessment.risks

Required:
No

Future Enhancement