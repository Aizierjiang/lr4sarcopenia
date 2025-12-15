import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle
import seaborn as sns

# ============================================
# CONFIGURABLE PARAMETERS - ADJUST THESE
# ============================================

# Font sizes
TITLE_FONTSIZE = 19
SUBTITLE_FONTSIZE = 16
SMI_FONTSIZE = 14
LEGEND_FONTSIZE = 13

# Text positioning (vertical offset from bottom of plot)
SMI_TEXT_Y_OFFSET = -1  # Distance below the plot for SMI text
SUBTITLE_PAD = 3  # Padding above subplot titles
TITLE_Y_POSITION = 0.98  # Vertical position of main title (0-1, higher = further up)

# Legend positioning
LEGEND_X_POSITION = 0  # X position within axes (0-1, left to right)
LEGEND_Y_POSITION = 1.25  # Y position within axes (0-1, bottom to top)

# Element positioning
VISCERAL_FAT_CENTER_X = 0  # X-coordinate of visceral fat center
VISCERAL_FAT_CENTER_Y = 0  # Y-coordinate of visceral fat center

# Muscle circle positioning
MUSCLE_DISTANCE_FROM_CENTER = 0.5  # Distance of muscle circles from center (affects spacing)

# Figure dimensions
FIGURE_WIDTH = 15
FIGURE_HEIGHT = 5

# Subplot spacing
SUBPLOT_HORIZONTAL_SPACING = 0.01  # Horizontal space between subplots (0-1, lower = closer together)

# ============================================
# END OF CONFIGURABLE PARAMETERS
# ============================================

# Set style
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")

def fig_body_composition():
    fig, axes = plt.subplots(1, 3, figsize=(FIGURE_WIDTH, FIGURE_HEIGHT))
    
    for idx, (ax, title, severity) in enumerate(zip(axes, 
                                                     ['Normal', 'Mild Sarcopenia', 'Severe Sarcopenia'],
                                                     [1.0, 0.7, 0.4])):
        ax.set_xlim(-1, 1)
        ax.set_ylim(-1, 1)
        ax.set_aspect('equal')
        ax.axis('off')
        
        # Outer body contour
        theta = np.linspace(0, 2*np.pi, 100)
        body_x = 0.9 * np.cos(theta)
        body_y = 0.9 * np.sin(theta)
        ax.fill(body_x, body_y, color='#F0E68C', alpha=0.3, edgecolor='black', linewidth=2)
        
        # Subcutaneous fat
        fat_thickness = 0.15 * (1.2 - severity*0.3)
        fat_x = (0.9 - fat_thickness) * np.cos(theta)
        fat_y = (0.9 - fat_thickness) * np.sin(theta)
        ax.fill(body_x, body_y, color='yellow', alpha=0.4, label='Subcutaneous Fat')
        ax.fill(fat_x, fat_y, color='#F0E68C', alpha=0.3)
        
        # Skeletal muscle (decreases with severity)
        muscle_radius = 0.6 * severity
        n_muscles = 8
        for i in range(n_muscles):
            angle = i * 2*np.pi/n_muscles
            x_center = MUSCLE_DISTANCE_FROM_CENTER * np.cos(angle)
            y_center = MUSCLE_DISTANCE_FROM_CENTER * np.sin(angle)
            muscle = Circle((x_center, y_center), muscle_radius/4, 
                          color='red', alpha=0.7, edgecolor='darkred', linewidth=1)
            ax.add_patch(muscle)
        
        # Visceral fat (increases slightly with sarcopenia)
        visc_fat_radius = 0.3 * (1 + (1-severity)*0.3)
        visc_fat = Circle((VISCERAL_FAT_CENTER_X, VISCERAL_FAT_CENTER_Y), visc_fat_radius, 
                         color='orange', alpha=0.5, label='Visceral Fat')
        ax.add_patch(visc_fat)
        
        # Spine
        spine = Rectangle((-0.08, -0.15), 0.16, 0.3, 
                         color='white', edgecolor='black', linewidth=2)
        ax.add_patch(spine)
        
        # Add measurements
        smi = 55 * severity  # Skeletal Muscle Index
        ax.text(0, SMI_TEXT_Y_OFFSET, f'SMI: {smi:.1f} cm²/m²', 
               ha='center', fontsize=SMI_FONTSIZE, fontweight='bold')
        
        ax.set_title(title, fontsize=SUBTITLE_FONTSIZE, fontweight='bold', pad=SUBTITLE_PAD)
        
        if idx == 0:
            ax.legend(loc='upper left', fontsize=LEGEND_FONTSIZE, framealpha=0.9,
                     bbox_to_anchor=(LEGEND_X_POSITION, LEGEND_Y_POSITION))
    
    plt.suptitle('L3 Cross-Sectional Body Composition Analysis', 
                fontsize=TITLE_FONTSIZE, fontweight='bold', y=TITLE_Y_POSITION)
    plt.subplots_adjust(wspace=SUBPLOT_HORIZONTAL_SPACING)
    return fig

# Generate figure
print("Generating Body Composition Figure...")
fig = fig_body_composition()
plt.savefig('body_composition.png', dpi=300, bbox_inches='tight')
print("Saved as body_composition.png")

print("\n✅ Figure generated successfully!")
print("\nFigure Description:")
print("L3 cross-sections showing sarcopenia severity with SMI values")
print("\nTo adjust font sizes and text positioning, modify the parameters at the top of the script.")

plt.show()