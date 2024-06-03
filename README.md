# 3PO


## Set up VM 

We use qemu for development. 

There are a bunch of scripts described below to make life easier. 

First we set up the VM with a ubuntu ISO. We download the ISO from the official ubuntu website, and use version ubuntu 20.04. 

Run the script as follows. 

```
./setup_qemu_iso.sh

```

We download the ISO from the official ubuntu website, and use version ubuntu 20.04. 

Once you are able to boot into the VM, we can set it up normally.

If you are using qemu in a remote server, you need to configure grub such that it can redirect output to seriel in /etc/grub..
 
We dont need the iso anymore, so it can be deleted.


## Boot into qemu after set up 

Once set up is finished, we need a different qemu config boot. Use 

```
./boot_qemu.sh 

```

## SSH into VM 

We can ssh into the VM using

```
ssh -p10022  tanyapsd@localhost
```

For some reason ssh works only for the generic kernel 


## Building kernel

Next we build the kernel, 

```
./build_and_copy.sh

```

This script builds the kernel in default config, makes it qemu ready and then proceeds to install the kernel image. 

It gives 10s delay to between the build and install to kill. 

It copies the kernel image into temp/. We can copy it into the VM using scp from here or viceversa 

## Copy images into the VM 

Make sure the VM has booted into the generic/default kernel. 

From this directory, 


```
scp -P10022 temp/*  tanyapsd@localhost:/home/tanyapsd/
```

This will copy the files into the VM's ~

Then from the VM, copy the files into /boot


## Boot 

Once the custom kernel is copied into the VM's /boot directory. 

Do, 

```
sudo update-grub
```

and then grub reboot 

## Commit your changes

> This was taken from Sid's Osmosis repo fot clean commits 

TLDR; Commit and push individual sub-modules first, and then do the same in the parent repo.

Set up this alias once. This alias will get added to your repo-local `.git/config`

```bash
git config alias.supercommit '!./supercommit.sh "$@"; #'
```

| Note: This will add and commit everything, which may be you do not want sometimes.

Then to commit do:
```bash
git supercommit "some message"
```

```bash
cat ./supercommit.sh
#!/bin/bash -e
if [ -z "$1" ]; then
    echo "You need to provide a commit message"
    exit
fi

git submodule foreach "
    git add -A .
    git update-index --refresh
    commits=\$(git diff-index HEAD)
    if [ ! -z \"\$commits\" ]; then
        git commit -am \"$1\"
    fi"

git add -A .
git commit -am "$1"
```

## Replicating 3PO

In this directory we will try to start implementing 3PO from the paper https://arxiv.org/pdf/2207.07688.pdf

## Part 1 - We start by implementing the tracer 


- Rough outline of tracer

```angular2html
 𝑚𝑖𝑐𝑟𝑜𝑠𝑒𝑡 = { }
 def on_page_fault(page p):
   // record access to p
    if size of microset == MICROSET_SIZE:
        // start a new microset
        for p’ in microset:
            append 𝑝′ to trace
            clear present bit for 𝑝'
        𝑚𝑖𝑐𝑟𝑜𝑠𝑒𝑡 = { }
   add 𝑝 to 𝑚𝑖𝑐𝑟𝑜𝑠𝑒𝑡

  // resolve page fault
    if p’s 3PO bit is set:
          // skip normal page-fault handling
          set 𝑝’s present bit
    else:
          // first access to p
          set 𝑝’s 3PO bit
          run normal page-fault handling
    return
```

- Starting easy, we first try to use eBPF to catch the pagefault and help in tracing.
- this way we don't have to rebuild the kernel again and again. 
- Need to find a way to record the page fault.
- Next we need to see how to extract the structure of Page Table Entry (PTE) of the faulted page, and how to make use of additional bits for 3PO bit and make page as present. 
- We need to then figure out how to record trace in a file, in a format useable by the tape generator.
- Add in microset functionality. 
- Get final trace 




## Part 2 - Generate the tape

- Need to simulate eviction and 
## Part 3 Replicate results

- we need to write workloads, like matrix operations etc. We should write this sooner, rather than later. 




