import ascii_magic
import argparse

parser = argparse.ArgumentParser(description='caricature')
parser.add_argument('path', metavar='P', type=str, help='path img')

args = parser.parse_args()
path = args.path

print("print img")

try:
    caricature = ascii_magic.from_image_file(
        path,
        columns=110,
        back=ascii_magic.Back.BLACK
    )
    ascii_magic.to_terminal(caricature)
except Exception as e:
    print("error : ", e)