###
#-------------------------------------------------------------------------------
# Makefile
#-------------------------------------------------------------------------------
#
# Author:       Alwin Tareen
# Created:      Feb 07, 2021
# Compilation:  make filter
#
# This Makefile compiles the filter.c program.
#
##

filter: helpers.c
	gcc -ggdb3 -O0 -std=c11 -Wall -Werror -Wextra -Wno-sign-compare -Wno-unused-parameter -Wno-unused-variable -Wshadow filter.c helpers.c -lcrypt -lm -o filter

clean:
	rm -f *.o a.out core filter log.txt

