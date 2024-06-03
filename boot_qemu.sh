#!/bin/bash

qemu-system-x86_64 \
    -enable-kvm \
    -m 8192 \
    -net user,hostfwd=tcp::10022-:22 \
    -net nic \
    -nic user\
    -hda ../ubuntu.qcow2 \
    -smp 8 \
    -cpu max \
    -serial mon:stdio -nographic -display curses
