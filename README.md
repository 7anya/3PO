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
   add 𝑝 to𝑚𝑖𝑐𝑟𝑜𝑠𝑒𝑡

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

## Part 2 - Generate the tape

## Replicate results 




