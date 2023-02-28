#!/usr/bin/env python3
import random

import atheris
import sys
import fuzz_helpers
import random

with atheris.instrument_imports(include=['markovify']):
    import markovify

def TestOneInput(data):
    fdp = fuzz_helpers.EnhancedFuzzedDataProvider(data)
    try:
        text_model = markovify.Text(fdp.ConsumeRemainingString())
        text_model.make_short_sentence(fdp.ConsumeIntInRange(0, 1000))
    except KeyError:
        return -1
def main():
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()


if __name__ == "__main__":
    main()
