import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter

def run_sfc_7_5():
    N, T, tau = 100, 450, 22
    empathy_factor, shared_learning_rate = 0.45, 0.035
    Psi, P, K = np.zeros((N, N)), np.zeros((N, N)), np.zeros((N, N)) + 0.06
    Psi_history = [Psi.copy() for _ in range(tau)]
    A_slice, B_slice = (slice(25,40), slice(25,40)), (slice(60,75), slice(60,75))

    for t in range(T):
        Psi_delay = Psi_history[0].copy()
        if 120 < t < 180: Psi[B_slice] += 0.8 * np.random.randn(15,15) # Shock
        
        epsilon = Psi - P
        eps_A, eps_B = np.mean(np.abs(epsilon[A_slice])), np.mean(np.abs(epsilon[B_slice]))
        
        # Empathy mechanism
        Psi[B_slice] -= (empathy_factor * eps_B if eps_B > 0.25 else 0) * 0.6
        Psi[A_slice] -= (empathy_factor * eps_A if eps_A > 0.25 else 0) * 0.6
        
        lap = gaussian_filter(Psi, sigma=1.1, order=2, mode='wrap') * 4.0
        Psi = Psi + (0.055*lap - 0.58*K*Psi - 0.39*Psi**3 + 0.56*Psi*Psi_delay - 0.26*epsilon) * 0.1
        P = P + shared_learning_rate * epsilon
        K = np.clip(K + 0.22*(Psi**2 - K) - 0.09*K**2, 0, 3.8)
        Psi = np.clip(Psi, -4.5, 4.5)
        Psi_history.pop(0); Psi_history.append(Psi.copy())

    plt.imshow(Psi, cmap='RdBu_r')
    plt.title("SFC 7.5: Intersubjective Resonance")
    plt.show()

if __name__ == "__main__":
    run_sfc_7_5()
      
