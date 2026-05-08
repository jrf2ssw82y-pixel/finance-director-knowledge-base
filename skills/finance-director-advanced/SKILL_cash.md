---
name: Cash Management Models
slug: cash-management
version: 1.0.0
homepage: https://clawic.com/skills/cash-management
changelog: "Initial version with 5 cash management models from Chinese CFO practices"
description: Chinese CFO cash management expertise - 5 essential cash management models for CFOs and financial directors. Based on Chinese CFO experience and "财务人必会的资金管理五大模型" documentation.
metadata: {"clawdbot":{"emoji":"💵","requires":{"bins":[]},"os":["linux","darwin","win32"]}}
---

## When to Use

Use this skill when:
- You need to analyze cash turnover cycles
- You need to determine optimal cash holding levels
- You need to manage inventory as cash
- You need to make credit decisions
- You need to create cash flow budgets
- You are a CFO or financial director managing cash flow

## Cash Management Models

Based on Chinese CFO experience and "财务人必会的资金管理五大模型" documentation:

### 1. Cash Turnover Cycle Model
**Formula:** Cash Turnover Cycle = Inventory Days + Receivables Days - Payables Days

**Key Insight:** Many companies fail not because they're unprofitable, but because cash cycles too long.

**Warning:** If cycle lengthens by 30 days, even large companies can be dragged down.

**Warning Mechanism:** Visual dashboard showing three turnover day indicators, automatic alerts when anomalies occur.

### 2. Optimal Cash Holding Model
**Problem:** How much cash should be kept on hand?

**Common Situation:** Too much cash → idle capital, wasteful; Too little cash → emergency shortages.

**Solution:** Set lower limit (must replenish below), upper limit (invest surplus above).

**Key Principle:** Don't need precise penny, but need a range.

**Case Study:** One company kept 20 million idle cash constantly; model calculated 8 million sufficient; remaining 12 million invested in short-term instruments → 50-60 thousand additional profit per year.

### 3. Inventory as Cash Model
**Common Misconception:** Many owners think inventory is goods → sell → cash.

**Correct View:** View inventory as frozen cash.

**ABC Classification:** 
- **A-class:** High value, few varieties → watch closely, less stock faster sales
- **C-class:** Small pieces → bulk purchase convenience
- **Principle:** Don't waste energy on small items, don't be casual with big items.

**Ordering Strategy:** Quantitative vs periodic ordering depends on business characteristics.

**Key Calculation:** When ordering, calculate how much capital cost is occupied by ordering one more batch.

**Impact:** Inventory stuck one more month → cash turnover cycle lengthens one month.

### 4. Credit Decision Model
**Core Problem:** Selling on credit, who to give credit? How much? How long?

**Decision Factors:** 
- How much profit margin from this deal?
- How long will capital be occupied?
- If buyer doesn't pay timely, what's our loss?

**Credit Grading:** 
- **New customers:** Cash upfront
- **Old customers:** Graded credit based on cooperation years, payment records, business scale
- **Dynamic Adjustment:** Credit limits and payment periods not fixed → adjust yearly

**Decision Principle:** If profit cannot cover bad debt risk and capital cost → this deal shouldn't be done.

### 5. Cash Flow Budget Model
**Core Function:** Forecast which points will lack cash, which will have surplus cash.

**How to Prepare:** 
- **Step 1:** Weekly schedule → list must-pay items (salary, rent, taxes, bank interest)
- **Step 2:** List expected receipts (big customer payments expected dates, new contract payments dates)
- **Step 3:** Check difference

**Contingency Plan:** Only after preparing know what backup plans if money doesn't return timely.
- Apply bank overdraft?
- Delay non-urgent payments?

**Rolling Budget:** This week plan next 4 weeks, next week re-plan next 4 weeks, keep rolling forward.

**System Support:** Provide cash flow net amount, inventory, receivables, payables key financial indicators year-on-year and quarter-on-quarter changes.

## Core CFO Principles

1. **Cash is oxygen** — Profitable companies die from cash flow problems
2. **13-week rolling forecast** — Short-term visibility prevents surprises
3. **Raise when you can** — Not when you must; desperation kills leverage
4. **No board surprises** — Bad news early, with context
5. **Every dollar has opportunity cost** — Compare returns across all options
6. **Simplicity over precision** — One-page models beat 50-tab spreadsheets
7. **Finance enables** — Partner with operations, don't gate them

## Implementation Steps

**Step 1:** Calculate cash turnover cycle, compare with industry average
**Step 2:** Set optimal cash holding upper/lower limits
**Step 3:** Implement inventory ABC classification management
**Step 4:** Establish customer credit rating system
**Step 5:** Prepare rolling cash flow budget

## CFO Mindset Alignment

**See Strategy:** Cash flow budget model → matches company strategy cash needs
**See Growth:** Cash turnover cycle model → cash efficiency matches growth speed
**See Efficiency:** Inventory as cash model → inventory management efficiency optimization
**See Asset Quality:** Credit decision model → receivables quality and customer credit management
**See Risk:** Cash turnover cycle model → cash turnover risk warning

**Work Plan & Suggestions:** Comprehensive 5 cash management model improvement measures

## Scripts and Tools

### cash_management.py
Complete implementation of 5 cash management models:

1. `cash_turnover_cycle()` - Cash turnover cycle analysis
2. `optimal_cash_holding()` - Optimal cash holding calculation
3. `inventory_as_cash()` - Inventory cash management analysis
4. `credit_decisions()` - Credit decision model
5. `cashflow_rolling_budget()` - Cash flow rolling budget

### Test Cases
The script includes test cases demonstrating practical applications of each model.

## Integration with Finance Director Skills

This skill integrates with `finance-director` skill to provide:
- Cash turnover cycle analysis
- Optimal cash holding calculation
- Inventory cash management
- Credit decision making
- Cash flow rolling budget

## Feedback

- If useful: `clawhub star cash-management`
- Stay updated: `clawhub sync`

## Credits

Based on Chinese CFO experience and documentation "财务人必会的资金管理五大模型" from Zhihu.

Created by: 福宝 (Team Wallet and Wind Indicator)
Created for: Yuanbao Pai Shared Folder
Date: 2026-04-18