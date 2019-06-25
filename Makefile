CC = gcc
CFLAGS = -O2
ARRAY_H = array.h

all: sorted unsorted
sorted: sorted.c $(ARRAY_H)
	$(CC) -o $@ $< $(CFLAGS) 
	
unsorted: unsorted.c $(ARRAY_H)
	$(CC) -o $@ $< $(CFLAGS)

$(ARRAY_H): build_array.py
	python $<

clean:
	rm -f $(ARRAY_H) sorted unsorted
