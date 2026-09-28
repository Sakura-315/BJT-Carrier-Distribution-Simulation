import sympy as sp

# 定义符号变量
sstd, ssam = sp.symbols('sstd ssam')

# 公式
deltaB = (1/(1-sstd) - 1/(1-ssam)) / (1/(1-sstd))
deltaN = (1 - ssam) - (1 - sstd)

# 化简表达式
deltaB_simp = sp.simplify(deltaB)
deltaN_simp = sp.simplify(deltaN)

print("deltaB =", deltaB_simp)
print("deltaN =", deltaN_simp)

# 画图，ssam固定为0.1
sp.plot(deltaB_simp.subs(ssam,0.1), (sstd, 0, 0.2), title="deltaB")
sp.plot(deltaN_simp.subs(ssam,0.1), (sstd, 0, 0.2), title="deltaN")

