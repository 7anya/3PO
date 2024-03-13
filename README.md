# 3PO

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




