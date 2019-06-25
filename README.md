# process-sorted-array
This is a performance test for processing sorted array problem on stackoverflow. The answer claimed processing sorted process is faster since fewer branch misses.
The experiment is observed by perf.

## Build
Make execution file for test.

    $ make

Open the execution permission of test.sh, a shell script to input perf command.
  
    $ chmod +x ./test.sh

Use test.sh to measure branch miss rate by perf. You can use -r flag to adjust the repeat times(the default value is 1000).

    $ ./test.sh [-r repeat-times]

## Orignal Problem
https://stackoverflow.com/questions/11227809/why-is-processing-a-sorted-array-faster-than-processing-an-unsorted-array
