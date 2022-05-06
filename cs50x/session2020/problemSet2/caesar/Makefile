###
#-------------------------------------------------------------------------------
# Makefile
#-------------------------------------------------------------------------------
#
# Author:       Alwin Tareen
# Created:      Jul 03, 2020
# Compilation:  make caesar
#
# This Makefile compiles the caesar.c program.
#
##

caesar: caesar.c
	gcc -ggdb3 -O0 -std=c11 -Wall -Werror -Wextra -Wno-sign-compare -Wno-unused-parameter -Wno-unused-variable -Wshadow -o caesar caesar.c

clean:
	rm -f *.o a.out core caesar log.txt

