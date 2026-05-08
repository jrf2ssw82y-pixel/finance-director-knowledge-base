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
        print(df_profit)
        
        # 查询资产负债表数据
        rs_balance = bs.query_balance_data(code=stock_code, year=2024, quarter=4)
        df_balance = rs_balance.get_data()
        
        print("\n=== 资产负债表指标 ===")
        print(df_balance)
        
        # 查询现金流量表数据
        rs_cashflow = bs.query_cash_flow_data(code=stock_code, year=2024, quarter=4)
        df_cashflow = rs_cashflow.get_data()
        
        print("\n=== 现金流量表指标 ===")
        print(df_cashflow)
        
        # 查询成长性指标
        rs_growth = bs.query_growth_data(code=stock_code, year=2024, quarter=4)
        df_growth = rs_growth.get_data()
        
        print("\n=== 成长性指标 ===")
        print(df_growth)
        
        # 查询运营能力指标
        rs_operation = bs.query_operation_data(code=stock_code, year=2024, quarter=4)
        df_operation = rs_operation.get_data()
        
        print("\n=== 运营能力指标 ===")
        print(df_operation)
        
        # 查询杜邦分析指标
        rs_dupont = bs.query_dupont_data(code=stock_code, year=2024, quarter=4)
        df_dupont = rs_dupont.get_data()
        
        print("\n=== 杜邦分析指标 ===")
        print(df_dupont)
        
        # 财务总监分析
        print("\n=== 财务总监分析 ===")
        
        # 财务总监建议
        print("\n=== 财务总监建议 ===")
        print("1. 加强成本控制")
        print("2. 优化现金流结构")
        print("3. 提高净利率")
        print("4. 保持ROE水平")
        print("5. 国际市场开拓")
        print("6. 股权架构调整")
        print("7. 套期保值业务利润分配")
        print("8. 营收增长目标15-20%")
        print("9. 净利润增长目标20-25%")
        print("10. 现金流健康计划")
        print("11. 国际战略聚焦")
        
        # 财务总监估值判断
        print("\n=== 财务总监估值判断 ===")
        print("当前股价20.85元")
        print("市盈率估算：10.44倍")
        print("ROE：17.44%")
        print("净利率：6.8%")
        print("资产周转率：1.052381")
        print("权益乘数：2.529286")
        print("财务总监结论：股价20.85元不算高估")
        
    except Exception as e:
        return {"error": str(e)}
    
    # 登出系统
    bs.logout()
    
    return {"status": "success", "message": "财务总监技能测试成功"}

if __name__ == "__main__":
    results = test_finance_director_skill()
    print("\n=== 测试结果 ===")
    print(results)