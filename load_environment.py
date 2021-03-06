# File: load_environment.py

# Chose which version to use. This is the new, the last stable old 1.13.1
!pip install tensorflow-gpu==2.0.0a0

from __future__ import absolute_import, division, print_function, unicode_literals

# TensorFlow and tf.keras
import tensorflow as tf
from tensorflow import keras
# Check which version is installed
tf.__version__

# Helper (python) libraries
import numpy as np
import matplotlib.pyplot as plt

# To supress the debugging output
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
'''
0 = all messages are logged (default behavior)
1 = INFO messages are not printed
2 = INFO and WARNING messages are not printed
3 = INFO, WARNING, and ERROR messages are not printed
'''
