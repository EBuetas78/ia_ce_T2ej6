#!/bin/bash
if [ -n "$1" ];
then
	git add .
	git commit -a -s -m "$1"
	git push
else
	echo "debes escribir un comentario para el commit"
fi
