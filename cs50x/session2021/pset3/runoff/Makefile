###
#-------------------------------------------------------------------------------
# Makefile
#-------------------------------------------------------------------------------
#
# Author:       Alwin Tareen
# Created:      Feb 04, 2021
# Compilation:  make runoff
#
# This Makefile compiles the runoff.c program.
#
##

runoff: runoff.c
	gcc -ggdb3 -O0 -std=c11 -Wall -Werror -Wextra -Wno-sign-compare -Wno-unused-parameter -Wno-unused-variable -Wshadow runoff.c -lcrypt -lm -o runoff

clean:
	rm -f *.o a.out core runoff log.txt

