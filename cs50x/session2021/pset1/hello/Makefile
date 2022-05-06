###
#-------------------------------------------------------------------------------
# Makefile
#-------------------------------------------------------------------------------
#
# Author:       Alwin Tareen
# Created:      Jan 26, 2021
# Compilation:  make hello
#
# This Makefile compiles the hello.c program.
#
##

hello: hello.c
	gcc -ggdb3 -O0 -std=c11 -Wall -Werror -Wextra -Wno-sign-compare -Wno-unused-parameter -Wno-unused-variable -Wshadow hello.c -lcrypt -lm -o hello

clean:
	rm -f *.o a.out core hello log.txt
