# DeLevo Port Scanner
If you found this application interesting or useful, please consider starring the repo above.

## Usage
1. Download Python from [here](https://python.org/downloads) if you haven't already. It is necessary for running the Python script.
2. Use [this link](https://github.com/walesworksltd/portscanner/releases/download/v2-py/portscanner.py) to download the Python script, or [this link](https://github.com/walesworksltd/portscanner/releases/download/v2-win/portscanner.exe) to download the Windows application.
3. Use [this link](https://github.com/walesworksltd/portscanner/releases/download/v2-win/portscanner.png) to download the asset image. Save this image in the same directory as the software downloaded in the last step.
4. Right-click the Python script, then select "Open With", then "Python IDLE". After that, select "Run" in the menu bar and then "Run as module" to run the script. Please note that double-clicking the Python script will **not** allow it to work properly!
5. Double click the Windows application to open it.

## Tips
- Be patient while waiting for the results. The software scans for all ports, from 1 to 65535, so it can take a while.

## Drawbacks
- The colored terminal text will not show up in IDLE, but will instead be printed as seemingly-random characters:
- <img width="517" alt="Screenshot 2022-04-18 at 12 06 04 AM" src="https://user-images.githubusercontent.com/87256750/163722789-3b09a469-c332-46a3-958e-cee3b8f2fa59.png">
- Despite that, you can still read the useful text.

## Implementation
- The software simply scans for ports 65535 times on any given IP address, but the UI makes it much easier to use than some other tools out there.
