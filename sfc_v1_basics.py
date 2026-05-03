import numpy as np  
import matplotlib.pyplot as plt  
  
N = 200  
T = 3000      # tăng thời gian để xem ổn định lâu dài  
tau = 30  
a = 0.15  
b = -0.008  
c = 0.55      # delay coupling  
  
phi = np.random.randn(N) * 0.08  
history = [phi.copy()]  
  
for t in range(T):  
    phi_new = phi.copy()  
    for i in range(N):  
        left = phi[(i-1) % N]  
        right = phi[(i+1) % N]  
          
        diffusion = a * (left - 2*phi[i] + right)  
        nonlinear = b * phi[i]**3  
          
        delay_term = c * history[t - tau][i] if t >= tau else 0  
          
        phi_new[i] = phi[i] + diffusion + nonlinear + delay_term  
      
    phi = np.clip(phi_new, -2, 2)   # tránh blow up  
    history.append(phi.copy())  
  
# Hiển thị  
data = np.array(history)  
  
plt.figure(figsize=(12, 5))  
plt.subplot(1, 2, 1)  
plt.plot(phi)  
plt.title("Final state (with delay)")  
plt.xlabel("Space")  
plt.ylabel("φ")  
  
plt.subplot(1, 2, 2)  
plt.imshow(data.T, aspect='auto', cmap='plasma', origin='lower')  
plt.title("Spacetime evolution (τ=30, c=0.55)")  
plt.xlabel("Time")  
plt.ylabel("Space")  
plt.colorbar()  
plt.tight_layout()  
plt.show()
  
