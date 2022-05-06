###
#-------------------------------------------------------------------------------
# Makefile
#-------------------------------------------------------------------------------
#
# Author:       Alwin Tareen
# Created:      Feb 04, 2021
# Compilation:  make plurality
#
# This Makefile compiles the plurality.c program.
#
##

plurality: plurality.c
	gcc -ggdb3 -O0 -std=c11 -Wall -Werror -Wextra -Wno-sign-compare -Wno-unused-parameter -Wno-unused-variable -Wshadow plurality.c -lcrypt -lm -o plurality

clean:
	rm -f *.o a.out core plurality log.txt

