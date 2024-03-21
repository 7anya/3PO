
cd linux-stable-6.1.8/

make defconfig
make kvm_guest.config

make -j $(nproc) arch=x86_64

echo "this is your chance to stop the script and check the build"
sleep 10
make modules_install arch=x86_64

echo "this is your chance to stop the script and check the build"
sleep 10
make install arch=x86_64

cd ..

cp /boot/vmlinuz-6.1.8 temp/
cp /boot/initrd.img-6.1.8 temp/
cp /boot/System.map-6.1.8 temp/
cp /boot/config-6.1.8 temp/



