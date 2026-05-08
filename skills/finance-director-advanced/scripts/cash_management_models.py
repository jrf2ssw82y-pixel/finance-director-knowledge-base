#!/usr/bin/env python3
"""
财务人必会的资金管理五大模型实现脚本
基于《财务人必会的资金管理五大模型.docx》文档
"""

import pandas as pd
import numpy as np

class CashManagementModels:
    """资金管理五大模型实现类"""
    
    def __init__(self):
        """初始化"""
        print("=== 资金管理五大模型 ===")
        print("1. 现金周转周期模型")
        print("2. 最佳现金持有量模型")
        print("3. 存货占用模型")
        print("4. 信用决策模型")
        print("5. 现金流预算模型")
        
    def cash_turnover_cycle_model(self, inventory_turnover_days, receivables_turnover_days, payables_turnover_days):
        """
        现金周转周期模型
        
        公式：现金周转周期 = 存货周转天数 + 应收账款周转天数 - 应付账款周转天数
        
        参数：
        - inventory_turnover_days：存货周转天数（进货到卖出多少天）
        - receivables_turnover_days：应收账款周转天数（卖了货到收回钱多少天）
        - payables_turnover_days：应付账款周转天数（欠供应商的钱能拖多少天）
        
        返回：现金周转周期分析和预警
        """
        cash_turnover_cycle = inventory_turnover_days + receivables_turnover_days - payables_turnover_days
        
        # 分析
        analysis = {
            "现金周转周期": cash_turnover_cycle,
            "存货周转天数": inventory_turnover_days,
            "应收账款周转天数": receivables_turnover_days,
            "应付账款周转天数": payables_turnover_days,
            "问题识别": {
                "存货周转过长": inventory_turnover_days > industry_avg_inventory_days,
                "应收账款周转过长": receivables_turnover_days > industry_avg_receivables_days,
                "应付账款周转过短": payables_turnover_days < industry_avg_payables_days
            },
            "预警机制": {
                "存货压多预警": inventory_turnover_days > threshold_inventory,
                "回款慢预警": receivables_turnover_days > threshold_receivables,
                "付款过快预警": payables_turnover_days < threshold_payables
            },
            "改进建议": {
                "存货周转过长": "优化库存管理，加快存货周转",
                "应收账款周转过长": "优化销售政策，加快应收账款回款",
                "应付账款周转过短": "优化采购政策，延长应付账款周转"
            },
            "资金影响": f"周期拉长{cash_turnover_cycle-industry_avg_cycle}天，可能导致资金周转困难"
        }
        
        # 行业平均水平示例
        industry_avg_inventory_days = 45  # 行业平均存货周转天数
        industry_avg_receivables_days = 60  # 行业平均应收账款周转天数
        industry_avg_payables_days = 30  # 行业平均应付账款周转天数
        industry_avg_cycle = industry_avg_inventory_days + industry_avg_receivables_days - industry_avg_payables_days
        
        # 预警阈值
        threshold_inventory = 60  # 存货周转天数阈值
        threshold_receivables = 90  # 应收账款周转天数阈值
        threshold_payables = 20  # 应付账款周转天数阈值
        
        return analysis
    
    def optimal_cash_holding_model(self, current_cash_balance, historical_cash_needs):
        """
        最佳现金持有量模型
        
        参数：
        - current_cash_balance：当前现金余额
        - historical_cash_needs：历史现金需求数据（月度/季度）
        
        返回：最佳现金持有量范围和建议
        """
        # 计算历史现金需求的平均值、最大值和最小值
        avg_needs = np.mean(historical_cash_needs)
        max_needs = np.max(historical_cash_needs)
        min_needs = np.min(historical_cash_needs)
        
        # 设置上下限（根据业务特点调整）
        lower_limit = avg_needs * 0.8  # 资金下限（低于这个数必须补钱）
        upper_limit = avg_needs * 1.2  # 资金上限（高于这个数可以做短期投资）
        
        # 分析
        analysis = {
            "当前现金余额": current_cash_balance,
            "历史现金需求平均值": avg_needs,
            "历史现金需求最大值": max_needs,
            "历史现金需求最小值": min_needs,
            "最佳现金持有量下限": lower_limit,
            "最佳现金持有量上限": upper_limit,
            "当前状况": {
                "低于下限": current_cash_balance < lower_limit,
                "高于上限": current_cash_balance > upper_limit,
                "合理范围": lower_limit <= current_cash_balance <= upper_limit
            },
            "行动建议": {
                "低于下限": "必须补钱，否则可能面临资金短缺风险",
                "高于上限": "多余资金可以拿去做短期投资，提高资金使用效率",
                "合理范围": "保持当前现金水平"
            },
            "资金利用建议": {
                "闲置资金": current_cash_balance - upper_limit if current_cash_balance > upper_limit else 0,
                "短缺资金": lower_limit - current_cash_balance if current_cash_balance < lower_limit else 0,
                "短期投资收益": (current_cash_balance - upper_limit) * investment_rate if current_cash_balance > upper_limit else 0
            }
        }
        
        # 投资收益率示例
        investment_rate = 0.05  # 短期理财收益率
        
        return analysis
    
    def inventory_cash_model(self, inventory_value, inventory_turnover_days, product_categories):
        """
        存货占用模型
        
        核心认知：库存是冻住的现金
        
        参数：
        - inventory_value：存货总价值
        - inventory_turnover_days：存货周转天数
        - product_categories：产品类别分类数据
        
        返回：存货占用分析和优化建议
        """
        # ABC分析法
        abc_classification = {}
        for category, value in product_categories.items():
            if value >= high_value_threshold:
                abc_classification[category] = "A类（货值高、品种少）"
            elif value >= medium_value_threshold:
                abc_classification[category] = "B类（中等货值）"
            else:
                abc_classification[category] = "C类（小零碎）"
        
        # 资金占用成本计算
        inventory_cash_cost = inventory_value * (inventory_turnover_days / 365) * funding_cost_rate
        
        # 订货策略
        ordering_strategy = "定量订货" if inventory_turnover_days < stable_demand else "定期订货"
        
        # 分析
        analysis = {
            "存货总价值": inventory_value,
            "存货周转天数": inventory_turnover_days,
            "ABC分类": abc_classification,
            "资金占用成本": inventory_cash_cost,
            "订货策略": ordering_strategy,
            "周转速度影响": f"存货每多压一个月，现金周转周期拉长一个月",
            "管理建议": {
                "A类产品": "盯着管，少进货快出货",
                "C类产品": "批量采购省事就行",
                "通用原则": "别把精力花在小东西上，也别在大件上太随意"
            },
            "订货计算": "多进一批货占用的资金成本是多少？"
        }
        
        # 阈值示例
        high_value_threshold = 50000000  # A类货值阈值
        medium_value_threshold = 10000000  # B类货值阈值
        funding_cost_rate = 0.06  # 资金占用成本率
        stable_demand = 30  # 稳定需求天数
        
        return analysis
    
    def credit_decision_model(self, customer_profile, transaction_value, profit_margin):
        """
        信用决策模型
        
        核心问题：赊给谁、赊多少、赊多久？
        
        参数：
        - customer_profile：客户信息（合作年限、过往付款记录、经营规模）
        - transaction_value：交易金额
        - profit_margin：毛利率
        
        返回：信用决策分析和授信额度
        """
        # 信用评级
        credit_score = 0
        
        # 合作年限评分
        if customer_profile["合作年限"] >= 5:
            credit_score += 20
        elif customer_profile["合作年限"] >= 3:
            credit_score += 15
        elif customer_profile["合作年限"] >= 1:
            credit_score += 10
        else:
            credit_score += 5
        
        # 付款记录评分
        if customer_profile["过往付款记录"] == "及时":
            credit_score += 20
        elif customer_profile["过往付款记录"] == "偶尔延迟":
            credit_score += 15
        elif customer_profile["过往付款记录"] == "经常延迟":
            credit_score += 5
        
        # 经营规模评分
        if customer_profile["经营规模"] == "大型企业":
            credit_score += 20
        elif customer_profile["经营规模"] == "中型企业":
            credit_score += 15
        elif customer_profile["经营规模"] == "小型企业":
            credit_score += 10
        
        # 信用评级
        credit_level = ""
        if credit_score >= 50:
            credit_level = "高信用等级"
        elif credit_score >= 30:
            credit_level = "中信用等级"
        else:
            credit_level = "低信用等级"
        
        # 授信额度计算
        if customer_profile["客户类型"] == "新客户":
            credit_limit = 0  # 一律款到发货
        elif customer_profile["客户类型"] == "老客户":
            if credit_level == "高信用等级":
                credit_limit = transaction_value * 1.5
            elif credit_level == "中信用等级":
                credit_limit = transaction_value * 1.0
            elif credit_level == "低信用等级":
                credit_limit = transaction_value * 0.5
        
        # 账期天数
        credit_days = 30 if credit_level == "高信用等级" else 15 if credit_level == "中信用等级" else 0
        
        # 决策分析
        analysis = {
            "信用评分": credit_score,
            "信用等级": credit_level,
            "客户类型": customer_profile["客户类型"],
            "授信额度": credit_limit,
            "账期天数": credit_days,
            "交易金额": transaction_value,
            "毛利率": profit_margin,
            "资金占用天数": credit_days,
            "资金占用成本": transaction_value * (credit_days / 365) * funding_cost_rate,
            "风险收益评估": {
                "收益": transaction_value * profit_margin,
                "资金占用成本": transaction_value * (credit_days / 365) * funding_cost_rate,
                "坏账风险": credit_limit * bad_debt_rate,
                "净收益": transaction_value * profit_margin - transaction_value * (credit_days / 365) * funding_cost_rate - credit_limit * bad_debt_rate
            },
            "决策建议": {
                "净收益大于0": "批准信用",
                "净收益小于0": "不建议赊账（不如不做）"
            },
            "动态调整": "额度和账期不是固定的，每年调整一次"
        }
        
        # 资金占用成本率和坏账率示例
        funding_cost_rate = 0.06
        bad_debt_rate = 0.02
        
        return analysis
    
    def cashflow_rolling_budget(self, cash_outflows, cash_inflows):
        """
        现金流预算模型
        
        核心功能：预测未来哪些时间点会缺钱，哪些时间点钱可能会多出来
        
        参数：
        - cash_outflows：未来四周现金流出（按周）
        - cash_inflows：未来四周现金流入（按周）
        
        返回：现金流预算分析和应急预案
        """
        weeks = 4
        cashflow_forecast = []
        cash_gaps = []
        cash_surplus = []
        contingency_plans = []
        
        for week in range(weeks):
            cashflow = cash_inflows[week] - cash_outflows[week]
            cashflow_forecast.append(cashflow)
            
            if cashflow < 0:
                cash_gaps.append({
                    "week": week+1,
                    "gap_amount": abs(cashflow),
                    "contingency_plan": "跟银行申请透支额度或推迟非紧急付款"
                })
            
            if cashflow > cash_surplus_threshold:
                cash_surplus.append({
                    "week": week+1,
                    "surplus_amount": cashflow,
                    "investment_plan": "多余资金做短期投资"
                })
        
        # 滚动预算
        rolling_budget = {
            "本周预算": cashflow_forecast[0],
            "下周预算": cashflow_forecast[1],
            "下两周预算": cashflow_forecast[2],
            "下三周预算": cashflow_forecast[3],
            "现金流缺口": cash_gaps,
            "资金盈余": cash_surplus,
            "应急预案": contingency_plans,
            "现金流出明细": {
                "工资": cash_outflows[0]["工资"],
                "房租": cash_outflows[0]["房租"],
                "税费": cash_outflows[0]["税费"],
                "银行利息": cash_outflows[0]["银行利息"],
                "其他支出": cash_outflows[0]["其他支出"]
            },
            "现金流入明细": {
                "大客户回款": cash_inflows[0]["大客户回款"],
                "新签合同收款": cash_inflows[0]["新签合同收款"],
                "其他收入": cash_inflows[0]["其他收入"]
            },
            "滚动预算原则": "这周排未来四周，下周再排未来四周，不断往前滚",
            "系统支持": "提供现金流净额、存货、应收账款、应付账款等关键财务指标的同比和环比变化"
        }
        
        # 盈余阈值示例
        cash_surplus_threshold = 10000000
        
        return rolling_budget
    
    def test_all_cash_management_models(self):
        """测试资金管理五大模型"""
        print("\n=== 资金管理五大模型测试 ===\n")
        
        # 1. 现金周转周期模型
        print("1. 现金周转周期模型:")
        cash_cycle_results = self.cash_turnover_cycle_model(
            inventory_turnover_days=60,
            receivables_turnover_days=90,
            payables_turnover_days=30
        )
        print(f"现金周转周期: {cash_cycle_results['现金周转周期']}天")
        print(f"存货周转过长: {cash_cycle_results['问题识别']['存货周转过长']}")
        print(f"应收账款周转过长: {cash_cycle_results['问题识别']['应收账款周转过长']}")
        print(f"资金影响: {cash_cycle_results['资金影响']}")
        
        # 2. 最佳现金持有量模型
        print("\n2. 最佳现金持有量模型:")
        cash_holding_results = self.optimal_cash_holding_model(
            current_cash_balance=150000000,
            historical_cash_needs=[80000000, 90000000, 70000000, 85000000]
        )
        print(f"当前现金余额: {cash_holding_results['当前现金余额']}")
        print(f"最佳现金持有量下限: {cash_holding_results['最佳现金持有量下限']}")
        print(f"最佳现金持有量上限: {cash_holding_results['最佳现金持有量上限']}")
        print(f"当前状况: {cash_holding_results['当前状况']['合理范围']}")
        
        # 3. 存货占用模型
        print("\n3. 存货占用模型:")
        inventory_results = self.inventory_cash_model(
            inventory_value=200000000,
            inventory_turnover_days=75,
            product_categories={
                "冰箱": 80000000,
                "洗衣机": 50000000,
                "空调": 40000000,
                "智能家居": 30000000,
                "零部件": 10000000
            }
        )
        print(f"存货总价值: {inventory_results['存货总价值']}")
        print(f"存货周转天数: {inventory_results['存货周转天数']}天")
        print(f"ABC分类: {inventory_results['ABC分类']}")
        print(f"资金占用成本: {inventory_results['资金占用成本']}")
        
        # 4. 信用决策模型
        print("\n4. 信用决策模型:")
        credit_results = self.credit_decision_model(
            customer_profile={
                "合作年限": 3,
                "过往付款记录": "及时",
                "经营规模": "中型企业",
                "客户类型": "老客户"
            },
            transaction_value=10000000,
            profit_margin=0.15
        )
        print(f"信用评分: {credit_results['信用评分']}")
        print(f"信用等级: {credit_results['信用等级']}")
        print(f"授信额度: {credit_results['授信额度']}")
        print(f"账期天数: {credit_results['账期天数']}")
        print(f"净收益: {credit_results['风险收益评估']['净收益']}")
        
        # 5. 现金流预算模型
        print("\n5. 现金流预算模型:")
        cashflow_results = self.cashflow_rolling_budget(
            cash_outflows=[
                {"工资": 5000000, "房租": 1000000, "税费": 2000000, "银行利息": 500000, "其他支出": 1500000},
                {"工资": 5000000, "房租": 1000000, "税费": 2000000, "银行利息": 500000, "其他支出": 1500000},
                {"工资": 5000000, "房租": 1000000, "税费": 2000000, "银行利息": 500000, "其他支出": 1500000},
                {"工资": 5000000, "房租": 1000000, "税费": 2000000, "银行利息": 500000, "其他支出": 1500000}
            ],
            cash_inflows=[
                {"大客户回款": 8000000, "新签合同收款": 5000000, "其他收入": 1000000},
                {"大客户回款": 7000000, "新签合同收款": 4000000, "其他收入": 1000000},
                {"大客户回款": 9000000, "新签合同收款": 6000000, "其他收入": 1000000},
                {"大客户回款": 8500000, "新签合同收款": 5000000, "其他收入": 1000000}
            ]
        )
        print(f"本周预算: {cashflow_results['本周预算']}")
        print(f"现金流缺口: {cashflow_results['现金流缺口']}")
        print(f"资金盈余: {cashflow_results['资金盈余']}")
        print(f"滚动预算原则: {cashflow_results['滚动预算原则']}")
        
        return "资金管理五大模型测试完成"

