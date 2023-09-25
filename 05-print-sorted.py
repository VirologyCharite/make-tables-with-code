#!/usr/bin/env python

import sys
import csv
from operator import attrgetter

from data import SAMPLES

writerow = csv.writer(sys.stdout, delimiter="\t").writerow

for sample in sorted(SAMPLES, key=attrgetter("ct")):
    writerow(
        (
            sample.id,
            sample.ct,
            sum(sample.reads),
            sample.reads_on_target,
            sample.min_reads,
            sample.max_reads,
            sample.mean_reads,
        )
    )
