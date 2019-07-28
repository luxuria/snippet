# 文字列１つ
S = input()

# 整数１つ
N = int(input())

# 配列として扱う複数の文字列（スペース区切り）
ss = input().split()

# AtCoder とか Paiza では見いひんけど、スペース以外で区切ってる場合
# 例: a,b,c,d
ss = input().split(',')

# それぞれを別々の変数として扱う場合
# 例: apple banana orange
a, b, c = input().split()

# 配列として扱う複数の数値
nn = list(map(int, input().split()))

# 個別に扱う場合
a, b, c = map(int, input().split())

# １次元で文字列が与えられている場合
# 例: 3
#     abc
#     efg
#     hij
ss = [input() for _ in range(int(input()))]

# ２次元で文字列が与えられている場合
# 例: 3 4
#     1 a b c
#     2 e f g
#     3 h i j
H, _ = map(int, input().split())
ss = [input().split() for _ in range(H)]
