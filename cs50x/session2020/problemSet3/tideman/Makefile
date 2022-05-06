###
#-------------------------------------------------------------------------------
# Makefile
#-------------------------------------------------------------------------------
#
# Author:       Alwin Tareen
# Created:      Jul 06, 2020
# Compilation:  make tideman
#
# This Makefile compiles the tideman.c program.
#
##

tideman: tideman.c
	gcc -ggdb3 -O0 -std=c11 -Wall -Werror -Wextra -Wno-sign-compare -Wno-unused-parameter -Wno-unused-variable -Wshadow -o tideman tideman.c

clean:
	rm -f *.o a.out core tideman log.txt

