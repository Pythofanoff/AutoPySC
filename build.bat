cls 
color 3
echo Install apysc...
color f
python -m pip uninstall apysc -y
python -m pip install -e .
color 3
echo apycs sucefull installed!
color f