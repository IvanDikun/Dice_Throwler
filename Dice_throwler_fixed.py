import random
import tkinter as tk
from tkinter import ttk


def roll_the_dice(number, skill, reroll_ones=False, reroll_failures=False, reroll_except_six=False, sustained_hits=0, lethal_hits=False):
    good = 0
    six = 0
    fail = 0
    one = 0
    bonus_hits = 0
    auto_wounds = 0

    reroll_pool = []

    for _ in range(number):
        result = random.randint(1, 6)
        if result == 1:
            one += 1
        if result == 6:
            six += 1
            if sustained_hits > 0:
                bonus_hits += sustained_hits
            if lethal_hits:
                auto_wounds += 1
        if result >= skill:
            good += 1
        else:
            fail += 1

        if reroll_ones and result == 1:
            reroll_pool.append("reroll")
        elif reroll_failures and result < skill:
            reroll_pool.append("reroll")
        elif reroll_except_six and result != 6:
            reroll_pool.append("reroll")

    for _ in reroll_pool:
        result = random.randint(1, 6)
        if result == 1:
            one += 1
        if result == 6:
            six += 1
            if sustained_hits > 0:
                bonus_hits += sustained_hits
            if lethal_hits:
                auto_wounds += 1
        if result >= skill:
            good += 1

    return good + bonus_hits, six, one, auto_wounds


def start():
    try:
        number = int(dice_entry.get())
        hit = int(to_hit_entry.get())
        wound = int(to_wound_entry.get())
    except ValueError:
        result_text.set("Ошибка ввода. Введите числа.")
        return

    reroll_ones_hit = reroll_hit.get() == "1"
    reroll_failed_hit = reroll_hit.get() == "2"
    reroll_ones_wound = reroll_wound.get() == "1"
    reroll_failed_wound = reroll_wound.get() == "2"
    reroll_except_six_wound = reroll_wound.get() == "3"

    sustained = int(sustained_var.get()) if sustained_hit_var.get() else 0
    lethal = bool(lethal_hit_var.get())

    hit_result = roll_the_dice(number, hit, reroll_ones_hit, reroll_failed_hit, False, sustained, lethal)
    wound_result = roll_the_dice(hit_result[0] - hit_result[3], wound, reroll_ones_wound, reroll_failed_wound, reroll_except_six_wound)

    result = (
        f"Промахов: {number - hit_result[0] + hit_result[3]}\n"
        f"Попаданий: {hit_result[0]} (в т.ч. 6ок: {hit_result[1]}, 1ц: {hit_result[2]})\n"
        f"Авто-пробитий от Lethal Hits: {hit_result[3]}\n"
        f"Пробитий: {wound_result[0]} (в т.ч. 6ок: {wound_result[1]}, 1ц: {wound_result[2]})"
    )

    result_text.set(result)


root = tk.Tk()
root.title("Warhammer Dice Thrower")

frame = ttk.Frame(root, padding="10")
frame.grid()

ttk.Label(frame, text="Кол-во бросков:").grid(column=0, row=0)
dice_entry = ttk.Entry(frame)
dice_entry.grid(column=1, row=0)

ttk.Label(frame, text="Попадание (to hit):").grid(column=0, row=1)
to_hit_entry = ttk.Entry(frame)
to_hit_entry.grid(column=1, row=1)

ttk.Label(frame, text="Пробитие (to wound):").grid(column=0, row=2)
to_wound_entry = ttk.Entry(frame)
to_wound_entry.grid(column=1, row=2)

# Перебросы попаданий
ttk.Label(frame, text="Перебросы попадания:").grid(column=0, row=3)
reroll_hit = ttk.Combobox(frame, values=["0 - Нет", "1 - Переброс 1ц", "2 - Переброс неудач"], state="readonly")
reroll_hit.grid(column=1, row=3)
reroll_hit.current(0)

# Перебросы пробитий с новым вариантом
ttk.Label(frame, text="Перебросы пробития:").grid(column=0, row=4)
reroll_wound = ttk.Combobox(frame, values=["0 - Нет", "1 - Переброс 1ц", "2 - Переброс неудач", "3 - Переброс всех кроме 6"], state="readonly")
reroll_wound.grid(column=1, row=4)
reroll_wound.current(0)

# Sustained Hits checkbox + entry
ttk.Label(frame, text="Sustained Hits:").grid(column=0, row=5)
sustained_hit_var = tk.BooleanVar()
sustained_hit_check = ttk.Checkbutton(frame, variable=sustained_hit_var)
sustained_hit_check.grid(column=1, row=5, sticky="w")

sustained_var = ttk.Combobox(frame, values=["1", "2", "3"], state="readonly", width=3)
sustained_var.grid(column=1, row=5, sticky="e")
sustained_var.current(0)

# Lethal Hits checkbox
ttk.Label(frame, text="Lethal Hits:").grid(column=0, row=6)
lethal_hit_var = tk.BooleanVar()
lethal_hit_check = ttk.Checkbutton(frame, variable=lethal_hit_var)
lethal_hit_check.grid(column=1, row=6, sticky="w")

# Кнопка старта и вывод результата
start_button = ttk.Button(frame, text="Бросить", command=start)
start_button.grid(column=0, row=7, columnspan=2, pady=10)

result_text = tk.StringVar()
result_label = ttk.Label(frame, textvariable=result_text, background="white", relief="solid", padding=10, anchor="center")
result_label.grid(column=0, row=8, columnspan=2, sticky="we")

root.mainloop()
