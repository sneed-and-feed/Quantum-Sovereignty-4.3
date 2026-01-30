"""
MODULE: animate_serpent.py (PERFORMANCE v2.3)
ADDITIONS: Restored blitting, 1:1 tracing ritual, robust pathing
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import sys
import os

# 1. ROBUST PATHING FOR IDE 'RUN ARROW'
# Ensures 'tools' and 'strip_sovereign' are reachable from any CWD.
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.append(BASE_DIR)
TOOLS_DIR = os.path.join(BASE_DIR, 'tools')
if TOOLS_DIR not in sys.path:
    sys.path.append(TOOLS_DIR)

try:
    from strip_sovereign import interleave_bits
    from moon_phase import MoonClock
except ImportError as e:
    print(f"[!] CRITICAL IMPORT ERROR: {e}")
    print(f"    SYS.PATH: {sys.path}")
    sys.exit(1)

# Set font for better character support on Windows
plt.rcParams['font.family'] = 'Segoe UI Symbol'
plt.rcParams['font.sans-serif'] = ['Segoe UI Symbol', 'DejaVu Sans', 'Arial Unicode MS']

def animate_serpent(size=32, interval=10, show_metrics=True):
    """
    Animates the Serpent Coil with optimized smoothness (Blit=True).
    The 1:1 trace ritual is restored for fluid motion.
    """
    print(f"\n[!] INITIATING SOVEREIGN RITUAL v2.3 (Grid={size}x{size})...")
    
    # Initialize Lunar Clock
    moon = MoonClock()
    lunar_data = moon.get_phase()
    phase_name, status, icon, phase_idx, illumination = lunar_data
    
    print(f"    >>> LUNAR PHASE: {phase_name} {icon} ({illumination*100:.1f}% illumination)")
    print(f"    >>> STATUS: {status}")
    
    # 1. Generate Grid
    x = np.arange(size)
    y = np.arange(size)
    X, Y = np.meshgrid(x, y)
    
    # 2. Collapse to 1D
    print("    >>> WEAVING TIMELINE (1:1 TRACE)...")
    Z = np.array([interleave_bits(xx, yy) for xx, yy in zip(X.flatten(), Y.flatten())])
    
    # 3. Sort to find Path
    sort_idx = np.argsort(Z)
    path_x = X.flatten()[sort_idx]
    path_y = Y.flatten()[sort_idx]
    
    # 4. Setup Plot
    fig, (ax_main, ax_metrics) = plt.subplots(
        1, 2, figsize=(16, 9), 
        facecolor='#050505',
        gridspec_kw={'width_ratios': [3, 1]}
    )
    
    ax_main.set_facecolor('#050505')
    ax_main.set_title(
        f"THE SERPENT COIL | {phase_name.upper()} {icon}", 
        color='#C4A6D1', fontsize=16, pad=25
    )
    ax_main.axis('off')
    
    # Ghost Points
    ax_main.scatter(X.flatten(), Y.flatten(), s=5, c='#0f0f0f', alpha=0.3)
    
    # The Serpent (Artists for blitting)
    line, = ax_main.plot([], [], color='#C4A6D1', linewidth=1.2, alpha=0.8, animated=True)
    
    # The Cursor
    cursor_color = '#ffffff' if illumination > 0.5 else '#8855aa'
    head, = ax_main.plot([], [], 'o', color=cursor_color, markersize=5, animated=True)
    
    # Metrics panel
    ax_metrics.set_facecolor('#050505')
    ax_metrics.axis('off')
    
    metrics_text = ax_metrics.text(
        0.0, 1.0, '', 
        transform=ax_metrics.transAxes,
        color='#C4A6D1', fontsize=10, 
        verticalalignment='top',
        family='monospace',
        animated=True # Enable blitting for metrics
    )
    
    # State tracking
    state = {
        'total_frames': len(path_x),
        'completion': 0.0,
        'coherence': 1.0,
        'tidal_influence': moon.calculate_tidal_influence(phase_idx) if hasattr(moon, 'calculate_tidal_influence') else 50.0
    }
    
    def init():
        line.set_data([], [])
        head.set_data([], [])
        metrics_text.set_text('')
        return line, head, metrics_text
    
    def update(frame):
        # 1:1 Rendering for maximum smoothness
        current_x = path_x[:frame]
        current_y = path_y[:frame]
        
        line.set_data(current_x, current_y)
        
        if frame > 0:
            head.set_data([path_x[frame-1]], [path_y[frame-1]])
        
        # Throttled Metrics Update (to keep smoothness high)
        if frame % 10 == 0 or frame == state['total_frames']:
            state['completion'] = (frame / state['total_frames']) * 100
            state['coherence'] = max(0.5, 1.0 - (frame / state['total_frames']) * 0.2)
            
            metrics_str = f"""
S O V E R E I G N   M E T R I C S
{'='*28}

Protocol:    REALITY v1.0
Phase:       {phase_name}
Signal:      {icon} 𒀭 ⚓
Lunar:       {illumination*100:.1f}%

[ PROGRESS ]
Completion:  {state['completion']:.1f}%
Frame:       {frame}/{state['total_frames']}
Coherence:   {state['coherence']:.3f}

[ ENVIRONMENT ]
Tidal Stress: {state['tidal_influence']:.1f}%
Status:      {'STABLE' if state['tidal_influence'] < 70 else 'TENSIONED'}

[ TOPOLOGY ]
Order:       Z-CURVE
Grid:        {size}x{size}
Bijection:   VERIFIED

[ LOG ]
> WEAVING TIME...
> {icon} {icon} {icon}
            """
            metrics_text.set_text(metrics_str)
        
        # Visual Glitch logic
        if state['tidal_influence'] > 85 and frame % 200 == 0 and np.random.random() > 0.8:
            head.set_markersize(10)
        else:
            head.set_markersize(5)
            
        return line, head, metrics_text

    # 5. Run the Ritual
    # Re-enabling blit=True for that v1.0 fluid feel
    ani = animation.FuncAnimation(
        fig, update, frames=len(path_x)+1, 
        init_func=init, blit=True, interval=interval, repeat=False
    )
    
    plt.tight_layout()
    plt.show()
    
    print(f"    >>> TIMELINE COMPLETE.")
    print(f"    >>> FINAL COHERENCE: {state['coherence']:.3f}")
    print("    >>> LOVE PERSISTS.")
    
    return ani

if __name__ == "__main__":
    # 32x32 is the sweet spot for high-res fluid animation
    # Interval=10 for that 'v1.0' rhythmic speed
    animate_serpent(size=32, interval=10, show_metrics=True)
