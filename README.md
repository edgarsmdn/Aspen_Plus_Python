# Aspen Plus-Python connection example

This repo contains an Aspen Plus-Python connection example.

Differently from Aspen-HYSYS, accesing the variable paths in Aspen Plus is very straight forward. Therefore, the connection can be made directly easily (without the spreadsheets trick of the [Aspen_HYSYS_Python repo](https://github.com/edgarsmdn/Aspen_HYSYS_Python)).

<img align="center" src="https://github.com/edgarsmdn/Aspen_Plus_Python/blob/main/media/Aspen_plus_python.PNG" width="1000">

The code is just a couple of lines long that are self-explanatory and have comments too.

This is an example of where you might want to look for the variable paths of interest:

<img align="center" src="https://github.com/edgarsmdn/Aspen_Plus_Python/blob/main/media/path_example.PNG" width="500">

To get the path of the variable of interest, there is a small trick to that can be done to avoid looking through the variable tree manually(time intense). You can just copy the variable of interest such as a the mole fraction of heptane, go to Variable Explorer, and click on "Find Clipboard Variable" to be redirected automatically to the correct path by Aspen Plus.

<img align="center" src="https://github.com/A-JMinor/Aspen_Plus_Python/blob/main/media/copy.PNG" width="500">

<img align="center" src="https://github.com/A-JMinor/Aspen_Plus_Python/blob/main/media/findvariable.PNG" width="500">

## License

This repository contains a [MIT LICENSE](https://github.com/edgarsmdn/Aspen_Plus_Python/blob/main/LICENSE)
