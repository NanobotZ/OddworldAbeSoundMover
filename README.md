# OddworldAbeSoundMover
Python tool for moving sounds between levels for PC versions of games:
- Abe's Oddysee
- Abe's Exoddus  

This tool is very **work-in-progress** and not well tested, **make sure to keep backups of files you'll be editing**.

# Usage
First you must run `python -m pip install -r requirements.txt`  
To launch the tool run `python sound_mover.py`.

# Notes
VH files this tool targets are stored inside the `.lvl` files for each game's level.  
After using this tool, you must repack the level's files into a `.lvl` file for the game to be able to pick it up.  
Use [LVL Extractor / Builder](https://aliveteam.github.io/legacy) to unpack and then repack the level.

# Python Requirements
- [FreeSimpleGUI](https://github.com/spyoungtech/FreeSimpleGUI)

# Credits
- Huge thanks to the contributors of [R.E.L.I.V.E](https://github.com/AliveTeam/alive_reversing/). This tool wouldn't exist without their reverse engineering efforts.