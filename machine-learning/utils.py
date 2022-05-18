import os
import joblib

def load(model_path):
    # print('loading %s ...' % (model_path))
    if os.path.isfile(model_path):
        return joblib.load(model_path)
    else:
        return None
        raise Exception(f"Not found model: {model_path}")

def save(model, path):
    # print('saving %s ...' % (path))
    joblib.dump(model, path, compress=True)
    return

def mkdir(dir):
    if (os.path.exists(dir) == False):
        os.mkdir(dir)