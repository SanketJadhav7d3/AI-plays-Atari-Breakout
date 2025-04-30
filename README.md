# AI plays Atari Breakout

Trained an AI to play Atari Breakout game using python NEAT.

https://github.com/user-attachments/assets/e6ce91d1-92af-4bd5-8259-850f37b9da01

More about NEAT Algorithm - https://nn.cs.utexas.edu/downloads/papers/stanley.cec02.pdf

This project uses the NEAT (NeuroEvolution of Augmenting Topologies) algorithm to evolve neural network controllers that learn to play a simplified version of Atari Breakout. Pygame provides the game simulation (ball, bricks, paddle), while NEAT-Python drives the evolutionary process. Training progress and results are visualized using Matplotlib and Graphviz.

---

## Features

- **Game Environment**: Implemented in Pygame with realistic ball physics, brick layouts, and paddle control.
- **NEAT Integration**: Uses NEAT-Python to evolve paddle-control neural networks based on fitness from bricks broken.
- **Configurable Hyperparameters**: NEAT parameters (population size, mutation rates, species thresholds, network topology) are easily adjusted via `config.txt`.
- **Visualization**: Generates average/best fitness and speciation plots (`avg_fitness.svg`, `speciation.svg`) to track evolutionary dynamics.
- **Modular Design**: Separate modules for game logic (`ball.py`, `tiles.py`, `player_block.py`) and training/visualization (`main.py`, `visualize.py`).

---

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/SanketJadhav7d3/AI-plays-Atari-Breakout.git
   cd AI-plays-Atari-Breakout
   ```

2. **Create a virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

*Note: Ensure your system has Pygame, NEAT-Python, Matplotlib, and Graphviz installed.*

---

## Configuration

All NEAT hyperparameters are specified in `config.txt`. Key settings include:

- `pop_size`: Number of genomes per generation
- `max_fitness_threshold`: Fitness at which training stops
- Mutation and crossover probabilities
- Network architecture parameters (number of hidden layers, nodes)

Edit `config.txt` to experiment with different evolutionary strategies.

---

## Usage

### Training

Run the evolutionary training loop for 40 generations (default):

```bash
python main.py
```

- Each genome represents a paddle controller receiving three inputs: paddle x-position, ball x-position, ball y-position.
- Actions: move left, move right, or stay.
- Fitness: +10 points per brick broken; game ends when the ball falls below the paddle or a high-score is reached.

### Visualization

After training, generate performance plots:

```bash
python visualize.py
```

- `avg_fitness.svg`: Mean and best fitness over generations.
- `speciation.svg`: Species sizes across generations.

You can also render the winning genome’s network topology using Graphviz (requires `neat-python`’s visualization helpers).

---

## File Structure

```
AI-plays-Atari-Breakout/
├─ ball.py            # Ball sprite & physics logic
├─ tiles.py           # Brick grid manager
├─ player_block.py    # Paddle sprites & NEAT genome integration
├─ main.py            # Training loop & NEAT setup
├─ visualize.py       # Plotting training statistics
├─ config.txt         # NEAT-Python configuration
├─ avg_fitness.svg    # Sample fitness plot
├─ speciation.svg     # Sample speciation plot
└─ README.md          # Project documentation
```

---

## Contributing

Contributions, issues, and feature requests are welcome! Please fork the repository and create a pull request.
