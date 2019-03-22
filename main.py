# -*- coding:utf-8 -*-

"""
@author:bairubin
@file:main.py
@description:
@time:2019/3/16
"""

import eel
import cvs_process


@eel.expose  # Expose this function to Javascript
def say_hello_py(x):
  print('Hello from %s' % x)


def print_num(n):
  print('Got this from Javascript:', n)


@eel.expose  # Expose this function to Javascript
def handleinput(x):
  print('%s' % x)


@eel.expose
def line_data():
  data = [i for i in range(10)]
  print(data)
  return data


@eel.expose
def csv_title():
  header = cvs_process.get_header()
  print(header)
  return header


def start_eel(develop):
  """Start Eel with either production or development configuration"""
  if develop:
    directory = 'src'
    app = None
    page = {'port': 4200}
    flags = ['--auto-open-devtools-for-tabs']
  else:
    directory = 'dist'
    app = 'chrome-app'
    page = 'index.html'
    flags = []

  eel.init(directory, ['.tsx', '.ts', '.jsx', '.js', '.html'])

  # These will be queued until the first connection is made, but won't be repeated on a page reload
  say_hello_py('Python World!')
  # eel.say_hello_js('Python World!')  # Call a JavaScript function (must be after `eel.init()`)

  eel.start(page, size=(1280, 800), options={
    'mode': app,
    'port': 8000,
    'host': 'localhost',
    'chromeFlags': flags
  })


if __name__ == '__main__':
  # Pass any second argument to enable debugging. Production distribution can't receive arguments
  start_eel(develop=True)
