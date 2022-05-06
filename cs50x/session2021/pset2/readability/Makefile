###
#-------------------------------------------------------------------------------
# Makefile
#-------------------------------------------------------------------------------
#
# Author:       Alwin Tareen
# Created:      Jan 31, 2021
# Compilation:  make readability
#
# This Makefile compiles the readability.c program.
#
##

readability: readability.c
	gcc -ggdb3 -O0 -std=c11 -Wall -Werror -Wextra -Wno-sign-compare -Wno-unused-parameter -Wno-unused-variable -Wshadow readability.c -lcrypt -lm -o readability

clean:
	rm -f *.o a.out core readability log.txt
