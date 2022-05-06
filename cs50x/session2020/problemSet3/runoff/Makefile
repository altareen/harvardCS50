###
#-------------------------------------------------------------------------------
# Makefile
#-------------------------------------------------------------------------------
#
# Author:       Alwin Tareen
# Created:      Jul 05, 2020
# Compilation:  make runoff
#
# This Makefile compiles the runoff.c program.
#
##

runoff: runoff.c
	gcc -ggdb3 -O0 -std=c11 -Wall -Werror -Wextra -Wno-sign-compare -Wno-unused-parameter -Wno-unused-variable -Wshadow -o runoff runoff.c

clean:
	rm -f *.o a.out core runoff log.txt

