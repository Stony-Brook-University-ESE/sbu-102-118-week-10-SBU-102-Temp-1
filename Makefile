CC=gcc
CFLAGS=-std=c11 -Wall -Wextra -Werror -pedantic

all: run

build:
	$(CC) $(CFLAGS) starter.c -o build/demo

run: build
	./build/demo

test:
	$(CC) $(CFLAGS) -DRUN_TESTS starter.c -o build/test
	./build/test

clean:
	rm -rf build/*