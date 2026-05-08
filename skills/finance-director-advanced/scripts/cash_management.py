#!/usr/bin/env python3
"""
CFO技能的资金管理补充模块
基于《财务人必会的资金管理五大模型.docx》文档
"""

import pandas as pd
import numpy as np
import datetime

class CashManagementModels:
    """资金管理五大模型实现类"""
    
    def __init__(self):
        """初始化"""
        print("=== 财务总监资金管理五大模型 ===")
        print("1. 现金周转周期模型")
        print("2. 最佳现金持有量模型")
        print("3. 存货占用模型")
        print("4. 信用决策模型")
        print("5. 现金流预算模型")
        
    def cash_turnover_cycle(self, inventory_days, receivables_days, payables_days):
        """
        现金周转周期模型
        
        公式：现金周转周期 = 存货周转天数 + 应收账款周转天数 - 应付账款周转天数
        
        参数：
        - inventory_days：存货周转天数
        - receivables_days：应收账款周转天数
        - payables_days：应付账款周转天数
        
        返回：现金周转周期分析和预警
        """
        cash_cycle = inventory_days + receivables_days - payables_days
        
        # 行业平均水平示例
        industry_avg_inventory = 45  # 行业平均存货周转天数
        industry_avg_receivables = 60  # 行业平均应收账款周转天数
        industry_avg_payables = 30  # 行业平均应付账款周转天数
        industry_avg_cycle = industry_avg_inventory + industry_avg_receivables - industry_avg_payables
        
        # 预警阈值
        inventory_threshold = 60
        receivables_threshold = 90
        payables_threshold = 20
        
        # 分析
        analysis = {
            "现金周转周期": cash_cycle,
            "存货周转天数": inventory_days,
            "应收账款周转天数": receivables_days,
            "应付账款周转天数": payables_days,
            "行业平均周期": industry_avg_cycle,
            "与行业对比": {
                "优于行业": cash_cycle < industry_avg_cycle,
                "劣于行业": cash_cycle > industry_avg_cycle,
                "差距天数": cash_cycle - industry_avg_cycle
            },
            "预警状态": {
                "存货周转过长": inventory_days > inventory_threshold,
                "应收账款周转过长": receivables_days > receivables_threshold,
                "应付账款周转过短": payables_days < payables_threshold
            },
            "改进建议": [],
            "资金周转风险": "低" if cash_cycle <= industry_avg_cycle else "高"
        }
        
        # 生成改进建议
        if inventory_days > industry_avg_inventory:
            analysis["改进建议"].append("优化库存管理，加快存货周转")
        if receivables_days > industry_avg_receivables:
            analysis["改进建议"].append("优化销售政策，加快应收账款回款")
        if payables_days < industry_avg_payables:
            analysis["改进建议"].append("优化采购政策，延长应付账款周转")
        
        return analysis
    
    def optimal_cash_holding(self, current_cash, historical_needs):
        """
        最佳现金持有量模型
        
        参数：
        - current_cash：当前现金余额
        - historical_needs：历史现金需求数据（列表）
        
        返回：最佳现金持有量范围和建议
        """
        if not historical_needs:
            return {
                "error": "需要历史现金需求数据"
            }
        
        avg_needs = np.mean(historical_needs)
        max_needs = np.max(historical_needs)
        min_needs = np.min(historical_needs)
        std_needs = np.std(historical_needs)
        
        # 计算最佳现金持有量上下限
        lower_limit = avg_needs * 0.8 - std_needs  # 下限：低于此值必须补钱
        upper_limit = avg_needs * 1.2 + std_needs  # 上限：高于此值可做短期投资
        
        analysis = {
            "当前现金余额": current_cash,
            "历史现金需求统计": {
                "平均值": avg_needs,
                "最大值": max_needs,
                "最小值": min_needs,
                "标准差": std_needs
            },
            "最佳现金持有量": {
                "下限": lower_limit,
                "上限": upper_limit,
                "合理范围": f"{lower_limit:.2f} - {upper_limit:.2f}"
            },
            "当前状况": {
                "低于下限": current_cash < lower_limit,
                "高于上限": current_cash > upper_limit,
                "在合理范围内": lower_limit <= current_cash <= upper_limit,
                "过剩资金": current_cash - upper_limit if current_cash > upper_limit else 0,
                "短缺资金": lower_limit - current_cash if current_cash < lower_limit else 0
            },
            "行动建议": {
                "低于下限": "必须补充现金，否则可能面临资金短缺风险",
                "高于上限": "多余资金可以拿去做短期投资，提高资金使用效率",
                "在合理范围内": "保持当前现金水平，定期监控"
            }
        }
        
        return analysis
    
    def inventory_as_cash(self, inventory_value, turnover_days, categories):
        """
        存货占用模型
        
        参数：
        - inventory_value：存货总价值
        - turnover_days：存货周转天数
        - categories：产品类别字典（类别:价值）
        
        返回：存货占用分析和优化建议
        """
        # ABC分类分析
        total_value = sum(categories.values())
        abc_classification = {}
        
        for category, value in categories.items():
            percentage = (value / total_value) * 100
            
            if percentage >= 70:
                abc_classification[category] = "A类（货值高、品种少）"
            elif percentage >= 20:
                abc_classification[category] = "B类（中等货值）"
            else:
                abc_classification[category] = "C类（小零碎）"
        
        # 资金占用成本计算（假设资金成本率为6%）
        funding_cost_rate = 0.06
        inventory_cash_cost = inventory_value * (turnover_days / 365) * funding_cost_rate
        
        # 订货策略判断
        if turnover_days < 30:
            ordering_strategy = "定量订货"
            strategy_reason = "需求稳定，周转快"
        else:
            ordering_strategy = "定期订货"
            strategy_reason = "需求不稳定，周转慢"
        
        analysis = {
            "存货总价值": inventory_value,
            "存货周转天数": turnover_days,
            "资金占用成本": inventory_cash_cost,
            "ABC分类结果": abc_classification,
            "订货策略": ordering_strategy,
            "策略理由": strategy_reason,
            "资金占用影响": f"库存每多压一个月，现金周转周期拉长一个月",
            "管理建议": {
                "A类产品": "盯着管，少进货快出货",
                "B类产品": "常规管理，适度库存",
                "C类产品": "批量采购省事就行"
            },
            "订货决策": "订货时计算：多进一批货占用的资金成本是多少？"
        }
        
        return analysis
    
    def credit_decisions(self, customer_data, transaction_value, profit_margin):
        """
        信用决策模型
        
        参数：
        - customer_data：客户信息字典
        - transaction_value：交易金额
        - profit_margin：毛利率
        
        返回：信用决策分析和授信额度
        """
        # 信用评分计算
        credit_score = 0
        
        # 合作年限评分
        years_cooperation = customer_data.get("合作年限", 0)
        if years_cooperation >= 5:
            credit_score += 20
        elif years_cooperation >= 3:
            credit_score += 15
        elif years_cooperation >= 1:
            credit_score += 10
        else:
            credit_score += 5
        
        # 付款记录评分
        payment_record = customer_data.get("过往付款记录", "未知")
        if payment_record == "及时":
            credit_score += 20
        elif payment_record == "偶尔延迟":
            credit_score += 15
        elif payment_record == "经常延迟":
            credit_score += 5
        
        # 经营规模评分
        business_size = customer_data.get("经营规模", "未知")
        if business_size == "大型企业":
            credit_score += 20
        elif business_size == "中型企业":
            credit_score += 15
        elif business_size == "小型企业":
            credit_score += 10
        
        # 信用评级
        if credit_score >= 50:
            credit_level = "高信用等级"
            credit_limit_multiplier = 1.5
            credit_days = 60
        elif credit_score >= 30:
            credit_level = "中信用等级"
            credit_limit_multiplier = 1.0
            credit_days = 30
        else:
            credit_level = "低信用等级"
            credit_limit_multiplier = 0.5
            credit_days = 0
        
        # 客户类型处理
        customer_type = customer_data.get("客户类型", "新客户")
        if customer_type == "新客户":
            credit_limit = 0  # 一律款到发货
        else:
            credit_limit = transaction_value * credit_limit_multiplier
        
        # 资金成本率和坏账率
        funding_cost_rate = 0.06
        bad_debt_rate = 0.02
        
        # 收益计算
        profit = transaction_value * profit_margin
        funding_cost = transaction_value * (credit_days / 365) * funding_cost_rate
        bad_debt_cost = credit_limit * bad_debt_rate
        net_profit = profit - funding_cost - bad_debt_cost
        
        analysis = {
            "信用评分": credit_score,
            "信用等级": credit_level,
            "客户类型": customer_type,
            "授信额度": credit_limit,
            "账期天数": credit_days,
            "交易金额": transaction_value,
            "毛利率": profit_margin,
            "资金占用成本": funding_cost,
            "坏账风险成本": bad_debt_cost,
            "收益分析": {
                "毛利润": profit,
                "资金占用成本": funding_cost,
                "坏账风险成本": bad_debt_cost,
                "净收益": net_profit
            },
            "决策建议": {
                "批准赊销": net_profit > 0,
                "建议": "净收益大于0时可批准赊销，否则不建议赊账"
            },
            "额度调整": "额度和账期每年调整一次"
        }
        
        return analysis
    
    def cashflow_rolling_budget(self, outflows, inflows, weeks=4):
        """
        现金流预算模型
        
        参数：
        - outflows：现金流出列表（按周）
        - inflows：现金流入列表（按周）
        - weeks：预测周数
        
        返回：现金流预算分析和应急预案
        """
        cashflow_forecast = []
        cash_gaps = []
        cash_surplus = []
        
        cash_surplus_threshold = 10000000  # 盈余阈值
        
        for week in range(weeks):
            outflow = sum(outflows[week].values())
            inflow = sum(inflows[week].values())
            cashflow = inflow - outflow
            
            cashflow_forecast.append(cashflow)
            
            if cashflow < 0:
                cash_gaps.append({
                    "周": week + 1,
                    "缺口金额": abs(cashflow),
                    "应急预案": "跟银行申请透支额度或推迟非紧急付款"
                })
            
            if cashflow > cash_surplus_threshold:
                cash_surplus.append({
                    "周": week + 1,
                    "盈余金额": cashflow,
                    "投资建议": "多余资金做短期投资"
                })
        
        analysis = {
            "现金流预测": cashflow_forecast,
            "现金流缺口": cash_gaps,
            "资金盈余": cash_surplus,
            "现金流出明细": {
                "工资": outflows[0].get("工资", 0),
                "房租": outflows[0].get("房租", 0),
                "税费": outflows[0].get("税费", 0),
                "银行利息": outflows[0].get("银行利息", 0),
                "其他支出": outflows[0].get("其他支出", 0)
            },
            "现金流入明细": {
                "大客户回款": inflows[0].get("大客户回款", 0),
                "新签合同收款": inflows[0].get("新签合同收款", 0),
                "其他收入": inflows[0].get("其他收入", 0)
            },
            "滚动预算原则": "这周排未来四周，下周再排未来四周，不断往前滚",
            "预算编制步骤": [
                "第一步：按周来排，把必须付的列出来（工资、房租、税费、银行利息）",
                "第二步：把预计要收的列进去（大客户回款预计哪天到，新签合同预计哪天打款）",
                "第三步：看差额"
            ],
            "系统支持": "提供现金流净额、存货、应收账款、应付账款等关键财务指标的同比和环比变化"
        }
        
        return analysis
    
    def generate_cfo_report(self):
        """生成CFO资金管理报告"""
        report = {
            "报告时间": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "资金管理五大模型": [
                "现金周转周期模型",
                "最佳现金持有量模型",
                "存货占用模型",
                "信用决策模型",
                "现金流预算模型"
            ],
            "CFO核心原则": {
                "Cash is oxygen": "现金流是氧气 - 盈利企业也会因现金流问题倒闭",
                "13-week rolling forecast": "13周滚动预测 - 短期可见性防止意外",
                "Raise when you can": "能融资时就融资 - 不要等到必须融资时",
                "No board surprises": "董事会无意外 - 及早报告坏消息并提供背景",
                "Every dollar has opportunity cost": "每一美元都有机会成本 - 比较所有选项的回报",
                "Simplicity over precision": "简单优于精确 - 一页模型胜过50页表格",
                "Finance enables": "财务赋能 - 与运营部门合作，不要阻碍他们"
            },
            "资金管理策略": {
                "现金周转": "重点关注存货周转天数、应收账款周转天数、应付账款周转天数",
                "现金持有": "避免资金闲置，也避免资金短缺",
                "库存管理": "把库存当成冻住的现金，优化库存管理",
                "信用决策": "信用额度动态调整，每年评估一次",
                "现金流预算": "滚动预算，提前预测资金缺口"
            },
            "实施建议": [
                "第一步：计算现金周转周期，与同行对比",
                "第二步：设定最佳现金持有量上下限",
                "第三步：实施库存ABC分类管理",
                "第四步：建立客户信用评级体系",
                "第五步：编制滚动现金流预算"
            ]
        }
        
        return report

