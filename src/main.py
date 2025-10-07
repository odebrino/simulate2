"""
SIMULATE 2 – main.py
Main entry point for the surgical coniotomy AR simulation.
"""

from ai.detection import analyze_frame
from unity_bridge.ar_sync import send_to_unity


def main():
    print("\n=== 🩺 SIMULATE 2 – AR Coniotomy Simulation ===\n")

    # Step 1: Run AI detection placeholder
    result = analyze_frame()
    print(f"Detection result → {result}")

    # Step 2: Send data to Unity bridge
    response = send_to_unity(result)
    print(f"Unity response → {response}")

    print("\n✅ Simulation pipeline executed successfully.\n")


if __name__ == "__main__":
    main()
