import os

base_dir = dir_path = os.path.abspath(
    os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)
)
data_dir = os.path.join(base_dir, 'data')
output_dir = os.path.join(base_dir, 'output')
