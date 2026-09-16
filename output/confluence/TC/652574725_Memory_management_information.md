---
id: confluence:652574725
source: confluence
type: page
space: TC
title: Memory management information
author: Richard van Klaveren
date: '2025-03-04'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/652574725
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/652574725
---
# Memory management information

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/652574725  

## Content

## Operating system level memory use

When viewing process information on a Linux system, various memory statistics are available. To understand the JVM memory usage, it is useful to understand the operating system memory statistics.

### Virtual size

The virtual size, virtual image (`VIRT` column in top) counts the total process image size. These are all the bytes in use, whether they are code or data, swapped or not. Important to note is that this number also includes shared memory, so it might *not* be an accurate reflection of memory use.

### Swapped size

The swapped size, `SWAP` column in top, counts the memory that is swapped out to disk.

### Resident size

The resident size, or resident set (`RES` column in top, often also called RSS) counts the physical memory that the task actually uses (including shared memory).

This is sometimes further split into text resident set (TRS), also called the code segment, which contains the executable code of the process, and the data resident set (DRS), containing modifiable data (i.e., heap space and stack)

### Shared memory

The shared memory complicates issues when you accurately want to determine memory usage. These are pages of memory that could potentially be shared among processes. Usually these are things like shared libraries, which are used by multiple processes. A good example is `glibc`, which is used by almost every process on a Linux system. Such a library is shared in memory by multiple processes by virtual memory management. The memory is counted, however, as belonging to the code segment, and is thus part of both the RSS and virtual size of a process.

### Committed vs. reserved

In some cases, a distinction is made between committed and reserved memory. Committed memory is memory that an application has requested (i.e., using `malloc()`), and reserved memory is memory that has actually been used. This is a side effect of the lazy memory allocation policy usually employed: if an application requests memory, virtual pages are assigned to the process, but not actually mapped to either memory or swap. Only when such pages are written to are they claimed (reserved).

## JVM memory use

Within a Java process, different memory types can be distinguished as well. From the types above, we will be focussing on the data segment, as the code segment contains the (native) code of the JVM itself, on which we have no influence.

### Heap space

The heap is where 'normal' objects are allocated during execution of an application, and usually takes up the bulk of the memory use of a Java application. The JVM allocates a pool of heap space at startup, and whenever an object is constructed some heap space is used for this. When a certain threshold is reached, the garbage collector kicks in, and tries to find objects in the heap that are not referenced by the executing process. Space taken up by such objects is returned to the free heap space. If not enough heap space can be freed by the garbage collector, the heap space in use is increased.

An important point here is that unused heap space is free from the perspective of the JVM, but not from the perspective of the operating system or container in which the JVM is running: the space is claimed by the JVM for future use, so it is part of the memory usage of the JVM.

### Metaspace

The metaspace (which was called *permanent generation* in older VMs) contains class metadata. In the past, you would in some cases go out of permanent generation memory, but the metaspace increases automatically, and will not go out of memory unless OS limits are reached. Usually, the metaspace does not take up a significant part of the memory usage.

### Stack space

For every thread, the JVM allocates memory for local variables. As these are pointers and primitive types (the actual object itself is stored on the heap) the stack is not very big. However, the more threads are created, the more stack space is used.

### Native memory usage

The JVM internals also use some memory, but this is usually not a problem. One area of attention are resource leaks, as these can cause significant native memory usage. An example would be not closing files properly: this triggers memory leaks in the native code underlying filesystem i/o.

## Tuning JVM memory usage

To influence and optimize memory usage, there are two different and complementary approaches you can use.

### Memory optimization

The first step is usually to optimize application memory usage, by looking for memory leaks or inefficient uses of memory, and eliminating these. `jvisualvm` is the tool of choice here, as it can give very good insight into what is using memory. One of the better ways to do this is the *heap dump* functionality. This works best if performed twice, with sufficient interval, or with sufficient triggering of suspect code. Perform an initial heap dump, wait a while, or trigger code which you believe is suspect, and perform a second heap dump. On the second heap dump, it is possible to make a comparison with the earlier heap dump. This gives you insight in memory allocated between the two heap dumps. If there is a leak, this should be really noticeable in the heap dump difference.

If you are troubleshooting an application deployed on Heroku, you can `heroku plugins:install heroku-cli-java`, and then `heroku java:jvisualvm -a <application name>` to fire up an instance of `jvisualvm` connected to your deployed application.

### Memory size and parameter tuning

If the used heap space is sufficiently low (after garbage collection), heap size tuning can be a useful second step, especially on platforms with limited amount of available memory (Heroku...). In this step, you can control how big the allocated heap will grow, when it will grow, and when garbage collection kicks in.

* The *minimal/initial heap size* (JVM option: `-Xms`) determines how big the initial heap allocation is. The heap will never shrink below this size. This is mainly a (startup) performance thing: if it is known that the heap will grow to a rather large size, it can be beneficial to increase the initial heap size. This can avoid several reallocations at startup.
* The *maximal heap size* (JVM option: `-Xmx`) determines how big the heap can maximally be. This is the most important 'knob' you have to limit memory usage: if the maximal heap size is reached, and there is no more unallocated space on the heap, allocations will trigger an out of memory exception. Note however that this is *not* the same as the maximal RSS size, as next to heap, there is also stack usage, metaspace, and native memory usage!
* The *stack size* (JVM option: '-Xss') specifies the stack size for each thread (the default is 1024k on 64-bit platforms). This is a fixed size, and allocated for each thread. This means that with the default 1024k stack size, a process with 50 threads consumes 50Mb memory alone for the stacks for all the threads.

For applications that usually have moderate memory usage, but sometimes experience spikes, there are some additional tuning parameters.

* The *maximum heap free ratio* (JVM option: `-XX:MaxHeapFreeRatio=##`) determines how much free heap space there may maximally be (expressed as a percentage, the default is 70%). If more than this percentage of the heap is free, the available heap space is reduced. This gives the memory back to the operating system, which reduces the RSS of the process.
* The *minimal heap free ratio* (JVM option: `-XX:MinHeapFreeRatio=##`) determines how little free heap space there may minimally be (expressed as a percentage, the default is 40%). If less than this percentage of the heap is free, the available heap space is increased. This claims additional memory from the operating system, which increases the RSS of the process.

An example combination would be `-Xmx300m -Xss384k -XX:MaxHeapFreeRatio=50 -XX:MinHeapFreeRatio=15`

### Garbage collector selection and tuning

As a last resort, it is also possible to influence the garbage collector itself. If reducing the RSS is your goal, the max/min free ratios should be adjusted first, as otherwise, you will end up with a slightly higher percentage of free heap, but the total heap usage will *not* be reduced, except if the usage falls below the max heap free ratio. I haven't experimented with these options yet, feel free to add details!