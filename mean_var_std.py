import numpy as np

def calculate(list):
    if len(list) != 9:
      raise ValueError("List must contain nine numbers.")
    cal_array = np.array(list).reshape(3,3)

    calculations = {
      'mean' : [
          np.mean(cal_array, axis=0).tolist(),
          np.mean(cal_array, axis=1).tolist(), 
          np.mean(cal_array.flatten())
      ],
      'variance' : [
          np.var(cal_array, axis=0).tolist(), 
          np.var(cal_array, axis=1).tolist(), 
          np.var(cal_array.flatten())
      ],
      'standard deviation' : [
          np.std(cal_array, axis=0).tolist(), 
          np.std(cal_array, axis=1).tolist(), 
          np.std(cal_array.flatten())
      ],
      'max' : [
          np.max(cal_array, axis=0).tolist(), 
          np.max(cal_array, axis=1).tolist(), 
          np.max(cal_array.flatten())
      ],
      'min' : [
          np.min(cal_array, axis=0).tolist(), 
          np.min(cal_array, axis=1).tolist(), 
          np.min(cal_array.flatten())
      ],
      'sum' : [
          np.sum(cal_array, axis=0).tolist(), 
          np.sum(cal_array, axis=1).tolist(),  
          np.sum(cal_array.flatten())
      ]
  }
    return calculations
