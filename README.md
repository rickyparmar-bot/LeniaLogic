# 🦠 LeniaLogic: Emergent Biological Computing

![Math](https://img.shields.io/badge/Math-Integral%20Differential-blueviolet) ![Performance](https://img.shields.io/badge/Perf-FFT--Accelerated-brightgreen) ![Substrate](https://img.shields.io/badge/Substrate-Continuous%20Automata-lightgrey)

LeniaLogic is a high-performance simulation of continuous cellular automata that investigates **Emergent Computation**. It explores how lifelike, self-organizing structures can be utilized as a physical substrate for logic gates.

## 🚀 The Mathematical Theory
Unlike discrete systems (Game of Life), Lenia exists in a continuous domain.
- **$\mu$ (Kernel):** A Gaussian ring kernel that defines the local neighborhood.
- **$\Phi$ (Growth):** A mapping that determines how cells grow or die based on neighborhood density.
- **FFT:** Computation is performed in the frequency domain for $O(N \log N)$ efficiency.

### 🛠️ Strategic Research
- **Kinetic Logic:** We are engineering gliders to collide at specific phases to perform **AND**, **OR**, and **NOT** operations.
- **Orbium Stable States:** Identification of autonomous entities that maintain structural integrity across the grid.

---

## 💻 Setup & Simulation
### Dependencies
```bash
pip install numpy scipy opencv-python
```

### Running the Primordial Soup
Launch the real-time simulation window.
```bash
python3 lenia.py
```

---

## 📂 Project Structure
```text
LeniaLogic/
├── lenia.py        # Core FFT engine and rendering loop
├── kernels.py      # Gaussian neighborhood definitions
├── patterns/       # Catalog of stable biological entities
└── README.md       # Surface & technical documentation
```

## 🗺️ Roadmap
- [ ] **Logic Substrate:** Hard-coding a collision-based adder circuit.
- [ ] **Genetic Evolution:** Evolving kernel parameters to maximize complexity.
- [ ] **PyTorch Port:** Moving convolutions to the GPU for massive scale.

---
