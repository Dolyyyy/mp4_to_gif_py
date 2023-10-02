import imageio
import os

class TargetFormat(object):
    GIF = ".gif"
    MP4 = ".mp4"
    AVI = ".avi"

def convertFile(inputpath, targetFormat):
    """
    Converts a file from one format to another format.

    Parameters:
        inputpath (str): The path of the input file.
        targetFormat (str): The desired format for the output file.

    Returns:
        None
    """
    outputpath = os.path.splitext(inputpath)[0] + targetFormat
    print("Converting\r\n\t{0}\r\nto\r\n\t{1}".format(inputpath, outputpath))

    reader = imageio.get_reader(inputpath)
    duration = 1.0 / reader.get_meta_data()['fps'] * 1000

    writer = imageio.get_writer(outputpath, duration=duration)
    for i, im in enumerate(reader):
        writer.append_data(im)
    writer.close()
    print("Done.")

def convert_mp4_files_in_directory(directory):
    """
    Converts all MP4 files in the specified directory to GIF format.

    Parameters:
    - directory (str): The path to the directory containing the MP4 files.

    Returns:
    - None
    """
    for filename in os.listdir(directory):
        if filename.endswith(".mp4"):
            input_file = os.path.join(directory, filename)
            output_file = os.path.splitext(input_file)[0] + TargetFormat.GIF
            if not os.path.exists(output_file):
                convertFile(input_file, TargetFormat.GIF)

if __name__ == "__main__":
    current_directory = os.getcwd()
    convert_mp4_files_in_directory(current_directory)
