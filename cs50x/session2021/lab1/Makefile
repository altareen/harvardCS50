###
#-------------------------------------------------------------------------------
# Makefile
#-------------------------------------------------------------------------------
#
# Author:       Alwin Tareen
# Created:      Jan 05, 2021
# Compilation:  make population
#
# This Makefile compiles the population.c program.
#
##

cash: cash.c
	gcc -ggdb3 -O0 -std=c11 -Wall -Werror -Wextra -Wno-sign-compare -Wno-unused-parameter -Wno-unused-variable -Wshadow population.c -lcrypt -lm -o population

clean:
	rm -f *.o a.out core population log.txt
