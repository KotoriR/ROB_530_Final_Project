# One-liner convenience to call `python evaluation/run_eval.py`
import subprocess, pathlib, sys
if __name__ == "__main__":
    cfg = sys.argv[1] if len(sys.argv) > 1 else "config.yaml"
    subprocess.run([sys.executable, "main.py", "--config", cfg], check=True)
    print("evaluation finished")
