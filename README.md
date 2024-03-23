# Video Converter

This script converts video files from one format to another using the MoviePy library. It provides a simple command-line interface to specify input and output files, output format, and whether to use high quality conversion (just for .mp4)

## How to Use

1. **Installation:**
   - Make sure you have the requirements installed. You can install them via pip:
     ```
     pip install moviepy
     pip install argparse
     ```

2. **Usage:**

- `-i`, `--input`: Name of the input file (required).
- `-o`, `--output`: Name of the output file (optional).
- `-f`, `--format`: Format of the output file (optional, default: mp4).
- `-hq`, `--high_quality`: Use high quality codec (optional, default: True).

## Example
```
python video_converter.py -i input_video.webm -o output_video.mp4 -f mp4 -hq True
```
