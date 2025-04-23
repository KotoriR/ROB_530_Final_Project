import numpy as np

class PreIntegrator:
    """Collects IMU packets and returns dpos, dtheta every call to delta()."""
    def __init__(self, rate_hz):
        self.dt = 1.0 / rate_hz
        self.reset()

    def reset(self):
        self.dpos = np.zeros(2)
        self.dtheta = 0.0

    def integrate(self, imu):
        # imu = (ax, ay, gyro_z)
        self.dpos += imu[:2] * self.dt**2 * 0.5
        self.dtheta += imu[2] * self.dt

    def delta(self):
        out = np.array([np.linalg.norm(self.dpos), self.dtheta])
        return out
