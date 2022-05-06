###
#-------------------------------------------------------------------------------
# Makefile
#-------------------------------------------------------------------------------
#
# Author:       Alwin Tareen
# Created:      Feb 09, 2021
# Compilation:  make inheritance
#
# This Makefile compiles the inheritance.c program.
#
##

inheritance: inheritance.c
	gcc -ggdb3 -O0 -std=c11 -Wall -Werror -Wextra -Wno-sign-compare -Wno-unused-parameter -Wno-unused-variable -Wshadow inheritance.c -lcrypt -lm -o inheritance

clean:
	rm -f *.o a.out core inheritance log.txt

