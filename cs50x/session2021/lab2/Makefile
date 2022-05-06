###
#-------------------------------------------------------------------------------
# Makefile
#-------------------------------------------------------------------------------
#
# Author:       Alwin Tareen
# Created:      Jan 28, 2021
# Compilation:  make scrabble
#
# This Makefile compiles the scrabble.c program.
#
##

scrabble: scrabble.c
	gcc -ggdb3 -O0 -std=c11 -Wall -Werror -Wextra -Wno-sign-compare -Wno-unused-parameter -Wno-unused-variable -Wshadow scrabble.c -lcrypt -lm -o scrabble

clean:
	rm -f *.o a.out core scrabble log.txt
