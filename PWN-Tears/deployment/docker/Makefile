CC=gcc
CFLAGS=-m32 --static -Wl,--omagic -o tears

all:
	$(CC) $(CFLAGS) tears.c
	cp ./tears ./bin

clean:
	rm tears
	rm ./bin/tears
