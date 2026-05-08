import baostock as bs
import pandas as pd

def test_finance_director_skill():
    """
    测试财务总监技能
    
    测试财务总监技能的所有功能
    """
    
    # 登录系统
    lg = bs.login()
    if lg.error_msg != "success":
        return {"error": "登录失败", "details": lg.error_msg}
    
    try:
        # 测试海尔智家财务总监分析
        stock_code = "sh.600690"
        
        # 查询股票基本信息
        rs_info = bs.query_stock_basic(code=stock_code)
        df_info = rs_info.get_data()
        
        print("=== 海尔智家财务总监分析测试 ===")
        print(f"股票代码: {df_info['code'].iloc[0]}")
        print(f"股票名称: {df_info['code_name'].iloc[0]}")
        print(f"上市日期: {df_info['ipoDate'].iloc[0]}")
        
        # 查询季度财务数据
        rs_profit = bs.query_profit_data(code=stock_code, year=2024, quarter=4)
        df_profit = rs_profit.get_data()
        
        print("\n=== 财务指标 ===")
        print(f"净资产收益率(ROE): {df_profit['roeAvg'].iloc[0]:.4f} ({df_profit['roeAvg'].iloc[0]*100:.2f}%)")
        print(f"净利率: {df_profit['npMargin'].iloc[0]:.4f} ({df_profit['npMargin'].iloc[0]*100:.2f}%)")
        print(f"毛利率: {df_profit['gpMargin'].iloc[0]:.4f} ({df_profit['gpMargin'].iloc[0]*100:.2f}%)")
        print(f"净利润: {df_profit['netProfit'].iloc[0]}元")
        print(f"每股收益: {df_profit['epsTTM'].iloc[0]}元")
        print(f"营业收入: {df_profit['MBRevenue'].iloc[0]}元")
        print(f"总股本: {df_profit['totalShare'].iloc[0]}股")
        print(f"流通股本: {df_profit['liqaShare'].iloc[0]}股")
        
        # 查询资产负债表数据
        rs_balance = bs.query_balance_data(code=stock_code, year=2024, quarter=4)
        df_balance = rs_balance.get_data()
        
        print("\n=== 资产负债表指标 ===")
        print(f"流动比率: {df_balance['currentRatio'].iloc[0]:.4f}")
        print(f"速动比率: {df_balance['quickRatio'].iloc[0]:.4f}")
        print(f"现金比率: {df_balance['cashRatio'].iloc[0]:.4f}")
        print(f"负债率: {df_balance['liabilityToAsset'].iloc[0]:.4f} ({df_balance['liabilityToAsset'].iloc[0]*100:.2f}%)")
        print(f"资产对权益比率: {df_balance['assetToEquity'].iloc[0]:.4f}")
        
        # 查询现金流量表数据
        rs_cashflow = bs.query_cash_flow_data(code=stock_code, year=2024, quarter=4)
        df_cashflow = rs_cashflow.get_data()
        
        print("\n=== 现金流量表指标 ===")
        print(f"经营活动现金流与营业收入比率: {df_cashflow['CFOToOR'].iloc[0]:.4f}")
        print(f"经营活动现金流与净利润比率: {df_cashflow['CFOToNP'].iloc[0]:.4f}")
        print(f"经营活动现金流与毛利润比率: {df_cashflow['CFOToGr'].iloc[0]:.4f}")
        
        # 查询成长性指标
        rs_growth = bs.query_growth_data(code=stock_code, year=2024, quarter=4)
        df_growth = rs_growth.get_data()
        
        print("\n=== 成长性指标 ===")
        print(f"净资产增长率: {df_growth['YOYEquity'].iloc[0]:.4f} ({df_growth['YOYEquity'].iloc[0]*100:.2f}%)")
        print(f"资产增长率: {df_growth['YOYAsset'].iloc[0]:.4f} ({df_growth['YOYAsset'].iloc[0]*100:.2f}%)")
        print(f"净利润增长率: {df_growth['YOYNI'].iloc[0]:.4f} ({df_growth['YOYNI'].iloc[0]*100:.2f}%)")
        print(f"每股收益增长率: {df_growth['YOYEPSBasic'].iloc[0]:.4f} ({df_growth['YOYEPSBasic'].iloc[0]*100:.2f}%)")
        
        # 查询运营能力指标
        rs_operation = bs.query_operation_data(code=stock_code, year=2024, quarter=4)
        df_operation = rs_operation.get_data()
        
        print("\n=== 运营能力指标 ===")
        print(f"应收账款周转率: {df_operation['NRTurnRatio'].iloc[0]:.4f}")
        print(f"应收账款周转天数: {df_operation['NRTurnDays'].iloc[0]:.4f}")
        print(f"存货周转率: {df_operation['INVTurnRatio'].iloc[0]:.4f}")
        print(f"存货周转天数: {df_operation['INVTurnDays'].iloc[0]:.4f}")
        print(f"流动资产周转率: {df_operation['CATurnRatio'].iloc[0]:.4f}")
        print(f"资产周转率: {df_operation['AssetTurnRatio'].iloc[0]:.4f}")
        
        # 查询杜邦分析指标
        rs_dupont = bs.query_dupont_data(code=stock_code, year=2024, quarter=4)
        df_dupont = rs_dupont.get_data()
        
        print("\n=== 杜邦分析指标 ===")
        print(f"杜邦ROE: {df_dupont['dupontROE'].iloc[0]:.4f} ({df_dupont['dupontROE'].iloc[0]*100:.2f}%)")
        print(f"净利率: {df_dupont['dupontNitogr'].iloc[0]:.4f} ({df_dupont['dupontNitogr'].iloc[0]*100:.2f}%)")
        print(f"资产周转率: {df_dupont['dupontAssetTurn'].iloc[0]:.4f}")
        print(f"权益乘数: {df_dupont['dupontAssetStoEquity'].iloc[0]:.4f}")
        
        # 财务总监分析
        print("\n=== 财务总监分析 ===")
        
        # 估值分析
        eps_ttm = df_profit['epsTTM'].iloc[0]
        current_price = 20.85
        
        pe = current_price / eps_ttm
        print(f"市盈率(PE): {pe:.4f}倍")
        
        roe = df_profit['roeAvg'].iloc[0]
        np_margin = df_profit['npMargin'].iloc[0]
        gp_margin = df_profit['gpMargin'].iloc[0]
        revenue = df_profit['MBRevenue'].iloc[0]
        net_profit = df_profit['netProfit'].iloc[0]
        
        print(f"净资产收益率(ROE): {roe:.4f} ({roe*100:.2f}%)")
        print(f"净利率: {np_margin:.4f} ({np_margin*100:.2f}%)")
        print(f"毛利率: {gp_margin:.4f} ({gp_margin*100:.2f}%)")
        print(f"营业收入: {revenue:.2f}元")
        print(f"净利润: {net_profit:.2f}元")
        
        # 财务总监建议
        print("\n=== 财务总监建议 ===")
        
        # 成本控制建议
        if gp_margin < 30:
            print("1. 加强成本控制")
        
        # 现金流优化建议
        cfo_to_np = df_cashflow['CFOToNP'].iloc[0]
        if cfo_to_np < 1:
            print("2. 优化现金流结构")
        
        # 净利率提升建议
        if np_margin < 8:
            print("3. 提高净利率")
        
        # ROE保持建议
        if roe < 15:
            print("4. 保持ROE水平")
        
        # 国际市场开拓建议
        if df_profit['totalShare'].iloc[0] > 5000000000:
            print("5. 国际市场开拓")
        
        # 股权架构调整建议
        liability_to_asset = df_balance['liabilityToAsset'].iloc[0]
        if liability_to_asset < 50:
            print("6. 股权架构调整")
        
        # 套期保值业务利润分配建议
        print("7. 套期保值业务利润分配")
        
        # 营收和净利润增长目标建议
        revenue_growth = df_growth['YOYAsset'].iloc[0]
        net_profit_growth = df_growth['YOYNI'].iloc[0]
        
        if revenue_growth < 15:
            print("8. 营收增长目标15-20%")
        
        if net_profit_growth < 20:
            print("9. 净利润增长目标20-25%")
        
        # 现金流健康计划建议
        print("10. 现金流健康计划")
        
        # 国际战略聚焦建议
        print("11. 国际战略聚焦")
        
    except Exception as e:
        return {"error": str(e)}
    
    # 登出系统
    bs.logout()
    
    return {"status": "success", "message": "财务总监技能测试成功"}

if __name__ == "__main__":
    results = test_finance_director_skill()
    print("\n=== 测试结果 ===")
    print(results)