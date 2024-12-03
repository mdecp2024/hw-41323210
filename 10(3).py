import math

# 定義已知數據
mass = 70  # 質量 (kg)
height = 100  # 懸崖高度 (m)
g = 9.8  # 重力加速度 (m/s^2)

# 計算重力勢能
potential_energy = mass * g * height
print(f"重力勢能: {potential_energy} 焦耳")

# 計算最終速度
final_velocity = math.sqrt(2 * g * height)
print(f"最終速度: {final_velocity:.2f} 米/秒")

# 計算最終動能
kinetic_energy = 0.5 * mass * final_velocity**2
print(f"動能: {kinetic_energy} 焦耳")
