@echo off


:start
cls

set python_ver=36

python ./get-pip.py

cd \
cd \python%python_ver%\Scripts\
pip install pydub
pip install ffmpeg
pip install requests~=2.28.1
pip install numpy~=1.22.4
pip install tqdm~=4.64.1
pip install matplotlib~=3.6.2
pip install PyWavelets
pip install cffi~=1.15.1
pip install Pillow~=9.3.0
pip install wheel~=0.38.4
pip install nltk~=3.7
pip install scipy~=1.9.3
pip install scikit-learn~=1.1.3
pip install click~=8.1.3
pip install pyparsing~=3.0.9
pip install pytz~=2022.6
pip install colorama~=0.4.6
pip install pandas~=1.5.2
pip install PyYAML~=6.0
pip install Babel~=2.11.0
pip install setuptools~=63.2.0
pip install jsonlines~=1.2.0
pip install dateparser~=1.1.5
pip install num2words~=0.5.12
pip install llvmlite~=0.38.1
pip install Pygments~=2.13.0
pip install psutil~=5.9.4
pip install Jinja2~=3.1.2
pip install ipykernel~=6.17.1
pip install Cython~=0.29.28
pip install pooch~=1.6.0
pip install packaging~=21.3
pip install appdirs~=1.4.4
pip install pysbd~=0.3.4
pip install tabulate~=0.9.0
pip install six~=1.16.0
pip install urllib3~=1.26.13
pip install coqpit~=0.0.17
pip install fsspec~=2022.11.0
pip install certifi~=2022.12.7
pip install threadpoolctl~=3.1.0
pip install trainer~=0.0.20
pip install soundfile~=0.11.0
pip install tensorboardX~=2.5.1
pip install tzlocal~=4.2
pip install python-dateutil~=2.8.2
pip install graphviz~=0.20.1
pip install contourpy~=1.0.6
pip install fonttools~=4.38.0
pip install pycparser~=2.21
pip install torchaudio~=0.13.1
pip install pyttsx3~=2.90

pause
exit