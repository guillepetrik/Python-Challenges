#!/bin/python3

from datetime import datetime as dt

# Complete the time_delta function below.

def time_delta(t1, t2):
        # Parse the first timestamp
        fi = dt.strptime(t1, "%a %d %b %Y %H:%M:%S %z")
        # Parse the second timestamp
        si = dt.strptime(t2, "%a %d %b %Y %H:%M:%S %z")
        
        # Calculate the absolute difference in seconds
        return  str(abs(int((fi - si).total_seconds())))

