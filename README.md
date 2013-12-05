TCP/UDP protocol research
========================================

Research of socket programming. All programs tested under Debian Squeeze.

## Build

This implementation requires:
* python 2.7.* to be installed
* virtualenv package to be installed (if you don't want to mess your environment with my modules)

To install virtualenv just run
 `sudo pip install virtualenv`

Then you can run `make`

## Usage
To run server or client you may want to run any of launchers from `bin` directory. This is set of hardcoded options for each laboratory work. If you want to run server manually, please remember that we are using `virtualenv`, so you need to run `./env/bin/python server ...`.

**Note**: Programs uses ``logging`` module, so if you need to see all debug stuff, you'll need to run program you want with ``--verbose`` flag

To generate random file of fixed size you may want to use command `head -c 100000 /dev/urandom > dummy`, which will generate file `dummy` with size of 100000 bytes