import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter

def run_sfc_7_3():
    N, T, tau = 80, 400, 22
    dt, eta, lambda_w = 0.08, 0.18, 0.32
    Psi = np.random.randn(N, N) * 0.05
    P = np.zeros((N, N))
    K = np.zeros((N, N)) + 0.05
    Psi_history = [Psi.copy() for _ in range(tau)]

    for t in range(T):
        Psi_delay = Psi_history[0].copy()
        epsilon = Psi - P
        will_force = -eta * epsilon * (1 + 0.5 * np.abs(epsilon))
        lap = gaussian_filter(Psi, sigma=1.0, order=2, mode='wrap') * 4.0
        
        Psi = Psi + (0.055*lap - 0.65*K*Psi - 0.42*Psi**3 + 0.52*Psi*Psi_delay - 0.28*epsilon + lambda_w*will_force) * dt
        P = P + 0.32*(Psi - P) + 0.14*(Psi_delay - P)
        K = np.clip(K + 0.22*(Psi**2 - K) - 0.10*K**2, 0, 3.5)
        Psi = np.clip(Psi, -4, 4)
        Psi_history.pop(0); Psi_history.append(Psi.copy())

    plt.imshow(Psi, cmap='RdBu_r')
    plt.title("SFC 7.3: Active Will Field")
    plt.colorbar(); plt.show()

if __name__ == "__main__":
    run_sfc_7_3()
      
