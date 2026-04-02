#!/usr/bin/env python3
"""
RGB 24-bit to RGB565 Conversion Educational Visualization
Simple visual explanation for non-CS freshmen using matplotlib

This creates static plots that explain:
1. What RGB colors are
2. Memory savings from compression
3. RGB565 bit allocation
4. Step-by-step conversion process
5. Visual comparison of original vs compressed colors
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle
import matplotlib.patches as mpatches

def create_introduction_plot():
    """Create introduction plot explaining RGB colors"""
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)
    ax.axis('off')
    
    # Title
    ax.text(5, 7.5, 'What are Colors on Computers?', 
            fontsize=24, weight='bold', ha='center', color='darkblue')
    
    # RGB squares
    red_rect = Rectangle((1.5, 5), 1.5, 1.5, facecolor='red', alpha=0.8)
    green_rect = Rectangle((4.25, 5), 1.5, 1.5, facecolor='green', alpha=0.8)
    blue_rect = Rectangle((7, 5), 1.5, 1.5, facecolor='blue', alpha=0.8)
    
    ax.add_patch(red_rect)
    ax.add_patch(green_rect)
    ax.add_patch(blue_rect)
    
    # Labels
    ax.text(2.25, 4.5, 'Red\n0-255', ha='center', fontsize=14, weight='bold')
    ax.text(5, 4.5, 'Green\n0-255', ha='center', fontsize=14, weight='bold')
    ax.text(7.75, 4.5, 'Blue\n0-255', ha='center', fontsize=14, weight='bold')
    
    # Explanation
    ax.text(5, 3.5, 'Every pixel is made of Red, Green, and Blue light', 
            ha='center', fontsize=16)
    ax.text(5, 3, 'Each color uses 8 bits (0-255 range)', 
            ha='center', fontsize=14, color='darkgreen')
    ax.text(5, 2.5, 'Total: 24 bits (3 bytes) per pixel', 
            ha='center', fontsize=14, weight='bold', color='red')
    
    # Example
    ax.text(5, 1.5, 'Example: RGB(255, 128, 64)', 
            ha='center', fontsize=14, weight='bold')
    example_rect = Rectangle((4.25, 0.5), 1.5, 0.8, 
                           facecolor=np.array([255, 128, 64])/255, alpha=1)
    ax.add_patch(example_rect)
    
    plt.tight_layout()
    plt.savefig('rgb_introduction.png', dpi=150, bbox_inches='tight')
    plt.show()

def create_memory_comparison():
    """Show memory savings comparison"""
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)
    ax.axis('off')
    
    # Title
    ax.text(5, 7.5, 'Why Compress Colors? Memory Savings!', 
            fontsize=22, weight='bold', ha='center', color='darkblue')
    
    # Phone example
    ax.text(5, 6.8, 'Example: Phone screen 1920 × 1080 pixels', 
            fontsize=16, ha='center')
    
    # Memory bars
    # 24-bit RGB
    rgb24_rect = Rectangle((1, 4.5), 4, 1, facecolor='lightcoral', alpha=0.8)
    ax.add_patch(rgb24_rect)
    ax.text(3, 5, '24-bit RGB', ha='center', fontsize=14, weight='bold')
    ax.text(3, 4, '6.2 MB per frame', ha='center', fontsize=12, color='red')
    
    # 16-bit RGB565
    rgb565_rect = Rectangle((5.5, 4.5), 2.7, 1, facecolor='lightgreen', alpha=0.8)
    ax.add_patch(rgb565_rect)
    ax.text(6.85, 5, '16-bit RGB565', ha='center', fontsize=14, weight='bold')
    ax.text(6.85, 4, '4.1 MB per frame', ha='center', fontsize=12, color='green')
    
    # Savings arrow
    ax.annotate('', xy=(5.5, 5), xytext=(5, 5), 
                arrowprops=dict(arrowstyle='->', lw=3, color='orange'))
    ax.text(5.25, 5.3, 'Saves\n33%!', ha='center', fontsize=12, 
            weight='bold', color='orange')
    
    # Benefits
    benefits = [
        '• Faster loading times',
        '• Less memory usage',
        '• Better performance on mobile devices',
        '• Reduced bandwidth for streaming'
    ]
    
    for i, benefit in enumerate(benefits):
        ax.text(5, 3 - i*0.3, benefit, ha='center', fontsize=12)
    
    plt.tight_layout()
    plt.savefig('memory_comparison.png', dpi=150, bbox_inches='tight')
    plt.show()

def create_rgb565_format():
    """Explain RGB565 bit allocation"""
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)
    ax.axis('off')
    
    # Title
    ax.text(5, 7.5, 'RGB565 Format: How 16 bits are allocated', 
            fontsize=20, weight='bold', ha='center', color='darkblue')
    
    # Bit allocation diagram
    bit_width = 0.4
    start_x = 1.5
    
    # Red bits (5 bits)
    for i in range(5):
        rect = Rectangle((start_x + i*bit_width, 5), bit_width, bit_width, 
                        facecolor='red', alpha=0.7, edgecolor='black')
        ax.add_patch(rect)
        ax.text(start_x + i*bit_width + bit_width/2, 5.2, str(15-i), 
                ha='center', va='bottom', fontsize=8)
    
    # Green bits (6 bits)
    green_start = start_x + 5*bit_width
    for i in range(6):
        rect = Rectangle((green_start + i*bit_width, 5), bit_width, bit_width, 
                        facecolor='green', alpha=0.7, edgecolor='black')
        ax.add_patch(rect)
        ax.text(green_start + i*bit_width + bit_width/2, 5.2, str(10-i), 
                ha='center', va='bottom', fontsize=8)
    
    # Blue bits (5 bits)
    blue_start = green_start + 6*bit_width
    for i in range(5):
        rect = Rectangle((blue_start + i*bit_width, 5), bit_width, bit_width, 
                        facecolor='blue', alpha=0.7, edgecolor='black')
        ax.add_patch(rect)
        ax.text(blue_start + i*bit_width + bit_width/2, 5.2, str(4-i), 
                ha='center', va='bottom', fontsize=8)
    
    # Labels
    ax.text(start_x + 2.5*bit_width, 4.3, 'Red (5 bits)', 
            ha='center', fontsize=12, weight='bold', color='red')
    ax.text(green_start + 3*bit_width, 4.3, 'Green (6 bits)', 
            ha='center', fontsize=12, weight='bold', color='green')
    ax.text(blue_start + 2.5*bit_width, 4.3, 'Blue (5 bits)', 
            ha='center', fontsize=12, weight='bold', color='blue')
    
    # Explanation
    ax.text(5, 3.5, 'Why this allocation?', 
            ha='center', fontsize=16, weight='bold', color='purple')
    ax.text(5, 3, 'Human eyes are most sensitive to GREEN light!', 
            ha='center', fontsize=14, weight='bold', color='green')
    ax.text(5, 2.5, 'So green gets 6 bits (64 levels) while red and blue get 5 bits (32 levels)', 
            ha='center', fontsize=12)
    
    # Bit positions
    ax.text(5, 1.5, 'Bit positions: Red[15:11] Green[10:5] Blue[4:0]', 
            ha='center', fontsize=12, style='italic')
    
    plt.tight_layout()
    plt.savefig('rgb565_format.png', dpi=150, bbox_inches='tight')
    plt.show()

def create_conversion_steps():
    """Show step-by-step conversion process"""
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))
    
    # Original color example
    original_rgb = [255, 128, 64]
    
    # Top plot: Original color and bit reduction
    ax1.set_xlim(0, 10)
    ax1.set_ylim(0, 6)
    ax1.axis('off')
    
    ax1.text(5, 5.5, 'Step-by-Step Conversion: RGB(255, 128, 64)', 
             fontsize=18, weight='bold', ha='center', color='darkblue')
    
    # Show original color
    orig_rect = Rectangle((1, 4), 2, 1, facecolor=np.array(original_rgb)/255)
    ax1.add_patch(orig_rect)
    ax1.text(2, 3.5, 'Original Color\nRGB(255, 128, 64)', 
             ha='center', fontsize=12, weight='bold')
    
    # Step 1: Bit reduction
    ax1.text(5, 4.5, 'Step 1: Reduce precision by removing lower bits', 
             ha='center', fontsize=14, weight='bold')
    
    conversions = [
        'Red: 255 ÷ 8 = 31 (keep top 5 bits)',
        'Green: 128 ÷ 4 = 32 (keep top 6 bits)', 
        'Blue: 64 ÷ 8 = 8 (keep top 5 bits)'
    ]
    
    for i, conv in enumerate(conversions):
        color = ['red', 'green', 'blue'][i]
        ax1.text(5, 3.5 - i*0.4, conv, ha='center', fontsize=12, color=color)
    
    # Bottom plot: Bit packing
    ax2.set_xlim(0, 10)
    ax2.set_ylim(0, 6)
    ax2.axis('off')
    
    ax2.text(5, 5.5, 'Step 2: Pack bits into 16-bit value', 
             fontsize=16, weight='bold', ha='center', color='darkblue')
    
    # Show bit packing visually
    bit_width = 0.3
    start_x = 2
    
    # Red bits (31 = 11111 in binary)
    red_bits = [1, 1, 1, 1, 1]  # 31 in binary
    for i, bit in enumerate(red_bits):
        color = 'red' if bit else 'white'
        rect = Rectangle((start_x + i*bit_width, 3.5), bit_width, bit_width, 
                        facecolor=color, alpha=0.7, edgecolor='black')
        ax2.add_patch(rect)
        ax2.text(start_x + i*bit_width + bit_width/2, 3.75, str(bit), 
                ha='center', va='center', fontsize=8, weight='bold')
    
    # Green bits (32 = 100000 in binary) 
    green_bits = [1, 0, 0, 0, 0, 0]  # 32 in binary
    green_start = start_x + 5*bit_width
    for i, bit in enumerate(green_bits):
        color = 'green' if bit else 'white'
        rect = Rectangle((green_start + i*bit_width, 3.5), bit_width, bit_width, 
                        facecolor=color, alpha=0.7, edgecolor='black')
        ax2.add_patch(rect)
        ax2.text(green_start + i*bit_width + bit_width/2, 3.75, str(bit), 
                ha='center', va='center', fontsize=8, weight='bold')
    
    # Blue bits (8 = 01000 in binary)
    blue_bits = [0, 1, 0, 0, 0]  # 8 in binary
    blue_start = green_start + 6*bit_width
    for i, bit in enumerate(blue_bits):
        color = 'blue' if bit else 'white'
        rect = Rectangle((blue_start + i*bit_width, 3.5), bit_width, bit_width, 
                        facecolor=color, alpha=0.7, edgecolor='black')
        ax2.add_patch(rect)
        ax2.text(blue_start + i*bit_width + bit_width/2, 3.75, str(bit), 
                ha='center', va='center', fontsize=8, weight='bold')
    
    # Formula
    ax2.text(5, 2.5, 'Formula: (31 << 11) | (32 << 5) | 8 = 64584', 
             ha='center', fontsize=14, weight='bold', 
             bbox=dict(boxstyle="round,pad=0.3", facecolor="lightyellow"))
    
    ax2.text(5, 1.8, 'Result: 16-bit value 64584 (0xFC48 in hex)', 
             ha='center', fontsize=12, style='italic')
    
    plt.tight_layout()
    plt.savefig('conversion_steps.png', dpi=150, bbox_inches='tight')
    plt.show()

def create_quality_comparison():
    """Show original vs compressed color quality"""
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)
    ax.axis('off')
    
    ax.text(5, 7.5, 'Quality Comparison: Original vs RGB565', 
            fontsize=20, weight='bold', ha='center', color='darkblue')
    
    # Color examples
    test_colors = [
        [255, 0, 0],    # Pure red
        [255, 128, 0],  # Orange  
        [255, 255, 0],  # Yellow
        [128, 255, 0],  # Lime
        [0, 255, 0],    # Green
        [0, 255, 128],  # Spring green
        [0, 255, 255],  # Cyan
        [0, 128, 255],  # Sky blue
        [0, 0, 255],    # Blue
        [128, 0, 255],  # Purple
    ]
    
    ax.text(2.5, 6.5, '24-bit Original', ha='center', fontsize=16, weight='bold')
    ax.text(7.5, 6.5, '16-bit RGB565', ha='center', fontsize=16, weight='bold')
    
    for i, color in enumerate(test_colors):
        row = i // 2
        col = i % 2
        y_pos = 5.5 - row * 0.8
        
        # Original color
        orig_rect = Rectangle((1.5 + col*1.2, y_pos), 1, 0.6, 
                             facecolor=np.array(color)/255)
        ax.add_patch(orig_rect)
        
        # RGB565 compressed color
        compressed = rgb_to_rgb565_and_back(color)
        comp_rect = Rectangle((6.5 + col*1.2, y_pos), 1, 0.6, 
                             facecolor=np.array(compressed)/255)
        ax.add_patch(comp_rect)
        
        # Labels
        if col == 0:
            ax.text(0.5, y_pos + 0.3, f'RGB({color[0]},{color[1]},{color[2]})', 
                   ha='left', fontsize=8, va='center')
    
    ax.text(5, 0.8, 'Quality loss is minimal for most applications!', 
            ha='center', fontsize=16, weight='bold', color='green',
            bbox=dict(boxstyle="round,pad=0.5", facecolor="lightgreen", alpha=0.3))
    
    plt.tight_layout()
    plt.savefig('quality_comparison.png', dpi=150, bbox_inches='tight')
    plt.show()

def rgb_to_rgb565_and_back(rgb):
    """Convert RGB to RGB565 and back to show compression effect"""
    r, g, b = rgb
    
    # Convert to RGB565 (simulate bit reduction)
    r5 = r >> 3  # Keep top 5 bits (0-31)
    g6 = g >> 2  # Keep top 6 bits (0-63) 
    b5 = b >> 3  # Keep top 5 bits (0-31)
    
    # Convert back to RGB (simulate expansion)
    r8 = (r5 << 3) | (r5 >> 2)  # Expand 5 bits to 8 bits
    g8 = (g6 << 2) | (g6 >> 4)  # Expand 6 bits to 8 bits
    b8 = (b5 << 3) | (b5 >> 2)  # Expand 5 bits to 8 bits
    
    return [min(255, r8), min(255, g8), min(255, b8)]

def create_summary_infographic():
    """Create a summary infographic"""
    fig, ax = plt.subplots(figsize=(12, 10))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')
    
    # Title
    ax.text(5, 9.5, 'RGB565 Conversion: Quick Summary', 
            fontsize=22, weight='bold', ha='center', color='darkblue')
    
    # Key points
    points = [
        '1. RGB24: 3 bytes per pixel (Red, Green, Blue each 0-255)',
        '2. RGB565: 2 bytes per pixel, saves 33% memory',
        '3. Bit allocation: Red=5bits, Green=6bits, Blue=5bits',
        '4. Green gets extra bit (human eyes more sensitive)',
        '5. Conversion: Divide by 8 (red/blue) or 4 (green)',
        '6. Quality loss is minimal for most applications'
    ]
    
    for i, point in enumerate(points):
        ax.text(0.5, 8.5 - i*0.8, point, fontsize=14, ha='left', 
                bbox=dict(boxstyle="round,pad=0.3", facecolor="lightblue", alpha=0.3))
    
    # Memory savings visual
    ax.text(5, 4, 'Memory Savings Example:', fontsize=16, weight='bold', ha='center')
    
    # Before
    before_rect = Rectangle((2, 3), 3, 0.5, facecolor='lightcoral', alpha=0.8)
    ax.add_patch(before_rect)
    ax.text(3.5, 3.25, 'Before: 24 bits', ha='center', fontsize=12, weight='bold')
    
    # After
    after_rect = Rectangle((5.5, 3), 2, 0.5, facecolor='lightgreen', alpha=0.8)
    ax.add_patch(after_rect)
    ax.text(6.5, 3.25, 'After: 16 bits', ha='center', fontsize=12, weight='bold')
    
    # Arrow
    ax.annotate('', xy=(5.5, 3.25), xytext=(5, 3.25), 
                arrowprops=dict(arrowstyle='->', lw=3, color='orange'))
    
    ax.text(5, 1.5, 'Perfect for mobile apps, games, and embedded systems!', 
            ha='center', fontsize=14, weight='bold', color='green',
            bbox=dict(boxstyle="round,pad=0.5", facecolor="lightgreen", alpha=0.5))
    
    plt.tight_layout()
    plt.savefig('rgb565_summary.png', dpi=150, bbox_inches='tight')
    plt.show()

def main():
    """Generate all educational plots"""
    print("Creating RGB565 Educational Visualizations...")
    print("This will create 6 different plots explaining the conversion process.")
    
    # Set matplotlib to non-interactive mode for better compatibility
    plt.ion()
    
    print("\n1. Creating introduction to RGB colors...")
    create_introduction_plot()
    
    print("2. Creating memory comparison...")
    create_memory_comparison()
    
    print("3. Creating RGB565 format explanation...")
    create_rgb565_format()
    
    print("4. Creating step-by-step conversion...")
    create_conversion_steps()
    
    print("5. Creating quality comparison...")
    create_quality_comparison()
    
    print("6. Creating summary infographic...")
    create_summary_infographic()
    
    print("\nAll visualizations saved as PNG files!")
    print("Files created:")
    print("- rgb_introduction.png")
    print("- memory_comparison.png") 
    print("- rgb565_format.png")
    print("- conversion_steps.png")
    print("- quality_comparison.png")
    print("- rgb565_summary.png")

if __name__ == "__main__":
    main()