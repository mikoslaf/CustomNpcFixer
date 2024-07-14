# Project CustomNpcFixer - Mob Cloner

## Helper for Minecraft Mod [CustomNPC](https://www.curseforge.com/minecraft/mc-mods/custom-npcs)

This program provides a solution for problems with skin URLs from [Imgur](https://imgur.com/) (a popular website for uploading small images). 
On my Minecraft server, for some reason, the skins on my NPCs stopped working. 
I had to change every skin URL to another host, such as [imgBB](https://imgbb.com/), so I created this program.

## Features

- Automatically uploads NPC skins to imgBB.
- Updates skin URLs in NPC files.
- Provides a summary of how many links were changed.
- Extra function to change specific options for all NPCs.

## How it works

1. The program retrieves skin images for your NPCs from the Mob Cloner and uploads these images to [imgBB](https://imgbb.com/).
2. In the second step, the program gets the new links and updates them in your NPC files.
3. Finally, the program provides information about how many links were changed.

## Installation

### Requirements

- [Python 3.12](https://www.python.org/)
- [Python requests](https://pypi.org/project/requests/)
- [Python dotenv](https://pypi.org/project/python-dotenv/)

### Steps:

1. Go to your Minecraft files.
2. Find the `customnpcs` folder.
3. Download the [latest version](https://github.com/mikoslaf/CustomNpcFixer_Mob-Cloner/releases/tag/v1).
4. Drop the program files into this folder or move the `clones` folder to another location and do it there.

   ![image](https://github.com/user-attachments/assets/27091486-1ae3-4e1c-a619-e56ef2e57967)

5. Go to [API ImgBB](https://api.imgbb.com/) to get an API key.
6. Create a `.env` file similar to `.env.example` and input your API key.
7. Open CMD and run `main.py` using Python.
8. Wait for information like this:

   ![image](https://github.com/user-attachments/assets/948558c8-6273-4d2b-8be5-515e118cf107)

## Extra Information

### Extra function: `change_something`

I added an extra function called `change_something`. If you want to change some option in all your NPCs, you can use it.

### How to use it

1. Firstly, you need to find how the option you want to change looks.
   - Example: `'"ReturnToStart": 1b,'` sets `ReturnToStart` to `NO`.
2. In the second step, you need to find how it looks after the change.
   - Set up one of your NPCs correctly and copy its settings.
   - Example: `'"ReturnToStart": 0b,'` sets `ReturnToStart` to `YES`.
3. Just in case, I recommend making a copy of your `clones` folder, before proceeding to the next step.
4. Run the code again. Now you should see a second message about changing the files.