# 测试函数
def test_cash_management():
    """测试资金管理五大模型"""
    cmm = CashManagementModels()
    
    print("=== CFO资金管理五大模型测试 ===\n")
    
    # 1. 现金周转周期模型
    cash_cycle_result = cmm.cash_turnover_cycle(
        inventory_days=60,
        receivables_days=90,
        payables_days=30
    )
    print("1. 现金周转周期模型:")
    print(f"现金周转周期: {cash_cycle_result['现金周转周期']}天")
    print(f"与行业对比: {cash_cycle_result['与行业对比']['差距天数']}天")
    print(f"资金周转风险: {cash_cycle_result['资金周转风险']}")
    
    # 2. 最佳现金持有量模型
    cash_holding_result = cmm.optimal_cash_holding(
        current_cash=150000000,
        historical_needs=[80000000, 90000000, 70000000, 85000000]
    )
    print("\n2. 最佳现金持有量模型:")
    print(f"当前现金: {cash_holding_result['当前现金余额']}")
    print(f"合理范围: {cash_holding_result['最佳现金持有量']['合理范围']}")
    print(f"当前状况: {cash_holding_result['当前状况']['在合理范围内']}")
    
    # 3. 存货占用模型
    inventory_result = cmm.inventory_as_cash(
        inventory_value=200000000,
        turnover_days=75,
        categories={
            "冰箱": 80000000,
            "洗衣机": 50000000,
            "空调": 40000000,
            "智能家居": 30000000,
            "零部件": 10000000
        }
    )
    print("\n3. 存货占用模型:")
    print(f"存货总价值: {inventory_result['存货总价值']}")
    print(f"ABC分类: {inventory_result['ABC分类结果']}")
    print(f"资金占用成本: {inventory_result['资金占用成本']:.2f}")
    
    # 4. 信用决策模型
    credit_result = cmm.credit_decisions(
        customer_data={
            "合作年限": 3,
            "过往付款记录": "及时",
            "经营规模": "中型企业",
            "客户类型": "老客户"
        },
        transaction_value=10000000,
        profit_margin=0.15
    )
    print("\n4. 信用决策模型:")
    print(f"信用评分: {credit_result['信用评分']}")
    print(f"信用等级: {credit_result['信用等级']}")
    print(f"授信额度: {credit_result['授信额度']}")
    print(f"净收益: {credit_result['收益分析']['净收益']:.2f}")
    print(f"决策建议: {credit_result['决策建议']['建议']}")
    
    # 5. 现金流预算模型
    cashflow_result = cmm.cashflow_rolling_budget(
        outflows=[
            {"工资": 5000000, "房租": 1000000, "税费": 2000000, "银行利息": 500000, "其他支出": 1500000},
            {"工资": 5000000, "房租": 1000000, "税费": 2000000, "银行利息": 500000, "其他支出": 1500000},
            {"工资": 5000000, "房租": 1000000, "税费": 2000000, "银行利息": 500000, "其他支出": 1500000},
            {"工资": 5000000, "房租": 1000000, "税费": 2000000, "银行利息": 500000, "其他支出": 1500000}
        ],
        inflows=[
            {"大客户回款": 8000000, "新签合同收款": 5000000, "其他收入": 1000000},
            {"大客户回款": 7000000, "新签合同收款": 4000000, "其他收入": 1000000},
            {"大客户回款": 9000000, "新签合同收款": 6000000, "其他收入": 1000000},
            {"大客户回款": 8500000, "新签合同收款": 5000000, "其他收入": 1000000}
        ],
        weeks=4
    )
    print("\n5. 现金流预算模型:")
    print(f"现金流预测: {cashflow_result['现金流预测']}")
    print(f"现金流缺口: {cashflow_result['现金流缺口']}")
    print(f"资金盈余: {cashflow_result['资金盈余']}")
    
    # 6. CFO报告
    cfo_report = cmm.generate_cfo_report()
    print("\n=== CFO资金管理报告 ===")
    print(f"报告时间: {cfo_report['报告时间']}")
    print(f"核心原则: Cash is oxygen - 现金流是氧气")
    print(f"实施建议: {cfo_report['实施建议'][0]}")
    
    return "CFO资金管理五大模型测试完成"

if __name__ == "__main__":
    test_cash_management()