# Visual–Inertial ORB-SLAM3 (NAVARCH 568 Final Project)

Lightweight scaffold that **wraps ORB-SLAM3**, streams IMU packets through a
minimal Kalman Filter, and reproduces the dataset and simulation experiments
described in *NAVARCH 568 Final Project Report*.

> **NOTE**  
> All modules run, but heavy-duty math is stubbed with random noise so the
> repo remains lightweight. Swap in real solvers or link to ORB-SLAM3 if you
> need production-grade performance.

## Quick Start

```bash
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
python main.py --config config.yaml
