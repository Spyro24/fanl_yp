# fanl_yp
A python fanfile loader lib based on [Proxydyzed's](https://github.com/proxydyzed) [edacnaF](https://github.com/proxydyzed/edacnaF) with a few extras

## Overview
* [Requirements](#requirements)
* [Setup](#setup)
* [TODO](#todo)

## Requirements
A working Python 3.12 (or later) installation

## Setup
Simply clone this repo with `git clone https://github.com/Spyro24/fanl_yp.git` and than copy the fanl_yp folder that is included in this repo in to your project root.

## Examples
### Simple fanfile info script (Example how to read a fanfile)
```python3
import zlib
import fanl_yp

#Open the Fanfile
fanfile = open("path/to/fanfile", "br")

#Load the game
game = fanl_yp.decode.decode(zlib.decompress(fanfile.read()))

title = game.title
description = game.description
author = game.author
objectCount = len(game.objectContainers)
indexOffset = game.indexOffset

#Print the infos
print(f"Game Title: {title}")
print(f"Game Description: {description}")
print(f"Author: {author}")
print(f"Object Count: {str(objectCount)}")
print(f"Index Offset: {str(indexOffset)}")

#Cleanup
fanfile.close()
```

## TODO

- [ ] Finish this README
- [ ] Add all 33 colors as a RGB value to the color palette (incl there name and ID)
- [ ] Add Example scripts
