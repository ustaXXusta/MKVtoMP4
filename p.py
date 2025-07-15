import ffmpeg
import sys
import os

def convert_mkv_to_mp4(input_file, output_file):
    try:
        # Check if input file exists
        if not os.path.exists(input_file):
            print(f"Error: Input file '{input_file}' does not exist.")
            return False

        # Verify input file is MKV
        if not input_file.lower().endswith('.mkv'):
            print("Error: Input file must be an MKV file.")
            return False

        # Define FFmpeg stream
        stream = ffmpeg.input(input_file)
        stream = ffmpeg.output(stream, output_file, c='copy', f='mp4')
        
        # Run FFmpeg conversion
        ffmpeg.run(stream, overwrite_output=True)
        print(f"Successfully converted '{input_file}' to '{output_file}'")
        return True

    except ffmpeg.Error as e:
        print(f"An error occurred: {e.stderr.decode()}")
        return False
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
        return False

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python mkv_to_mp4.py <input.mkv> <output.mp4>")
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        convert_mkv_to_mp4(input_file, output_file)