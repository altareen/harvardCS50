###
#-------------------------------------------------------------------------------
# Makefile
#-------------------------------------------------------------------------------
#
# Author:       Alwin Tareen
# Created:      Jan 31, 2021
# Compilation:  make caesar
#
# This Makefile compiles the caesar.c program.
#
##

caesar: caesar.c
	gcc -ggdb3 -O0 -std=c11 -Wall -Werror -Wextra -Wno-sign-compare -Wno-unused-parameter -Wno-unused-variable -Wshadow caesar.c -lcrypt -lm -o caesar

clean:
	rm -f *.o a.out core caesar log.txt

