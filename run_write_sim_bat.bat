set WF="sim.bat"

del %WF%

python write_sim_bat.py %WF% data
python write_sim_bat.py %WF% data\src
python write_sim_bat.py %WF% data\src\src

