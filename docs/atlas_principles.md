# Atlas Principles

These principles guide every design and implementation decision within Atlas.

---

# 1. Coaching First

Atlas exists to improve long-term health through better decisions and consistent execution.

Every feature should help answer one of two questions:

- Am I becoming healthier?
- Am I executing my plan?

---

# 2. Strategic Over Tactical

The dashboard emphasizes long-term outcomes over short-term fluctuations.

Weekly execution drives strategic outcomes.

---

# 3. Progressive Disclosure

The dashboard presents only the most important information first.

Users can drill deeper into supporting metrics without overwhelming the primary view.

---

# 4. Derived Over Manual

Whenever possible, Atlas calculates values instead of requiring manual entry.

Examples include:

- Adaptive TDEE
- Average Daily Deficit
- Weekly Strength Volume
- Average Strength Volume per Session
- Health Score
- Goal Progress
- Confidence

---

# 5. Graceful Degradation

Atlas always produces coaching.

Missing or incomplete observations never prevent analysis.

Instead, Atlas communicates uncertainty through a Confidence rating.

Missing data reduces confidence—not functionality.

---

# 6. Confidence Reflects Data Quality

Confidence measures the completeness and quality of available evidence.

It is never a measure of user performance.

Examples:

- Home week with complete data → High
- Travel week without scale → Medium
- Multiple missing recovery metrics → Low

---

# 7. Separation of Responsibilities

The User provides observations.

ChatGPT structures observations.

Atlas performs calculations.

The Dashboard presents results.

Each layer has a single responsibility.

---

# 8. Historical Integrity

Observations become permanent historical records.

Atlas calculations become part of those records so historical dashboards can always be reproduced exactly as they originally appeared.

---

# 9. Dashboard Is the Destination

Weekly, monthly, DEXA, laboratory, and annual physical reviews all exist to update the dashboard.

The dashboard remains the single source of truth for long-term health.