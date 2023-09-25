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
            "%0.2e" % sum(sample.reads),
            "%0.2e" % sample.reads_on_target,
            sample.min_reads,
            sample.max_reads,
            sample.mean_reads,
        )
    )
