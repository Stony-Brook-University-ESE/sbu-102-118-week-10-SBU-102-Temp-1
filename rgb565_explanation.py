#!/usr/bin/env python3
"""
RGB 24-bit to RGB565 Conversion Animation
Educational video for non-CS freshmen using Manim

This animation explains:
1. What colors are on computers
2. Why we need to compress colors
3. How RGB565 works step by step
4. Visual examples of the conversion process
"""

from manim import *
import numpy as np

class RGB565Explanation(Scene):
    def construct(self):
        # Title and introduction
        self.intro_scene()
        self.wait(2)
        self.clear()
        
        # Part 1: What are colors on computers?
        self.what_are_colors()
        self.wait(2)
        self.clear()
        
        # Part 2: Why do we need compression?
        self.why_compression()
        self.wait(2)
        self.clear()
        
        # Part 3: RGB565 format explanation
        self.rgb565_format()
        self.wait(2)
        self.clear()
        
        # Part 4: Step-by-step conversion
        self.conversion_steps()
        self.wait(2)
        self.clear()
        
        # Part 5: Visual example
        self.visual_example()
        self.wait(3)

    def intro_scene(self):
        """Introduction with colorful title"""
        title = Text("RGB24 → RGB565", font_size=72, gradient=[RED, GREEN, BLUE])
        subtitle = Text("Color Compression Explained", font_size=36).next_to(title, DOWN, buff=0.5)
        subtitle2 = Text("For Beginners", font_size=28, color=GRAY).next_to(subtitle, DOWN, buff=0.3)
        
        self.play(Write(title), run_time=2)
        self.play(FadeIn(subtitle))
        self.play(FadeIn(subtitle2))

    def what_are_colors(self):
        """Explain RGB color model"""
        title = Text("What are colors on computers?", font_size=48, color=YELLOW).to_edge(UP)
        self.play(Write(title))
        
        # RGB explanation
        rgb_text = Text("Every pixel is made of:", font_size=32).shift(UP*2)
        self.play(Write(rgb_text))
        
        # Create RGB squares
        red_square = Square(1, fill_color=RED, fill_opacity=0.8).shift(LEFT*3 + UP*0.5)
        green_square = Square(1, fill_color=GREEN, fill_opacity=0.8).shift(UP*0.5)
        blue_square = Square(1, fill_color=BLUE, fill_opacity=0.8).shift(RIGHT*3 + UP*0.5)
        
        red_label = Text("Red", color=RED, font_size=24).next_to(red_square, DOWN)
        green_label = Text("Green", color=GREEN, font_size=24).next_to(green_square, DOWN)
        blue_label = Text("Blue", color=BLUE, font_size=24).next_to(blue_square, DOWN)
        
        # RGB values
        red_value = Text("0-255", font_size=20, color=WHITE).next_to(red_label, DOWN)
        green_value = Text("0-255", font_size=20, color=WHITE).next_to(green_label, DOWN)
        blue_value = Text("0-255", font_size=20, color=WHITE).next_to(blue_label, DOWN)
        
        self.play(FadeIn(red_square), FadeIn(green_square), FadeIn(blue_square))
        self.play(Write(red_label), Write(green_label), Write(blue_label))
        self.play(Write(red_value), Write(green_value), Write(blue_value))
        
        # Show bit information
        bit_info = Text("Each color uses 8 bits (1 byte)", font_size=28).shift(DOWN*1)
        total_info = Text("Total: 24 bits (3 bytes) per pixel", font_size=28, color=YELLOW).shift(DOWN*1.8)
        
        self.play(Write(bit_info))
        self.play(Write(total_info))

    def why_compression(self):
        """Explain why we need compression"""
        title = Text("Why compress colors?", font_size=48, color=YELLOW).to_edge(UP)
        self.play(Write(title))
        
        # Memory usage example
        phone_text = Text("Consider a phone screen:", font_size=32).shift(UP*2)
        resolution_text = Text("1920 × 1080 pixels", font_size=28, color=BLUE).shift(UP*1.3)
        
        self.play(Write(phone_text))
        self.play(Write(resolution_text))
        
        # Create visual representation of memory
        memory_rgb24 = Rectangle(width=4, height=1, color=RED, fill_opacity=0.3).shift(LEFT*1.5)
        memory_rgb565 = Rectangle(width=2.7, height=1, color=GREEN, fill_opacity=0.3).shift(RIGHT*1.5)
        
        rgb24_label = Text("24-bit RGB", font_size=20).next_to(memory_rgb24, UP)
        rgb565_label = Text("16-bit RGB565", font_size=20).next_to(memory_rgb565, UP)
        
        rgb24_size = Text("6.2 MB", font_size=18, color=RED).next_to(memory_rgb24, DOWN)
        rgb565_size = Text("4.1 MB", font_size=18, color=GREEN).next_to(memory_rgb565, DOWN)
        
        self.play(FadeIn(memory_rgb24), FadeIn(memory_rgb565))
        self.play(Write(rgb24_label), Write(rgb565_label))
        self.play(Write(rgb24_size), Write(rgb565_size))
        
        # Savings
        savings = Text("Saves 33% memory!", font_size=32, color=GREEN).shift(DOWN*2)
        self.play(Write(savings))

    def rgb565_format(self):
        """Explain RGB565 bit allocation"""
        title = Text("RGB565 Format", font_size=48, color=YELLOW).to_edge(UP)
        self.play(Write(title))
        
        # Bit allocation diagram
        explanation = Text("16 bits total, allocated as:", font_size=28).shift(UP*2)
        self.play(Write(explanation))
        
        # Create bit boxes
        red_bits = self.create_bit_boxes(5, RED, "Red (5 bits)").shift(LEFT*2 + UP*0.5)
        green_bits = self.create_bit_boxes(6, GREEN, "Green (6 bits)").shift(UP*0.5)
        blue_bits = self.create_bit_boxes(5, BLUE, "Blue (5 bits)").shift(RIGHT*2 + UP*0.5)
        
        # Why this allocation?
        why_text = Text("Why this allocation?", font_size=24, color=YELLOW).shift(DOWN*1)
        reason_text = Text("Human eyes are most sensitive to green light!", 
                          font_size=20).shift(DOWN*1.7)
        
        self.play(Write(why_text))
        self.play(Write(reason_text))

    def create_bit_boxes(self, num_bits, color, label):
        """Helper function to create bit representation"""
        boxes = VGroup()
        for i in range(num_bits):
            box = Square(0.3, color=color, fill_opacity=0.7)
            if i > 0:
                box.next_to(boxes[-1], RIGHT, buff=0.05)
            boxes.add(box)
        
        label_text = Text(label, font_size=18).next_to(boxes, DOWN, buff=0.2)
        return VGroup(boxes, label_text)

    def conversion_steps(self):
        """Show step-by-step conversion process"""
        title = Text("Conversion Steps", font_size=48, color=YELLOW).to_edge(UP)
        self.play(Write(title))
        
        # Example color
        example_text = Text("Example: RGB(255, 128, 64)", font_size=32, color=WHITE).shift(UP*2.5)
        
        # Show the actual color
        color_square = Square(1, fill_color=rgb_to_hex_color([255, 128, 64]), 
                             fill_opacity=1).shift(RIGHT*3 + UP*2.5)
        
        self.play(Write(example_text))
        self.play(FadeIn(color_square))
        
        # Step 1: Reduce precision
        step1 = Text("Step 1: Reduce precision", font_size=24, color=YELLOW).shift(UP*1.5)
        red_calc = Text("Red: 255 ÷ 8 = 31 (keep 5 bits)", font_size=20).shift(UP*0.8)
        green_calc = Text("Green: 128 ÷ 4 = 32 (keep 6 bits)", font_size=20).shift(UP*0.4)
        blue_calc = Text("Blue: 64 ÷ 8 = 8 (keep 5 bits)", font_size=20).shift(UP*0)
        
        self.play(Write(step1))
        self.play(Write(red_calc))
        self.play(Write(green_calc))
        self.play(Write(blue_calc))
        
        # Step 2: Bit packing
        step2 = Text("Step 2: Pack into 16 bits", font_size=24, color=YELLOW).shift(DOWN*0.5)
        packing = Text("(31 << 11) | (32 << 5) | 8 = 64584", font_size=20).shift(DOWN*1)
        
        self.play(Write(step2))
        self.play(Write(packing))

    def visual_example(self):
        """Visual comparison of original vs compressed"""
        title = Text("Original vs Compressed", font_size=48, color=YELLOW).to_edge(UP)
        self.play(Write(title))
        
        # Create gradient showing compression effect
        original_colors = [
            [255, 0, 0], [255, 128, 0], [255, 255, 0],
            [128, 255, 0], [0, 255, 0], [0, 255, 128],
            [0, 255, 255], [0, 128, 255], [0, 0, 255]
        ]
        
        # Show original colors
        original_label = Text("24-bit Original", font_size=24).shift(UP*1.5 + LEFT*3)
        compressed_label = Text("16-bit RGB565", font_size=24).shift(UP*1.5 + RIGHT*3)
        
        self.play(Write(original_label), Write(compressed_label))
        
        for i, color in enumerate(original_colors):
            y_pos = 0.5 - (i * 0.3)
            
            # Original color
            orig_square = Square(0.5, fill_color=rgb_to_hex_color(color), 
                               fill_opacity=1).shift(LEFT*3 + UP*y_pos)
            
            # RGB565 compressed color
            compressed_color = self.rgb_to_rgb565_and_back(color)
            comp_square = Square(0.5, fill_color=rgb_to_hex_color(compressed_color), 
                               fill_opacity=1).shift(RIGHT*3 + UP*y_pos)
            
            self.play(FadeIn(orig_square), FadeIn(comp_square), run_time=0.3)
        
        # Final message
        final_text = Text("Quality loss is minimal for most applications!", 
                         font_size=28, color=GREEN).shift(DOWN*2.5)
        self.play(Write(final_text))

    def rgb_to_rgb565_and_back(self, rgb):
        """Simulate RGB565 conversion and back"""
        r, g, b = rgb
        
        # Convert to RGB565
        r5 = r >> 3
        g6 = g >> 2
        b5 = b >> 3
        
        # Convert back to RGB24
        r8 = (r5 << 3) | (r5 >> 2)
        g8 = (g6 << 2) | (g6 >> 4)
        b8 = (b5 << 3) | (b5 >> 2)
        
        return [r8, g8, b8]


def rgb_to_hex_color(rgb):
    """Convert RGB values to hex color string"""
    r, g, b = rgb
    return f"#{r:02x}{g:02x}{b:02x}"


if __name__ == "__main__":
    # To render this animation, run:
    # manim -pql rgb565_explanation.py RGB565Explanation
    pass