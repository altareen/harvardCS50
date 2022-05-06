###
#-------------------------------------------------------------------------------
# Makefile
#-------------------------------------------------------------------------------
#
# Author:       Alwin Tareen
# Created:      Jan 26, 2021
# Compilation:  make mario
#
# This Makefile compiles the mario.c program.
#
##

mario: mario.c
	gcc -ggdb3 -O0 -std=c11 -Wall -Werror -Wextra -Wno-sign-compare -Wno-unused-parameter -Wno-unused-variable -Wshadow mario.c -lcrypt -lm -o mario

clean:
	rm -f *.o a.out core mario log.txt
