###
#-------------------------------------------------------------------------------
# Makefile
#-------------------------------------------------------------------------------
#
# Author:       Alwin Tareen
# Created:      Jun 29, 2020
# Compilation:  make hello
#
# This Makefile compiles the hello.c program.
#
##

hello: hello.c
	gcc -ggdb3 -O0 -std=c11 -Wall -Werror -Wextra -Wno-sign-compare -Wno-unused-parameter -Wno-unused-variable -Wshadow -o hello hello.c

clean:
	rm -f *.o a.out core hello log.txt
