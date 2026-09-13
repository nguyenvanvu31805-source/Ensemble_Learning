import subprocess
import sys
from pathlib import Path

def main():
    print("=== Ensemble Learning - Iris Classification ===")
    print("Training models...\n")

    project_root = Path(__file__).resolve().parents[1]

    subprocess.run(
        [sys.executable, "-m", "app.train"],
        check=True,
        cwd=project_root
    )

    print("\nTraining completed.")
    print("Results saved in results/comparison.csv")


if __name__ == "__main__":
    main()