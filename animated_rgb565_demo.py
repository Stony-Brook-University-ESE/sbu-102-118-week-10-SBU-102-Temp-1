#!/usr/bin/env python3
"""
Simple RGB to RGB565 Animated Demonstration
Creates a step-by-step animated explanation using matplotlib

This creates a simple animation showing:
1. RGB color input
2. Bit reduction process
3. Packing process
4. Quality comparison
"""

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from matplotlib.patches import Rectangle
import time

class RGB565AnimationDemo:
    def __init__(self):
        self.fig, self.ax = plt.subplots(figsize=(12, 8))
        self.ax.set_xlim(0, 10)
        self.ax.set_ylim(0, 8)
        self.ax.axis('off')
        
        # Example color to demonstrate
        self.original_rgb = [255, 128, 64]  # Orange from the assignment
        
        # Animation steps
        self.steps = [
            self.show_title,
            self.show_original_color,
            self.explain_rgb_concept,
            self.show_memory_problem,
            self.introduce_rgb565,
            self.show_bit_reduction,
            self.show_packing,
            self.show_final_comparison,
            self.show_summary
        ]
        self.current_step = 0
        
    def clear_screen(self):
        """Clear the screen for next step"""
        self.ax.clear()
        self.ax.set_xlim(0, 10)
        self.ax.set_ylim(0, 8)
        self.ax.axis('off')
    
    def show_title(self):
        """Show animated title"""
        self.clear_screen()
        
        # Main title
        title = self.ax.text(5, 6, 'RGB → RGB565', fontsize=48, weight='bold', 
                           ha='center', color='darkblue', alpha=0)
        subtitle = self.ax.text(5, 5, 'Color Compression Explained', fontsize=24, 
                              ha='center', color='gray', alpha=0)
        subtitle2 = self.ax.text(5, 4, 'For Beginners', fontsize=18, 
                               ha='center', color='green', alpha=0)
        
        # Fade in effect (simulated)
        for alpha in np.linspace(0, 1, 20):
            title.set_alpha(alpha)
            subtitle.set_alpha(alpha) 
            subtitle2.set_alpha(alpha)
            plt.pause(0.1)
        
        plt.pause(2)
    
    def show_original_color(self):
        """Show the original RGB color"""
        self.clear_screen()
        
        title = self.ax.text(5, 7.5, 'Starting with a color...', fontsize=24, 
                           weight='bold', ha='center', color='darkblue')
        
        # Show original color square
        r, g, b = self.original_rgb
        color_rect = Rectangle((4, 4), 2, 2, facecolor=np.array([r, g, b])/255)
        self.ax.add_patch(color_rect)
        
        # RGB values
        rgb_text = self.ax.text(5, 3, f'RGB({r}, {g}, {b})', fontsize=20, 
                              weight='bold', ha='center')
        
        # Explain each component with color coding
        plt.pause(1)
        red_text = self.ax.text(5, 2.2, f'Red: {r} (8 bits)', fontsize=16, 
                              ha='center', color='red')
        plt.pause(0.5)
        green_text = self.ax.text(5, 1.8, f'Green: {g} (8 bits)', fontsize=16, 
                                ha='center', color='green')
        plt.pause(0.5)
        blue_text = self.ax.text(5, 1.4, f'Blue: {b} (8 bits)', fontsize=16, 
                               ha='center', color='blue')
        plt.pause(0.5)
        
        total_text = self.ax.text(5, 0.8, 'Total: 24 bits per pixel', fontsize=16, 
                                weight='bold', ha='center', color='purple')
        plt.pause(2)
    
    def explain_rgb_concept(self):
        """Explain RGB concept with visual mixing"""
        self.clear_screen()
        
        title = self.ax.text(5, 7.5, 'How RGB Colors Work', fontsize=24, 
                           weight='bold', ha='center', color='darkblue')
        
        # Show individual color channels
        r, g, b = self.original_rgb
        
        # Red channel
        red_rect = Rectangle((1.5, 5), 1.5, 1.5, facecolor=[r/255, 0, 0])
        self.ax.add_patch(red_rect)
        self.ax.text(2.25, 4.3, f'Red\n{r}', ha='center', fontsize=12, weight='bold')
        plt.pause(0.8)
        
        # Green channel
        green_rect = Rectangle((4.25, 5), 1.5, 1.5, facecolor=[0, g/255, 0])
        self.ax.add_patch(green_rect)
        self.ax.text(5, 4.3, f'Green\n{g}', ha='center', fontsize=12, weight='bold')
        plt.pause(0.8)
        
        # Blue channel
        blue_rect = Rectangle((7, 5), 1.5, 1.5, facecolor=[0, 0, b/255])
        self.ax.add_patch(blue_rect)
        self.ax.text(7.75, 4.3, f'Blue\n{b}', ha='center', fontsize=12, weight='bold')
        plt.pause(0.8)
        
        # Plus signs
        self.ax.text(3.5, 5.75, '+', fontsize=24, weight='bold', ha='center')
        self.ax.text(6.1, 5.75, '+', fontsize=24, weight='bold', ha='center')
        
        # Equals sign and result
        self.ax.text(5, 3.5, '=', fontsize=24, weight='bold', ha='center')
        
        # Combined result
        combined_rect = Rectangle((4.25, 2), 1.5, 1.5, facecolor=np.array([r, g, b])/255)
        self.ax.add_patch(combined_rect)
        self.ax.text(5, 1.3, f'Combined\nRGB({r},{g},{b})', ha='center', 
                   fontsize=12, weight='bold')
        plt.pause(2)
    
    def show_memory_problem(self):
        """Show why memory usage is a problem"""
        self.clear_screen()
        
        title = self.ax.text(5, 7.5, 'The Memory Problem', fontsize=24, 
                           weight='bold', ha='center', color='red')
        
        # Show phone screen
        self.ax.text(5, 6.5, 'Modern phone: 1920 × 1080 screen', fontsize=16, 
                   ha='center')
        
        # Memory calculation animation
        calc_steps = [
            '1920 × 1080 = 2,073,600 pixels',
            '2,073,600 × 3 bytes = 6.2 MB per frame',
            '6.2 MB × 60 FPS = 372 MB per second!',
            'Too much for mobile devices! 😱'
        ]
        
        for i, step in enumerate(calc_steps):
            color = 'red' if i == len(calc_steps)-1 else 'black'
            text = self.ax.text(5, 5.5 - i*0.6, step, fontsize=14, 
                              ha='center', color=color)
            if i == len(calc_steps)-1:
                text.set_weight('bold')
            plt.pause(1.5)
        
        # Solution hint
        solution = self.ax.text(5, 1.5, 'Solution: Compress the colors!', 
                              fontsize=18, weight='bold', ha='center', color='green')
        plt.pause(2)
    
    def introduce_rgb565(self):
        """Introduce RGB565 format"""
        self.clear_screen()
        
        title = self.ax.text(5, 7.5, 'Introducing RGB565', fontsize=24, 
                           weight='bold', ha='center', color='green')
        
        # Show bit allocation
        self.ax.text(5, 6.5, '16 bits total, allocated as:', fontsize=16, ha='center')
        
        # Draw bit boxes with animation
        bit_width = 0.25
        start_x = 3
        
        # Red bits (5 bits)
        plt.pause(0.5)
        self.ax.text(2, 5.5, 'Red: 5 bits', fontsize=14, weight='bold', color='red')
        for i in range(5):
            rect = Rectangle((start_x + i*bit_width, 4.5), bit_width, bit_width, 
                           facecolor='red', alpha=0.7, edgecolor='black')
            self.ax.add_patch(rect)
            plt.pause(0.2)
        
        # Green bits (6 bits)
        plt.pause(0.5)
        green_start = start_x + 5*bit_width + 0.1
        self.ax.text(4.5, 5.5, 'Green: 6 bits', fontsize=14, weight='bold', color='green')
        for i in range(6):
            rect = Rectangle((green_start + i*bit_width, 4.5), bit_width, bit_width, 
                           facecolor='green', alpha=0.7, edgecolor='black')
            self.ax.add_patch(rect)
            plt.pause(0.2)
        
        # Blue bits (5 bits)
        plt.pause(0.5)
        blue_start = green_start + 6*bit_width + 0.1
        self.ax.text(7.5, 5.5, 'Blue: 5 bits', fontsize=14, weight='bold', color='blue')
        for i in range(5):
            rect = Rectangle((blue_start + i*bit_width, 4.5), bit_width, bit_width, 
                           facecolor='blue', alpha=0.7, edgecolor='black')
            self.ax.add_patch(rect)
            plt.pause(0.2)
        
        # Explanation
        plt.pause(1)
        self.ax.text(5, 3.5, 'Why 6 bits for green?', fontsize=16, 
                   weight='bold', ha='center', color='purple')
        plt.pause(1)
        self.ax.text(5, 3, 'Human eyes are most sensitive to green light!', 
                   fontsize=14, ha='center', color='green')
        plt.pause(2)
    
    def show_bit_reduction(self):
        """Show the bit reduction process"""
        self.clear_screen()
        
        title = self.ax.text(5, 7.5, 'Step 1: Reduce Bit Precision', fontsize=20, 
                           weight='bold', ha='center', color='darkblue')
        
        r, g, b = self.original_rgb
        
        # Show original values 
        self.ax.text(5, 6.5, f'Original: RGB({r}, {g}, {b})', fontsize=16, 
                   ha='center', weight='bold')
        
        # Animated reduction
        reductions = [
            (f'Red: {r} ÷ 8 = {r//8}', 'red', r, r//8),
            (f'Green: {g} ÷ 4 = {g//4}', 'green', g, g//4), 
            (f'Blue: {b} ÷ 8 = {b//8}', 'blue', b, b//8)
        ]
        
        for i, (text, color, original, reduced) in enumerate(reductions):
            y_pos = 5.5 - i*0.8
            
            # Show calculation
            calc_text = self.ax.text(5, y_pos, text, fontsize=14, ha='center', color=color)
            plt.pause(1)
            
            # Show what this means
            meaning = f'Keep top {"5" if color != "green" else "6"} bits, discard lower {"3" if color != "green" else "2"}'
            self.ax.text(5, y_pos - 0.3, meaning, fontsize=10, ha='center', 
                       style='italic', color='gray')
            plt.pause(1)
        
        # Show final reduced values
        r5, g6, b5 = r//8, g//4, b//8
        final_text = self.ax.text(5, 1.5, f'Reduced: R={r5}, G={g6}, B={b5}', 
                                fontsize=16, weight='bold', ha='center', 
                                bbox=dict(boxstyle="round,pad=0.5", facecolor="lightyellow"))
        plt.pause(2)
    
    def show_packing(self):
        """Show the bit packing process"""
        self.clear_screen()
        
        title = self.ax.text(5, 7.5, 'Step 2: Pack into 16-bit Value', fontsize=20, 
                           weight='bold', ha='center', color='darkblue')
        
        r, g, b = self.original_rgb
        r5, g6, b5 = r//8, g//4, b//8
        
        # Show the formula
        formula = f'({r5} << 11) | ({g6} << 5) | {b5}'
        self.ax.text(5, 6.2, f'Formula: {formula}', fontsize=16, ha='center', weight='bold')
        plt.pause(1)
        
        # Show bit positions
        bit_width = 0.2
        start_x = 2
        
        # Red bits in positions 15-11
        self.ax.text(1, 5, 'Red (15-11):', fontsize=12, weight='bold', color='red')
        for i in range(5):
            rect = Rectangle((start_x + i*bit_width, 4.5), bit_width, bit_width, 
                           facecolor='red', alpha=0.7, edgecolor='black')
            self.ax.add_patch(rect)
            self.ax.text(start_x + i*bit_width + bit_width/2, 4.7, str((r5 >> (4-i)) & 1), 
                       ha='center', va='center', fontsize=8, weight='bold')
        plt.pause(1)
        
        # Green bits in positions 10-5
        green_start = start_x + 5*bit_width + 0.1
        self.ax.text(1, 4, 'Green (10-5):', fontsize=12, weight='bold', color='green')
        for i in range(6):
            rect = Rectangle((green_start + i*bit_width, 4.5), bit_width, bit_width, 
                           facecolor='green', alpha=0.7, edgecolor='black')
            self.ax.add_patch(rect)
            self.ax.text(green_start + i*bit_width + bit_width/2, 4.7, str((g6 >> (5-i)) & 1), 
                       ha='center', va='center', fontsize=8, weight='bold')
        plt.pause(1)
        
        # Blue bits in positions 4-0
        blue_start = green_start + 6*bit_width + 0.1
        self.ax.text(1, 3, 'Blue (4-0):', fontsize=12, weight='bold', color='blue')
        for i in range(5):
            rect = Rectangle((blue_start + i*bit_width, 4.5), bit_width, bit_width, 
                           facecolor='blue', alpha=0.7, edgecolor='black')
            self.ax.add_patch(rect)
            self.ax.text(blue_start + i*bit_width + bit_width/2, 4.7, str((b5 >> (4-i)) & 1), 
                       ha='center', va='center', fontsize=8, weight='bold')
        plt.pause(1)
        
        # Calculate final value
        rgb565 = (r5 << 11) | (g6 << 5) | b5
        result_text = self.ax.text(5, 2, f'Result: {rgb565} (0x{rgb565:04X})', 
                                 fontsize=16, weight='bold', ha='center',
                                 bbox=dict(boxstyle="round,pad=0.5", facecolor="lightgreen"))
        plt.pause(2)
    
    def show_final_comparison(self):
        """Show before and after comparison"""
        self.clear_screen()
        
        title = self.ax.text(5, 7.5, 'Before vs After Comparison', fontsize=20, 
                           weight='bold', ha='center', color='darkblue')
        
        r, g, b = self.original_rgb
        
        # Convert to RGB565 and back
        r5, g6, b5 = r//8, g//4, b//8
        r_back = (r5 << 3) | (r5 >> 2)
        g_back = (g6 << 2) | (g6 >> 4)  
        b_back = (b5 << 3) | (b5 >> 2)
        
        # Clamp values
        r_back = min(255, r_back)
        g_back = min(255, g_back)
        b_back = min(255, b_back)
        
        # Original color
        orig_rect = Rectangle((2, 4), 2, 1.5, facecolor=np.array([r, g, b])/255)
        self.ax.add_patch(orig_rect)
        self.ax.text(3, 3.3, f'Original\n24-bit\nRGB({r},{g},{b})', 
                   ha='center', fontsize=10, weight='bold')
        plt.pause(1)
        
        # Converted color
        conv_rect = Rectangle((6, 4), 2, 1.5, facecolor=np.array([r_back, g_back, b_back])/255)
        self.ax.add_patch(conv_rect)
        self.ax.text(7, 3.3, f'RGB565\n16-bit\nRGB({r_back},{g_back},{b_back})', 
                   ha='center', fontsize=10, weight='bold')
        plt.pause(1)
        
        # Arrow between them
        self.ax.annotate('', xy=(6, 4.75), xytext=(4, 4.75), 
                        arrowprops=dict(arrowstyle='->', lw=3, color='orange'))
        
        # Show differences
        r_diff = abs(r - r_back)
        g_diff = abs(g - g_back)
        b_diff = abs(b - b_back)
        
        self.ax.text(5, 2.5, f'Differences: R±{r_diff}, G±{g_diff}, B±{b_diff}', 
                   ha='center', fontsize=12, weight='bold')
        
        if r_diff + g_diff + b_diff < 10:
            quality_text = 'Excellent quality! 😊'
            color = 'green'
        elif r_diff + g_diff + b_diff < 30:
            quality_text = 'Good quality! 👍'
            color = 'orange'
        else:
            quality_text = 'Noticeable difference'
            color = 'red'
            
        self.ax.text(5, 2, quality_text, ha='center', fontsize=14, 
                   weight='bold', color=color)
        plt.pause(3)
    
    def show_summary(self):
        """Show final summary"""
        self.clear_screen()
        
        title = self.ax.text(5, 7.5, '🎉 RGB565 Conversion Complete! 🎉', 
                           fontsize=18, weight='bold', ha='center', color='green')
        
        summary_points = [
            '✅ Reduced from 24 bits to 16 bits (33% savings)',
            '✅ Maintained good visual quality',
            '✅ Perfect for mobile and embedded devices',
            '✅ Widely used in games and apps',
            '',
            '🧠 Key takeaway: Smart compression saves memory',
            '   while keeping colors looking great!'
        ]
        
        for i, point in enumerate(summary_points):
            if point:  # Skip empty lines
                y_pos = 6.2 - i*0.4
                text_color = 'green' if '✅' in point else 'blue' if '🧠' in point else 'black'
                weight = 'bold' if '🧠' in point else 'normal'
                
                self.ax.text(5, y_pos, point, fontsize=12, ha='center', 
                           color=text_color, weight=weight)
                plt.pause(0.8)
        
        plt.pause(3)
    
    def run_animation(self):
        """Run the complete animation sequence"""
        print("🎬 Starting RGB565 Animation Demo...")
        print("Close the plot window to continue to the next step.")
        print("Press Ctrl+C to stop the animation.\n")
        
        try:
            for i, step_function in enumerate(self.steps):
                print(f"Step {i+1}/{len(self.steps)}: {step_function.__name__.replace('_', ' ').title()}")
                step_function()
                
                if i < len(self.steps) - 1:  # Don't wait after last step
                    input("Press Enter to continue to next step...")
                    
            print("\n🎉 Animation complete!")
            print("The RGB565 conversion process explanation is finished.")
            input("Press Enter to close...")
            
        except KeyboardInterrupt:
            print("\n\nAnimation stopped by user.")
        finally:
            plt.close()

def main():
    """Main function to run the animation demo"""
    print("🎨 RGB565 Animated Explanation 🎨")
    print("\nThis animation will walk you through:")
    print("• What RGB colors are") 
    print("• Why compression is needed")
    print("• How RGB565 works")
    print("• The step-by-step conversion process")
    print("• Quality comparison")
    
    print(f"\n{'='*50}")
    input("Press Enter to start the animation...")
    
    demo = RGB565AnimationDemo()
    demo.run_animation()

if __name__ == "__main__":
    main()