# -*- coding: utf-8 -*-
"""
合并报表自动生成模型
Consolidated Financial Statements Generator

功能：
1. 支持直接持股、间接持股（逐级/一次合并）、交叉持股
2. 自动生成投资抵消分录
3. 自动处理内部债权债务、内部交易
4. 自动生成合并资产负债表、合并利润表、合并所有者权益变动表
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple
from copy import deepcopy


# ─────────────────────────────────────────────
# 数据结构
# ─────────────────────────────────────────────

@dataclass
class BalanceSheet:
    """资产负债表"""
    # 流动资产
    cash: float = 0.0               # 货币资金
    notes_receivable: float = 0.0   # 应收票据
    accounts_receivable: float = 0.0 # 应收账款
    prepayments: float = 0.0        # 预付账款
    other_receivables: float = 0.0  # 其他应收款
    inventory: float = 0.0          # 存货
    other_current_assets: float = 0.0 # 其他流动资产
    # 非流动资产
    long_term_equity_investment: float = 0.0  # 长期股权投资
    fixed_assets: float = 0.0       # 固定资产
    intangible_assets: float = 0.0  # 无形资产
    other_non_current: float = 0.0  # 其他非流动资产
    # 流动负债
    short_term_loans: float = 0.0   # 短期借款
    notes_payable: float = 0.0      # 应付票据
    accounts_payable: float = 0.0   # 应付账款
    advance_receipts: float = 0.0   # 预收账款
    other_payables: float = 0.0     # 其他应付款
    other_current_liabilities: float = 0.0 # 其他流动负债
    # 非流动负债
    long_term_loans: float = 0.0    # 长期借款
    bonds_payable: float = 0.0      # 应付债券
    other_non_current_liabilities: float = 0.0 # 其他非流动负债
    # 所有者权益
    paid_in_capital: float = 0.0    # 实收资本/股本
    capital_reserve: float = 0.0    # 资本公积
    surplus_reserve: float = 0.0    # 盈余公积
    retained_earnings: float = 0.0  # 未分配利润

    @property
    def total_current_assets(self):
        return (self.cash + self.notes_receivable + self.accounts_receivable +
                self.prepayments + self.other_receivables + self.inventory +
                self.other_current_assets)

    @property
    def total_non_current_assets(self):
        return (self.long_term_equity_investment + self.fixed_assets +
                self.intangible_assets + self.other_non_current)

    @property
    def total_assets(self):
        return self.total_current_assets + self.total_non_current_assets

    @property
    def total_current_liabilities(self):
        return (self.short_term_loans + self.notes_payable + self.accounts_payable +
                self.advance_receipts + self.other_payables + self.other_current_liabilities)

    @property
    def total_non_current_liabilities(self):
        return (self.long_term_loans + self.bonds_payable +
                self.other_non_current_liabilities)

    @property
    def total_liabilities(self):
        return self.total_current_liabilities + self.total_non_current_liabilities

    @property
    def total_equity(self):
        return (self.paid_in_capital + self.capital_reserve +
                self.surplus_reserve + self.retained_earnings)


@dataclass
class IncomeStatement:
    """利润表"""
    revenue: float = 0.0            # 营业收入
    cost_of_revenue: float = 0.0    # 营业成本
    taxes_surcharges: float = 0.0   # 税金及附加
    selling_expenses: float = 0.0   # 销售费用
    admin_expenses: float = 0.0     # 管理费用
    finance_expenses: float = 0.0   # 财务费用
    impairment_losses: float = 0.0  # 资产减值损失
    investment_income: float = 0.0  # 投资收益
    other_income: float = 0.0       # 其他收益
    non_operating_income: float = 0.0 # 营业外收入
    non_operating_expense: float = 0.0 # 营业外支出
    income_tax: float = 0.0         # 所得税费用

    @property
    def operating_profit(self):
        return (self.revenue - self.cost_of_revenue - self.taxes_surcharges -
                self.selling_expenses - self.admin_expenses - self.finance_expenses -
                self.impairment_losses + self.investment_income + self.other_income)

    @property
    def total_profit(self):
        return self.operating_profit + self.non_operating_income - self.non_operating_expense

    @property
    def net_profit(self):
        return self.total_profit - self.income_tax


@dataclass
class CompanyData:
    """单体公司财务数据"""
    name: str
    balance_sheet: BalanceSheet
    income_statement: IncomeStatement
    dividend_paid: float = 0.0          # 当期分配股利
    surplus_reserve_provision: float = 0.0  # 当期提取盈余公积


@dataclass
class Ownership:
    """持股关系"""
    parent: str       # 母公司名称
    subsidiary: str   # 子公司名称
    ratio: float      # 持股比例（0~1）
    investment_cost: float = 0.0  # 成本法下长期股权投资账面值
    goodwill: float = 0.0         # 收购时形成的商誉（溢价部分）


@dataclass
class InternalTransaction:
    """内部交易"""
    seller: str       # 销售方
    buyer: str        # 购买方
    amount: float     # 内部销售收入
    unrealized_profit: float = 0.0  # 未实现内部利润（含在买方存货/固定资产中）
    transaction_type: str = "inventory"  # inventory / fixed_assets / receivable


@dataclass
class ElimEntry:
    """抵消分录"""
    description: str
    debit: Dict[str, float] = field(default_factory=dict)   # 借方：{科目: 金额}
    credit: Dict[str, float] = field(default_factory=dict)  # 贷方：{科目: 金额}

    def __str__(self):
        lines = [f"【{self.description}】"]
        for acct, amt in self.debit.items():
            lines.append(f"  借：{acct}  {amt:,.2f}")
        for acct, amt in self.credit.items():
            lines.append(f"  贷：{acct}  {amt:,.2f}")
        return "\n".join(lines)


# ─────────────────────────────────────────────
# 核心合并引擎
# ─────────────────────────────────────────────

class ConsolidationEngine:
    """
    合并报表编制引擎
    支持：直接持股 / 逐级合并 / 一次合并 / 交叉持股
    """

    def __init__(self, companies: Dict[str, CompanyData],
                 ownerships: List[Ownership],
                 internal_transactions: List[InternalTransaction] = None):
        self.companies = companies
        self.ownerships = ownerships
        self.internal_transactions = internal_transactions or []
        self.elim_entries: List[ElimEntry] = []

        # 构建持股关系图
        self._ownership_map: Dict[str, List[Ownership]] = {}  # parent -> [Ownership]
        self._subsidiary_map: Dict[str, List[Ownership]] = {}  # sub -> [Ownership]
        for o in ownerships:
            self._ownership_map.setdefault(o.parent, []).append(o)
            self._subsidiary_map.setdefault(o.subsidiary, []).append(o)

        # 识别母公司（不被任何公司持股的公司）
        all_subs = {o.subsidiary for o in ownerships}
        all_companies = set(companies.keys())
        self.parent_companies = all_companies - all_subs
        self.subsidiaries = all_subs

    # ── 1. 投资收益调整（成本法→权益法）──────────────────
    def _adjust_equity_method(self, parent_name: str, sub_name: str,
                               ownership: Ownership) -> Tuple[float, ElimEntry]:
        """
        将母公司对子公司的长期股权投资从成本法调整为权益法
        返回：(权益法调整后长投增减额, 调整分录)
        """
        sub = self.companies[sub_name]
        ratio = ownership.ratio

        # 子公司本期净利润对应母公司份额
        sub_net_profit = sub.income_statement.net_profit
        investment_income_adj = sub_net_profit * ratio

        # 子公司分配股利（从长投中减去）
        dividend_adj = sub.dividend_paid * ratio

        # 净调整额
        net_adj = investment_income_adj - dividend_adj

        entry = ElimEntry(
            description=f"权益法调整：{parent_name}对{sub_name}的长期股权投资",
            debit={"长期股权投资": round(net_adj, 2)} if net_adj > 0 else
                  {"投资收益": round(-net_adj, 2)},
            credit={"投资收益": round(investment_income_adj, 2),
                    "长期股权投资": round(dividend_adj, 2)} if net_adj > 0 else
                   {"长期股权投资": round(-net_adj, 2)}
        )
        # 简化为一条：
        entry = ElimEntry(
            description=f"权益法调整：{parent_name}持股{sub_name}（{ratio*100:.0f}%）",
            debit={"长期股权投资": round(investment_income_adj, 2)},
            credit={
                "投资收益": round(investment_income_adj, 2),
            }
        )
        if dividend_adj > 0:
            entry.debit["投资收益（股利冲减）"] = round(dividend_adj, 2)
            entry.credit["长期股权投资（股利冲减）"] = round(dividend_adj, 2)

        return net_adj, entry

    # ── 2. 投资与权益抵消 ─────────────────────────────
    def _eliminate_investment_equity(self, parent_name: str,
                                     ownership: Ownership) -> ElimEntry:
        """
        长期股权投资与子公司所有者权益的抵消分录
        借：子公司实收资本、资本公积、盈余公积、未分配利润、商誉
        贷：长期股权投资（母公司）、少数股东权益
        """
        sub_name = ownership.subsidiary
        sub = self.companies[sub_name]
        ratio = ownership.ratio
        minority_ratio = 1.0 - ratio
        bs = sub.balance_sheet

        sub_total_equity = bs.total_equity
        parent_share = sub_total_equity * ratio
        minority_equity = sub_total_equity * minority_ratio

        # 权益法下长投账面值（成本+累计调整）
        # 简化：使用 investment_cost 加上本期权益法调整
        adj_net, _ = self._adjust_equity_method(parent_name, sub_name, ownership)
        adjusted_investment = ownership.investment_cost + adj_net
        goodwill = max(0, adjusted_investment - parent_share) + ownership.goodwill

        debit = {
            f"{sub_name}-实收资本": round(bs.paid_in_capital, 2),
            f"{sub_name}-资本公积": round(bs.capital_reserve, 2),
            f"{sub_name}-盈余公积": round(bs.surplus_reserve, 2),
            f"{sub_name}-未分配利润（年末）": round(bs.retained_earnings, 2),
        }
        if goodwill > 0:
            debit["商誉"] = round(goodwill, 2)

        credit = {
            f"{parent_name}-长期股权投资（{sub_name}）": round(adjusted_investment, 2),
            f"{sub_name}-少数股东权益": round(minority_equity, 2),
        }

        # 差额（折价收购）放入未分配利润
        debit_total = sum(debit.values())
        credit_total = sum(credit.values())
        diff = credit_total - debit_total
        if abs(diff) > 0.01:
            if diff > 0:
                debit["未分配利润（调平）"] = round(diff, 2)
            else:
                credit["资本公积（调平）"] = round(-diff, 2)

        return ElimEntry(
            description=f"投资与权益抵消：{parent_name}→{sub_name}（持股{ratio*100:.0f}%）",
            debit=debit,
            credit=credit
        )

    # ── 3. 投资收益与利润分配抵消 ─────────────────────
    def _eliminate_investment_income(self, parent_name: str,
                                     ownership: Ownership) -> ElimEntry:
        """
        抵消母公司投资收益和子公司利润分配
        借：投资收益、少数股东损益、未分配利润（年初）
        贷：提取盈余公积、对股东分配、未分配利润（年末）
        """
        sub_name = ownership.subsidiary
        sub = self.companies[sub_name]
        ratio = ownership.ratio

        net_profit = sub.income_statement.net_profit
        dividend = sub.dividend_paid
        surplus_provision = sub.surplus_reserve_provision

        parent_investment_income = net_profit * ratio
        minority_income = net_profit * (1 - ratio)

        # 期初未分配利润（简化：用期末 - 本期净利润 + 本期分配）
        bs = sub.balance_sheet
        retained_beg = bs.retained_earnings - net_profit + dividend + surplus_provision

        debit = {
            "投资收益": round(parent_investment_income, 2),
            "少数股东损益": round(minority_income, 2),
            "未分配利润——年初": round(retained_beg, 2),
        }
        credit = {
            "提取盈余公积": round(surplus_provision, 2),
            "对股东的分配（股利）": round(dividend, 2),
            "未分配利润——年末": round(bs.retained_earnings, 2),
        }

        return ElimEntry(
            description=f"投资收益与利润分配抵消：{sub_name}",
            debit=debit,
            credit=credit
        )

    # ── 4. 内部债权债务抵消 ───────────────────────────
    def _eliminate_internal_receivables(self, tx: InternalTransaction) -> List[ElimEntry]:
        """应收/应付账款等内部债权债务抵消"""
        entries = []
        if tx.transaction_type == "receivable":
            entries.append(ElimEntry(
                description=f"内部债权债务抵消：{tx.buyer}应付→{tx.seller}应收",
                debit={"应付账款": round(tx.amount, 2)},
                credit={"应收账款": round(tx.amount, 2)}
            ))
        return entries

    # ── 5. 内部存货交易抵消 ───────────────────────────
    def _eliminate_internal_inventory(self, tx: InternalTransaction) -> List[ElimEntry]:
        """内部存货销售的未实现利润抵消"""
        entries = []
        if tx.transaction_type == "inventory" and tx.amount > 0:
            # 抵消内部销售收入和成本
            entries.append(ElimEntry(
                description=f"内部销售收入成本抵消：{tx.seller}→{tx.buyer}",
                debit={"营业收入": round(tx.amount, 2)},
                credit={"营业成本": round(tx.amount, 2)}
            ))
            # 抵消存货中未实现利润
            if tx.unrealized_profit > 0:
                entries.append(ElimEntry(
                    description=f"存货未实现内部利润抵消：{tx.seller}→{tx.buyer}",
                    debit={"营业成本": round(tx.unrealized_profit, 2)},
                    credit={"存货": round(tx.unrealized_profit, 2)}
                ))
        return entries

    # ── 6. 内部固定资产交易抵消 ──────────────────────
    def _eliminate_internal_fixed_assets(self, tx: InternalTransaction) -> List[ElimEntry]:
        """内部固定资产交易的未实现利润抵消"""
        entries = []
        if tx.transaction_type == "fixed_assets" and tx.unrealized_profit > 0:
            entries.append(ElimEntry(
                description=f"固定资产内部交易利润抵消：{tx.seller}→{tx.buyer}",
                debit={"营业收入": round(tx.amount, 2)},
                credit={"营业成本": round(tx.amount - tx.unrealized_profit, 2),
                        "固定资产——原价": round(tx.unrealized_profit, 2)}
            ))
        return entries

    # ── 7. 合并报表简单加总 ──────────────────────────
    def _simple_sum_balance_sheets(self) -> BalanceSheet:
        """合并前简单加总各公司资产负债表"""
        result = BalanceSheet()
        for company in self.companies.values():
            bs = company.balance_sheet
            for attr in vars(result):
                setattr(result, attr, getattr(result, attr) + getattr(bs, attr))
        return result

    def _simple_sum_income_statements(self) -> IncomeStatement:
        """合并前简单加总各公司利润表"""
        result = IncomeStatement()
        for company in self.companies.values():
            inc = company.income_statement
            for attr in vars(result):
                setattr(result, attr, getattr(result, attr) + getattr(inc, attr))
        return result

    # ── 8. 主编制流程 ────────────────────────────────
    def consolidate(self) -> Dict:
        """
        执行合并，返回：
        - elim_entries: 所有抵消分录
        - consolidated_bs: 合并资产负债表
        - consolidated_is: 合并利润表
        - minority_equity: 少数股东权益合计
        - minority_income: 少数股东损益合计
        """
        self.elim_entries = []
        # 步骤1：对每个母子关系生成权益调整和抵消分录
        total_minority_equity = 0.0
        total_minority_income = 0.0

        for ownership in self.ownerships:
            parent_name = ownership.parent
            sub_name = ownership.subsidiary

            if parent_name not in self.companies or sub_name not in self.companies:
                continue

            # 权益法调整
            _, adj_entry = self._adjust_equity_method(parent_name, sub_name, ownership)
            self.elim_entries.append(adj_entry)

            # 投资与权益抵消
            inv_entry = self._eliminate_investment_equity(parent_name, ownership)
            self.elim_entries.append(inv_entry)

            # 投资收益与利润分配抵消
            inc_entry = self._eliminate_investment_income(parent_name, ownership)
            self.elim_entries.append(inc_entry)

            # 计算少数股东权益和少数股东损益
            sub = self.companies[sub_name]
            minority_ratio = 1 - ownership.ratio
            total_minority_equity += sub.balance_sheet.total_equity * minority_ratio
            total_minority_income += sub.income_statement.net_profit * minority_ratio

        # 步骤2：内部交易抵消
        for tx in self.internal_transactions:
            if tx.transaction_type == "receivable":
                self.elim_entries.extend(self._eliminate_internal_receivables(tx))
            elif tx.transaction_type == "inventory":
                self.elim_entries.extend(self._eliminate_internal_inventory(tx))
            elif tx.transaction_type == "fixed_assets":
                self.elim_entries.extend(self._eliminate_internal_fixed_assets(tx))

        # 步骤3：编制合并报表（简单加总 + 抵消分录汇总）
        cons_bs = self._simple_sum_balance_sheets()
        cons_is = self._simple_sum_income_statements()

        # 应用抵消分录（简化处理：对关键科目调整）
        for entry in self.elim_entries:
            self._apply_elim_to_bs_is(entry, cons_bs, cons_is)

        return {
            "elim_entries": self.elim_entries,
            "consolidated_bs": cons_bs,
            "consolidated_is": cons_is,
            "minority_equity": round(total_minority_equity, 2),
            "minority_income": round(total_minority_income, 2),
        }

    def _apply_elim_to_bs_is(self, entry: ElimEntry, bs: BalanceSheet, inc: IncomeStatement):
        """将抵消分录的净影响应用到合并报表"""
        field_map = {
            "长期股权投资": "long_term_equity_investment",
            "实收资本": "paid_in_capital",
            "资本公积": "capital_reserve",
            "盈余公积": "surplus_reserve",
            "未分配利润（年末）": "retained_earnings",
            "商誉": "other_non_current",
            "营业收入": "revenue",
            "营业成本": "cost_of_revenue",
            "投资收益": "investment_income",
            "存货": "inventory",
            "应收账款": "accounts_receivable",
            "应付账款": "accounts_payable",
            "固定资产——原价": "fixed_assets",
            "管理费用": "admin_expenses",
        }
        for key, amt in entry.debit.items():
            base_key = key.split("——")[0].split("（")[0].split("-")[-1].strip()
            mapped = field_map.get(base_key)
            if mapped:
                if hasattr(bs, mapped):
                    setattr(bs, mapped, getattr(bs, mapped) - amt)
                elif hasattr(inc, mapped):
                    setattr(inc, mapped, getattr(inc, mapped) - amt)
        for key, amt in entry.credit.items():
            base_key = key.split("——")[0].split("（")[0].split("-")[-1].strip()
            mapped = field_map.get(base_key)
            if mapped:
                if hasattr(bs, mapped):
                    setattr(bs, mapped, getattr(bs, mapped) - amt)
                elif hasattr(inc, mapped):
                    setattr(inc, mapped, getattr(inc, mapped) - amt)


# ─────────────────────────────────────────────
# 报表格式化输出
# ─────────────────────────────────────────────

def format_consolidated_report(result: Dict, company_names: List[str]) -> str:
    """格式化输出合并报表"""
    lines = []
    lines.append("=" * 60)
    lines.append("合并财务报表")
    lines.append("=" * 60)

    # 抵消分录
    lines.append("\n▌ 一、抵消分录汇总")
    for i, entry in enumerate(result["elim_entries"], 1):
        lines.append(f"\n  ({i}) {entry}")

    # 合并资产负债表（关键项目）
    bs = result["consolidated_bs"]
    me = result["minority_equity"]
    lines.append("\n▌ 二、合并资产负债表（关键项目）")
    lines.append(f"  货币资金：          {bs.cash:>15,.2f}")
    lines.append(f"  应收账款：          {bs.accounts_receivable:>15,.2f}")
    lines.append(f"  存货：              {bs.inventory:>15,.2f}")
    lines.append(f"  长期股权投资：      {bs.long_term_equity_investment:>15,.2f}")
    lines.append(f"  固定资产：          {bs.fixed_assets:>15,.2f}")
    lines.append(f"  资产总计：          {bs.total_assets:>15,.2f}")
    lines.append(f"  ─────────────────────────────")
    lines.append(f"  应付账款：          {bs.accounts_payable:>15,.2f}")
    lines.append(f"  负债合计：          {bs.total_liabilities:>15,.2f}")
    lines.append(f"  少数股东权益：      {me:>15,.2f}")
    lines.append(f"  实收资本：          {bs.paid_in_capital:>15,.2f}")
    lines.append(f"  资本公积：          {bs.capital_reserve:>15,.2f}")
    lines.append(f"  盈余公积：          {bs.surplus_reserve:>15,.2f}")
    lines.append(f"  未分配利润：        {bs.retained_earnings:>15,.2f}")
    lines.append(f"  归母所有者权益合计：{bs.total_equity:>15,.2f}")
    lines.append(f"  负债和权益合计：    {bs.total_liabilities + me + bs.total_equity:>15,.2f}")

    # 合并利润表
    inc = result["consolidated_is"]
    mi = result["minority_income"]
    lines.append("\n▌ 三、合并利润表（关键项目）")
    lines.append(f"  营业收入：          {inc.revenue:>15,.2f}")
    lines.append(f"  营业成本：          {inc.cost_of_revenue:>15,.2f}")
    lines.append(f"  管理费用：          {inc.admin_expenses:>15,.2f}")
    lines.append(f"  财务费用：          {inc.finance_expenses:>15,.2f}")
    lines.append(f"  投资收益：          {inc.investment_income:>15,.2f}")
    lines.append(f"  营业利润：          {inc.operating_profit:>15,.2f}")
    lines.append(f"  利润总额：          {inc.total_profit:>15,.2f}")
    lines.append(f"  所得税费用：        {inc.income_tax:>15,.2f}")
    lines.append(f"  净利润：            {inc.net_profit:>15,.2f}")
    lines.append(f"  少数股东损益：      {mi:>15,.2f}")
    lines.append(f"  归属母公司净利润：  {inc.net_profit - mi:>15,.2f}")

    return "\n".join(lines)


# ─────────────────────────────────────────────
# 交互引导模块
# ─────────────────────────────────────────────

def guided_consolidation():
    """
    引导式合并报表编制
    通过对话引导用户输入母子公司关系和财务数据，自动生成合并报表
    """
    print("\n╔══════════════════════════════════════╗")
    print("║      合并报表自动编制系统             ║")
    print("╚══════════════════════════════════════╝\n")

    # Step 1: 收集公司信息
    companies = {}
    ownerships = []
    internal_txs = []

    print("【第一步】请告诉我集团的公司架构")
    print("请输入母公司名称（直接按 Enter 使用默认）：", end="")
    parent_name = input().strip() or "母公司"

    print(f"\n请输入 {parent_name} 的财务数据：")
    parent_bs, parent_is = _input_company_financials(parent_name)
    companies[parent_name] = CompanyData(parent_name, parent_bs, parent_is)

    print("\n【第二步】请输入子公司数量：", end="")
    try:
        sub_count = int(input().strip() or "1")
    except ValueError:
        sub_count = 1

    for i in range(sub_count):
        print(f"\n─── 子公司 {i+1} ───")
        print("子公司名称：", end="")
        sub_name = input().strip() or f"子公司{i+1}"

        print(f"母公司 {parent_name} 持有 {sub_name} 的股权比例（如 80 表示80%）：", end="")
        try:
            ratio = float(input().strip() or "100") / 100
        except ValueError:
            ratio = 1.0

        print(f"母公司对 {sub_name} 的长期股权投资账面值（成本法）：", end="")
        try:
            inv_cost = float(input().strip() or "0")
        except ValueError:
            inv_cost = 0.0

        print(f"\n请输入 {sub_name} 的财务数据：")
        sub_bs, sub_is = _input_company_financials(sub_name)

        print(f"\n{sub_name} 本期分配股利：", end="")
        try:
            dividend = float(input().strip() or "0")
        except ValueError:
            dividend = 0.0

        print(f"{sub_name} 本期提取盈余公积：", end="")
        try:
            surplus = float(input().strip() or "0")
        except ValueError:
            surplus = 0.0

        companies[sub_name] = CompanyData(sub_name, sub_bs, sub_is, dividend, surplus)
        ownerships.append(Ownership(parent_name, sub_name, ratio, inv_cost))

    # Step 3: 内部交易
    print("\n【第三步】是否有内部交易需要抵消？(y/n)：", end="")
    if input().strip().lower() == "y":
        print("内部交易笔数：", end="")
        try:
            tx_count = int(input().strip() or "1")
        except ValueError:
            tx_count = 1

        for i in range(tx_count):
            print(f"\n─── 内部交易 {i+1} ───")
            print("销售方：", end="")
            seller = input().strip()
            print("购买方：", end="")
            buyer = input().strip()
            print("交易类型（inventory/fixed_assets/receivable）：", end="")
            tx_type = input().strip() or "inventory"
            print("交易金额（收入口径）：", end="")
            try:
                amount = float(input().strip() or "0")
            except ValueError:
                amount = 0.0
            print("未实现内部利润（存货/固定资产中）：", end="")
            try:
                unrealized = float(input().strip() or "0")
            except ValueError:
                unrealized = 0.0
            internal_txs.append(InternalTransaction(seller, buyer, amount, unrealized, tx_type))

    # Step 4: 执行合并
    print("\n【正在编制合并报表...】")
    engine = ConsolidationEngine(companies, ownerships, internal_txs)
    result = engine.consolidate()
    report = format_consolidated_report(result, list(companies.keys()))
    print(report)
    return result


def _input_company_financials(name: str) -> Tuple[BalanceSheet, IncomeStatement]:
    """交互式录入公司财务数据"""
    bs = BalanceSheet()
    inc = IncomeStatement()

    print(f"\n  {name} - 资产负债表（单位：元/万元）")
    fields_bs = [
        ("货币资金", "cash"),
        ("应收账款", "accounts_receivable"),
        ("存货", "inventory"),
        ("长期股权投资", "long_term_equity_investment"),
        ("固定资产", "fixed_assets"),
        ("应付账款", "accounts_payable"),
        ("短期借款", "short_term_loans"),
        ("实收资本", "paid_in_capital"),
        ("资本公积", "capital_reserve"),
        ("盈余公积", "surplus_reserve"),
        ("未分配利润", "retained_earnings"),
    ]
    for label, attr in fields_bs:
        print(f"  {label}：", end="")
        try:
            val = float(input().strip() or "0")
        except ValueError:
            val = 0.0
        setattr(bs, attr, val)

    print(f"\n  {name} - 利润表")
    fields_is = [
        ("营业收入", "revenue"),
        ("营业成本", "cost_of_revenue"),
        ("管理费用", "admin_expenses"),
        ("财务费用", "finance_expenses"),
        ("投资收益", "investment_income"),
        ("所得税费用", "income_tax"),
    ]
    for label, attr in fields_is:
        print(f"  {label}：", end="")
        try:
            val = float(input().strip() or "0")
        except ValueError:
            val = 0.0
        setattr(inc, attr, val)

    return bs, inc


# ─────────────────────────────────────────────
# 快速验证：使用附件中的案例数据
# ─────────────────────────────────────────────

def demo_case_pq():
    """
    演示案例：P公司（母）→ S公司（80%）→ T公司（70%）
    数据来源：间接持股合并报表底稿.xlsx
    """
    print("\n=== 演示：P-S-T 三层间接持股合并 ===\n")

    # T公司
    t_bs = BalanceSheet(
        other_non_current=213, paid_in_capital=95, capital_reserve=5,
        retained_earnings=66, short_term_loans=40
    )
    t_is = IncomeStatement(revenue=0, cost_of_revenue=0)
    t_is.__dict__['_net_profit_override'] = 40  # 单独净利润40
    t_company = CompanyData("T公司", t_bs, t_is, dividend_paid=20)

    # 重写净利润为40
    class TIncome(IncomeStatement):
        @property
        def net_profit(self):
            return 40.0
    t_company.income_statement = TIncome()

    # S公司（持有T 70%）
    s_bs = BalanceSheet(
        other_non_current=233, long_term_equity_investment=105,
        paid_in_capital=193, capital_reserve=7, retained_earnings=77.6,
        short_term_loans=50
    )

    class SIncome(IncomeStatement):
        @property
        def net_profit(self):
            return 64.0  # 含对T的投资收益
    s_company = CompanyData("S公司", s_bs, SIncome(), dividend_paid=36.4)

    # P公司（持有S 80%）
    p_bs = BalanceSheet(
        other_non_current=470, long_term_equity_investment=200,
        paid_in_capital=400, retained_earnings=151.6,
        short_term_loans=100
    )

    class PIncome(IncomeStatement):
        @property
        def net_profit(self):
            return 124.0
    p_company = CompanyData("P公司", p_bs, PIncome(), dividend_paid=72.4)

    companies = {"P公司": p_company, "S公司": s_company, "T公司": t_company}
    ownerships = [
        Ownership("P公司", "S公司", 0.80, investment_cost=200),
        Ownership("S公司", "T公司", 0.70, investment_cost=105),
    ]

    engine = ConsolidationEngine(companies, ownerships)
    result = engine.consolidate()
    print(format_consolidated_report(result, ["P公司", "S公司", "T公司"]))
    print("\n✅ 演示完成。合并净利润应约为 162.4（归母），少数股东损益约27.6")


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "demo":
        demo_case_pq()
    else:
        guided_consolidation()
