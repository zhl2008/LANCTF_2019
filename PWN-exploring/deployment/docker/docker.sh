#!/bin/sh

docker run -v `pwd`/../source:/home/pwn:ro -v `pwd`/xinetd:/etc/xinetd.d/xinetd:ro -v `pwd`:/root/ -p 2333:60001 -ti introspelliam/pwn:16.04 /root/run.sh
