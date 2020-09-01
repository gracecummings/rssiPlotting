# rssiPlotting
scripts to handle the many ways we need to plot stuff during 2020 rssi investigations

## Notes for Usage
Both `jay_plotter.py` and `server_plotter.py` require `python3` with `numpy`, `matplotlib`, and `pandas` installed. The script `jay_plotter.py` takes two command line arguments
* `-r [rbx]` This is the float number of the RBx you wish to plot, encode +/- side info as sign on integer. Currently buggy can cannot pick out sign.
* `-f [path to text file]` Takes the path to the text file with the script monitoring output
Right now, the output of the script needs to be modified to remove the `HEM` and `HEP` prefixes to the RBXs. It encodes this info with sign, but pull the sign out currently is broken, so beware!
