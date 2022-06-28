# WorkoutViewer

Workout Viewr is a very simple app you can use to see your progress in bodybuilding. To get the data, you have to export it from "Carnet de Musculation" app on the PlayStore.

## Views

![](https://zupimages.net/up/22/26/lcsu.png)

![](https://zupimages.net/up/22/23/1pvq.png)

## Installation

This app is intended to be compiled into an executable. You can do it simply in some steps :

1. Install `pyinstaller` Python package

2. Run the following command at the root of the project : `pyinstaller app.py --add-binary "classes;classes" --add-binary "ui;ui" --paths '/' -n "Workout Viewer" --onefile -i "icon.ico" --windowed`

3. Delete `build` folder and keep `dist`. You can rename it as you want

4. Launch the executable and wait because the app while eventually reboot when launched for the first time

5. To use the app, you have to store your workout sessions in [Carnet de Musculation](https://www.carnetdemusculation.fr/) and export data from there
