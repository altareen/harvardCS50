###
#-------------------------------------------------------------------------------
# Makefile
#-------------------------------------------------------------------------------
#
# Author:       Alwin Tareen
# Created:      Feb 06, 2021
# Compilation:  make volume
#
# This Makefile compiles the volume.c program.
#
##

volume: volume.c
	gcc -ggdb3 -O0 -std=c11 -Wall -Werror -Wextra -Wno-sign-compare -Wno-unused-parameter -Wno-unused-variable -Wshadow volume.c -lcrypt -lm -o volume

clean:
	rm -f *.o a.out core volume log.txt

