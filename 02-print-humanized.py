#!/usr/bin/env python

import sys
import csv
from humanize import metric

from data import SAMPLES

writerow = csv.writer(sys.stdout, delimiter="\t").writerow

for sample in SAMPLES:
    writerow(
        (
            sample.id,
            sample.ct,
            metric(sum(sample.reads)),
            sample.reads_on_target,
            metric(sample.min_reads),
            metric(sample.max_reads),
            metric(sample.mean_reads),
        )
    )
