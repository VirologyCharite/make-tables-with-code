test:
	pytest

# Run all the scripts and chuck away the output, to verify it all runs
# without error.
run:
	./00-print-table.py > /dev/null
	./01-print-with-commas.py > /dev/null
	./02-print-humanized.py > /dev/null
	./03-print-scientific.py > /dev/null
	./04-print-with-decimals.py > /dev/null
	./05-print-sorted.py > /dev/null
	./06-print-with-date.py > /dev/null
	./07-print-with-row-numbers.py > /dev/null

plots:
	./plot-on-target.py
	./plot-pie-chart.py

clean:
	rm -fr plot-on-target.pdf plot-pie-chart.pdf data.tsv __pycache__ .mypy_cache .pytest_cache *~
