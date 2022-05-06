###
#-------------------------------------------------------------------------------
# Makefile
#-------------------------------------------------------------------------------
#
# Author:       Alwin Tareen
# Created:      Jan 27, 2021
# Compilation:  make credit
#
# This Makefile compiles the credit.c program.
#
##

credit: credit.c
	gcc -ggdb3 -O0 -std=c11 -Wall -Werror -Wextra -Wno-sign-compare -Wno-unused-parameter -Wno-unused-variable -Wshadow credit.c -lcrypt -lm -o credit

clean:
	rm -f *.o a.out core credit log.txt

