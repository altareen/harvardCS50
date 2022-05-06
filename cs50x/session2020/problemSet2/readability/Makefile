###
#-------------------------------------------------------------------------------
# Makefile
#-------------------------------------------------------------------------------
#
# Author:       Alwin Tareen
# Created:      Jul 02, 2020
# Compilation:  make readability
#
# This Makefile compiles the readability.c program.
#
##

readability: readability.c
	gcc -ggdb3 -O0 -std=c11 -Wall -Werror -Wextra -Wno-sign-compare -Wno-unused-parameter -Wno-unused-variable -Wshadow -o readability readability.c -lm

clean:
	rm -f *.o a.out core readability log.txt

