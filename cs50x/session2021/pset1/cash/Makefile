###
#-------------------------------------------------------------------------------
# Makefile
#-------------------------------------------------------------------------------
#
# Author:       Alwin Tareen
# Created:      Jan 26, 2021
# Compilation:  make cash
#
# This Makefile compiles the cash.c program.
#
##

cash: cash.c
	gcc -ggdb3 -O0 -std=c11 -Wall -Werror -Wextra -Wno-sign-compare -Wno-unused-parameter -Wno-unused-variable -Wshadow cash.c -lcrypt -lm -o cash

clean:
	rm -f *.o a.out core cash log.txt
