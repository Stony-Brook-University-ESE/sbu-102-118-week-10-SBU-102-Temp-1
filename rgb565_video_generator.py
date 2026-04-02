#!/usr/bin/env python3
"""
RGB to RGB565 Video Generator
Creates an educational video explaining color compression for non-CS students

This script generates a complete video showing:
1. Introduction to RGB colors
2. Memory usage problems  
3. RGB565 format explanation
4. Step-by-step conversion process
5. Quality comparison
6. Summary and applications

Output: rgb565_explanation.mp4 video file
"""

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from matplotlib.patches import Rectangle
import matplotlib.patches as mpatches

class RGB565VideoGenerator:
    def __init__(self):
        # Set up the figure and axis
        self.fig, self.ax = plt.subplots(figsize=(16, 9))  # 16:9 aspect ratio for video
        self.ax.set_facecolor('#f8f9fa')  # Light background
        
        # Example color for demonstration
        self.example_rgb = [255, 128, 64]  # Orange from assignment
        
        # Video timing (frames per second and durations)
        self.fps = 30
        self.scene_durations = {
            'intro': 6.0,            # 6 seconds intro - enough time to read title and context
            'rgb_explanation': 10.0, # 10 seconds RGB concept - complex visual explanation
            'memory_problem': 8.0,   # 8 seconds memory issues - important motivation
            'rgb565_intro': 10.0,    # 10 seconds RGB565 format - key concept explanation
            'conversion': 12.0,      # 12 seconds step-by-step - most complex content
            'packing': 10.0,         # 10 seconds bit packing - detailed bit manipulation
            'comparison': 8.0,       # 8 seconds quality comparison - analysis time
            'summary': 6.0           # 6 seconds summary - applications and wrap-up
        }
        
        # Calculate total frames for each scene
        self.scene_frames = {k: int(v * self.fps) for k, v in self.scene_durations.items()}
        self.total_frames = sum(self.scene_frames.values())
        
        # Current frame tracking
        self.current_frame = 0
        self.current_scene = 'intro'
        
    def clear_and_setup(self, title="", title_color='darkblue'):
        """Clear axis and set up for new scene"""
        self.ax.clear()
        self.ax.set_xlim(0, 16)
        self.ax.set_ylim(0, 9)
        self.ax.set_facecolor('#f8f9fa')
        self.ax.axis('off')
        
        if title:
            self.ax.text(8, 8.2, title, fontsize=32, weight='bold', 
                        ha='center', color=title_color)
    
    def get_scene_progress(self, scene_name):
        """Get progress (0-1) within current scene"""
        scene_start = sum(self.scene_frames[s] for s in list(self.scene_frames.keys())[:list(self.scene_frames.keys()).index(scene_name)])
        scene_frame = self.current_frame - scene_start
        return min(1.0, scene_frame / self.scene_frames[scene_name])
    
    def smooth_transition(self, progress, delay=0.1):
        """No fade transition - elements appear immediately when their time comes"""
        if progress <= delay:
            return 0
        return 1.0  # Full opacity immediately, no fade
    
    def animate_intro(self):
        """Animated introduction scene"""
        self.clear_and_setup()
        progress = self.get_scene_progress('intro')
        
        # Main title - appears immediately
        if progress > 0.0:
            self.ax.text(8, 6.5, 'RGB → RGB565', fontsize=52, weight='bold', 
                        ha='center', color='darkblue', alpha=1.0)
        
        # Subtitle - appears early and stays
        if progress > 0.15:
            self.ax.text(8, 5.5, 'Color Compression Explained', fontsize=28, 
                        ha='center', color='gray', alpha=1.0)
        
        # For beginners - appears early and stays  
        if progress > 0.3:
            self.ax.text(8, 4.8, 'A Visual Guide for Beginners', fontsize=20, 
                        ha='center', color='green', alpha=1.0)
        
        # Decorative color squares - appear early and stay
        if progress > 0.4:
            colors = ['red', 'green', 'blue']
        # Decorative color squares - appear early and stay
        if progress > 0.4:
            colors = ['red', 'green', 'blue']
            positions = [5.5, 8, 10.5]
            
            for i, (color, x) in enumerate(zip(colors, positions)):
                rect = Rectangle((x-0.5, 3), 1, 1, facecolor=color, alpha=0.7)
                self.ax.add_patch(rect)

    def animate_rgb_explanation(self):
        """Explain RGB color concept"""
        self.clear_and_setup("What are Colors on Computers?")
        progress = self.get_scene_progress('rgb_explanation')
        
        # RGB concept text - appears immediately
        if progress > 0.05:
            self.ax.text(8, 7.2, 'Every pixel is made of three colors:', fontsize=22, 
                        ha='center', alpha=1.0)
        
        # RGB squares with staggered appearance but no fade
        r, g, b = self.example_rgb
        colors = [[r, 0, 0], [0, g, 0], [0, 0, b]]
        labels = [f'Red\n{r}', f'Green\n{g}', f'Blue\n{b}']
        positions = [4, 8, 12]
        
        # Red square - appears early
        if progress > 0.15:
            rect = Rectangle((4-1, 5), 2, 2, facecolor=np.array([r, 0, 0])/255, alpha=1.0)
            self.ax.add_patch(rect)
            self.ax.text(4, 4.3, labels[0], ha='center', fontsize=16, weight='bold', alpha=1.0)
            self.ax.text(4, 3.9, '0-255\n(8 bits)', ha='center', fontsize=12, alpha=1.0, style='italic')
        
        # Green square  
        if progress > 0.25:
            rect = Rectangle((8-1, 5), 2, 2, facecolor=np.array([0, g, 0])/255, alpha=1.0)
            self.ax.add_patch(rect)
            self.ax.text(8, 4.3, labels[1], ha='center', fontsize=16, weight='bold', alpha=1.0)
            self.ax.text(8, 3.9, '0-255\n(8 bits)', ha='center', fontsize=12, alpha=1.0, style='italic')
        
        # Blue square
        if progress > 0.35:
            rect = Rectangle((12-1, 5), 2, 2, facecolor=np.array([0, 0, b])/255, alpha=1.0)
            self.ax.add_patch(rect)
            self.ax.text(12, 4.3, labels[2], ha='center', fontsize=16, weight='bold', alpha=1.0)
            self.ax.text(12, 3.9, '0-255\n(8 bits)', ha='center', fontsize=12, alpha=1.0, style='italic')
        
        # Plus signs and equals - appear early for more reading time
        if progress > 0.4:
            self.ax.text(6, 6, '+', fontsize=32, weight='bold', ha='center', alpha=1.0)
            self.ax.text(10, 6, '+', fontsize=32, weight='bold', ha='center', alpha=1.0)
            self.ax.text(8, 4, '=', fontsize=32, weight='bold', ha='center', alpha=1.0)
        
        # Final combined color - appears early and stays long
        if progress > 0.5:
            combined_rect = Rectangle((7, 2), 2, 1.5, facecolor=np.array([r, g, b])/255, alpha=1.0)
            self.ax.add_patch(combined_rect)
            self.ax.text(8, 1.3, f'Combined Color\nRGB({r}, {g}, {b})', 
                        ha='center', fontsize=14, weight='bold', alpha=1.0)
            
        # Total bits info - KEY MESSAGE appears early and stays long for reading
        if progress > 0.6:
            self.ax.text(8, 0.5, 'Total: 24 bits (3 bytes) per pixel', 
                        ha='center', fontsize=18, weight='bold', color='purple', alpha=1.0)

    def animate_memory_problem(self):
        """Show memory usage problems"""
        self.clear_and_setup("The Memory Problem", 'red')
        progress = self.get_scene_progress('memory_problem')
        
        # Phone screen example - appears immediately
        if progress > 0.05:
            self.ax.text(8, 7, 'Modern Phone Screen: 1920 × 1080 pixels', 
                        fontsize=20, ha='center', alpha=1.0)
        
        # Memory calculation steps - appear quickly in sequence
        calc_steps = [
            '1920 × 1080 = 2,073,600 pixels',
            '2,073,600 × 3 bytes = 6.2 MB per frame',
            '6.2 MB × 60 FPS = 372 MB per second!',
            'WAY TOO MUCH! 😱'
        ]
        
        # Show calculation steps with earlier timing
        if progress > 0.15:
            self.ax.text(8, 6, calc_steps[0], fontsize=18, ha='center', alpha=1.0)
        if progress > 0.25:
            self.ax.text(8, 5.3, calc_steps[1], fontsize=18, ha='center', alpha=1.0)
        if progress > 0.35:
            self.ax.text(8, 4.6, calc_steps[2], fontsize=18, ha='center', alpha=1.0)
        if progress > 0.45:
            self.ax.text(8, 3.9, calc_steps[3], fontsize=24, ha='center', 
                        color='red', weight='bold', alpha=1.0)
        
        # Memory bars comparison - appear early for more reading time
        if progress > 0.55:
            # 24-bit bar
            large_rect = Rectangle((2, 2), 6, 0.8, facecolor='red', alpha=0.7)
            self.ax.add_patch(large_rect)
            self.ax.text(5, 2.4, '24-bit RGB: HUGE', ha='center', fontsize=14, 
                        weight='bold', alpha=1.0)
            
            # 16-bit bar
            small_rect = Rectangle((10, 2), 4, 0.8, facecolor='green', alpha=0.7)
            self.ax.add_patch(small_rect)
            self.ax.text(12, 2.4, '16-bit: Better!', ha='center', fontsize=14, 
                        weight='bold', alpha=1.0)
        
        # Solution - KEY MESSAGE appears early and stays long for reading
        if progress > 0.65:
            self.ax.text(8, 0.8, 'Solution: Compress the colors!', 
                        fontsize=20, weight='bold', ha='center', color='green', alpha=1.0)

    def animate_rgb565_intro(self):
        """Introduction to RGB565 format"""
        self.clear_and_setup("RGB565: Smart Compression", 'green')
        progress = self.get_scene_progress('rgb565_intro')
        
        # Introduction text - appears immediately
        if progress > 0.05:
            self.ax.text(8, 7.2, '16 bits total, cleverly allocated:', 
                        fontsize=20, ha='center', alpha=1.0)
        
        # Bit allocation with early timing for more reading time
        bit_width = 0.4
        start_x = 3
        
        # Red bits (5 bits) - appears early
        if progress > 0.15:
            self.ax.text(2, 6, 'Red: 5 bits', fontsize=16, weight='bold', 
                        color='red', alpha=1.0)
            for i in range(5):
                rect = Rectangle((start_x + i*bit_width, 5.5), bit_width*0.9, bit_width, 
                               facecolor='red', alpha=0.7, edgecolor='black')
                self.ax.add_patch(rect)
                self.ax.text(start_x + i*bit_width + bit_width*0.45, 5.7, 
                           str(15-i), ha='center', va='center', fontsize=10, 
                           weight='bold', alpha=1.0)
        
        # Green bits (6 bits) - appears early  
        if progress > 0.25:
            green_start = start_x + 5*bit_width + 0.2
            self.ax.text(8, 6, 'Green: 6 bits', fontsize=16, weight='bold', 
                        color='green', alpha=1.0)
            for i in range(6):
                rect = Rectangle((green_start + i*bit_width, 5.5), bit_width*0.9, bit_width, 
                               facecolor='green', alpha=0.7, edgecolor='black')
                self.ax.add_patch(rect)
                self.ax.text(green_start + i*bit_width + bit_width*0.45, 5.7, 
                           str(10-i), ha='center', va='center', fontsize=10, 
                           weight='bold', alpha=1.0)
        
        # Blue bits (5 bits) - appears early
        if progress > 0.35:
            blue_start = green_start + 6*bit_width + 0.2
            self.ax.text(14, 6, 'Blue: 5 bits', fontsize=16, weight='bold', 
                        color='blue', alpha=1.0)
            for i in range(5):
                rect = Rectangle((blue_start + i*bit_width, 5.5), bit_width*0.9, bit_width, 
                               facecolor='blue', alpha=0.7, edgecolor='black')
                self.ax.add_patch(rect)
                self.ax.text(blue_start + i*bit_width + bit_width*0.45, 5.7, 
                           str(4-i), ha='center', va='center', fontsize=10, 
                           weight='bold', alpha=1.0)
        
        # Why this allocation? - appears early for reading time
        if progress > 0.45:
            self.ax.text(8, 4, 'Why 6 bits for green?', fontsize=18, 
                        weight='bold', ha='center', color='purple', alpha=1.0)
            self.ax.text(8, 3.4, 'Human eyes are most sensitive to green light!', 
                        fontsize=16, ha='center', color='green', alpha=1.0)
        
        # Memory savings - KEY MESSAGE appears early and stays long for reading  
        if progress > 0.55:
            self.ax.text(8, 2.5, 'Memory savings: 24 bits → 16 bits = 33% reduction!', 
                        fontsize=16, weight='bold', ha='center', color='orange', alpha=1.0)

    def animate_conversion(self):
        """Show step-by-step conversion"""
        self.clear_and_setup("Step-by-Step Conversion")
        progress = self.get_scene_progress('conversion')
        
        r, g, b = self.example_rgb
        
        # Original color display - appears immediately
        if progress > 0.05:
            self.ax.text(8, 7.2, f'Converting: RGB({r}, {g}, {b})', 
                        fontsize=20, weight='bold', ha='center', alpha=1.0)
            
            # Show original color
            orig_rect = Rectangle((7, 6.2), 2, 0.8, facecolor=np.array([r, g, b])/255, alpha=1.0)
            self.ax.add_patch(orig_rect)
        
        # Step 1: Bit reduction - appears early
        if progress > 0.15:
            self.ax.text(8, 5.5, 'Step 1: Reduce Precision', fontsize=18, 
                        weight='bold', ha='center', color='darkblue', alpha=1.0)
        
        # Red reduction - appears early
        if progress > 0.25:
            r5 = r >> 3
            self.ax.text(8, 4.8, f'Red: {r} ÷ 8 = {r5} (keep top 5 bits)', 
                        fontsize=16, ha='center', color='red', alpha=1.0)
        
        # Green reduction
        if progress > 0.35:
            g6 = g >> 2
            self.ax.text(8, 4.3, f'Green: {g} ÷ 4 = {g6} (keep top 6 bits)', 
                        fontsize=16, ha='center', color='green', alpha=1.0)
        
        # Blue reduction
        if progress > 0.45:
            b5 = b >> 3
            self.ax.text(8, 3.8, f'Blue: {b} ÷ 8 = {b5} (keep top 5 bits)', 
                        fontsize=16, ha='center', color='blue', alpha=1.0)
        
        # Results - KEY MESSAGE appears early for more reading time
        if progress > 0.55:
            r5, g6, b5 = r >> 3, g >> 2, b >> 3
            self.ax.text(8, 3, f'Reduced values: R={r5}, G={g6}, B={b5}', 
                        fontsize=16, weight='bold', ha='center', alpha=1.0,
                        bbox=dict(boxstyle="round,pad=0.5", facecolor="lightyellow", alpha=1.0))
        
        # What's next - appears early and stays long
        if progress > 0.65:
            self.ax.text(8, 2, 'Next: Pack these into 16 bits!', 
                        fontsize=16, weight='bold', ha='center', color='purple', alpha=1.0)

    def animate_packing(self):
        """Show bit packing process"""
        self.clear_and_setup("Step 2: Bit Packing")
        progress = self.get_scene_progress('packing')
        
        r, g, b = self.example_rgb
        r5, g6, b5 = r >> 3, g >> 2, b >> 3
        
        # Formula introduction - appears immediately
        if progress > 0.05:
            self.ax.text(8, 7.2, f'Formula: ({r5} << 11) | ({g6} << 5) | {b5}', 
                        fontsize=18, weight='bold', ha='center', alpha=1.0)
        
        # Visualize bit shifting with early timing
        bit_width = 0.25
        start_x = 2.5
        
        # Show red bits being shifted - appears early
        if progress > 0.15:
            self.ax.text(1.5, 6, 'Red → bits 15-11:', fontsize=14, 
                        weight='bold', color='red', alpha=1.0)
            
            for i in range(5):
                bit_val = (r5 >> (4-i)) & 1
                rect = Rectangle((start_x + i*bit_width, 5.5), bit_width*0.9, bit_width, 
                               facecolor='red' if bit_val else 'white', 
                               alpha=0.8, edgecolor='black')
                self.ax.add_patch(rect)
                self.ax.text(start_x + i*bit_width + bit_width*0.45, 5.7, 
                           str(bit_val), ha='center', va='center', fontsize=10, 
                           weight='bold', alpha=1.0)
        
        # Show green bits - appears early
        if progress > 0.25:
            green_start = start_x + 5*bit_width + 0.1
            self.ax.text(1.5, 5, 'Green → bits 10-5:', fontsize=14, 
                        weight='bold', color='green', alpha=1.0)
            
            for i in range(6):
                bit_val = (g6 >> (5-i)) & 1
                rect = Rectangle((green_start + i*bit_width, 5.5), bit_width*0.9, bit_width, 
                               facecolor='green' if bit_val else 'white', 
                               alpha=0.8, edgecolor='black')
                self.ax.add_patch(rect)
                self.ax.text(green_start + i*bit_width + bit_width*0.45, 5.7, 
                           str(bit_val), ha='center', va='center', fontsize=10, 
                           weight='bold', alpha=1.0)
        
        # Show blue bits - appears early
        if progress > 0.35:
            blue_start = green_start + 6*bit_width + 0.1
            self.ax.text(1.5, 4, 'Blue → bits 4-0:', fontsize=14, 
                        weight='bold', color='blue', alpha=1.0)
            
            for i in range(5):
                bit_val = (b5 >> (4-i)) & 1
                rect = Rectangle((blue_start + i*bit_width, 5.5), bit_width*0.9, bit_width, 
                               facecolor='blue' if bit_val else 'white', 
                               alpha=0.8, edgecolor='black')
                self.ax.add_patch(rect)
                self.ax.text(blue_start + i*bit_width + bit_width*0.45, 5.7, 
                           str(bit_val), ha='center', va='center', fontsize=10, 
                           weight='bold', alpha=1.0)
        
        # Final result - KEY MESSAGES appear early for long reading time
        if progress > 0.5:
            rgb565 = (r5 << 11) | (g6 << 5) | b5
            self.ax.text(8, 3.5, f'Final RGB565 value: {rgb565}', 
                        fontsize=18, weight='bold', ha='center', alpha=1.0)
            self.ax.text(8, 3, f'In hexadecimal: 0x{rgb565:04X}', 
                        fontsize=16, ha='center', color='purple', alpha=1.0)
            self.ax.text(8, 2.5, 'Success! 24 bits compressed to 16 bits!', 
                        fontsize=16, weight='bold', ha='center', color='green', alpha=1.0)

    def animate_comparison(self):
        """Show quality comparison"""
        self.clear_and_setup("Quality Comparison")
        progress = self.get_scene_progress('comparison')
        
        r, g, b = self.example_rgb
        
        # Convert to RGB565 and back
        r5, g6, b5 = r >> 3, g >> 2, b >> 3
        r_back = (r5 << 3) | (r5 >> 2)
        g_back = (g6 << 2) | (g6 >> 4)
        b_back = (b5 << 3) | (b5 >> 2)
        r_back, g_back, b_back = min(255, r_back), min(255, g_back), min(255, b_back)
        
        # Original color - appears early
        if progress > 0.1:
            orig_rect = Rectangle((3, 5), 3, 2, facecolor=np.array([r, g, b])/255, alpha=1.0)
            self.ax.add_patch(orig_rect)
            self.ax.text(4.5, 4.3, f'Original\n24-bit\nRGB({r}, {g}, {b})', 
                        ha='center', fontsize=14, weight='bold', alpha=1.0)
        
        # Converted color - appears early  
        if progress > 0.2:
            conv_rect = Rectangle((10, 5), 3, 2, facecolor=np.array([r_back, g_back, b_back])/255, alpha=1.0)
            self.ax.add_patch(conv_rect)
            self.ax.text(11.5, 4.3, f'RGB565\n16-bit\nRGB({r_back}, {g_back}, {b_back})', 
                        ha='center', fontsize=14, weight='bold', alpha=1.0)
        
        # Arrow - appears early
        if progress > 0.3:
            self.ax.annotate('', xy=(10, 6), xytext=(6, 6), 
                            arrowprops=dict(arrowstyle='->', lw=4, color='orange', alpha=1.0))
            self.ax.text(8, 6.5, 'Compress', ha='center', fontsize=14, 
                        weight='bold', alpha=1.0)
        
        # Quality analysis - KEY MESSAGE appears early for long reading time
        if progress > 0.4:
            r_diff = abs(r - r_back)
            g_diff = abs(g - g_back)
            b_diff = abs(b - b_back)
            
            self.ax.text(8, 3.5, f'Differences: R±{r_diff}, G±{g_diff}, B±{b_diff}', 
                        ha='center', fontsize=16, alpha=1.0)
            
            total_error = r_diff + g_diff + b_diff
            if total_error < 10:
                quality_msg = 'Excellent quality! 😊'
                color = 'green'
            elif total_error < 30:
                quality_msg = 'Very good quality! 👍'
                color = 'orange'
            else:
                quality_msg = 'Acceptable quality'
                color = 'red'
            
            self.ax.text(8, 2.8, quality_msg, ha='center', fontsize=18, 
                        weight='bold', color=color, alpha=1.0)

    def animate_summary(self):
        """Show final summary"""
        self.clear_and_setup("🎉 Mission Accomplished! 🎉", 'green')
        progress = self.get_scene_progress('summary')
        
        # Key achievements - appear early with staggered timing for readability
        achievements = [
            '✅ Reduced memory usage by 33%',
            '✅ Maintained excellent visual quality', 
            '✅ Enabled mobile and embedded applications',
            '✅ Mastered bit manipulation concepts!'
        ]
        
        # Show achievements with early timing for maximum reading time
        if progress > 0.1:
            self.ax.text(8, 6.5, achievements[0], fontsize=18, 
                       ha='center', color='green', weight='bold', alpha=1.0)
        if progress > 0.2:
            self.ax.text(8, 5.9, achievements[1], fontsize=18, 
                       ha='center', color='green', weight='bold', alpha=1.0)
        if progress > 0.3:
            self.ax.text(8, 5.3, achievements[2], fontsize=18, 
                       ha='center', color='green', weight='bold', alpha=1.0)
        if progress > 0.4:
            self.ax.text(8, 4.7, achievements[3], fontsize=18, 
                       ha='center', color='green', weight='bold', alpha=1.0)
        
        # Applications - KEY MESSAGE appears early for long reading time
        if progress > 0.5:
            self.ax.text(8, 3.5, 'RGB565 is used in:', fontsize=16, 
                        weight='bold', ha='center', color='purple', alpha=1.0)
            
            apps = ['📱 Mobile phones', '🎮 Game consoles', '🚗 Car displays', '⌚ Smart watches']
            for i, app in enumerate(apps):
                x_pos = 2 + (i % 2) * 8  # Two columns
                y_pos = 2.8 - (i // 2) * 0.6
                self.ax.text(x_pos, y_pos, app, fontsize=14, ha='left', alpha=1.0)
        
        # Thank you message - appears early and stays long
        if progress > 0.7:
            self.ax.text(8, 0.8, 'Thanks for learning about RGB565!', 
                        fontsize=20, weight='bold', ha='center', color='blue', alpha=1.0)
    
    def animate(self, frame):
        """Main animation function called for each frame"""
        self.current_frame = frame
        
        # Determine current scene
        frame_count = 0
        for scene_name, scene_frames in self.scene_frames.items():
            if frame < frame_count + scene_frames:
                self.current_scene = scene_name
                break
            frame_count += scene_frames
        
        # Call appropriate animation function
        if self.current_scene == 'intro':
            self.animate_intro()
        elif self.current_scene == 'rgb_explanation':
            self.animate_rgb_explanation()
        elif self.current_scene == 'memory_problem':
            self.animate_memory_problem()
        elif self.current_scene == 'rgb565_intro':
            self.animate_rgb565_intro()
        elif self.current_scene == 'conversion':
            self.animate_conversion()
        elif self.current_scene == 'packing':
            self.animate_packing()
        elif self.current_scene == 'comparison':
            self.animate_comparison()
        elif self.current_scene == 'summary':
            self.animate_summary()
        
        # Add progress bar at bottom
        progress_width = 14
        progress_x = 1
        progress_y = 0.2
        
        # Background bar
        bg_rect = Rectangle((progress_x, progress_y), progress_width, 0.1, 
                          facecolor='lightgray', alpha=0.3)
        self.ax.add_patch(bg_rect)
        
        # Progress bar
        overall_progress = frame / self.total_frames
        prog_rect = Rectangle((progress_x, progress_y), progress_width * overall_progress, 0.1, 
                            facecolor='green', alpha=0.7)
        self.ax.add_patch(prog_rect)
        
        return []
    
    def generate_video(self, filename='rgb565_explanation.mp4', quality='high'):
        """Generate the complete video"""
        print(f"🎬 Generating RGB565 explanation video...")
        print(f"📊 Total duration: {sum(self.scene_durations.values()):.1f} seconds")
        print(f"🎞️ Frame rate: {self.fps} FPS")
        print(f"📈 Total frames: {self.total_frames}")
        print(f"💾 Output file: {filename}")
        
        # Set up video writer
        Writer = animation.writers['ffmpeg']
        
        # Quality settings
        if quality == 'high':
            bitrate = 5000
            dpi = 150
        elif quality == 'medium':
            bitrate = 2000
            dpi = 100
        else:  # low
            bitrate = 1000
            dpi = 80
            
        writer = Writer(fps=self.fps, metadata=dict(artist='RGB565 Educational Video'), 
                       bitrate=bitrate)
        
        # Create animation
        anim = animation.FuncAnimation(self.fig, self.animate, frames=self.total_frames, 
                                     interval=1000/self.fps, blit=False, repeat=False)
        
        # Save video
        print("🔄 Rendering video... (this may take a few minutes)")
        try:
            anim.save(filename, writer=writer, dpi=dpi, 
                     savefig_kwargs={'facecolor': 'white', 'edgecolor': 'none'})
            print(f"✅ Video saved successfully: {filename}")
            return True
        except Exception as e:
            print(f"❌ Error generating video: {e}")
            print("💡 Make sure FFmpeg is installed for video generation.")
            return False

def main():
    """Main function to generate the video"""
    print("🎨 RGB565 Educational Video Generator 🎨")
    print("\nThis tool creates a complete educational video explaining:")
    print("• RGB color fundamentals")
    print("• Memory usage problems") 
    print("• RGB565 compression format")
    print("• Step-by-step conversion process")
    print("• Quality analysis and applications")
    
    # Check if ffmpeg is available
    try:
        import subprocess
        subprocess.run(['ffmpeg', '-version'], capture_output=True, check=True)
        ffmpeg_available = True
    except (subprocess.CalledProcessError, FileNotFoundError):
        ffmpeg_available = False
        print("\n⚠️  Warning: FFmpeg not found. Video generation may fail.")
        print("💡 To install FFmpeg: sudo apt install ffmpeg")
    
    print(f"\n{'='*60}")
    
    # Get user preferences
    print("Video quality options:")
    print("1. High quality (5MB bitrate, ~30MB file)")
    print("2. Medium quality (2MB bitrate, ~12MB file)")
    print("3. Low quality (1MB bitrate, ~6MB file)")
    
    while True:
        try:
            choice = input("\nChoose quality (1-3) [2]: ").strip() or "2"
            quality_map = {"1": "high", "2": "medium", "3": "low"}
            if choice in quality_map:
                quality = quality_map[choice]
                break
            else:
                print("❌ Please enter 1, 2, or 3")
        except KeyboardInterrupt:
            print("\n\nCancelled by user.")
            return
    
    filename = input("Output filename [rgb565_explanation.mp4]: ").strip() or "rgb565_explanation.mp4"
    
    if not filename.endswith('.mp4'):
        filename += '.mp4'
    
    print(f"\n🎬 Starting video generation with {quality} quality...")
    
    # Generate video
    generator = RGB565VideoGenerator()
    success = generator.generate_video(filename, quality)
    
    if success:
        print(f"\n🎉 Success! Your educational video is ready!")
        print(f"📁 File: {filename}")
        print(f"🎯 Perfect for teaching RGB565 conversion to beginners!")
        print(f"\n💡 You can now:")
        print(f"•  Share this video with students")
        print(f"•  Use it in presentations") 
        print(f"•  Upload to learning management systems")
    else:
        print(f"\n💾 Attempting to save as GIF instead...")
        try:
            gif_filename = filename.replace('.mp4', '.gif')
            generator.generate_video(gif_filename, quality)
            print(f"✅ GIF animation saved: {gif_filename}")
        except Exception as e:
            print(f"❌ Could not generate video or GIF: {e}")

if __name__ == "__main__":
    main()