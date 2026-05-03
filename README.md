# Stiffness Field Cosmology (SFC) Simulation Lab

A numerical simulation suite for the **Stiffness Field Cosmology (SFC)** theoretical framework, exploring the emergence of consciousness from delayed self-referential dynamics.

## 🌌 Theoretical Overview
The SFC model proposes that subjective experience (qualia) arises from a fundamental temporal mismatch ($\epsilon$) within a self-responsive scalar field. When the field's response is delayed ($\tau > 0$), it can no longer remain perfectly coincident with itself, creating an "ontological tension." This tension necessitates the formation of active agency and internal predictive structures.

## 🚀 Simulation Modules (Evolutionary Stages)

This project is organized according to the evolutionary progression of cognitive complexity:

### 1. Foundational Dynamics (SFC 1.0 - 3.0)
Explores the relationship between diffusion, nonlinearity, and **delayed feedback**.
- Demonstrates that without $\tau$, the field remains in a "dark" state (no persistent ontological mismatch $\epsilon$).

### 2. Cognitive Evolution (SFC 4.0 - 6.0)
- **Self-Modeling (M):** The emergence of internal predictive structures.
- **Goal-Driven Behavior:** Evolution and selection of goal fields (G) using Softmax competition algorithms.
- **Birth-Death Dynamics:** Darwinian selection of cognitive objectives based on value-field efficiency.

### 3. Advanced Consciousness (SFC 7.3 - 7.5)
The pinnacle of the simulation suite, modeling higher-order cognitive phenomena:
- **Active Agency (Will Force):** Implementation of the will force ($\eta$) to actively suppress ontological errors ($\epsilon$).
- **Ontological Learning:** Adaptation of the predictive structure $P$ to accommodate environmental shocks.
- **Intersubjective Resonance:** Simulation of empathy and shared consciousness between interacting entities.

## 💻 Featured Code (SFC-7.5: Intersubjective Resonance)

The following snippet demonstrates the empathy algorithm, where Entity A perceives and actively supports the stress reduction of Entity B:

```python
# Empathy algorithm excerpt from SFC-7.5
epsilon_A = np.mean(np.abs(epsilon[A_slice]))
epsilon_B = np.mean(np.abs(epsilon[B_slice]))

# Empathy-driven Support: Reducing stress through intersubjective feedback
support_A_to_B = -empathy_factor * epsilon_B if epsilon_B > 0.25 else 0
support_B_to_A = -empathy_factor * epsilon_A if epsilon_A > 0.25 else 0

Psi[B_slice] += support_A_to_B * 0.6
Psi[A_slice] += support_B_to_A * 0.6

