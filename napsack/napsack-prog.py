import itertools

def knapsack_brute_force(weights, values, capacity):
    n = len(weights)
    max_value = 0
    best_combination = []

    # 0個選ぶ場合からn個選ぶ場合まで、すべての組み合わせを試す
    for r in range(n + 1):
        # itertools.combinations を使って、n個の中からr個選ぶ組み合わせを全列挙
        for indices in itertools.combinations(range(n), r):
            total_weight = sum(weights[i] for i in indices)
            total_value = sum(values[i] for i in indices)

            # 重量の制限以下、かつこれまでの最大価値を超えていたら更新
            if total_weight <= capacity and total_value > max_value:
                max_value = total_value
                best_combination = indices

    return max_value, best_combination

# --- 動作確認用のデータ ---
# アイテムの重さ
weights = [2, 3, 4, 5]
# アイテムの価値
values = [3, 4, 5, 8]
# ナップサックの容量（制限重量）
capacity = 7

# 関数の実行
max_val, items = knapsack_brute_force(weights, values, capacity)

# 結果の表示
print(f"最大価値: {max_val}")
print(f"選んだアイテムのインデックス: {list(items)}")
print(f"選んだアイテムの重さの合計: {sum(weights[i] for i in items)}")