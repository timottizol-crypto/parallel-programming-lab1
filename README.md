# Лабораторная работа №1 — Параллельное умножение матриц

Отчёт доступен по ссылке: **https://timottizol-crypto.github.io/parallel-programming-lab1/**

## Описание
Реализация последовательного и параллельного (OpenMP) алгоритмов умножения квадратных матриц.

## Структура
- `index.html` — веб-отчёт
- `style.css` — оформление
- `plot.py` — построение графиков
- `cpp/main.cpp` — программа на C++
- `python/generate.py` — генерация матриц
- `python/verify.py` — верификация через NumPy
- `img/speedup_graph.png` — график ускорения

## Сборка

### Windows (Visual Studio)
1. Включить OpenMP: C/C++ → Язык → Поддержка OpenMP → Да
2. Оптимизация /O2, Release

### Linux
```bash
g++ -O2 -fopenmp -o matrix main.cpp
OMP_NUM_THREADS=4 ./matrix
