#!/usr/bin/env python3
"""
九大财务模型实现脚本
基于《财务分析必备：九大财务模型详解》文档
"""

import pandas as pd
import numpy as np
import baostock as bs
from datetime import datetime

class FinancialModels:
    """九大财务模型实现类"""
    
    def __init__(self):
        """初始化"""
        print("=== 九大财务模型 ===")
        print("1. 比率分析模型")
        print("2. 杜邦分析模型")
        print("3. 现金流分析模型")
        print("4. 现金流折现模型（DCF）")
        print("5. 可比公司分析法")
        print("6. 并购整合分析模型")
        print("7. 全面财务预测模型")
        print("8. 敏感性分析模型")
        print("9. SWOT与财务融合分析")
        
    def ratio_analysis_model(self, revenue, profit, assets, liabilities, equity):
        """
        比率分析模型：消除公司规模影响，便于与同行/历年对比
        """
        ratios = {
            "盈利能力": {
                "毛利率": None,  # 需要成本数据
                "净利率": profit / revenue if revenue > 0 else None,
                "ROE": profit / equity if equity > 0 else None
            },
            "偿债能力": {
                "资产负债率": liabilities / assets if assets > 0 else None,
                "流动比率": None  # 需要流动资产和流动负债数据
            },
            "运营能力": {
                "应收账款周转率": None,  # 需要应收账款数据
                "存货周转率": None  # 需要存货数据
            },
            "成长能力": {
                "营收增长率": None,  # 需要上年营收数据
                "净利润增长率": None  # 需要上年净利润数据
            }
        }
        
        # 示例行业对比分析
        industry_averages = {
            "净利率": 0.15,  # 行业平均净利率15%
            "资产负债率": 0.55,
            "应收账款周转率": 5.0
        }
        
        assessment = {}
        if ratios["盈利能力"]["净利率"]:
            assessment["盈利状况"] = "盈利能力不如同行" if ratios["盈利能力"]["净利率"] < industry_averages["净利率"] else "盈利健康"
        if ratios["偿债能力"]["资产负债率"]:
            assessment["偿债能力"] = "负债偏高" if ratios["偿债能力"]["资产负债率"] > industry_averages["资产负债率"] else "偿债稳健"
        
        return {"比率分析": ratios, "行业对比": assessment}
    
    def dupont_analysis_model(self, roe, net_profit_margin, asset_turnover, equity_multiplier):
        """
        杜邦分析模型：分解ROE为三个指标的乘积，找出问题根源
        ROE = 净利率 × 资产周转率 × 权益乘数
        """
        decomposition = {
            "净利率": net_profit_margin,
            "资产周转率": asset_turnover,
            "权益乘数": equity_multiplier,
            "ROE": roe
        }
        
        # 示例ROE下滑分析
        historical_npm = 0.068451  # 海尔智家2024年净利率
        historical_at = 0.174433  # 海尔智家ROE
        historical_em = 2.5  # 示例权益乘数
        
        root_causes = []
        if net_profit_margin < historical_npm:
            root_causes.append("净利率下降 → 成本费用没控制好")
        if asset_turnover < historical_at:
            root_causes.append("资产周转率下降 → 存货/应收账款积压")
        if equity_multiplier < historical_em:
            root_causes.append("权益乘数下降 → 负债太少，没合理利用资金放大收益")
        
        return {
            "杜邦分解": decomposition,
            "问题根源": root_causes,
            "管理层建议": ["调整成本结构", "优化库存管理", "优化负债结构"]
        }
    
    def cashflow_analysis_model(self, operating_cf, investing_cf, financing_cf, strategic_focus="扩张"):
        """
        现金流分析模型：重点关注三大现金流
        """
        cashflow_health = {
            "经营现金流持续为正": operating_cf > 0,
            "投资现金流匹配战略": (investing_cf < 0 and strategic_focus == "扩张") or (investing_cf >= 0 and strategic_focus == "稳定"),
            "偿债风险分析": financing_cf > 0  # 融资现金流为正表示有融资流入
        }
        
        # 战略匹配分析
        strategic_assessment = []
        if strategic_focus == "扩张" and investing_cf < 0:
            strategic_assessment.append("投资现金流负→正常：公司在扩张期")
        elif strategic_focus == "稳定" and investing_cf < 0:
            strategic_assessment.append("投资现金流负→异常：资产有问题")
        
        # 偿债压力分析（示例）
        debt_pressure = financing_cf < 0
        
        return {
            "现金流健康状况": cashflow_health,
            "战略匹配": strategic_assessment,
            "偿债压力": debt_pressure,
            "关键建议": ["优化经营现金流", "匹配投资与战略", "控制短期负债规模"]
        }
    
    def dcf_model(self, free_cashflows, discount_rate=0.08, growth_rate=0.05, terminal_value_method="永续增长"):
        """
        DCF估值模型：公司未来自由现金流折现到当前价值
        """
        # 预测未来5年自由现金流
        future_fcf = [free_cashflows * (1 + growth_rate)**i for i in range(1, 6)]
        
        # 计算折现值
        discounted_fcf = [fcf / (1 + discount_rate)**i for i, fcf in enumerate(future_fcf)]
        
        # 终端价值计算
        if terminal_value_method == "永续增长":
            terminal_value = future_fcf[-1] * (1 + growth_rate) / (discount_rate - growth_rate)
        elif terminal_value_method == "倍数法":
            terminal_multiple = 10  # 示例倍数
            terminal_value = future_fcf[-1] * terminal_multiple
        
        # 总价值
        total_value = sum(discounted_fcf) + terminal_value
        
        return {
            "预测现金流": future_fcf,
            "折现值": discounted_fcf,
            "终端价值": terminal_value,
            "总价值": total_value,
            "适用场景": "商业模式稳定、现金流可预测的公司（消费、公用事业等）"
        }
    
    def comparable_company_analysis(self, target_company, comparable_companies):
        """
        可比公司分析法：参考相似上市公司估值水平
        """
        # 可比公司数据（示例）
        comparable_data = {
            "公司1": {"市盈率": 20, "市净率": 2.5, "市值": 50000000000},
            "公司2": {"市盈率": 18, "市净率": 2.3, "市值": 48000000000},
            "公司3": {"市盈率": 22, "市净率": 2.7, "市值": 55000000000}
        }
        
        # 平均估值水平
        average_pe = sum([comp["市盈率"] for comp in comparable_data.values()]) / len(comparable_data)
        average_pb = sum([comp["市净率"] for comp in comparable_data.values()]) / len(comparable_data)
        
        # 目标公司估值
        target_valuation = {
            "基于市盈率": target_company["净利润"] * average_pe,
            "基于市净率": target_company["净资产"] * average_pb,
            "估值区间": [target_company["净利润"] * min([comp["市盈率"] for comp in comparable_data.values()]),
                        target_company["净利润"] * max([comp["市盈率"] for comp in comparable_data.values()])]
        }
        
        return {
            "可比公司": comparable_data,
            "平均估值水平": {"市盈率": average_pe, "市净率": average_pb},
            "目标公司估值": target_valuation,
            "注意事项": ["参照本身可能失真", "需结合其他估值方法"]
        }
    
    def valuation_model_selection(self, company_type):
        """
        根据公司类型选择合适的估值模型
        """
        if company_type == "高分红":
            return "股利折现模型（适合分红公司）"
        elif company_type == "低分红高盈利":
            return "剩余收益模型（适合高盈利低分红公司）"
        elif company_type == "稳定现金流":
            return "现金流折现模型（DCF）"
        else:
            return "可比公司分析法"
    
    def merger_integration_model(self, synergies):
        """
        并购整合分析模型：量化协同效应
        """
        synergy_analysis = {
            "成本节省": synergies["cost_saving"],
            "收入增加": synergies["revenue_increase"],
            "效率提升": synergies["efficiency_gain"],
            "具体量化": {
                "人员优化": synergies["staff_reduction"],
                "供应链整合": synergies["supply_chain"],
                "技术共享": synergies["technology"],
                "市场协同": synergies["market"]
            }
        }
        
        return {
            "协同效应分析": synergy_analysis,
            "关键问题": [
                "两家公司合并后，是否真的能节省成本？",
                "具体能提升多少收入？",
                "效率提升体现在哪些方面？"
            ],
            "难点": "考验对两个企业业务细节的理解"
        }
    
    def comprehensive_financial_prediction_model(self, revenue_target, business_plan):
        """
        全面财务预测模型：三表联动预算编制
        """
        # 假设比率
        cost_ratio = 0.70  # 成本占比70%
        expense_ratio = 0.15  # 费用占比15%
        asset_ratio = 1.2  # 资产与营收比例
        liability_ratio = 0.6  # 负债与营收比例
        retention_rate = 0.3  # 利润留存率30%
        
        # 利润表预测
        profit_statement = {
            "营收目标": revenue_target,
            "成本预测": revenue_target * cost_ratio,
            "费用预测": revenue_target * expense_ratio,
            "利润预测": revenue_target - (revenue_target * cost_ratio) - (revenue_target * expense_ratio)
        }
        
        # 资产负债表预测
        balance_sheet = {
            "资产预测": revenue_target * asset_ratio,
            "负债预测": revenue_target * liability_ratio,
            "权益预测": profit_statement["利润预测"] * retention_rate
        }
        
        # 现金流量表预测
        depreciation = revenue_target * 0.05  # 折旧占比5%
        change_in_working_capital = revenue_target * 0.1  # 营运资本变化占比10%
        capital_investment = revenue_target * 0.2  # 资本投资占比20%
        debt_issuance = revenue_target * 0.1  # 债务发行占比10%
        equity_issuance = revenue_target * 0.05  # 股权发行占比5%
        
        cashflow_statement = {
            "经营现金流": profit_statement["利润预测"] + depreciation - change_in_working_capital,
            "投资现金流": capital_investment,
            "筹资现金流": debt_issuance + equity_issuance
        }
        
        # 三表联动校验
        check_logic = {
            "逻辑勾稽": cashflow_statement["经营现金流"] + cashflow_statement["投资现金流"] + cashflow_statement["筹资现金流"] == profit_statement["利润预测"],
            "平衡检查": balance_sheet["资产预测"] == balance_sheet["负债预测"] + balance_sheet["权益预测"]
        }
        
        return {
            "利润表": profit_statement,
            "资产负债表": balance_sheet,
            "现金流量表": cashflow_statement,
            "三表联动": check_logic,
            "应用场景": ["年度预算", "新业务扩张评估"],
            "关键假设": "revenue_target必须结合市场规模和业务规划"
        }
    
    def sensitivity_analysis_model(self, base_case, key_variables):
        """
        敏感性分析：关键变量对利润/估值的影响分析
        """
        sensitivity_results = {}
        
        # 示例影响系数
        cost_impact = 0.3  # 成本影响利润的系数
        discount_factor = 0.2  # 利率影响估值的系数
        
        for variable in key_variables:
            if variable == "市场需求":
                scenarios = {
                    "-10%": base_case["利润"] * 0.9,
                    "-5%": base_case["利润"] * 0.95,
                    "+5%": base_case["利润"] * 1.05,
                    "+10%": base_case["利润"] * 1.10
                }
            elif variable == "原材料成本":
                scenarios = {
                    "+5%": base_case["利润"] * (1 - 0.05 * cost_impact),
                    "+10%": base_case["利润"] * (1 - 0.10 * cost_impact),
                    "+15%": base_case["利润"] * (1 - 0.15 * cost_impact)
                }
            elif variable == "利率":
                scenarios = {
                    "+1%": base_case["估值"] * (1 - 0.01 * discount_factor),
                    "+2%": base_case["估值"] * (1 - 0.02 * discount_factor),
                    "+3%": base_case["估值"] * (1 - 0.03 * discount_factor)
                }
            
            sensitivity_results[variable] = scenarios
        
        return {
            "敏感性分析": sensitivity_results,
            "重点关注变量": ["市场需求", "原材料成本", "利率"],
            "关键问题": [
                "如果市场需求比预期低了10%，对利润目标影响多大？",
                "如果原材料成本比预期高了5%，影响多大？"
            ]
        }
    
    def swot_financial_analysis_model(self, swot_strategic):
        """
        SWOT与财务融合分析：让战略有数据支撑
        """
        swot_financial = {}
        
        # SWOT优势转化为财务指标
        if "技术优势" in swot_strategic["strengths"]:
            swot_financial["研发投入回报率"] = "ROI >= 20%"  # 示例
        
        if "品牌优势" in swot_strategic["strengths"]:
            swot_financial["品牌溢价利润率"] = "利润率提升10%"  # 示例
        
        # SWOT机会转化为财务预测
        if "市场新机会" in swot_strategic["opportunities"]:
            swot_financial["新增营收预测"] = "年均增长20%"  # 示例
        
        # SWOT劣势转化为财务风险
        if "成本劣势" in swot_strategic["weaknesses"]:
            swot_financial["成本劣势影响"] = "毛利率下降5%"  # 示例
        
        # SWOT威胁转化为财务预警
        if "竞争加剧" in swot_strategic["threats"]:
            swot_financial["竞争威胁利润率下降"] = "利润率下降5%"  # 示例
        
        return {
            "SWOT财务转化": swot_financial,
            "战略落地": {
                "技术优势": "研发投入回报率",
                "市场新机会": "新增营收预测",
                "成本劣势": "成本控制目标",
                "竞争加剧": "利润率预警阈值"
            },
            "价值": "使战略更落地，财务工作更有方向"
        }
    
    def test_all_models(self):
        """测试九大财务模型"""
        print("\n=== 九大财务模型测试 ===")
        
        # 1. 比率分析模型
        ratio_results = self.ratio_analysis_model(
            revenue=284582637563.47,
            profit=19575612501.68,
            assets=500000000000,
            liabilities=300000000000,
            equity=200000000000
        )
        print("\n1. 比率分析模型:")
        print(ratio_results)
        
        # 2. 杜邦分析模型
        dupont_results = self.dupont_analysis_model(
            roe=0.174433,
            net_profit_margin=0.068451,
            asset_turnover=0.277970,
            equity_multiplier=2.5
        )
        print("\n2. 杜邦分析模型:")
        print(dupont_results)
        
        # 3. 现金流分析模型
        cashflow_results = self.cashflow_analysis_model(
            operating_cf=50000000000,
            investing_cf=-20000000000,
            financing_cf=10000000000,
            strategic_focus="扩张"
        )
        print("\n3. 现金流分析模型:")
        print(cashflow_results)
        
        # 4. DCF模型
        dcf_results = self.dcf_model(free_cashflows=10000000000)
        print("\n4. DCF估值模型:")
        print(dcf_results)
        
        # 5. 可比公司分析法
        comparable_results = self.comparable_company_analysis(
            target_company={"净利润": 19575612501.68, "净资产": 200000000000},
            comparable_companies=None
        )
        print("\n5. 可比公司分析法:")
        print(comparable_results)
        
        # 6. 并购整合分析模型
        merger_results = self.merger_integration_model({
            "cost_saving": 10000000000,
            "revenue_increase": 50000000000,
            "efficiency_gain": "运营效率提升20%",
            "staff_reduction": "人员精简15%",
            "supply_chain": "供应链成本降低10%",
            "technology": "技术共享收益5亿",
            "market": "市场协同新增营收10亿"
        })
        print("\n6. 并购整合分析模型:")
        print(merger_results)
        
        # 7. 全面财务预测模型
        prediction_results = self.comprehensive_financial_prediction_model(
            revenue_target=300000000000,
            business_plan={"市场规模": "1000亿", "市场份额": "30%"}
        )
        print("\n7. 全面财务预测模型:")
        print(prediction_results)
        
        # 8. 敏感性分析模型
        sensitivity_results = self.sensitivity_analysis_model(
            base_case={"利润": 19575612501.68, "估值": 500000000000},
            key_variables=["市场需求", "原材料成本", "利率"]
        )
        print("\n8. 敏感性分析模型:")
        print(sensitivity_results)
        
        # 9. SWOT与财务融合分析
        swot_results = self.swot_financial_analysis_model({
            "strengths": ["技术优势", "品牌优势"],
            "weaknesses": ["成本劣势"],
            "opportunities": ["市场新机会"],
            "threats": ["竞争加剧"]
        })
        print("\n9. SWOT与财务融合分析:")
        print(swot_results)
        
        return "九大财务模型测试完成"

if __name__ == "__main__":
    fm = FinancialModels()
    fm.test_all_models()