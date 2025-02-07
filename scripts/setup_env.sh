#!/bin/bash

# Create conda environment
conda create -n interviewx python=3.8 -y
conda activate interviewx

# Install dependencies
pip install -r requirements.txt