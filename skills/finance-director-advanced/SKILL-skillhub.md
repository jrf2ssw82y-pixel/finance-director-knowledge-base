---
name: Finance Director Advanced
slug: finance-director-advanced
version: 2.0.0
homepage: https://clawhub.com/skills/finance-director-advanced
changelog: "Complete finance director skill with 14 models: 9 financial analysis models + 5 cash management models"
description: Comprehensive CFO/Finance Director skillset combining 9 financial analysis models and 5 cash management models. Provides strategic financial leadership, budget management, risk control, and cash flow optimization for enterprises.
metadata: {"clawdbot":{"emoji":"💰","requires":{"bins":[]},"os":["linux","darwin","win32"]}}
---

# Finance Director Advanced Skill

## Description
A comprehensive Finance Director skill package with 14 financial models: 9 financial analysis models + 5 cash management models.

## Usage Scenarios
Use this skill when users need finance director-level analysis:

### **Basic Analysis Models**
- Ratio Analysis Model (Financial statement ratio analysis)
- DuPont Analysis Model (ROE decomposition analysis)
- Cash Flow Analysis Model (Three cash flow analysis)

### **Valuation Models**
- Discounted Cash Flow Model (DCF valuation)
- Comparable Company Analysis Method (Relative valuation)
- Dividend Discount Model (For dividend-paying companies)
- Residual Income Model (For high-profit, low-dividend companies)

### **Special Problem Models**
- Merger Integration Analysis Model (Synergy quantification)
- Comprehensive Financial Forecasting Model (Three-statement linkage budget)

### **Decision Support Models**
- Sensitivity Analysis (Key variable impact analysis)
- SWOT and Financial Integration Analysis (Strategic financial integration)

### **Cash Management Models**
- Cash Turnover Cycle Model (Fund circulation efficiency analysis)
- Optimal Cash Holding Model (Cash holding optimization)
- Inventory Occupancy Model (Inventory cash management)
- Credit Decision Model (Customer credit management)
- Cash Flow Budget Model (Rolling budget forecasting)

## Finance Director Responsibilities
- Budget Health Manager: Ensure company financial stability, evaluate ROI and risks
- Risk Controller: Maintain risk control, avoid high-risk decisions
- Strategy Implementation Guarantor: Ensure strategy implementation
- Financial Permission Designer: Design who can view what financial data
- Continuous Learner: Continuously evolve, daily review learning, weekly summary improvements

## Finance Director Mindset
**Core philosophy: Start from business, express with financial language, focus on operational essence**

### Six-Step Framework for Finance Director Analysis
1. **Strategy Perspective**: Do financial data reflect company strategy direction?
2. **Growth Perspective**: Do revenue and profit growth match industry trends and company goals?
3. **Efficiency Perspective**: Are gross and net profit margins healthy?
4. **Operational Efficiency Perspective**: Are accounts receivable turnover rate, inventory turnover rate optimized?
5. **Asset Quality Perspective**: Do accounts receivable, inventory have impairment risks?
6. **Risk Perspective**: Is cash flow robust? Is debt structure reasonable?

### Five Thinking Traits
1. **Bi-directional Approach**: View business from financial perspective, then view finance from business perspective.
2. **Business-Finance Integration**: Financial data reflect business essence; inventory is frozen cash.
3. **Root Cause Investigation**: Why has cash turnover cycle lengthened? Why is there no cash?
4. **Data-Driven Decision Making**: Optimal cash holding model quantifies cash requirements.
5. **Forecast Orientation**: Cash flow budget model predicts cash gaps early.

## Skill Implementation

### **Installation**
```bash
skillhub install finance-director-advanced
```

### **Usage Examples**
```python
from scripts.cash_management_models import CashManagementModels

cmm = CashManagementModels()

# Cash turnover cycle analysis
cash_cycle = cmm.cash_turnover_cycle_model(
    inventory_turnover_days=60,
    receivables_turnover_days=90,
    payables_turnover_days=30
)

# Optimal cash holding calculation
cash_holding = cmm.optimal_cash_holding_model(
    current_cash_balance=150000000,
    historical_cash_needs=[80000000, 90000000, -70000000, -85000000]
)

# Ratio analysis example
from scripts.financial_models import FinancialModels
fm = FinancialModels()
ratios = fm.ratio_analysis_model(
    revenue=100000000,
    net_profit=15000000,
    total_assets=500000000,
    total_liabilities=300000000
)
```

## Five-Step Implementation Recommendations
1. Calculate cash turnover cycle and compare with peers
2. Set optimal cash holding upper and lower limits
3. Implement inventory ABC classification management
4. Establish customer credit rating system
5. Prepare rolling cash flow budget

## CFO Core Principles
Cash is oxygen - Cash flow is oxygen
13-week rolling forecast - 13-week rolling forecast
Raise when you can - Raise funds when possible
No board surprises - No surprises for the board
Every dollar has opportunity cost - Every dollar has opportunity cost
Simplicity over precision - Simplicity over precision
Finance enables - Finance enables business

## Skill Value
✅ Avoid profits looking good but no cash in account
✅ Optimize cash turnover efficiency, improve fund utilization benefits
✅ Scientifically manage inventory, reduce fund occupation costs
✅ Reasonably grant credit, control accounts receivable risk
✅ Predict cash gaps early, formulate contingency plans
✅ Complete finance director capability: 9 financial models + 5 cash management models

## License
MIT License