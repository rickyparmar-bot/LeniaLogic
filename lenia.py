import numpy as np
import cv2
from scipy.signal import fftconvolve

class LeniaSimulation:
    def __init__(self, width=200, height=200):
        self.width = width
        self.height = height
        
        # --- PHYSICS PARAMETERS (Finding Life) ---
        self.R = 13.0      # Radius of influence
        self.T = 10.0      # Time step
        self.mu = 0.15     # Growth center
        self.sigma = 0.015 # Growth width
        
        # Initialize grid with random "biological" noise
        self.grid = np.zeros((height, width), dtype=np.float32)
        self._seed_life()
        
        # Precompute the Convolutional Kernel (The "Brain" of the cell)
        y, x = np.ogrid[-self.R:self.R, -self.R:self.R]
        dist = np.sqrt(x**2 + y**2) / self.R
        kernel = np.exp(4 - 4 / (4 * dist * (1 - dist) + 1e-9)) # Polynomial-like ring
        kernel[dist >= 1] = 0
        self.kernel = kernel / np.sum(kernel)

    def _seed_life(self):
        """Add some starting droplets."""
        for _ in range(10):
            cx, cy = np.random.randint(50, 150, 2)
            r = 10
            y, x = np.ogrid[-r:r, -r:r]
            mask = x**2 + y**2 <= r**2
            self.grid[cy-r:cy+r, cx-r:cx+r][mask] = 0.5

    def growth(self, U):
        """The growth function: A Bell curve around mu."""
        return 2 * np.exp(-((U - self.mu)**2) / (2 * self.sigma**2)) - 1

    def step(self):
        """Perform one biological time step."""
        # 1. Neighbor density calculation (via FFT Convolution)
        U = fftconvolve(self.grid, self.kernel, mode='same')
        
        # 2. Apply growth rules
        self.grid = np.clip(self.grid + (1.0/self.T) * self.growth(U), 0, 1)

    def run(self):
        print("🦠 LeniaLogic: Biological Computing Arena Booting...")
        print("Press 'q' to quit, 'r' to re-seed life.")
        
        while True:
            self.step()
            
            # Rendering: Turn the grid into a beautiful heatmap
            display = (self.grid * 255).astype(np.uint8)
            colored = cv2.applyColorMap(display, cv2.COLORMAP_MAGMA)
            
            # Upscale for better viewing
            resized = cv2.resize(colored, (600, 600), interpolation=cv2.INTER_LINEAR)
            
            cv2.imshow("LeniaLogic: Emergent Biological Computer", resized)
            
            key = cv2.waitKey(1) & 0xFF
            if key == ord('q'):
                break
            elif key == ord('r'):
                self.grid.fill(0)
                self._seed_life()

        cv2.destroyAllWindows()

if __name__ == "__main__":
    sim = LeniaSimulation()
    sim.run()
