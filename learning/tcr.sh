#!/bin/bash

# This is a simple TCR setup for a Ruby-based project with 
# RSpec.

(rspec && git commit -am "WIP") || git checkout .

