#!/usr/bin/env python3
"""
Interactive RGB to RGB565 Conversion Demo
Simple tool for students to experiment with color conversion

This allows students to:
1. Input RGB values and see the conversion step-by-step
2. Visualize the color before and after conversion
3. Understand the bit-level operations
4. See the quality difference
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle

def rgb_to_rgb565(r, g, b):
    """Convert RGB24 to RGB565 format"""
    # Reduce precision by keeping only the top bits
    r5 = r >> 3  # Keep top 5 bits (divide by 8)
    g6 = g >> 2  # Keep top 6 bits (divide by 4)
    b5 = b >> 3  # Keep top 5 bits (divide by 8)
    
    # Pack into 16-bit value
    rgb565 = (r5 << 11) | (g6 << 5) | b5
    
    return rgb565, r5, g6, b5

def rgb565_to_rgb(rgb565):
    """Convert RGB565 back to RGB24 format"""
    # Extract components using bit masks
    r5 = (rgb565 >> 11) & 0x1F  # Extract red (bits 15-11)
    g6 = (rgb565 >> 5) & 0x3F   # Extract green (bits 10-5)
    b5 = rgb565 & 0x1F          # Extract blue (bits 4-0)
    
    # Expand to 8-bit values
    r8 = (r5 << 3) | (r5 >> 2)  # Expand 5 bits to 8 bits
    g8 = (g6 << 2) | (g6 >> 4)  # Expand 6 bits to 8 bits
    b8 = (b5 << 3) | (b5 >> 2)  # Expand 5 bits to 8 bits
    
    return min(255, r8), min(255, g8), min(255, b8)

def demonstrate_conversion(r, g, b):
    """Demonstrate the conversion process with detailed explanation"""
    print(f"\n{'='*60}")
    print(f"RGB to RGB565 Conversion Demo")
    print(f"{'='*60}")
    print(f"Original Color: RGB({r}, {g}, {b})")
    
    # Step 1: Convert to RGB565
    rgb565, r5, g6, b5 = rgb_to_rgb565(r, g, b)
    
    print(f"\nStep 1: Reduce bit precision")
    print(f"  Red:   {r:3d} ÷ 8 = {r5:2d} (keep top 5 bits)")
    print(f"  Green: {g:3d} ÷ 4 = {g6:2d} (keep top 6 bits)")
    print(f"  Blue:  {b:3d} ÷ 8 = {b5:2d} (keep top 5 bits)")
    
    print(f"\nStep 2: Pack into 16-bit value")
    print(f"  Formula: ({r5} << 11) | ({g6} << 5) | {b5}")
    print(f"  Binary:  {r5:05b} {g6:06b} {b5:05b}")
    print(f"  Result:  {rgb565} (decimal) or 0x{rgb565:04X} (hex)")
    
    # Step 3: Convert back
    r_back, g_back, b_back = rgb565_to_rgb(rgb565)
    
    print(f"\nStep 3: Convert back to RGB24")
    print(f"  Expanded: RGB({r_back}, {g_back}, {b_back})")
    
    # Show quality loss
    r_loss = abs(r - r_back)
    g_loss = abs(g - g_back)  
    b_loss = abs(b - b_back)
    total_loss = r_loss + g_loss + b_loss
    
    print(f"\nQuality Analysis:")
    print(f"  Red loss:   {r_loss:3d} ({100*r_loss/255:.1f}%)")
    print(f"  Green loss: {g_loss:3d} ({100*g_loss/255:.1f}%)")
    print(f"  Blue loss:  {b_loss:3d} ({100*b_loss/255:.1f}%)")
    print(f"  Total loss: {total_loss:3d} ({100*total_loss/(3*255):.1f}%)")
    
    return (r, g, b), (r_back, g_back, b_back)

def visualize_colors(original, converted):
    """Create a visual comparison of the colors"""
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.axis('off')
    
    # Title
    ax.text(5, 5.5, 'Color Comparison: Original vs RGB565', 
            fontsize=16, weight='bold', ha='center')
    
    # Original color
    orig_rect = Rectangle((2, 3), 2, 1.5, facecolor=np.array(original)/255)
    ax.add_patch(orig_rect)
    ax.text(3, 2.5, f'Original\nRGB{original}', 
            ha='center', fontsize=12, weight='bold',
            bbox=dict(boxstyle="round,pad=0.3", facecolor="white", alpha=0.8))
    
    # Converted color 
    conv_rect = Rectangle((6, 3), 2, 1.5, facecolor=np.array(converted)/255)
    ax.add_patch(conv_rect)
    ax.text(7, 2.5, f'RGB565\nRGB{converted}', 
            ha='center', fontsize=12, weight='bold',
            bbox=dict(boxstyle="round,pad=0.3", facecolor="white", alpha=0.8))
            
    # Arrow
    ax.annotate('', xy=(6, 3.75), xytext=(4, 3.75), 
                arrowprops=dict(arrowstyle='->', lw=3, color='black'))
    ax.text(5, 4.2, 'Convert', ha='center', fontsize=10, weight='bold')
    
    # Show difference
    r_diff = abs(original[0] - converted[0])
    g_diff = abs(original[1] - converted[1])
    b_diff = abs(original[2] - converted[2])
    
    ax.text(5, 1.5, f'Differences: R={r_diff}, G={g_diff}, B={b_diff}', 
            ha='center', fontsize=12, 
            bbox=dict(boxstyle="round,pad=0.3", facecolor="lightyellow"))
    
    plt.tight_layout()
    plt.savefig('color_comparison_demo.png', dpi=150, bbox_inches='tight')
    plt.show()

def interactive_demo():
    """Run an interactive demo session"""
    print("🎨 RGB to RGB565 Interactive Conversion Demo 🎨")
    print("\nThis tool helps you understand how RGB colors are compressed.")
    print("You can input RGB values and see exactly what happens!")
    
    while True:
        print(f"\n{'='*60}")
        try:
            # Get input from user
            print("Enter RGB values (0-255) or 'quit' to exit:")
            user_input = input("Format: R G B (e.g., '255 128 64'): ").strip()
            
            if user_input.lower() in ['quit', 'exit', 'q']:
                print("Thanks for using the RGB565 demo! 👋")
                break
                
            # Parse input
            if user_input.lower() == 'random':
                r, g, b = np.random.randint(0, 256, 3)
                print(f"Random color generated: RGB({r}, {g}, {b})")
            else:
                rgb_values = list(map(int, user_input.split()))
                if len(rgb_values) != 3:
                    print("❌ Please enter exactly 3 numbers!")
                    continue
                r, g, b = rgb_values
                
            # Validate range
            if not all(0 <= val <= 255 for val in [r, g, b]):
                print("❌ RGB values must be between 0 and 255!")
                continue
            
            # Demonstrate conversion
            original, converted = demonstrate_conversion(r, g, b)
            
            # Ask if user wants to see visual comparison
            show_visual = input("\nShow visual comparison? (y/n): ").lower().startswith('y')
            if show_visual:
                visualize_colors(original, converted)
                
        except ValueError:
            print("❌ Invalid input! Please enter numbers only.")
        except KeyboardInterrupt:
            print("\n\nThanks for using the RGB565 demo! 👋")
            break
        except Exception as e:
            print(f"❌ An error occurred: {e}")

def run_example_demos():
    """Run some predefined examples"""
    print("🌟 Running Example Demonstrations 🌟\n")
    
    examples = [
        (255, 0, 0),     # Pure red
        (0, 255, 0),     # Pure green  
        (0, 0, 255),     # Pure blue
        (255, 255, 255), # White
        (128, 128, 128), # Gray
        (255, 128, 64),  # Orange (from assignment)
        (64, 128, 255),  # Sky blue
        (255, 192, 203), # Pink
    ]
    
    print("Here are some example conversions:")
    
    for r, g, b in examples:
        original, converted = demonstrate_conversion(r, g, b)
        input("Press Enter to continue to next example...")

def main():
    """Main function to run the demo"""
    print("Welcome to the RGB565 Conversion Learning Tool!")
    print("\nThis interactive demo will help you understand:")
    print("• How RGB colors work")
    print("• Why we compress colors")
    print("• How RGB565 compression works")
    print("• The step-by-step conversion process")
    print("• Quality differences between original and compressed")
    
    while True:
        print(f"\n{'='*60}")
        print("Choose an option:")
        print("1. Interactive demo (enter your own colors)")
        print("2. See example conversions")
        print("3. Quit")
        
        choice = input("Your choice (1-3): ").strip()
        
        if choice == '1':
            interactive_demo()
        elif choice == '2':
            run_example_demos()
        elif choice == '3':
            print("Thanks for learning about RGB565! 🎨✨")
            break
        else:
            print("❌ Invalid choice! Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()