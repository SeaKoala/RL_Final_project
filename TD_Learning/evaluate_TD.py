#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  9 00:07:04 2022

@author: srinivas
"""
import os
from trainer import Trainer
import numpy as np

max_value_count = np.zeros((10,16))

for batch in range(10):
    
    trainer = Trainer(True, 500, 500)
    
    for episode in range(100):
        trainer = Trainer(False, 1000, 100)
        final_state = trainer.Game.getBoard()
        max_value = np.max(final_state)
        max_value_count[batch][max_value]  = max_value_count[batch][max_value] + 1