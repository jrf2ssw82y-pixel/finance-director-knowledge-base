import baostock as bs
import pandas as pd
import numpy as np

def analyze_finance_director(stock_code="sh.600690"):
    """
    财务总监级别的上市公司财务分析
    
    参数：
    stock_code: 股票代码，如sh.600690、sz.000001等
    
    返回：
    dict: 包含财务总监级别分析的字典
    """
    
    # 登录系统
    lg = bs.login()
    if lg.error_msg != "success":
        return {"error": "登录失败", "details": lg.error_msg}
    
    try:
        # 基本信息
        rs_info = bs.query_stock_basic(code=stock_code)
        df_info = rs_info.get_data()
        
        # 财务数据获取（最近4个季度）
        analysis_results = {}
        
        # 获取最近的年份和季度
        current_year = 2024
        current_quarter = 4
        
        # 利润表数据
        rs_profit = bs.query_profit_data(code=stock_code, year=current_year, quarter=current_quarter)
        df_profit = rs_profit.get_data()
        
        # 资产负债表数据
        rs_balance = bs.query_balance_data(code=stock_code, year=current_year, quarter=current_quarter)
        df_balance = rs_balance.get_data()
        
        # 现金流量表数据
        rs_cashflow = bs.query_cash_flow_data(code=stock_code, year=current_year, quarter=current_quarter)
        df_cashflow = rs_cashflow.get_data()
        
        # 成长性指标
        rs_growth = bs.query_growth_data(code=stock_code, year=current_year, quarter=current_quarter)
        df_growth = rs_growth.get_data()
        
        # 运营能力指标
        rs_operation = bs.query_operation_data(code=stock_code, year=current_year, quarter=current_quarter)
        df_operation = rs_operation.get_data()
        
        # 杜邦分析指标
        rs_dupont = bs.query_dupont_data(code=stock_code, year=current_year, quarter=current_quarter)
        df_dupont = rs_dupont.get_data()
        
        # 财务总监分析
        analysis_results["基本信息"] = df_info
        analysis_results["利润表"] = df_profit
        analysis_results["资产负债表"] = df_balance
        analysis_results["现金流量表"] = df_cashflow
        analysis_results["成长性指标"] = df_growth
        analysis_results["运营能力指标"] = df_operation
        analysis_results["杜邦分析"] = df_dupont
        
        # 财务总监级别分析
        # 1. 营收增长速度分析
        if "MBRevenue" in df_profit.columns:
            revenue = df_profit["MBRevenue"].iloc[0]
            analysis_results["营业收入"] = revenue
        
        # 2. 净利润增长速度分析
        if "netProfit" in df_profit.columns:
            net_profit = df_profit["netProfit"].iloc[0]
            analysis_results["净利润"] = net_profit
        
        # 3. 净利率分析
        if "npMargin" in df_profit.columns:
            np_margin = df_profit["npMargin"].iloc[0]
            analysis_results["净利率"] = np_margin
        
        # 4. 毛利率分析
        if "gpMargin" in df_profit.columns:
            gp_margin = df_profit["gpMargin"].iloc[0]
            analysis_results["毛利率"] = gp_margin
        
        # 5. ROE分析
        if "roeAvg" in df_profit.columns:
            roe_avg = df_profit["roeAvg"].iloc[0]
            analysis_results["净资产收益率"] = roe_avg
        
        # 6. 每股收益分析
        if "epsTTM" in df_profit.columns:
            eps_ttm = df_profit["epsTTM"].iloc[0]
            analysis_results["每股收益"] = eps_ttm
        
        # 7. 现金流量分析
        if "CFOToNP" in df_cashflow.columns:
            cfo_to_np = df_cashflow["CFOToNP"].iloc[0]
            analysis_results["现金流与净利润比率"] = cfo_to_np
        
        # 8. 负债率分析
        if "liabilityToAsset" in df_balance.columns:
            liability_to_asset = df_balance["liabilityToAsset"].iloc[0]
            analysis_results["负债率"] = liability_to_asset
        
        # 9. 成长性分析
        if "YOYNI" in df_growth.columns:
            yoyni = df_growth["YOYNI"].iloc[0]
            analysis_results["净利润增长率"] = yoyni
        
        if "YOYAsset" in df_growth.columns:
            yoyasset = df_growth["YOYAsset"].iloc[0]
            analysis_results["资产增长率"] = yoyasset
        
        # 10. 运营能力分析
        if "NRTurnRatio" in df_operation.columns:
            nr_turn_ratio = df_operation["NRTurnRatio"].iloc[0]
            analysis_results["应收账款周转率"] = nr_turn_ratio
        
        if "INVTurnRatio" in df_operation.columns:
            inv_turn_ratio = df_operation["INVTurnRatio"].iloc[0]
            analysis_results["存货周转率"] = inv_turn_ratio
        
        if "CATurnRatio" in df_operation.columns:
            ca_turn_ratio = df_operation["CATurnRatio"].iloc[0]
            analysis_results["流动资产周转率"] = ca_turn_ratio
        
        if "AssetTurnRatio" in df_operation.columns:
            asset_turn_ratio = df_operation["AssetTurnRatio"].iloc[0]
            analysis_results["资产周转率"] = asset_turn_ratio
        
        # 11. 杜邦分析
        if "dupontROE" in df_dupont.columns:
            dupont_roe = df_dupont["dupontROE"].iloc[0]
            analysis_results["杜邦ROE"] = dupont_roe
        
        if "dupontAssetStoEquity" in df_dupont.columns:
            dupont_asset_sto_equity = df_dupont["dupontAssetStoEquity"].iloc[0]
            analysis_results["权益乘数"] = dupont_asset_sto_equity
        
        if "dupontAssetTurn" in df_dupont.columns:
            dupont_asset_turn = df_dupont["dupontAssetTurn"].iloc[0]
            analysis_results["资产周转率"] = dupont_asset_turn
        
        if "dupontNitogr" in df_dupont.columns:
            dupont_nitogr = df_dupont["dupontNitogr"].iloc[0]
            analysis_results["净利率"] = dupont_nitogr
        
    except Exception as e:
        analysis_results["error"] = str(e)
    
    # 登出系统
    bs.logout()
    
    return analysis_results

if __name__ == "__main__":
    # 测试海尔智家财务分析
    results = analyze_finance_director("sh.600690")
    
    print("=== 海尔智家财务总监级别分析结果 ===")
    for key, value in results.items():
        print(f"\n{key}:")
        if isinstance(value, pd.DataFrame):
            print(value)
        else:
            print(value)