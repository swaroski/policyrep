

# 🧠 PolicyRep Assignment Projects

This project contains two assignments demonstrating concepts in **Object-Oriented Design** and **evaluation metrics in machine learning**.

## 📌 Assignments

### ✅ Assignment 1: Best Threshold Finder
- Evaluates binary classification thresholds.
- Finds the best threshold (0.1–0.9) where **recall ≥ 0.9** and **precision is maximized**.

### ✅ Assignment 2: FSM for Modulo 3
- Uses a **Finite State Machine (FSM)** to compute remainder of a binary string when divided by 3.
- Follows clean Object-Oriented Design using state classes (`S0`, `S1`, `S2`).


## Environment Setup (Using uv)
# Create a new project folder (optional)
```
pip install uv  
uv init policyrep
cd policyrep/assignment2
```

# Pin Python version
```
uv python pin 3.13.0
```

# Create a virtual environment
```
uv venv
```

# Activate the virtual environment (Linux/macOS)
```
source .venv/bin/activate
```

# OR (Windows)
```
.venv\\Scripts\\activate
```

# Open project in VS Code (optional but recommended)
```
code .
```


## 🧪 How to Run

Use the `main.py` script to launch either assignment from the command line and follow instructions:

```
uv run main.py
```

## Running test cases
```
uv run test_fsm.py
uv run test_assignment1.py
``` 