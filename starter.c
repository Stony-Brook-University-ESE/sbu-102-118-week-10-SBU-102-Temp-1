#include <assert.h>
#include <stdint.h>
#include <stdio.h>

// ----------------------------
// Part 1: Bit operations
// ----------------------------

uint8_t low_nibble(uint8_t x) {
	// TODO: keep only the last 4 bits (hint: mask with 0x0F)
	return 0; // placeholder
}

uint8_t set_bit(uint8_t x, unsigned bit_index) {
	// TODO: turn ON one bit (hint: OR with 1u << bit_index)
	return 0; // placeholder
}

uint8_t clear_bit(uint8_t x, unsigned bit_index) {
	// TODO: turn OFF one bit (hint: AND with NOT(1u << bit_index))
	return 0; // placeholder
}

uint8_t toggle_bit(uint8_t x, unsigned bit_index) {
	// TODO: flip one bit (hint: XOR with 1u << bit_index)
	return 0; // placeholder
}

// ----------------------------
// Part 2: RGB565 packing
// ----------------------------

uint16_t pack_rgb565(uint8_t r8, uint8_t g8, uint8_t b8) {
	// RGB565 uses: R = 5 bits, G = 6 bits, B = 5 bits
	// Hint: r5 = r8 >> 3, g6 = g8 >> 2, b5 = b8 >> 3

	// TODO: compute r5, g6, b5
	uint16_t r5 = 0;
	uint16_t g6 = 0;
	uint16_t b5 = 0;

	// TODO: pack into 16-bit value: (r5 << 11) | (g6 << 5) | b5
	return 0; // placeholder
}

uint8_t unpack_r8(uint16_t rgb) {
	// TODO: r5 = (rgb >> 11) & 0x1F
	uint16_t r5 = 0;
	// TODO: expand to 8-bit: (r5 << 3) | (r5 >> 2)
	return 0; // placeholder
}

uint8_t unpack_g8(uint16_t rgb) {
	// TODO: g6 = (rgb >> 5) & 0x3F
	uint16_t g6 = 0;
	// TODO: expand to 8-bit: (g6 << 2) | (g6 >> 4)
	return 0; // placeholder
}

uint8_t unpack_b8(uint16_t rgb) {
	// TODO: b5 = rgb & 0x1F
	uint16_t b5 = 0;
	// TODO: expand to 8-bit: (b5 << 3) | (b5 >> 2)
	return 0; // placeholder
}

// ----------------------------
// Demo + tests
// ----------------------------

static void print_bits8(uint8_t x) {
	for (int i = 7; i >= 0; i--) {
		printf("%u", (x >> i) & 1u);
	}
}

static void run_tests(void) {
	// pack tests
	assert(pack_rgb565(0, 0, 0) == 0x0000);
	assert(pack_rgb565(255, 255, 255) == 0xFFFF);

	// basic sanity (approx ok)
	{
		uint16_t rgb = pack_rgb565(255, 0, 0);
		assert(unpack_r8(rgb) >= 248);
		assert(unpack_g8(rgb) <= 8);
		assert(unpack_b8(rgb) <= 8);
	}
}

int main(void) {
#ifdef RUN_TESTS
	run_tests();
	printf("All tests passed.\n");
	return 0;
#else
	uint8_t x = 0b10101101;
	printf("x        = "); print_bits8(x); printf("\n");
	printf("lowNib   = "); print_bits8(low_nibble(x)); printf("\n\n");

	uint16_t rgb = pack_rgb565(255, 128, 0);
	printf("packed rgb565: 0x%04X\n", rgb);
	printf("unpacked r,g,b: %u, %u, %u\n",
		unpack_r8(rgb), unpack_g8(rgb), unpack_b8(rgb));
	return 0;
#endif
}