# 财务总监的资金管理建议
def finance_director_cash_management_suggestions():
    """财务总监的资金管理建议"""
    suggestions = {
        "资金管理原则": {
            "现金周转周期": "重点关注存货周转天数、应收账款周转天数、应付账款周转天数",
            "最佳现金持有量": "避免资金闲置，也避免资金短缺",
            "库存管理": "把库存当成冻住的现金，优化库存管理",
            "信用决策": "信用额度动态调整，每年评估一次",
            "现金流预算": "滚动预算，提前预测资金缺口"
        },
        "财务总监六步框架对应": {
            "看战略": "现金流预算模型 → 匹配公司发展战略的资金需求预测",
            "看成长": "现金周转周期模型 → 资金周转效率与成长速度匹配",
            "看效益": "最佳现金持有量模型 → 资金使用效益最大化",
            "看效率": "存货占用模型 → 库存周转效率优化",
            "看资产质量": "信用决策模型 → 应收账款质量与客户信用管理",
            "看风险": "现金周转周期模型 → 资金周转风险预警",
            "工作计划与建议": "综合五大资金模型提出改进措施"
        },
        "财务总监思维特质应用": {
            "双向奔赴思维": "从财务看业务（现金周转天数过长），也从业务看财务（销售政策影响应收账款周转）",
            "业财融合": "库存不仅仅是货，更是冻住的现金",
            "问题刨根问底": "为什么资金周转周期长了？为什么账上没钱？",
            "数据驱动决策": "最佳现金持有量模型量化资金需求",
            "预测导向": "现金流预算模型提前预测资金缺口"
        },
        "实施建议": [
            "第一步：计算现金周转周期，与同行对比",
            "第二步：设定最佳现金持有量上下限",
            "第三步：实施库存ABC分类管理",
            "第四步：建立客户信用评级体系",
            "第五步：编制滚动现金流预算"
        ]
    }
    
    return suggestions

if __name__ == "__main__":
    cmm = CashManagementModels()
    cmm.test_all_cash_management_models()
    
    print("\n=== 财务总监的资金管理建议 ===\n")
    suggestions = finance_director_cash_management_suggestions()
    for key, value in suggestions.items():
        print(f"{key}:")
        if isinstance(value, dict):
            for sub_key, sub_value in value.items():
                print(f"  {sub_key}: {sub_value}")
        elif isinstance(value, list):
            for item in value:
                print(f"  {item}")
        else:
            print(f"  {value}")