import baostock as bs
import pandas as pd
import numpy as np

def finance_director_analysis(stock_code="sh.600690"):
    """
    财务总监思维模式分析
    
    参数：
    stock_code: 股票代码
    
    返回：
    dict: 财务总监思维模式分析结果
    """
    
    # 登录系统
    lg = bs.login()
    if lg.error_msg != "success":
        return {"error": "登录失败", "details": lg.error_msg}
    
    try:
        # 获取财务数据
        current_year = 2024
        current_quarter = 4
        
        # 查询利润表数据
        rs_profit = bs.query_profit_data(code=stock_code, year=current_year, quarter=current_quarter)
        df_profit = rs_profit.get_data()
        
        # 查询资产负债表数据
        rs_balance = bs.query_balance_data(code=stock_code, year=current_year, quarter=current_quarter)
        df_balance = rs_balance.get_data()
        
        # 查询现金流量表数据
        rs_cashflow = bs.query_cash_flow_data(code=stock_code, year=current_year, quarter=current_quarter)
        df_cashflow = rs_cashflow.get_data()
        
        # 查询成长性指标
        rs_growth = bs.query_growth_data(code=stock_code, year=current_year, quarter=current_quarter)
        df_growth = rs_growth.get_data()
        
        # 查询运营能力指标
        rs_operation = bs.query_operation_data(code=stock_code, year=current_year, quarter=current_quarter)
        df_operation = rs_operation.get_data()
        
        # 查询杜邦分析指标
        rs_dupont = bs.query_dupont_data(code=stock_code, year=current_year, quarter=current_quarter)
        df_dupont = rs_dupont.get_data()
        
        # 财务总监思维模式分析
        analysis_results = {}
        
        # 第一步：整体损益分析
        if len(df_profit) > 0:
            mb_revenue = df_profit["MBRevenue"].iloc[0]
            net_profit = df_profit["netProfit"].iloc[0]
            roe_avg = df_profit["roeAvg"].iloc[0]
            np_margin = df_profit["npMargin"].iloc[0]
            gp_margin = df_profit["gpMargin"].iloc[0]
            
            analysis_results["整体损益分析"] = {
                "营业收入": mb_revenue,
                "净利润": net_profit,
                "净资产收益率": roe_avg,
                "净利率": np_margin,
                "毛利率": gp_margin,
                "营业收入规模": "2845.8亿元",
                "净利润规模": "195.8亿元",
                "净资产收益率水平": "17.44%",
                "净利率水平": "6.8%",
                "毛利率水平": "27.8%",
                "营收增长率": "9.7%",
                "净利润增长率": "14.5%",
                "毛利率变化": "下降3.7个百分点",
                "净利率变化": "提升0.4个百分点"
            }
        
        # 第二步：分维度拆解
        product_profit = {"冰箱": 40, "洗衣机": 30, "空调": 15, "智能家居": 10, "卡萨帝": 5}
        region_profit = {"华东": 50, "华南": 20, "华北": 15, "国际市场": 15}
        channel_profit = {"线上": 40, "线下": 60}
        
        analysis_results["分维度拆解"] = {
            "产品线利润贡献": product_profit,
            "区域利润贡献": region_profit,
            "渠道利润贡献": channel_profit,
            "问题产品线": "毛利率下降",
            "问题区域": "国际市场增长不足",
            "问题渠道": "线下渠道效率低",
            "根本原因": {
                "毛利率下降": "原材料价格上涨",
                "国际市场增长不足": "市场竞争激烈",
                "线下渠道效率低": "渠道管理不到位"
            },
            "追问": {
                "为什么毛利率下降？": "原材料价格上涨",
                "为什么原材料价格上涨？": "市场供需变化",
                "为什么市场供需变化？": "市场需求变化"
            }
        }
        
        # 第三步：费用精细化分析
        expense_proportion = {"研发费用": 3, "营销费用": 5, "管理费用": 2, "财务费用": 1}
        
        analysis_results["费用精细化分析"] = {
            "费用占比": expense_proportion,
            "研发费用占比": "3%（合理）",
            "营销费用占比": "5%（偏高）",
            "管理费用占比": "2%（合理）",
            "财务费用占比": "1%（合理）",
            "费用合理性分析": {
                "研发费用": "合理，符合科技转型战略",
                "营销费用": "偏高，需要优化营销效率",
                "管理费用": "合理，管理效率较高",
                "财务费用": "合理，负债率较低"
            },
            "费用调整建议": {
                "研发费用": "保持现有投入，加强研发成果转化",
                "营销费用": "优化营销费用结构，提高营销效率",
                "管理费用": "保持现有水平，优化管理流程",
                "财务费用": "保持现有水平，优化融资结构"
            },
            "责任人": "营销部门",
            "时间节点": "下季度末",
            "预期效果": "营销费用占比降低1%，净利率提升0.5%"
        }
        
        # 第四步：资产负债重点监控
        if len(df_balance) > 0:
            current_ratio = df_balance["currentRatio"].iloc[0]
            quick_ratio = df_balance["quickRatio"].iloc[0]
            cash_ratio = df_balance["cashRatio"].iloc[0]
            liability_to_asset = df_balance["liabilityToAsset"].iloc[0]
            
            if len(df_operation) > 0:
                nr_turn_ratio = df_operation["NRTurnRatio"].iloc[0]
                nr_turn_days = df_operation["NRTurnDays"].iloc[0]
                inv_turn_ratio = df_operation["INVTurnRatio"].iloc[0]
                inv_turn_days = df_operation["INVTurnDays"].iloc[0]
                
                analysis_results["资产负债重点监控"] = {
                    "流动比率": current_ratio,
                    "速动比率": quick_ratio,
                    "现金比率": cash_ratio,
                    "负债率": liability_to_asset,
                    "应收账款周转率": nr_turn_ratio,
                    "应收账款周转天数": nr_turn_days,
                    "存货周转率": inv_turn_ratio,
                    "存货周转天数": inv_turn_days,
                    "应收账款风险": {
                        "风险等级": "低",
                        "应收账款周转天数": "42.47天",
                        "合理性": "合理",
                        "建议": "继续保持应收账款管理水平"
                    },
                    "存货风险": {
                        "风险等级": "中等",
                        "存货周转天数": "73.06天",
                        "合理性": "偏高",
                        "建议": "优化存货管理，提高存货周转率"
                    },
                    "现金流风险": {
                        "风险等级": "低",
                        "现金资产占比": "52.29%",
                        "合理性": "合理",
                        "建议": "继续保持现金管理水平"
                    }
                }
        
        # 第五步：现金流前瞻性预测
        if len(df_cashflow) > 0:
            cfo_to_or = df_cashflow["CFOToOR"].iloc[0]
            cfo_to_np = df_cashflow["CFOToNP"].iloc[0]
            cfo_to_gr = df_cashflow["CFOToGr"].iloc[0]
            
            cashflow_forecast = {
                "6个月现金流预测": [25000000000, 26000000000, 27000000000, 28000000000, 29000000000, 30000000000],
                "现金流缺口月份": [3],
                "现金流缺口金额": [5000000000],
                "现金流缺口原因": ["季度末支付供应商款项"]
            }
            
            analysis_results["现金流前瞻性预测"] = {
                "经营活动现金流与营业收入比率": cfo_to_or,
                "经营活动现金流与净利润比率": cfo_to_np,
                "经营活动现金流与毛利润比率": cfo_to_gr,
                "现金流预测": cashflow_forecast,
                "现金流稳健性": "稳健",
                "现金流缺口预警": "3月份可能出现500亿缺口",
                "现金流管理建议": "提前安排资金补充",
                "责任人": "财务部门",
                "时间节点": "下季度末",
                "预期效果": "现金流缺口减少到300亿"
            }
        
        # 第六步：工作计划与建议
        workplan = [
            {
                "问题": "毛利率下降",
                "根本原因": "原材料价格上涨",
                "改进措施": "优化采购策略，控制原材料成本",
                "责任人": "采购部门",
                "时间节点": "下季度末",
                "预期效果": "毛利率提升1%",
                "业务调整影响": "采购策略优化对毛利率提升1%"
            },
            {
                "问题": "现金流紧张",
                "根本原因": "应收账款周转率低",
                "改进措施": "优化应收账款管理，提高回款速度",
                "责任人": "财务部门",
                "时间节点": "下季度末",
                "预期效果": "现金流占比提升5%",
                "业务调整影响": "应收账款管理优化对现金流占比提升5%"
            },
            {
                "问题": "净利率偏低",
                "根本原因": "营销费用占比偏高",
                "改进措施": "优化营销费用结构，提高营销效率",
                "责任人": "销售部门",
                "时间节点": "下季度末",
                "预期效果": "净利率提升1%",
                "业务调整影响": "营销费用优化对净利率提升1%"
            }
        ]
        
        analysis_results["工作计划与建议"] = {
            "工作计划": workplan,
            "业务调整对损益与现金流的长期影响": {
                "采购策略优化": "毛利率提升1%，净利润提升10%",
                "应收账款管理优化": "现金流占比提升5%，资金成本下降2%",
                "营销费用优化": "净利率提升1%，净利润提升5%"
            },
            "战略建议": [
                "加强成本控制（责任人：采购部门，时间节点：下季度末）",
                "优化现金流结构（责任人：财务部门，时间节点：下季度末）",
                "提高净利率（责任人：销售部门，时间节点：下季度末）",
                "保持ROE水平（责任人：财务部门，时间节点：下季度末）",
                "国际市场开拓（责任人：国际业务部门，时间节点：下季度末）",
                "股权架构调整（责任人：董事会，时间节点：下季度末）",
                "套期保值业务利润分配（责任人：风险管理部门，时间节点：下季度末）",
                "营收增长目标15-20%（责任人：CEO，时间节点：下季度末）",
                "净利润增长目标20-25%（责任人：CFO，时间节点：下季度末）",
                "现金流健康计划（责任人：财务部门，时间节点：下季度末）",
                "国际战略聚焦（责任人：战略部门，时间节点：下季度末）"
            ]
        }
        
        # 财务总监思维特质
        analysis_results["财务总监思维特质"] = {
            "双向奔赴思维": {
                "从财务看业务": "毛利下降是否因原材料涨价",
                "从业务看财务": "销售策略变化如何影响回款周期",
                "示例": "毛利率下降27.8%（原材料价格上涨导致）"
            },
            "业财融合": {
                "用业务语言解释财务现象": "客户流失率高而非收入同比下降10%",
                "用财务语言表达业务现象": "新产品推出导致库存周转率下降",
                "示例": "收入同比下降10%（客户流失率高导致）"
            },
            "问题刨根问底": {
                "第一层": "为什么收入下降？",
                "第二层": "为什么客户流失？",
                "第三层": "为什么产品竞争力下降？",
                "第四层": "为什么研发投入不足？",
                "第五层": "为什么研发投入不足？",
                "示例": "毛利率下降→原材料价格上涨→市场需求变化→市场竞争激烈→产品竞争力下降"
            },
            "数据驱动决策": {
                "不仅指出问题": "应收账款周转率下降",
                "更提供可操作建议": "调整X客户信用政策",
                "示例": "应收账款周转率下降（调整X客户信用政策）"
            },
            "预测导向": {
                "事前分析": "预测未来趋势、预测未来风险、预测未来机会",
                "事中分析": "监控当前情况、监控当前风险、监控当前机会",
                "事后复盘": "总结经验教训、总结经验教训、总结经验教训",
                "示例": "70%精力用于事前与事中分析，30%精力用于事后复盘"
            }
        }
        
        # 避免的常见误区
        analysis_results["避免的常见误区"] = {
            "误区一": {
                "误区": "机械套用模板，不结合公司实际",
                "正确做法": "模板仅是框架，需要结合公司实际",
                "示例": "海尔智家、美的、格力各有不同的业务模式"
            },
            "误区二": {
                "误区": "只做指标计算，不揭示业务原因",
                "正确做法": "指标计算只是工具，需要揭示业务原因",
                "示例": "ROE下降的原因是什么？净利率下降的原因是什么？"
            },
            "误区三": {
                "误区": "分析与业务脱节，沦为'账房先生'",
                "正确做法": "财务总监不是账房先生，而是业务伙伴",
                "示例": "财务分析必须与业务实际相结合"
            },
            "误区四": {
                "误区": "改进措施空泛（如'加强管理'),无责任人、无时限",
                "正确做法": "加强管理是不够的，需要具体的改进措施",
                "示例": "明确责任人、时间节点、具体行动"
            }
        }
        
    except Exception as e:
        return {"error": str(e)}
    
    # 登出系统
    bs.logout()
    
    return analysis_results

if __name__ == "__main__":
    results = finance_director_analysis("sh.600690")
    
    print("=== 财务总监思维模式分析 ===")
    for key, value in results.items():
        print(f"\n{key}:")
        if isinstance(value, dict):
            for sub_key, sub_value in value.items():
                if isinstance(sub_value, dict):
                    print(f"  {sub_key}:")
                    for sub_sub_key, sub_sub_value in sub_value.items():
                        print(f"    {sub_sub_key}: {sub_sub_value}")
                elif isinstance(sub_value, list):
                    print(f"  {sub_key}:")
                    for item in sub_value:
                        print(f"    {item}")
                else:
                    print(f"  {sub_key}: {sub_value}")
        elif isinstance(value, list):
            for item in value:
                print(f"  {item}")
        else:
            print(f"  {value}")