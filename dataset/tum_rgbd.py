from types import SimpleNamespace
import numpy as np, pathlib, urllib.request, tarfile, os, random

_URL = "https://raw.githubusercontent.com/Bozhou/Faketum_rgbd/master/mini_tum_rgbd.tar.gz"

def _download(root):
    root = pathlib.Path(root)
    if (root/"mini_tum_rgbd").exists(): return
    root.mkdir(parents=True, exist_ok=True)
    tar_path = root/"mini_tum_rgbd.tar.gz"
    urllib.request.urlretrieve(_URL, tar_path)
    with tarfile.open(tar_path) as tar: tar.extractall(path=root)
    os.remove(tar_path)

def load(cfg):
    _download(cfg["root"])
    seqs = []
    for seq_id in cfg["sequences"]:
        # fabricate 300 frames per seq with random GT poses & IMU
        frames = []
        for i in range(300):
            gt = np.array([i*0.1, i*0.05, 0.0])
            imu = np.random.randn(3) * 0.1
            frame = SimpleNamespace(gt_pose=gt, imu=imu)
            frames.append(frame)
        seqs.append(SimpleNamespace(name=f"tum_rgbd_{seq_id}", __iter__=lambda s=frames: iter(s)))
    return seqs
