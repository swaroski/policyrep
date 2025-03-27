


from assignment2.fsm import FSM, S0
from assignment1.best_threshold import best_threshold
from assignment1.best_threshold_test import TestBestThreshold 
from assignment2.test_fsm import TestMod3FSM
import unittest

def run_fsm():
    binary_input = input("Enter a binary string: ").strip().replace('\"', '')
    fsm = FSM(S0())
    result = fsm.process(binary_input)
    print(f"Remainder when {binary_input} is divided by 3 is: {result}")


def run_best_threshold():
    print("Enter metric data for each threshold (TP, FP, FN). Type 'done' to finish.")
    metrics = []
    while True:
        entry = input("Threshold TP FP FN (e.g. 0.3 90 20 10): ").strip()
        if entry.lower() == 'done':
            break
        parts = entry.split()
        if len(parts) != 4:
            print("❌ Please enter exactly 4 values: threshold TP FP FN")
            continue
        try:
            threshold, tp, fp, fn = map(float, parts)
            metrics.append({
                'threshold': threshold,
                'TP': int(tp),
                'FP': int(fp),
                'FN': int(fn)
            })
        except ValueError:
            print("❌ Invalid input. Please ensure all values are numeric.")
    
    result = best_threshold(metrics)
    if result is not None:
        print(f"✅ Best threshold with recall ≥ 0.9: {result}")
    else:
        print("⚠️ No threshold met the recall ≥ 0.9 requirement.")



def run_tests():
    print("Running all test cases...\n")
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    # Load tests from both test files
    
    suite.addTests(loader.loadTestsFromTestCase(TestMod3FSM))
    suite.addTests(loader.loadTestsFromTestCase(TestBestThreshold))

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)


def main():
    print("🎓 Welcome to the PolicyRep Assignment Runner!")
    print("Select an option to run:")
    print("1. Assignment 1: Best Threshold Finder")
    print("2. Assignment 2: FSM for Binary Modulo 3")
    print("3. Run All Tests")
    choice = input("Enter 1, 2 or 3: ").strip()

    if choice == "1":
        run_best_threshold()
    elif choice == "2":
        run_fsm()
    elif choice == "3":
        run_tests()
    else:
        print("❌ Invalid selection. Please enter 1, 2 or 3.")


if __name__ == "__main__":
    main()



