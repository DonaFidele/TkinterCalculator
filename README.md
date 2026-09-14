# 🧮 TkinterCalculator

A **scientific calculator** desktop app built with Python's `tkinter`, combining classic arithmetic operations with scientific functions (trigonometry, logarithms, powers, factorials) in a clean button-grid interface.

![The calculator's image](calculator.png)


## 📖 Table of Contents

- [About](#-about)
- [Features](#-features)
- [Interface Overview](#-interface-overview)
- [Installation](#-installation)
- [Usage](#-usage)
- [Code Overview](#-code-overview)
- [Known Limitations](#-known-limitations)
- [Roadmap](#-roadmap)
- [Author](#-author)
- [License](#-license)

## 🎮 About

**TkinterCalculator** is a desktop calculator application built entirely with Python's standard `tkinter` library — no external dependencies required. It reproduces the look and feel of a scientific calculator, with a grid of buttons for digits, basic operators, and scientific functions, plus a live display screen at the top.

## ✨ Features

- 🖥️ Clean, dark-themed button-grid GUI
- ➕ Basic arithmetic: addition, subtraction, multiplication, division
- 🧠 Scientific function buttons: `sin`, `cos`, `tan`, `log`, `ln`, `√`, `x!`, `x^y`, `π`, `e`, `EXP`
- 🧹 Clear entry (`CE`) button to reset the screen
- 🔢 Direct expression evaluation on `=`
- 🪟 Fixed-size, non-resizable window for a consistent layout

## 🖼️ Interface Overview

The calculator window is organized as a grid:

- **Row 0** — display screen (right-aligned input/output field)
- **Row 1** — `Rad/Deg`, `x!`, `(`, `)`, `%`, `CE`
- **Rows 2–4** — scientific functions (`Inv`, `sin`, `cos`, `tan`, `ln`, `log`, `√`) alongside the numeric keypad and basic operators
- **Row 5** — `Ans`, `EXP`, `x^y`, `0`, `.`, `=`, `+`

## ⚙️ Installation

No external libraries required — `tkinter` ships with most standard Python installations.

```bash
git clone https://github.com/DonaFidele/TkinterCalculator.git
cd TkinterCalculator
```

**Requirements:**
- Python 3.x with `tkinter` installed
  - Linux: `sudo apt-get install python3-tk` if not already present
  - Windows/macOS: included by default with the standard Python installer

## ▶️ Usage

Run the app from your terminal:

```bash
python3 calculatrice.py
```

Click the buttons to build your expression, then press `=` to evaluate it.

## 🧠 Code Overview

- Built around a single `Calculatrice` class extending `tkinter.Tk`.
- `self.a` (a `StringVar`) holds the current expression, bound live to the display `Entry` widget.
- `clic(texte)` handles every button press:
  - `=` evaluates the current expression using Python's `eval()`
  - `x` is translated to `*` for multiplication
  - `CE` clears the screen
  - `x^y` appends a `^` placeholder to the expression
  - All other buttons append their symbol directly to the expression
- `bouttons()` and `num_btn()` are helper methods that generate styled function/number buttons and place them on the grid using `partial()` to bind each button to `clic()` with its own label.
- `creer_btn()` lays out every button in its correct row/column position.

## ⚠️ Known Limitations

- Uses Python's `eval()` directly on user input — **not safe** for untrusted input; fine for personal/local use, but should not be exposed in any public-facing context.
- Scientific buttons like `sin`, `cos`, `tan`, `log`, `ln`, `√`, `x!`, `π`, `e`, `Ans`, `EXP`, and `Rad/Deg` currently just insert their **label as text** into the expression rather than performing the actual computation — the `math` module is imported but not yet wired into `clic()`.
- `x^y` inserts a `^` character, which Python's `eval()` does not interpret as exponentiation (Python uses `**`), so this will currently raise an error rather than compute a power.
- No error handling around `eval()` — invalid expressions (e.g. trailing operators, mismatched parentheses) will raise unhandled exceptions.

## 🗺️ Roadmap

- [ ] Wire up scientific functions (`sin`, `cos`, `tan`, `log`, `ln`, `sqrt`, `factorial`) to the `math` module
- [ ] Fix `x^y` to map to Python's `**` operator
- [ ] Add try/except around `eval()` to handle invalid expressions gracefully
- [ ] Implement `Rad`/`Deg` toggle logic for trig functions
- [ ] Implement `Ans` to recall the last computed result
- [ ] Replace raw `eval()` with a safer expression parser

## 👤 Author

**DonaFidele**
[GitHub Profile](https://github.com/DonaFidele)

## 📄 License

Free to fork and contribute — no need to ask permission first. Feel free to use, modify, and build on this project.

---

<p align="center">Made with 🧮😁️ by <b>Dona😎</b></p>
