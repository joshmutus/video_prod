"""Tests for move_even_odd."""
import pytest
import move_even_odd
import os
import shutil

@pytest.fixture(scope="session")
def make_files():
  print('setting up')
  test_path = os.path.join(os.getcwd(),'test')
  if not os.path.exists(test_path):
    os.makedirs(test_path)
  for i in range(101):
    open(os.path.join(test_path,'IMG{}.foo'.format(i)),'a').close()
  return test_path

# def teardown_function(make_files):
#   print(make_files)
#   shutil.rmtree(make_files)
#   print('tearing down')

def test_get_file_no():
  fn = "IMG11122233.jpeg"
  num = move_even_odd.get_file_no(fn)
  assert num == 11122233


def test_create_new_paths(make_files):
  print(make_files)
  assert 1 == 1
