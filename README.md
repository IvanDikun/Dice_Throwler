# 🎲 Warhammer Dice Throwler

A lightweight GUI application for simulating Warhammer-style dice rolls with support for rerolls, auto-wounds, and special effects like **Sustained Hits** and **Lethal Hits**.

Designed for players who want a fast and structured way to calculate dice results during tabletop battles.

---

## ⚔️ Features

- 🧮 Input number of dice, hit and wound thresholds
- 🔁 Supports rerolls:
  - Reroll 1s
  - Reroll failed hits/wounds
  - Reroll all except 6s
- 💥 Special rules:
  - **Sustained Hits**: Rolling a 6 on hit adds 1–3 extra hits
  - **Lethal Hits**: Rolling a 6 on hit becomes an automatic wound
- 📊 Shows full breakdown:
  - Total hits/wounds
  - How many 6s, 1s, and fails
- 🖥 Built with tkinter — fast and easy to use

---

## 🛠 Tech Stack

- Python 3.x  
- `tkinter` — GUI  
- `random` — for dice simulation

---

## 🚀 Getting Started

1. **Install Python 3** (if not already installed)

2. **Run the script**

```bash
python warhammer_dice_throwler.py
