
wget https://releases.ubuntu.com/20.04.6/ubuntu-20.04.6-live-server-amd64.iso
qemu-img create -f qcow2 ubuntu.qcow2 50G
qemu-system-x86_64 \
    -enable-kvm \
    -m 8192 \
    -net user,hostfwd=tcp::2222-:22 \
    -net nic \
    -nic user,model=virtio \
    -drive file=../ubuntu.qcow2,media=disk,if=virtio \
    -cdrom ../ubuntu-20.04.6-live-server-amd64.iso \
    -smp 8 \
    -cpu max \
    -serial mon:stdio -nographic -display curses

