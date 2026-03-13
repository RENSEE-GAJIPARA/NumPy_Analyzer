<div align="center">

# 🔢 NumPy Analyzer

### *A powerful console-based data analytics toolkit built with Python & NumPy*

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-1.24%2B-013243?style=for-the-badge&logo=numpy&logoColor=white)
![OOP](https://img.shields.io/badge/Paradigm-OOP-ff6b6b?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Complete-4CAF50?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

<br/>

> *"Bringing the power of NumPy to your fingertips through an intuitive, menu-driven interface"*

<br/>

[🚀 Quick Start](#-quick-start) • [✨ Features](#-features) • [📸 Screenshots](#-screenshots) • [🏗️ Architecture](#️-architecture) • [📊 Flowchart](#-program-flowchart)

</div>

---

## 📌 About The Project

**NumPy Analyzer** is a menu-driven console application that combines the power of **NumPy** with **Object-Oriented Programming** principles. Built as part of the Red & White Skill Education curriculum, this project allows users to perform real-world data operations — from array creation and mathematical operations to statistical analysis — all through a clean, interactive interface.

### 🎯 What makes this project stand out?

- ✅ Full **OOP design** with a single `DataAnalytics` class
- ✅ Uses `@classmethod`, `@staticmethod`, and **encapsulation**
- ✅ Supports **1D, 2D, and 3D** array operations
- ✅ **11 different operations** across 5 major categories
- ✅ Clean **menu-driven UI** with input validation

---

## ✨ Features

<table>
<tr>
<td width="50%">

### 📐 Array Management
- ➕ Create **1D, 2D, 3D** arrays
- 🔍 **Indexing** — access specific elements
- ✂️ **Slicing** — extract rows, columns, sub-arrays

### ➗ Mathematical Operations
- Element-wise **Addition, Subtraction**
- Element-wise **Multiplication, Division**
- **Dot Product** & **Matrix Multiplication**

</td>
<td width="50%">

### 🔗 Array Manipulation
- 🧩 **Combine** — Horizontal & Vertical Stack
- ✂️ **Split** — Horizontal & Vertical Split

### 🔎 Search · Sort · Filter
- 🔍 Search for values with **exact position**
- 🔃 Sort **Ascending/Descending**, Row/Column-wise
- 🎯 Filter by **>, <, ==** conditions

### 📊 Aggregates & Statistics
- Sum, Mean, Median, Std Dev, Variance
- Min, Max, Percentile, Correlation Coefficient

</td>
</tr>
</table>

---

## 📸 Screenshots

### 🏠 Welcome Screen & Main Menu
<img width="630" height="326" alt="Screenshot 2026-03-13 172912" src="https://github.com/user-attachments/assets/59d1bad1-ff7a-427d-8309-3ebe427cc2e4" />

---

### 📐 Case 1 — Array Creation & Slicing
<img width="694" height="785" alt="Screenshot 2026-03-13 183648" src="https://github.com/user-attachments/assets/3d571830-55c2-43c9-a6d0-5f80d3a6594a" />

---

### ➗ Case 2 — Matrix Multiplication
<img width="534" height="590" alt="Screenshot 2026-03-13 183731" src="https://github.com/user-attachments/assets/f33e8f0e-cd36-45de-a0a3-94097383a1bc" />

---

### 🔗 Case 3 — Combine Arrays (Horizontal Stack)
<img width="575" height="646" alt="Screenshot 2026-03-13 183808" src="https://github.com/user-attachments/assets/265e6cda-b304-4e17-bbf9-7109306aa473" />

---

### 🔃 Case 4 — Sort (Descending, Column-Wise)
<img width="403" height="544" alt="Screenshot 2026-03-13 183923" src="https://github.com/user-attachments/assets/3279df8c-55a7-4f7e-a26b-3cfd330e8ba4" />

---

### 📊 Case 5 — Aggregation (Sum)
<img width="288" height="444" alt="Screenshot 2026-03-13 184003" src="https://github.com/user-attachments/assets/c46b4015-cdb1-4060-8b2b-ce281cbfffe6" />

---

### 🚪 Exit
<img width="377" height="238" alt="Screenshot 2026-03-13 184021" src="https://github.com/user-attachments/assets/a85a2654-b759-4250-b48c-35e81c32c9b1" />

---

## 📊 Program Flowchart

```
                    ┌─────────────────────────┐
                    │   START NumPy Analyzer   │
                    └────────────┬────────────┘
                                 │
                    ┌────────────▼────────────┐
                    │      Display Welcome     │
                    │      & Main Menu         │
                    └────────────┬────────────┘
                                 │
              ┌──────────────────▼──────────────────────┐
              │           User Selects Option            │
              └──┬──────┬──────┬──────┬─────────┬───────┘
                 │      │      │      │         │
                 ▼      ▼      ▼      ▼         ▼
              [1]     [2]    [3]    [4]       [5]       [6]
               │       │      │      │         │         │
               ▼       ▼      ▼      ▼         ▼         ▼
           Create   Math   Combine Search   Agg &     EXIT
           Array     Ops   / Split  Sort   Stats
             │       │      │      Filter    │
             ▼       ▼      ▼      │         ▼
          ┌──────┐ ┌────┐ ┌────┐  ▼      ┌──────────┐
          │  1D  │ │Add │ │ H  │┌────┐   │Aggregation│
          │  2D  │ │Sub │ │ V  ││Srch│   │  Sum      │
          │  3D  │ │Mul │ │Stk ││Sort│   │  Mean     │
          └──┬───┘ │Div │ │Spl ││Filt│   │  Median   │
             │     │Dot │ └────┘└────┘   │  Std Dev  │
             ▼     │Mat │               │  Variance │
          ┌──────┐ │Mul │               └──────────┘
          │Index │ └────┘               Statistical
          │Slice │                      │  Max/Min  │
          └──────┘                      │  Percentil│
                                        │  Corr Coef│
                    ◄────────────────────────────────
                    │     Return to Main Menu        │
                    └────────────────────────────────
```

---

## 🏗️ Architecture

### Class Design — `DataAnalytics`

```python
class DataAnalytics:
    │
    ├── __init__()                  # Initializes current_array = None
    │
    ├── @classmethod welcome()      # Displays welcome banner
    ├── @staticmethod main_menu()   # Displays main menu options
    │
    ├── PUBLIC METHODS
    │   ├── create_array()          # Case 1 — Array creation menu
    │   ├── math_operation()        # Case 2 — Math operations menu
    │   ├── combine_split()         # Case 3 — Combine/Split menu
    │   ├── search_sort_filter()    # Case 4 — Search/Sort/Filter menu
    │   ├── aggregation_statistical() # Case 5 — Stats menu
    │   └── run()                   # Main program loop
    │
    └── PRIVATE METHODS (Encapsulated)
        ├── __indexing()            # Index into array
        ├── __slicing()             # Slice array
        ├── __combine_arr()         # Combine two arrays
        ├── __split_arr()           # Split array into parts
        ├── __search()              # Search for value
        ├── __sort()                # Sort array
        ├── __filter()              # Filter by condition
        ├── __aggregation()         # Sum, Mean, Median, Std, Var
        └── __statistical()         # Max, Min, Percentile, Corr
```

---

## 🧠 OOP Concepts Used

| Concept | Implementation | Purpose |
|---|---|---|
| 🏛️ **Class** | `DataAnalytics` | Encapsulates all project functionality |
| 🔧 **Constructor** | `__init__()` | Initializes `self.current_array = None` |
| 🔒 **Encapsulation** | `__indexing`, `__sort`, etc. | Hides internal logic from outside |
| 🏷️ **@classmethod** | `welcome()` | Called on the class, not the object |
| ⚡ **@staticmethod** | `main_menu()` | Utility — needs no `self` or `cls` |
| 🔗 **Object** | `analyzer = DataAnalytics()` | Instance that runs the program |

---

## 🚀 Quick Start

### Prerequisites

```bash
Python 3.10 or higher
NumPy library
```

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/RENSEE-GAJIPARA/NumPy_Analyzer.git

# 2. Navigate into the project directory
cd NumPy_Analyzer

# 3. Install NumPy
pip install numpy

# 4. Run the program
python Numpy_Analyzer.py
```

---

## 🖥️ Sample Console Interaction

```
Welcome to the NumPy Analyzer!!
==================================================

Choose an option:
1.Create a numpy array.
2.Perform Mathematical Operation.
3.Combine or Split array.
4.Search, Sort, or Filter Array.
5.Compute Aggregates and Statistics
6.Exit

Enter your choice: 1

Select the type of array to create:
1.1D Array
2.2D Array
3.3D Array
4.Go Back

Enter your choice: 2

Enter number of Rows: 3
Enter number of columns: 3
Enter total 9 Elements as space separated: 2 6 5 9 1 7 3 8 4

Created 2D Array:
[[2 6 5]
 [9 1 7]
 [3 8 4]]

Choose an operation:
1.Indexing
2.Slicing
3.Go Back

Enter your choice: 2

Sliced Array:
[[2 6]
 [9 1]]
```

---

## 📁 Project Structure

```
NumPy_Analyzer/
│
├── 📄 Numpy_Analyzer.py       # Main project file (all logic)
├── 📄 README.md               # Project documentation
└── 📁 screenshots/            # Add your screenshots here
    ├── welcome.png
    ├── case1_array.png
    ├── case2_math.png
    ├── case3_combine.png
    ├── case4_sort.png
    ├── case5_agg.png
    └── exit.png
```

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| ![Python](https://img.shields.io/badge/-Python-3776AB?style=flat&logo=python&logoColor=white) | Core programming language |
| ![NumPy](https://img.shields.io/badge/-NumPy-013243?style=flat&logo=numpy&logoColor=white) | Array operations & mathematical functions |
| **OOP** | Class-based architecture & encapsulation |
| **match-case** | Python 3.10+ structural pattern matching |

---

## 👨‍💻 Author

<div align="center">

**Rensee Gajipara**

[![GitHub](https://img.shields.io/badge/GitHub-RENSEE--GAJIPARA-181717?style=for-the-badge&logo=github)](https://github.com/RENSEE-GAJIPARA)


</div>

---



