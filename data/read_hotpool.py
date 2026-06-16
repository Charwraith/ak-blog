#!/usr/bin/env python3
"""验证 hotpool.jsonl 可被星野读取的脚本"""
import json

HOTPOOL = "/root/ak-blog/data/hotpool.jsonl"

def main():
    # 1. 解析全部
    items = []
    with open(HOTPOOL) as f:
        for i, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue
            try:
                obj = json.loads(line)
                items.append(obj)
            except json.JSONDecodeError as e:
                print(f"❌ 第 {i} 行 JSON 解析失败: {e}")
                return

    print(f"✅ 共解析 {len(items)} 条热点\n")

    # 2. 按 score 过滤
    high_potential = [it for it in items if it["score"] >= 4]
    print(f"📊 评分 4+（高潜力）: {len(high_potential)} 条")
    for it in high_potential:
        print(f"   [{it['score']}★] {it['title'][:60]}")
    print()

    # 3. 按 tier 分组
    tiers = {}
    for it in items:
        t = it["tier"]
        tiers.setdefault(t, []).append(it)
    print("📂 按 tier 分组:")
    for t in ["pillar", "cluster", "newsjack"]:
        group = tiers.get(t, [])
        print(f"   {t}: {len(group)} 条")
        for it in group:
            print(f"     - {it['id']} [{it['score']}★] {it['title'][:50]}")
    print()

    # 4. pillar_match 覆盖统计
    all_pillars = set()
    for it in items:
        for p in it.get("pillar_match", []):
            all_pillars.add(p)
    print(f"🏷️ 覆盖 pillar: {', '.join(sorted(all_pillars))}")

    all_clusters = set()
    for it in items:
        for c in it.get("cluster_match", []):
            all_clusters.add(c)
    print(f"🏷️ 覆盖 cluster: {', '.join(sorted(all_clusters))}")

    # 5. 来源统计
    sources = {}
    for it in items:
        src = it["source"].split("/")[0]
        sources[src] = sources.get(src, 0) + 1
    print(f"\n🌐 来源分布: {sources}")

    print("\n✅ 验证通过 — hotpool 格式正确，星野可正常读取")

if __name__ == "__main__":
    main()
