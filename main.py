import argparse, yaml, random, numpy as np
from slam.vio_frontend import VIOFrontend
from slam.backend import Backend
from datasets import kitti, tum_rgbd, euroc

def set_seed(seed):
    random.seed(seed)
    np.random.seed(seed)

def load_cfg(path):
    with open(path, "r") as f:
        return yaml.safe_load(f)

def build_datasets(cfg):
    ds = []
    if "kitti" in cfg["datasets"]:  ds += kitti.load(cfg["datasets"]["kitti"])
    if "tum"   in cfg["datasets"]:  ds += tum_rgbd.load(cfg["datasets"]["tum"])
    if "euroc" in cfg["datasets"]:  ds += euroc.load(cfg["datasets"]["euroc"])
    return ds

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", default="config.yaml")
    args = ap.parse_args()

    cfg = load_cfg(args.config)
    set_seed(cfg["general"]["random_seed"])

    vio = VIOFrontend(cfg["ekf"])
    backend = Backend(cfg)

    for seq in build_datasets(cfg):
        vio.reset()
        backend.reset(seq.name)
        for frame in seq:                       # iterate synchronised cam+IMU
            pose_pred = vio.process(frame)      # Kalman predict+update
            backend.record(frame, pose_pred)    # save trajectories etc.
        backend.finalize()

    backend.summarize()  # -> metrics.csv & plots/
    print("✅  all done — results stored in", cfg["general"]["output_dir"])

if __name__ == "__main__":
    main()
