"""
Automated Test Suite for Electricity Usage Predictor (PS No. 64)
Tests all 4 cases from the problem specification and verifies expected outputs.
"""

import sys
import os
import io
import contextlib

# Import functions from electricity_predictor
import electricity_predictor as ep


def run_all_tests():
    print("=" * 60)
    print("RUNNING AUTOMATED TEST SUITE FOR PS NO. 64")
    print("=" * 60)

    tests_passed = 0
    total_tests = 4

    # -------------------------------------------------------------
    # Test Case 1: Normal Input
    # -------------------------------------------------------------
    print("\n[TEST 1] Normal Input (4 months of data)")
    df1 = ep.load_dataset("testcase1_normal.csv", show_summary=False)
    buffer1 = io.StringIO()
    with contextlib.redirect_stdout(buffer1):
        res1 = ep.predict_usage_and_bill(df1, 5)
    out1 = buffer1.getvalue().strip()

    print("Output received:")
    print(out1)

    expected_1 = [
        "Slope: 20.00 | Intercept: 180.00",
        "Predicted units (Month 5): 280.00",
        "Estimated bill: Rs. 1680.00"
    ]
    tc1_pass = all(line in out1 for line in expected_1)
    if tc1_pass:
        print(">>> Test Case 1: PASSED [OK]")
        tests_passed += 1
    else:
        print(">>> Test Case 1: FAILED [X]")

    # -------------------------------------------------------------
    # Test Case 2: Boundary / Minimum Input (2 rows only)
    # -------------------------------------------------------------
    print("\n[TEST 2] Boundary / Minimum Input (2 rows only)")
    df2 = ep.load_dataset("testcase2_boundary.csv", show_summary=False)
    buffer2 = io.StringIO()
    with contextlib.redirect_stdout(buffer2):
        res2 = ep.predict_usage_and_bill(df2, 3)
    out2 = buffer2.getvalue().strip()

    print("Output received:")
    print(out2)

    expected_2 = [
        "Slope: 50.00 | Intercept: 50.00",
        "Predicted units (Month 3): 200.00",
        "Estimated bill: Rs. 1200.00"
    ]
    tc2_pass = all(line in out2 for line in expected_2)
    if tc2_pass:
        print(">>> Test Case 2: PASSED [OK]")
        tests_passed += 1
    else:
        print(">>> Test Case 2: FAILED [X]")

    # -------------------------------------------------------------
    # Test Case 3: Invalid Input (1 row only)
    # -------------------------------------------------------------
    print("\n[TEST 3] Invalid Input (1 row only)")
    df3 = ep.load_dataset("testcase3_invalid.csv", show_summary=False)
    buffer3 = io.StringIO()
    with contextlib.redirect_stdout(buffer3):
        res3 = ep.predict_usage_and_bill(df3, 2)
    out3 = buffer2_val = buffer3.getvalue().strip()

    print("Output received:")
    print(out3)

    expected_3 = "Error: At least 2 months of data are required for prediction."
    tc3_pass = expected_3 in out3
    if tc3_pass:
        print(">>> Test Case 3: PASSED [OK]")
        tests_passed += 1
    else:
        print(">>> Test Case 3: FAILED [X]")

    # -------------------------------------------------------------
    # Test Case 4: Different Valid Scenario
    # -------------------------------------------------------------
    print("\n[TEST 4] Different Valid Scenario")
    df4 = ep.load_dataset("testcase4_scenario.csv", show_summary=False)
    buffer4 = io.StringIO()
    with contextlib.redirect_stdout(buffer4):
        res4 = ep.predict_usage_and_bill(df4, 6)
        if res4:
            ep.plot_actual_vs_predicted(
                df4, res4["slope"], res4["intercept"], res4["target_month"], res4["predicted_units"]
            )
    out4 = buffer4.getvalue().strip()

    print("Output received:")
    print(out4)

    expected_4 = [
        "Slope: 24.00 | Intercept: 75.00 | R2: 0.99",
        "Predicted units (Month 6): 219.00",
        "Estimated bill: Rs. 1314.00",
        "Line chart 'Actual vs Predicted' displayed"
    ]
    tc4_pass = all(line in out4 for line in expected_4)
    if tc4_pass:
        print(">>> Test Case 4: PASSED [OK]")
        tests_passed += 1
    else:
        print(">>> Test Case 4: FAILED [X]")

    # -------------------------------------------------------------
    # Summary
    # -------------------------------------------------------------
    print("\n" + "=" * 60)
    print(f"TEST RESULTS SUMMARY: {tests_passed}/{total_tests} PASSED ({(tests_passed/total_tests)*100:.0f}%)")
    print("=" * 60)

    return tests_passed == total_tests


if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
