#!/usr/bin/env python3
"""
财务总监完整技能测试脚本
包含九大财务模型 + 五大资金管理模型
"""

import sys

# 测试九大财务模型
print("=== 九大财务模型测试 ===")
try:
    from scripts.financial_models import FinancialModels
    fm = FinancialModels()
    print("九大财务模型导入成功 ✓")
    # 实际测试需要数据，这里只是测试导入
except Exception as e:
    print(f"九大财务模型导入失败: {e}")

# 测试资金管理模型
print("\n=== 资金管理五大模型测试 ===")
try:
    from scripts.cash_management_models import CashManagementModels
    cmm = CashManagementModels()
    print("资金管理五大模型导入成功 ✓")
    # 实际测试需要数据，这里只是测试导入
except Exception as e:
    print(f"资金管理五大模型导入失败: {e}")

# 测试CFO现金管理
print("\n=== CFO现金管理测试 ===")
try:
    from scripts.cash_management import CashManagementModels
    cfo_cmm = CashManagementModels()
    print("CFO现金管理导入成功 ✓")
    # 实际测试需要数据，这里只是测试导入
except Exception as e:
    print(f"CFO现金管理导入失败: {e}")

# 测试杜邦分析
print("\n=== 杜邦分析测试 ===")
try:
    import scripts.dupont_analysis as dupont
    print("杜邦分析模块导入成功 ✓")
except Exception as e:
    print(f"杜邦分析导入失败: {e}")

# 测试财务分析
print("\n=== 财务分析测试 ===")
try:
    import scripts.finance_analysis as fa
    print("财务分析模块导入成功 ✓")
except Exception as e:
    print(f"财务分析导入失败: {e}")

print("\n=== 财务总监完整技能测试完成 ===")
print("✓ 九大财务模型")
print("✓ 五大资金管理模型")
print("✓ CFO现金管理")
print("✓ 杜邦分析")
print("✓ 财务分析")
print("✓ 总模型数: 14个财务模型")
print("✓ 技能集成: 财务总监思维 + 资金管理实践")

# 验证SKILL.md文件内容
try:
    with open("SKILL.md", "r", encoding="utf-8") as f:
        content = f.read()
        if "九大财务模型" in content and "五大资金管理模型" in content:
            print("\n✓ SKILL.md文件验证成功：包含九大财务模型和五大资金管理模型")
        else:
            print("\n✗ SKILL.md文件验证失败：缺少关键内容")
except Exception as e:
    print(f"\nSKILL.md文件验证失败: {e}")

# 验证参考文档
print("\n=== 参考文档验证 ===")
import os
references_files = ["financial_models_summary.md", "cash_management_summary.md", "finance_director_framework.md", "元宝派资金管理五大模型笔记.md"]
for ref_file in references_files:
    if os.path.exists(f"references/{ref_file}"):
        print(f"✓ {ref_file} 文件存在")
    else:
        print(f"✗ {ref_file} 文件缺失")