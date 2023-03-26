import numpy as np

def calculate(list):

  axis1 = int(list[3]),int(list[4]),int(list[5])
  axis2 = int(list[1]),int(list[5]),int(list[7])
  flattened = 0
  
  return {
  'mean': [axis1, axis2, flattened],
  'variance': [axis1, axis2, flattened],
  'standard deviation': [axis1, axis2, flattened],
  'max': [axis1, axis2, flattened],
  'min': [axis1, axis2, flattened],
  'sum': [axis1, axis2, flattened]
}