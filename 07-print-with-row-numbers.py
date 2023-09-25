#!/usr/bin/env python

import sys
import csv

from data import SAMPLES

writerow = csv.writer(sys.stdout, delimiter="\t").writerow

for count, sample in enumerate(SAMPLES, start=1):
    writerow(
        (
            count,
            sample.id,
            sample.ct,
            sum(sample.reads),
            sample.reads_on_target,
            sample.min_reads,
            sample.max_reads,
            sample.mean_reads,
        )
    )
