import math

gamma = 1.4
R = 287

def calc(speed_mph, temp_k):
    v = speed_mph * 0.44704
    a = math.sqrt(gamma * R * temp_k)
    M = v / a
    p_ratio = (1 + ((gamma - 1) / 2) * M**2) ** (-gamma / (gamma - 1))
    t_ratio = (1 + ((gamma - 1) / 2) * M**2) ** -1
    rho_ratio = (1 + ((gamma - 1) / 2) * M**2) ** (-1 / (gamma - 1))

    print(f"\n== speed: {speed_mph} mph @ {temp_k}K ==")
    print(f"v: {v:.2f} m/s")
    print(f"a: {a:.2f} m/s")
    print(f"mach: {M:.2f}")
    print(f"p/p0: {p_ratio:.4f}")
    print(f"t/t0: {t_ratio:.4f}")
    print(f"rho/rho0: {rho_ratio:.4f}")

for speed in [700, 1500]:
    calc(speed, 223)

if input("\ncustom? (y/n): ").lower() == 'y':
    s = float(input("speed mph: "))
    t = float(input("temp K: "))
    calc(s, t)
