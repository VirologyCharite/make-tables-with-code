from data import SAMPLES


def testCount():
    "There must be 75 samples."
    assert len(SAMPLES) == 75


def testPrefix():
    "Sample ids must have the ChVir prefix."
    for sample in SAMPLES:
        assert sample.id.startswith("ChVir")


def testSorted():
    "Sample ids must be sorted."
    ids = [sample.id for sample in SAMPLES]
    assert ids == sorted(ids)


def testIntSuffix():
    "Sample ids must end with an integer."
    for sample in SAMPLES:
        # This fails if what follows "ChVir" is not an integer.
        int(sample.id[5:])


def testNoDuplicates():
    "There must be no duplicate sample ids."
    assert len(SAMPLES) == len(set(sample.id for sample in SAMPLES))


def testCtValues():
    "Ct values must be in a reasonable range."
    for sample in SAMPLES:
        assert 15 <= sample.ct <= 35


def testReadCounts():
    "Read counts must make sense."
    for sample in SAMPLES:
        assert 0 <= sample.min_reads <= sample.mean_reads <= sample.max_reads
        assert 0 < sample.reads_on_target <= sum(sample.reads)


def testGisaidIds():
    "GISAID ids must start with EPI_ISL_ and then have a (big) number."
    for sample in SAMPLES:
        assert sample.gisaid.startswith("EPI_ISL_")
        assert int(sample.gisaid[8:]) > 13880000


def testCountriesAreKnown():
    "All countries must be known."
    known = {"Australia", "Germany", "Ghana", "Spain"}
    for sample in SAMPLES:
        assert sample.country in known


from datetime import date


def testDates():
    "Dates must be after the start of the outbreak and can't be in the future."
    start = date(2022, 5, 19)
    now = date.today()
    for sample in SAMPLES:
        assert start < sample.date <= now
