from setuptools import setup, find_packages
import site

setup(
    name='parquet_tree_browser_using_ipyaggrid',
    version='0.0.1',
    description='A Jupyter browser widget for hive partitioned parquet trees using ipyaggrid.',
    url='http://github.com/mister-average/parquet_tree_browser_using_ipyaggrid',
    author='mister-average',
    author_email='mister_person@averageaddress.com',
    license='BSD',
    data_files=[('/', ['parquet_tree_browser_using_ipyaggrid.ipynb'])],
    python_requires='>=3.9'
)
