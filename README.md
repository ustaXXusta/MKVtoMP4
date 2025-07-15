# MKV to MP4 Converter

A simple Python script to convert MKV video files to MP4 format using FFmpeg. The script copies the video and audio streams without re-encoding, ensuring fast conversion with no quality loss.

## Features
- Converts MKV files to MP4 format
- Preserves original video and audio quality
- Simple command-line interface
- Error handling for invalid inputs or FFmpeg issues

## Prerequisites
- [FFmpeg](https://ffmpeg.org/download.html) installed on your system
- Python 3.x
- `ffmpeg-python` library (`pip install ffmpeg-python`)

## Installation
1. Install FFmpeg:
   - Windows: Download from FFmpeg website or use Chocolatey:
     ```bash
     choco install ffmpeg
     ```
   - macOS: Use Homebrew:
     ```bash
     brew install ffmpeg
     ```
   - Linux: Use your package manager (e.g., for Ubuntu):
     ```bash
     sudo apt install ffmpeg
     ```
2. Install the Python dependency:
   ```bash
   pip install ffmpeg-python
   ```
   
## Notes

The script assumes the MKV file contains MP4-compatible codecs (e.g., H.264 video, AAC audio).

If the input file has incompatible codecs, you may need to modify the script to include transcoding.

## License

MIT License

   
