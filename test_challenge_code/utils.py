import os
import hdf5storage

def save_matv73(mat_name, var_name, var):
    # Ensure the directory exists
    os.makedirs(os.path.dirname(mat_name), exist_ok=True)
    
    hdf5storage.savemat(mat_name, {var_name: var}, format='7.3', store_python_metadata=True)
