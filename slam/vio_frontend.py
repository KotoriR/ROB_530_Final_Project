import numpy as np
from .ekf import EKF
from .imu_preintegration import PreIntegrator

class VIOFrontend:
    """Wraps ORB feature tracking and a *minimal* Kalman filter."""

    def __init__(self, ekf_cfg):
        self.ekf = EKF(ekf_cfg)
        self.preint = PreIntegrator(ekf_cfg["imu_rate_hz"])

    def reset(self):
        self.ekf.reset()
        self.preint.reset()

    def process(self, frame):
        # 1) visual tracking (placeholder)
        meas_z = np.random.randn(2) * 0.5  # fake pixel obs

        # 2) inertial propagation
        self.preint.integrate(frame.imu)

        # 3) fuse
        pose = self.ekf.step(self.preint.delta(), meas_z)
        self.preint.reset()  # start next interval
        return pose
