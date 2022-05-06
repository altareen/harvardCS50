###
#-------------------------------------------------------------------------------
# Makefile
#-------------------------------------------------------------------------------
#
# Author:       Alwin Tareen
# Created:      Jun 29, 2020
# Compilation:  make cash
#
# This Makefile compiles the cash.c program.
#
##

cash: cash.c
	gcc -ggdb3 -O0 -std=c11 -Wall -Werror -Wextra -Wno-sign-compare -Wno-unused-parameter -Wno-unused-variable -Wshadow -o cash cash.c -lm

clean:
	rm -f *.o a.out core cash log.txt

