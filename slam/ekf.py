import numpy as np

class EKF:
    """Toy error-state EKF — keeps state as [x, y, yaw] for demo purposes."""

    def __init__(self, cfg):
        self.Q = np.diag([cfg["accel_noise"]**2]*2 + [cfg["gyro_noise"]**2])
        self.R = np.diag([1.0, 1.0])  # pixel noise
        self.reset()

    def reset(self):
        self.x = np.zeros(3)          # pose
        self.P = np.eye(3) * 1e-3

    def f(self, x, u):                # simple SE2 motion model
        dt = 0.01
        return x + dt * np.array([u[0]*np.cos(x[2]), u[0]*np.sin(x[2]), u[1]])

    def step(self, u, z):
        # Predict
        self.x = self.f(self.x, u)
        self.P = self.P + self.Q

        # Update
        H = np.array([[1,0,0], [0,1,0]])
        y = z - H @ self.x[:2]
        S = H @ self.P @ H.T + self.R
        K = self.P @ H.T @ np.linalg.inv(S)
        self.x += K @ y
        self.P = (np.eye(3) - K @ H) @ self.P
        return self.x.copy()
