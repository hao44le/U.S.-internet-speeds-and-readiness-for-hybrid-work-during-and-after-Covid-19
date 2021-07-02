wget https://repo.anaconda.com/archive/Anaconda3-2021.04-Linux-x86_64.sh
bash Anaconda3-2021.04-Linux-x86_64.sh

conda create -n branch-env python=3.7
source activate branch-env

conda install geopandas
conda install -c conda-forge pyogrio
conda install -c conda-forge descartes
conda install -c conda-forge gdal
