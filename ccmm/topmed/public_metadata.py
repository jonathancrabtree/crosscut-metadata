#!/usr/bin/env python3

import ccmm.dbgap.public_metadata 
import logging

# Read all dbGaP XML metadata files in a given directory and read and parse their contents.
def read_study_metadata(dir):
    return ccmm.dbgap.public_metadata.read_study_metadata(dir)
