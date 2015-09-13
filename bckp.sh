#!/bin/sh

cd $HOME

if [ ! -d archives ] ; then
	mkdir archives
fi

curr_time=$(date +%Y%m%d%H%M%S)
if [ $# -eq 0 ] ; then 
	tar -czf archive${curr_time}.tar.gz projects	
else
	tar -czf atchive${curr_time}.tar.gz $*
fi

if [ $? -eq 0 ] ; then
	mv archive${curr_time}.tar.gz $HOME/archives/
	echo "$curr_time - резервное копирование завершено успешно"
else
	echo "$curr_time - резервное копирование не было завершено"
	exit 1
fi
