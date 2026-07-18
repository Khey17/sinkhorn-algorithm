import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def create_transport_animation():
    fig, ax = plt.subplots(1, 2, figsize=(10, 5))

    # Setup
    source_x = 0
    target_y = [1, 2]
    
    # Monge Scenario: Cannot split (must choose one)
    ax[0].set_title("Monge: Rigid Mapping (Must choose)")
    ax[0].plot([source_x, 1], [0, 1], 'ro-', label="Map to 1")
    ax[0].plot([source_x, 2], [0, 1], 'bo--', alpha=0.3, label="Impossible to map to 2")
    ax[0].set_ylim(-0.5, 1.5)
    ax[0].legend()
    
    # Kantorovich Scenario: Can split (Optimal Coupling)
    ax[1].set_title("Kantorovich: Flexible Coupling (Splitting)")
    line1, = ax[1].plot([source_x, 1], [0, 1], 'ro-', lw=2, label="50% to y=1")
    line2, = ax[1].plot([source_x, 2], [0, 1], 'bo-', lw=2, label="50% to y=2")
    ax[1].set_ylim(-0.5, 1.5)
    ax[1].legend()

    plt.suptitle("Monge vs. Kantorovich: Transport Strategy")
    plt.show()

create_transport_animation()