
# --- 

import pandas as pd

def load_csv(file_name, file_route, **args):
    """
    """ 

    data = pd.read_csv(file_route + file_name)

    return data

