# simple-calculator with Python

**Version:** 0.1.0

This is a simple console calculator written in Python. The user can perform basic math operations such as addition, subtraction, multiplication, division, power, and percentage.

This is my second Python project. I wrote it with simple syntax on purpose, and my plan is to add more features and clean up the code step by step as I learn more Python.

---

## What is this project?

This is an educational mini-project: a simple calculator in Python that can:

- Add two numbers  
- Subtract two numbers  
- Multiply two numbers  
- Divide two numbers  
- Raise a number to a power  
- Calculate the percentage of a number  
- Show a history of previous results  
- Exit the program  

The main goal of this project is to practice Python and basic programming concepts. Over time I will add new features and fix bugs as I go.

---

## How to run

After starting the program, a simple text-based menu is shown.  
The user can choose an option depending on what they want to calculate.

To run the app locally:

```bash
python simple-calculator.py
```
---

## Features (current version)

The current version includes:

- Addition

- Subtraction

- Multiplication

- Division

- Power

- Percentage

- History (show previous results)

- Exit

---

## Requirements

- Python 3.x

No external libraries are required at the moment.
You only need a working Python 3 installation to run the script.

---

## Future improvements (Roadmap)

- Support floating-point numbers instead of only integers

- Refactor the menu logic to remove duplicated code for reading the two input numbers

- Extend the Math class with more operations (e.g. square root, modulo, absolute value, etc.)

- Improve the history feature by storing both the full expression (e.g. 3 + 5 = 8) and the result

- Add the option to clear the history or change the history size limit at runtime

- Persist the history to a file (e.g. JSON or text) so that it is available between program runs

- Add unit tests for the Math and History classes to ensure correctness and prevent regressions

- Wrap the main loop into a dedicated CalculatorApp class with a run() method to further separate logic and UI

- Add localization (e.g. English/German/Persian menus) using a simple translation layer

- Enhance the CLI user experience (colors, better formatting, input prompts) to make it more user-friendly

- Add a simple graphical menu or GUI version of the calculator

-Optimize and refactor the code to reduce unnecessary lines and make the logic cleaner

---

### Known Issues

- Non-numeric input is not validated and will cause the program to crash instead of showing a clear error message

- Division by zero is only printed as an error message and may still result in None being used or stored in the history

---

## Technologies used

- Programming language: Python

- IDE: Spyder

In the future I might also try to work with other editors or IDEs (like VS Code) on this project.

---

## Project status

This is the first version of this program. As I continue learning Python and computer science in general, I will try to improve it step by step.

The code is intentionally simple and still has a lot of room to grow. My goal with this project is to practice and build my knowledge, and to keep this calculator as a small “learning lab” while I discover new things in programming.

## Version history

- **v0.1.0** – Initial version of the calculator (basic operations and history).
