#!/bin/bash

#Unit test
python -m unittest wwoproxy.tests.test
#Integration test
python -m unittest wwoproxy.tests.int_test
