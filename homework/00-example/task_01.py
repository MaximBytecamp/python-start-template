# ДЗ 0, задача 1. Стоимость поездки
# Поездка на 500 км: стоимость топлива плюс проживание.

# Исходные данные
distance = 500          # расстояние, км
fuel_price = 45.5       # цена литра топлива, руб.
fuel_efficiency = 12    # сколько км проезжает машина на литре
cost_home = 2500        # проживание, руб.

# Расчёт
fuel_cost = (distance / fuel_efficiency) * fuel_price
total_cost = fuel_cost + cost_home

# Вывод
print("Стоимость путешествия:")
print(f"Расходы на топливо: {fuel_cost:.2f} руб.")
print(f"Расходы на проживание: {cost_home} руб.")
print(f"Общая стоимость: {total_cost:.2f} руб.")
