import numpy as np
import matplotlib.pyplot as plt

def run_sfc_cognitive_evolution():
    print("Running SFC 4.0 - 6.0: Cognitive Evolution & Goal Selection...")
    
    N, T = 100, 1000
    phi = np.random.randn(N) * 0.1
    P = np.zeros(N)  # Predictive model
    G = np.array([np.sin(np.linspace(0, 2*np.pi, N)), 
                  np.cos(np.linspace(0, 2*np.pi, N))]) # Two competing goals
    
    learning_rate = 0.05
    history = []

    for t in range(T):
        # 1. Tính toán sai số dự báo (epsilon)
        epsilon = phi - P
        
        # 2. Cơ chế Softmax để chọn mục tiêu (Goal Selection)
        # Mục tiêu nào giúp giảm epsilon tốt hơn sẽ được ưu tiên
        scores = np.array([-np.sum((g - phi)**2) for g in G])
        probs = np.exp(scores) / np.sum(np.exp(scores))
        current_goal = G[0] * probs[0] + G[1] * probs[1]
        
        # 3. Cập nhật trạng thái dựa trên mục tiêu và mô hình dự báo
        phi = phi + 0.1 * (current_goal - phi) + 0.05 * np.random.randn(N)
        P = P + learning_rate * (phi - P) # Cập nhật mô hình P
        
        history.append(phi.copy())

    plt.imshow(np.array(history).T, aspect='auto', cmap='viridis')
    plt.title("SFC 4.0-6.0: Goal Competition & Predictive Learning")
    plt.xlabel("Time")
    plt.ylabel("Field Space")
    plt.colorbar(label="Field Intensity")
    plt.show()

if __name__ == "__main__":
    run_sfc_cognitive_evolution()
  
