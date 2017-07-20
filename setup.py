#!/usr/bin/env python3
import os
from setuptools import setup
from setuptools.config import read_configuration
from pathlib import Path

thisDir=Path(__file__).parent
cfg = read_configuration(str(thisDir/'setup.cfg'))
#print(cfg)
cfg["options"].update(cfg["metadata"])
cfg=cfg["options"]

if __name__ == "__main__":
	setup(**cfg)