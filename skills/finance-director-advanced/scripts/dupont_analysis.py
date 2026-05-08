import baostock as bs
import pandas as pd

def dupont_analysis(stock_code="sh.600690"):
    """
    杜邦分析 - 分解ROE为净利率×资产周转率×权益乘数
    
    杜邦分析公式：
    ROE = 净利率 × 资产周转率 × 权益乘数
    
    参数：
    stock_code: 股票代码
    
    返回：
    dict: 杜邦分析结果
    """
    
    # 登录系统
    lg = bs.login()
    if lg.error_msg != "success":
        return {"error": "登录失败", "details": lg.error_msg}
    
    try:
        # 查询杜邦分析指标
        rs = bs.query_dupont_data(code=stock_code, year=2024, quarter=4)
        df_dupont = rs.get_data()
        
        if len(df_dupont) == 0:
            return {"error": "没有杜邦分析数据"}
        
        dupont_roe = df_dupont["dupontROE"].iloc[0]
        dupont_asset_sto_equity = df_dupont["dupontAssetStoEquity"].iloc[0]
        dupont_asset_turn = df_dupont["dupontAssetTurn"].iloc[0]
        dupont_nitogr = df_dupont["dupontNitogr"].iloc[0]
        
        # 验证杜邦公式
        calculated_roe = dupont_nitogr * dupont_asset_turn * dupont_asset_sto_equity
        
        results = {
            "杜邦ROE": dupont_roe,
            "净利率": dupont_nitogr,
            "资产周转率": dupont_asset_turn,
            "权益乘数": dupont_asset_sto_equity,
            "杜邦公式验证": {
                "净利率×资产周转率×权益乘数": dupont_nitogr * dupont_asset_turn * dupont_asset_sto_equity,
                "杜邦ROE": dupont_roe,
                "验证结果": calculated_roe == dupont_roe
            },
            "杜邦分析解读": {
                "净利率": f"净利率为{dupont_nitogr:.4f}（{dupont_nitogr*100:.2f}%），显示盈利能力",
                "资产周转率": f"资产周转率为{dupont_asset_turn:.4f}，显示资产运营效率",
                "权益乘数": f"权益乘数为{dupont_asset_sto_equity:.4f}，显示负债水平",
                "ROE": f"ROE为{dupont_roe:.4f}（{dupont_roe*100:.2f}%），显示股东回报率"
            },
            "财务总监建议": {
                "净利率": "净利率越高，盈利能力越强",
                "资产周转率": "资产周转率越高，资产运营效率越高",
                "权益乘数": "权益乘数越高，负债水平越高",
                "ROE": "ROE越高，股东回报率越高"
            }
        }
        
        # 财务总监级别分析
        dupont_analysis_results = {
            "净资产收益率": dupont_roe,
            "净利率": dupont_nitogr,
            "资产周转率": dupont_asset_turn,
            "权益乘数": dupont_asset_sto_equity,
            "杜邦公式验证": dupont_nitogr * dupont_asset_turn * dupont_asset_sto_equity
        }
        
    except Exception as e:
        return {"error": str(e)}
    
    # 登出系统
    bs.logout()
    
    return dupont_analysis_results

def dupont_trend_analysis(stock_code="sh.600690"):
    """
    杜邦趋势分析 - 分析杜邦指标的变化趋势
    
    参数：
    stock_code: 股票代码
    
    返回：
    dict: 杜邦趋势分析结果
    """
    
    # 登录系统
    lg = bs.login()
    if lg.error_msg != "success":
        return {"error": "登录失败", "details": lg.error_msg}
    
    try:
        # 查询最近3年的杜邦分析数据
        years = [2021, 2022, 2023]
        dupont_trend_data = []
        
        for year in years:
            rs = bs.query_dupont_data(code=stock_code, year=year, quarter=4)
            df_dupont = rs.get_data()
            
            if len(df_dupont) == 0:
                continue
            
            dupont_roe = df_dupont["dupontROE"].iloc[0]
            dupont_asset_sto_equity = df_dupont["dupontAssetStoEquity"].iloc[0]
            dupont_asset_turn = df_dupont["dupontAssetTurn"].iloc[0]
            dupont_nitogr = df_dupont["dupontNitogr"].iloc[0]
            
            dupont_trend_data.append({
                "年份": year,
                "净资产收益率": dupont_roe,
                "净利率": dupont_nitogr,
                "资产周转率": dupont_asset_turn,
                "权益乘数": dupont_asset_sto_equity
            })
        
        # 计算趋势
        trend_results = {
            "杜邦趋势数据": dupont_trend_data,
            "净利率趋势": "净利率变化趋势",
            "资产周转率趋势": "资产周转率变化趋势",
            "权益乘数趋势": "权益乘数变化趋势",
            "净资产收益率趋势": "净资产收益率变化趋势"
        }
        
    except Exception as e:
        return {"error": str(e)}
    
    # 登出系统
    bs.logout()
    
    return trend_results

if __name__ == "__main__":
    # 测试杜邦分析
    dupont_results = dupont_analysis("sh.600690")
    
    print("=== 杜邦分析结果 ===")
    for key, value in dupont_results.items():
        print(f"\n{key}: {value}")
    
    # 测试杜邦趋势分析
    dupont_trend_results = dupont_trend_analysis("sh.600690")
    
    print("\n=== 杜邦趋势分析结果 ===")
    for key, value in dupont_trend_results.items():
        print(f"\n{key}: {value}")