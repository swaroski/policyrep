


def best_threshold(metrics):
    """
    Finds the best threshold with recall >= 0.9.
    Among those, selects the one with the highest precision.

    Args:
        metrics (list of dict): Each dictionary contains the following keys:
            - 'threshold' (float)
            - 'TP' (int): True Positives
            - 'FP' (int): False Positives
            - 'FN' (int): False Negatives

    Returns:
        float or None: Best threshold value or None if no valid threshold meets criteria.
    """
    candidates = []

    for entry in metrics:
        tp = entry['TP']
        fn = entry['FN']
        fp = entry['FP']
        threshold = entry['threshold']

        recall = tp / (tp + fn) if (tp + fn) > 0 else 0
        if recall >= 0.9:
            precision = tp / (tp + fp) if (tp + fp) > 0 else 0
            candidates.append((threshold, precision))

    if not candidates:
        return None

    # Return the threshold with highest precision
    return max(candidates, key=lambda x: x[1])[0]


# Example usage
if __name__ == "__main__":
    example_data = [
        {'threshold': 0.1, 'TP': 90, 'FP': 30, 'FN': 10},
        {'threshold': 0.2, 'TP': 85, 'FP': 25, 'FN': 15},
        {'threshold': 0.3, 'TP': 92, 'FP': 20, 'FN': 8},
        {'threshold': 0.4, 'TP': 95, 'FP': 15, 'FN': 5},
        {'threshold': 0.5, 'TP': 88, 'FP': 10, 'FN': 12},
    ]
    result = best_threshold(example_data)
    print(f"Best threshold with recall >= 0.9: {result}")