#!/usr/bin/env python

import sys
import csv

from data import SAMPLES

writerow = csv.writer(sys.stdout, delimiter="\t").writerow

for sample in SAMPLES:
    writerow(
        (
            sample.id,
            f"{sample.ct:.02f}",
            sum(sample.reads),
            sample.reads_on_target,
            sample.min_reads,
            sample.max_reads,
            sample.mean_reads,
        )
    )
