###
#-------------------------------------------------------------------------------
# Makefile
#-------------------------------------------------------------------------------
#
# Author:       Alwin Tareen
# Created:      Feb 05, 2021
# Compilation:  make tideman
#
# This Makefile compiles the tideman.c program.
#
##

tideman: tideman.c
	gcc -ggdb3 -O0 -std=c11 -Wall -Werror -Wextra -Wno-sign-compare -Wno-unused-parameter -Wno-unused-variable -Wshadow tideman.c -lcrypt -lm -o tideman

clean:
	rm -f *.o a.out core tideman log.txt
