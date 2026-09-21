import matplotlib.pyplot as plt

n = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]

speedup_windows = [0.17, 0.86, 5.12, 6.39, 9.89, 8.35, 9.35, 9.55, 10.66, 9.93]
speedup_ubuntu  = [0.20, 2.00, 2.67, 2.67, 3.30, 2.40, 2.63, 2.66, 3.27, 3.46]
plt.figure(figsize=(10, 6))
plt.plot(n, speedup_windows, 'o-', label='Windows (нативно)', color='blue')
plt.plot(n, speedup_ubuntu,  's-', label='Ubuntu (VirtualBox)', color='orange')
plt.axhline(y=1, color='gray', linestyle='--', label='Без ускорения (1x)')
plt.xlabel('Размер матрицы N')
plt.ylabel('Ускорение (Speedup)')
plt.title('Зависимость ускорения от размера матрицы')
plt.grid(True, alpha=0.3)
plt.legend()
plt.savefig('speedup_graph.png', dpi=150)
plt.show()