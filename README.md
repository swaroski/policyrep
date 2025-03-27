
![Pytest](https://github.com/swaroski/policyrep/actions/workflows/tests.yml/badge.svg)



# 🧠 PolicyRep Assignment Projects

This project contains two assignments demonstrating concepts in **Object-Oriented Design** and **evaluation metrics in machine learning**.

## 📌 Assignments

### ✅ Assignment 1: Best Threshold Finder
- Evaluates binary classification thresholds.
- Finds the best threshold (0.1–0.9) where **recall ≥ 0.9** and **precision is maximized**.
- Code location: assignment1/

### ✅ Assignment 2: FSM for Modulo 3
- Uses a **Finite State Machine (FSM)** to compute remainder of a binary string when divided by 3.
- Follows clean Object-Oriented Design using state classes (`S0`, `S1`, `S2`).
- Code location: assignment2/

---

## 📥 Clone the Repository

```bash
git clone https://github.com/swaroski/policyrep.git
cd policyrep
```

## Environment Setup (Using uv)
### 1. Install uv (Python package manager)
```
pip install uv  
```

### 2. Pin Python version
```
uv python pin 3.13.0
```

### 3. Create a virtual environment
```
uv venv
```

### 4. Activate the virtual environment (Linux/macOS)
```
source .venv/bin/activate
```

### 5. Open project in VS Code (optional but recommended)
```
code .
```

## 🧪 How to Run

Use the `main.py` script to launch either assignment from the command line and follow instructions:

```
uv run main.py
```
You'll be prompted to select which assignment to run or run test cases interactively.

## Running Inidividual Test Cases
```
uv run -m assignment2.test_fsm
uv run -m assignment1.test_best_threshold
``` 

## 