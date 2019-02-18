"""
Move odd and even files into subfolder.

usage:
  python move_even_odd.py --path /path/to/folder
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import os
import re
import sys
import argparse
import shutil

def list_files(path):
  """Takes n ls and returns the files not the folders."""
  onlyfiles = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
  return onlyfiles

def move_file(filename, old_path, new_path):
  """Move a file to a relative path."""
  if not os.path.exists(new_path):
    os.makedirs(new_path)
  og_loc = os.path.join(old_path, filename)
  new_loc = os.path.join(new_path, filename)
  shutil.move(og_loc, new_loc)

def create_paths(root_path):
  """Creates input and output paths."""
  odd_dir = os.path.join(root_path,'odd')
  even_dir = os.path.join(root_path, 'even')
  return odd_dir, even_dir

def get_file_no(fname):
  """Returns the number label of a given image file."""
  res = re.findall(r'\d+', fname)
  return int(res[0])

def main(argv):
  parser = argparse.ArgumentParser()
  parser.add_argument('--path')
  args = parser.parse_args()
  print(args)
  print(args.path)
  print(list_files(args.path))
  file_list = list_files(args.path)
  odd_dir, even_dir = create_paths(args.path)
  for f in file_list:
    if get_file_no(f)%2 == 0:
      move_file(f, args.path, even_dir)
    else:
      move_file(f, args.path, odd_dir)

if __name__ == '__main__':
  main(sys.argv)

