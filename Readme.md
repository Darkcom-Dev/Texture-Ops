# Texture Ops

Created for realize various operation over textures *.png for optimize videogames projects or 3D models.

## How to use

Clone the repository, and execute `python3 main.py`

## Improvments

- Added support for Image Preview.
- Unified all apps in only common system.
- Created Flowmap (Experimental).
- Created Channel Splitter in RGBA Textures.
- Created normal map generator from Gray scale texture.
- Created Gray scale from Normal map texture.
- Added Simple Noise Generator
- Added White Noise Generator
- Added Worley Noise Generator

## To Do

- Create ocean flowmap generator.
- Create Help Top level (partially created)
- Create manual of application use.

## Fixes

- Added Random seed to White and Worley Noise.
- Error in load textures from file dialog.
- Unscaled normal textures in preview.
- Standarize Save Texture Widget in all tops.
- get_channel_split manage missed channels with white channel.
- get_atlas manage missing textures adding alpha textures.

## Know issue

- 