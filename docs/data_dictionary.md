# Atlas Data Dictionary

## Purpose

The Atlas Data Dictionary is the authoritative definition of every field used by Atlas.

It defines:

- Where each field originates.
- How often it is collected.
- Who is responsible for it.
- Where it is used.

This document is the contract between the check-in process, the journal, the dashboard, and the Health Score.

---

# Weekly Fields

| Field | Source | Frequency | Owner | Stored | Dashboard | Health Score |
|--------|--------|-----------|-------|:------:|:---------:|:------------:|
| Today's Weight | Weekly Check-in | Weekly | User | ✓ | ✓ | ✓ |
| 7-Day Average Weight | Weekly Check-in | Weekly | User | ✓ | ✓ | ✓ |
| Average Daily Calorie Burn | Weekly Check-in | Weekly | User | ✓ | ✓ | ✓ |
| HRV (Daily) | Weekly Check-in | Weekly | User | ✓ | ✓ | ✓ |
| Resting Heart Rate (Daily) | Weekly Check-in | Weekly | User | ✓ | ✓ | ✓ |
| Sleep Performance (Daily) | Weekly Check-in | Weekly | User | ✓ | ✓ | ✓ |
| Average Daily Steps | Weekly Check-in | Weekly | User | ✓ | ✓ | ✓ |
| Strength Sessions | Weekly Check-in | Weekly | User | ✓ | ✓ | ✓ |
| WHOOP Strength Volume | Weekly Check-in | Weekly | User | ✓ | ✓ | ✓ |
| Workout 1 Volume | Weekly Check-in | Weekly | User | ✓ | | |
| Workout 2 Volume | Weekly Check-in | Weekly | User | ✓ | | |
| Workout 3 Volume | Weekly Check-in | Weekly | User | ✓ | | |
| Interval Runs | Weekly Check-in | Weekly | User | ✓ | ✓ | ✓ |
| Zone 2 Rides | Weekly Check-in | Weekly | User | ✓ | ✓ | ✓ |
| Zone 1–3 Time | Weekly Check-in | Weekly | User | ✓ | ✓ | ✓ |
| Zone 4–5 Time | Weekly Check-in | Weekly | User | ✓ | ✓ | ✓ |
| Average Daily Calories | Weekly Check-in | Weekly | User | ✓ | ✓ | ✓ |
| Average Daily Protein | Weekly Check-in | Weekly | User | ✓ | ✓ | ✓ |
| Average Daily Carbohydrates | Weekly Check-in | Weekly | User | ✓ | ✓ | ✓ |
| Average Daily Fat | Weekly Check-in | Weekly | User | ✓ | ✓ | ✓ |
| Alcohol (Daily) | Weekly Check-in | Weekly | User | ✓ | ✓ | ✓ |
| Work Stress | Weekly Check-in | Weekly | User | ✓ | ✓ | ✓ |
| Sleep Quality | Weekly Check-in | Weekly | User | ✓ | ✓ | |
| Recovery / Performance | Weekly Check-in | Weekly | User | ✓ | ✓ | |
| Anything Unusual | Weekly Check-in | Weekly | User | ✓ | ✓ | |

---

# Weekly Review Outputs

These values are produced during the weekly review conversation.

| Field | Source | Frequency | Owner | Stored | Dashboard | Health Score |
|--------|--------|-----------|-------|:------:|:---------:|:------------:|
| Adaptive TDEE | Weekly Review | Weekly | ChatGPT | ✓ | ✓ | ✓ |
| Average Daily Deficit | Weekly Review | Weekly | ChatGPT | ✓ | ✓ | ✓ |
| Overall Status | Weekly Review | Weekly | ChatGPT | ✓ | ✓ | |
| Confidence | Weekly Review | Weekly | ChatGPT | ✓ | ✓ | ✓ |
| Biggest Win | Weekly Review | Weekly | ChatGPT | ✓ | ✓ | |
| Biggest Opportunity | Weekly Review | Weekly | ChatGPT | ✓ | ✓ | |
| Focus Next Week | Weekly Review | Weekly | ChatGPT | ✓ | ✓ | |
| Coach Summary | Weekly Review | Weekly | ChatGPT | ✓ | ✓ | |

---

# Atlas Calculations

These values are never entered manually.

| Field | Source | Frequency | Owner | Dashboard |
|--------|--------|-----------|-------|:---------:|
| Atlas Health Score | Atlas | Weekly | Atlas | ✓ |
| Goal Progress | Atlas | Weekly | Atlas | ✓ |
| Historical Trends | Atlas | Weekly | Atlas | ✓ |