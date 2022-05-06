###
#-------------------------------------------------------------------------------
# Makefile
#-------------------------------------------------------------------------------
#
# Author:       Alwin Tareen
# Created:      Nov 22, 2020
# Compilation:  make recover
#
# This Makefile compiles the recover.c program.
#
##

recover: recover.c
	gcc -ggdb3 -O0 -std=c11 -Wall -Werror -Wextra -Wno-sign-compare -Wno-unused-parameter -Wno-unused-variable -Wshadow -o recover recover.c

clean:
	rm -f *.o a.out core recover log.txt

