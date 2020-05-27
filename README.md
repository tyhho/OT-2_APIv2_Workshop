# OT-2_APIv2_Workshop

This repository stores workshop materials for "Introduction to OT-2 APIv2" workshops. The workshops are designed for biologists with little to no programming experiences in Python. The goal is to allow participants to 1) set up their protocols from scratch, and 2) debug their own protocols.

## Dependency
The Opentrons package.

## Structure
The workshops are roughly divided into 3 sections. Our approach is: **First you make it work, then you make it work bettter**.

Note that the duration is not final.

## 1. Elementary Python for OT-2 API (~3 hours)
Covers topics on: installation of Anaconda and navigation within the Spyder IDE, basic syntax, basic variables, lists and dictionaries, basic string manipulation, simple custom functions, for loops, and the superficial concept of object-oriented programming (without details). It covers the minimal amount of materials for understanding and programming in the OT-2 APIv2.

Relevant files:
Python exercises with solutions.ipynb

## 2. A beginner's approach to OT-2 APIv2 Part I (~3 hours)
The workshop introduces participants to the Opentrons OT-2 API (version 2), which can be written and simulated without a physical robot. It is designed for participants comfortable with basic Python. Topics covered: APIv2 documentation and where to seek help, setting up an environment within an IDE for drafting and debugging a protocol, loading pipettes and labwares, method of accessing wells in labwares, the pipette.transfer() function, scaling up by for-loops, formating the script for execution and exporting simulated output commands for documentation. It is a recommended approach from start to finish.

Relevant files:

Test_script.py (Example executable script for uploading to an OT-2)

simulate.py (A standalone Python script for proper simulation of OT-2 executable scripts)

Test_script_log.txt (Example output file from simulation of the example executable script)

## 3. A beginner's approach to OT-2 APIv2 Part II (~ 1.5 hours)
This workshop goes into the customizations of protocols to make them pratical. It covers: customizations for liquid transfers, building block commands, suggestions for reusable protocols and manual integration with Excel to generate transfer commands.

Relevant files:

Example_Excel_for_Python-parsable_commands.xlsx (Example Excel file for generating transfer commands)

## License
Licensed under CC-BY-SA 4.0
