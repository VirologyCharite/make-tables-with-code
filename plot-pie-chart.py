#!/usr/bin/env python

import matplotlib.pyplot as plt
from collections import Counter

from data import SAMPLES

counts = Counter()

for sample in SAMPLES:
    counts[sample.country] += 1


fig, ax = plt.subplots()
ax.pie(counts.values(), labels=counts, autopct="%1.1f%%")

ax.set_title("Infection incidence by country")

fig.savefig("plot-pie-chart.pdf")
