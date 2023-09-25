#!/usr/bin/env python

import matplotlib.pyplot as plt
from datetime import date

from data import SAMPLES

x = []
y = []

for sample in SAMPLES:
    x.append(sample.date)
    y.append(100.0 * sample.reads_on_target / sum(sample.reads))


fig, ax = plt.subplots()
ax.scatter(x, y, s=8)
ax.tick_params(axis="x", labelrotation=10, labelsize=7)
ax.tick_params(axis="y", labelsize=7)

ax.set_title("Read percentage on target by date")
ax.set_xlabel("Date")
ax.set_ylabel("Percentage of reads on target")

fig.savefig("plot-on-target.pdf")
