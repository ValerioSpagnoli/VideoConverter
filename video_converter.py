from moviepy.editor import VideoFileClip
import argparse

def video_converter(input_file, output_file, output_format, high_quality=False):

    low_quality_mp4_codec = 'libx264'
    high_quality_mp4_codec = 'mpeg4'
    avi_codec = 'rawvideo'
    png_codec = 'png'

    if output_format == 'mp4' and high_quality:
        codec = high_quality_mp4_codec
    elif output_format == 'mp4' and not high_quality:
        codec = low_quality_mp4_codec
    elif output_format == 'avi':
        codec = avi_codec
    elif output_format == 'png':
        codec = png_codec
    else:
        raise ValueError("Invalid output format. Please use 'mp4', 'avi', or 'png'.")
    
    try:
        video = VideoFileClip(input_file)
        video.write_videofile(output_file, codec=codec, audio_codec='aac')
        print("Conversion completed successfully!")
    except Exception as e:
        raise ValueError("Error during conversion: ", e)


parser = argparse.ArgumentParser(description='Convert WebM video to MP4 format')
parser.add_argument('-i', '--input', help='Name of the input file', required=True)
parser.add_argument('-o', '--output', help='Name of the output file', required=False)
parser.add_argument('-f', '--format', help='Format of the output file', required=False, default='mp4')
parser.add_argument('-hq', '--high_quality', help='Use high quality codec', required=False, default=True)

args = parser.parse_args()

path_input_file = args.input    
name_input_file = args.input.split(".")[0]
name_output_file = args.output
output_format = args.format
high_quality = args.high_quality

if not name_output_file:
    path_output_file = name_input_file + "." + output_format
else:
    path_output_file = name_output_file + "." + output_format

print("Input file: ", path_input_file)
print("Output file: ", path_output_file)
print("Output format: ", output_format)
print("High quality: ", high_quality)
    
video_converter(path_input_file, path_output_file, output_format, high_quality)
