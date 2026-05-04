import numpy as np
import matplotlib.pyplot as plt

def run_sfc_v1():
    print("Running SFC-V1: Basic Delay Dynamics...")
    N, T, tau = 200, 3000, 30
    a, b, c = 0.15, -0.008, 0.55
    phi = np.random.randn(N) * 0.08
    history = [phi.copy()]
    for t in range(T):
        phi_new = phi.copy()
        for i in range(N):
            lap = a * (phi[(i-1)%N] - 2*phi[i] + phi[(i+1)%N])
            delay = c * history[t-tau][i] if t >= tau else 0
            phi_new[i] = phi[i] + lap + b*phi[i]**3 + delay
        phi = np.clip(phi_new, -2, 2)
        history.append(phi.copy())
    return np.array(history)

def run_sfc_v3():
    print("Running SFC-V3: Self-Model (M) Integration...")
    N, T, tau = 200, 5000, 35
    D, alpha, beta, gamma = 0.12, 0.45, 0.008, 0.55
    rho, sigma, lam = 0.22, 0.045, 0.42
    phi, K, M = np.random.randn(N)*0.1, np.ones(N)*0.4, np.zeros(N)
    h_phi = [phi.copy()]
    for t in range(T):
        phi_new, M_new = phi.copy(), M.copy()
        for i in range(N):
            delay = h_phi[t-tau][i] if t >= tau else 0.0
            phi_new[i] = phi[i] + D*(phi[(i-1)%N]-2*phi[i]+phi[(i+1)%N]) - alpha*K[i]*phi[i] - beta*phi[i]**3 + gamma*phi[i]*delay + lam*M[i]*phi[i]
            M_new[i] = M[i] + rho*(delay - M[i]) + sigma*(M[(i-1)%N]-2*M[i]+M[(i+1)%N])
        phi, M = np.clip(phi_new, -3, 3), np.clip(M_new, -2.5, 2.5)
        h_phi.append(phi.copy())
    return np.array(h_phi)

if __name__ == "__main__":
    # Chạy bản V3 làm mặc định
    data = run_sfc_v3()
    plt.imshow(data.T, aspect='auto', cmap='plasma')
    plt.title("SFC V3: Self-Model Evolution")
    plt.show()
  
