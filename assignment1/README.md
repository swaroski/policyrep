## 🧪 Assignment 1 - Threshold Selection for Binary Classification

### Function: `best_threshold(metrics)`

This function selects the best classification threshold that:
- Achieves **recall ≥ 0.9**
- And has the **highest precision** among those thresholds.

### Input Format

A list of dictionaries, each with:
- `threshold`: float (e.g., 0.1, 0.2, ..., 0.9)
- `TP`: True Positives
- `FP`: False Positives
- `FN`: False Negatives

### Example Call

```
from best_threshold import best_threshold

metrics = [
    {'threshold': 0.1, 'TP': 90, 'FP': 30, 'FN': 10},
    {'threshold': 0.4, 'TP': 95, 'FP': 15, 'FN': 5}
]

print(best_threshold(metrics))  # Output: 0.4
```