#!/usr/bin/env sh

pip install --user coverage -U
pip install --user "python-dateutil>=2" -U

python -m coverage run -m unittest discover || exit 1
python -m coverage xml -i || exit 1

[ -f coverage.xml ] || exit 1
