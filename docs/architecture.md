# Atlas Architecture

## Vision

Atlas is a long-term personal health operating system.

Its purpose is to preserve health observations, present meaningful trends, and provide a consistent historical record of progress.

Atlas is not the coach.

Wilson is the coach.

Atlas remembers.

---

# System Components

## User

Provides observations through structured check-ins.

Examples:

- Weekly Check-In
- Monthly Health Check-In
- DEXA
- Laboratory Results
- Annual Physical

---

## Wilson (ChatGPT)

Wilson is Atlas's reasoning engine.

Responsibilities:

- Interpret observations
- Understand context
- Calculate derived metrics
- Determine confidence
- Produce coaching
- Identify trends
- Generate summaries

Wilson produces an Atlas Observation.

---

## Atlas

Atlas is the system of record.

Responsibilities:

- Store observations
- Preserve history
- Display dashboards
- Display trends
- Display coaching
- Never alter historical observations

Atlas presents information.

Atlas does not reason.

---

# Observation Lifecycle

Weekly Check-In

↓

Wilson Analysis

↓

Atlas Observation

↓

Historical Repository

↓

Dashboard

---

# Dashboard Philosophy

The dashboard is the destination.

Every observation updates the dashboard.

Weekly reviews explain execution.

Monthly reviews provide a snapshot.

DEXA, Labs and Annual Physicals enrich long-term health trends.

---

# Core Principles

## Coaching First

Atlas always produces coaching.

---

## Graceful Degradation

Missing data reduces confidence.

Missing data never prevents coaching.

---

## Derived Over Manual

Wilson calculates information whenever possible.

Examples:

- Adaptive TDEE
- Average Deficit
- Weekly Strength Volume
- Average Strength Volume per Session
- Confidence
- Coaching Summary

---

## Historical Integrity

Historical observations are immutable.

Once stored, observations represent exactly what Wilson concluded at that point in time.

---

## Dashboard Is the Source of Truth

The dashboard is Atlas.

Everything else exists to update it.

---

# Responsibility Matrix

User
    ↓
Provides observations

Wilson
    ↓
Analyzes
Calculates
produces atlas observation

Atlas
    ↓
Stores
Trends
Displays