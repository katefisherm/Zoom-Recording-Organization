# Zoom Recording Organizer

A Python script that automatically organizes Zoom recording files into dated folders.

## What it does

Takes messy Zoom downloads and organizes them into clean, dated folders. If you have multiple recordings from the same meeting series, it creates a separate folder for each date.

**Example:**
- Input: Random Zoom files in one folder
- Output: `Fundamentals L1 Cohort 35A_2024-12-01`, `Fundamentals L1 Cohort 35A_2024-12-03`, etc.

## Setup

1. **Install Python 3** (if you don't have it already)

2. **Download this script** to your computer

3. **Configure your path** - open `organize_zoom_files.py` and update line 6:
```python
   ZOOM_DIRECTORY = "/Users/yourname/Desktop/Zoom Downloads"
```
   Change this to wherever you want to put your Zoom files.

## How to use

1. **Download your Zoom recordings** from Zoom (can be multiple sessions)

2. **Move all the files** into the folder you specified in the script

3. **Run the script:**
```
   python organize_zoom_files.py
```

4. **Enter the meeting name** when prompted
   - Example: "Fundamentals L1 Cohort 35A"
   - Use the same name for all sessions in the same series

5. **Done!** Your files are now organized into dated folders

## What files it organizes

- Video recordings (.mp4)
- Audio files (.m4a)
- Transcripts (.vtt)
- Text files (.txt)

All other files are ignored.

## Requirements

- Python 3.x
- No additional libraries needed (uses standard Python modules)
