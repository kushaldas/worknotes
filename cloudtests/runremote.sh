#!/bin/sh

fab --hide=output -H $1 --port 22 --user fedora alltasks

