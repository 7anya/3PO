#!/bin/bash
cd linux-stable-6.1.8/

# make defconfig


# Check if an argument is provided and if it's a number
if [[ $# -eq 0 ]] || ! [[ $1 =~ ^[0-9]+$ ]]; then
    echo "Usage: $0 <number>"
    exit 1
fi

if [[ $1 -eq 1 ]]; then
    make defconfig
elif [[ $1 -eq 2 ]]; then
    make menuconfig
else
    echo "Invalid args, exiting."
    exit 1
fi

make kvm_guest.config
make -j $(nproc) arch=x86_64

echo "this is your chance to stop the script and check the build"
sleep 10
make modules_install arch=x86_64

echo "this is your chance to stop the script and check the build"
sleep 10
make install arch=x86_64

cd ..

cp /boot/vmlinuz-6.1.8* temp/
cp /boot/initrd.img-6.1.8* temp/
cp /boot/System.map-6.1.8* temp/
cp /boot/config-6.1.8* temp/



