import numpy as np

def ate_rmse(gt, est):
    return np.linalg.norm(np.array(gt) - np.array(est)) / len(gt)**0.5

def rpe(gt, est, step=1):
    gt, est = np.array(gt), np.array(est)
    diffs = gt[step:] - gt[:-step] - (est[step:] - est[:-step])
    return np.linalg.norm(diffs) / (len(diffs))**0.5
