TCP/UDP protocol research
========================================

Research of socket programming. All programs tested under Debian Squeeze. Please see [architecture overview](blob/master/Architecture.md)

## Build instruction and requirements
This implementation requires:
* python 2.7.* to be installed
* virtualenv package to be installed (you don't want to mess your environment with my modules, are you?)

To install virtualenv just run
 `sudo pip install virtualenv`

Then you can run `make install`

## Running tests
just run `make test` to execute all unit tests. Each test run requires environment reinitialization.

## Running examples
As we are using virtual environment, we need to run all of our examples through `env/bin/python`. Global activation of environment just does not work yet.

## Notes
All examples uses ``logging`` module, so if you need to see all debug stuff, you'll need to run program you want with ``--verbose`` flag

To generate random file of fixed size you may want to use command `head -c 100000 /dev/urandom > dummy`, which will generate file `dummy` with size of 100000 bytes