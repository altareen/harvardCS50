###
#-------------------------------------------------------------------------------
# Makefile
#-------------------------------------------------------------------------------
#
# Author:       Alwin Tareen
# Created:      Jun 30, 2020
# Compilation:  make mario
#
# This Makefile compiles the mario.c program.
#
##

mario: mario.c
	gcc -ggdb3 -O0 -std=c11 -Wall -Werror -Wextra -Wno-sign-compare -Wno-unused-parameter -Wno-unused-variable -Wshadow -o mario mario.c

clean:
	rm -f *.o a.out core mario log.txt

