import numpy as np
import matplotlib.pyplot as plt

def run_sfc_v3_2():
    print("Running SFC-V3.2: Emergent Pattern Diversity...")
    N, T, tau = 200, 5000, 40
    
    # --- ĐIỀU CHỈNH ĐỂ TRÁNH ĐỒNG BỘ HÓA ---
    D = 0.04          # Giảm khuếch tán để giữ tính cá thể
    alpha = 0.4       # Tăng áp lực môi trường
    beta = 0.15       # Tăng tính phi tuyến để tạo ra sự khác biệt
    gamma = 0.45      # Giảm nhẹ quán tính để không bị 'đóng băng'
    rho = 0.15        # Tánh biết học chậm hơn, cẩn trọng hơn
    lam = 0.35        
    
    phi = np.random.uniform(-1, 1, N)
    # Tạo môi trường K không đồng nhất (Vũ trụ lồi lõm)
    K = 0.5 + 0.2 * np.sin(np.linspace(0, 4*np.pi, N)) 
    M = np.zeros(N)
    
    h_phi = [phi.copy()]
    
    for t in range(T):
        delay = h_phi[t-tau] if t >= tau else h_phi[0]
        
        # Thêm một chút nhiễu nền (Sự ngẫu nhiên của Tánh biết)
        noise = np.random.normal(0, 0.01, N)
        
        lap_phi = D * (np.roll(phi, 1) - 2*phi + np.roll(phi, -1))
        # Phương trình SFC core
        phi_new = phi + lap_phi - alpha*K*phi - beta*(phi**3) + gamma*delay + lam*M*phi + noise
        
        M_new = M + rho * (delay - M)
        
        phi, M = np.clip(phi_new, -2.5, 2.5), np.clip(M_new, -2, 2)
        h_phi.append(phi.copy())
        
    return np.array(h_phi)

data = run_sfc_v3_2()
plt.figure(figsize=(12, 8))
# Sử dụng 'twilight_shifted' hoặc 'gnuplot2' để thấy rõ các vân sóng phức tạp
img = plt.imshow(data.T, aspect='auto', cmap='gnuplot2', origin='lower')
plt.colorbar(img, label='Góc nhìn nội tại (Phân hóa)')
plt.title("SFC V3.2: Sự phân hóa góc nhìn và Quán tính phi tuyến")
plt.show()
