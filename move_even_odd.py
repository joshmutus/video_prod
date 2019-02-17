"""
Move odd and even files into subfolder.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import os
import sys
import argparse
import shutil

def list_files(path):
  onlyfiles = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
  return onlyfiles

def move_file(filename, path):
  """Move a file to a relative path."""
  if not os.path.exists(path):
    os.makedirs(path)
  og_loc = os.path.join(os.getcwd(), filename)
  new_loc = os.path.join(path, filename)
  shutil.move(og_loc, new_loc)

def main(argv):
  parser = argparse.ArgumentParser()
  parser.add_argument('--output')
  args = parser.parse_args()
  print(args)
  print(list_files(os.getcwd()))
  file_list = list_files(os.getcwd())
  odd_dir = os.path.join(os.getcwd(),'odd')
  even_dir = os.path.join(os.getcwd(), 'even')
  for idx, f in enumerate(file_list):
    if idx%2 == 0:
      move_file(f, even_dir)
    else:
      move_file(f, odd_dir)

if __name__ == '__main__':
  main(sys.argv)

