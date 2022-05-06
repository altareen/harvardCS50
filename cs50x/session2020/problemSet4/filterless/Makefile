###
#-------------------------------------------------------------------------------
# Makefile
#-------------------------------------------------------------------------------
#
# Author:       Alwin Tareen
# Created:      Nov 17, 2020
# Compilation:  make filter
#
# This Makefile compiles the filter.c program.
#
##

filter: helpers.c
	gcc -ggdb3 -O0 -std=c11 -Wall -Werror -Wextra -Wno-sign-compare -Wno-unused-parameter -Wno-unused-variable -Wshadow -o filter filter.c helpers.c -lm

clean:
	rm -f *.o a.out core filter log.txt

