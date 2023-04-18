##
## EPITECH PROJECT, 2023
## 107TRANSFER
## File description:
## Makefile
##

NAME	=	107transfer

SRC		=	107transfer.py

$(NAME):
		cp	$(SRC) $(NAME)
		chmod 755 $(NAME)

all:	$(NAME)
