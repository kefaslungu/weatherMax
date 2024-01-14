# weatherMax by [kefaslungu](github.com/kefaslungu)
[https://weathermax.azurewebsites.net]

quickly check the weather of any location of your choice for free.

Part of the requirement for [alx 9-12 months software engineering program.](https://alxafrica.com/)

Built using the [weatherstack api](https://weatherstack.com/), and [visual crossing api.](https://www.visualcrossing.com/)

you will need both api keys for weather stack and visual crossing to run this locally, but if you don't have one, or don't want to get one, no problem! The webapp is hosted on Microsoft azure!

[Click here](https://weathermax.azurewebsites.net/) to check it out.
## to run locally
clone this repo to your machine:
```
https://github.com/kefaslungu/weathermax.git
```

then move to the project directory. To do that, run
``` cd\weathermax```

You should then create a virtual enviroment to hold all the required files. Run:

```
python -m venv weathermax
```

then, activate the virtual enviroment so that it will not use your system wide enviroment. To do that, run:
```
weathermax\scripts\activate.bat
```

You should then install all the required dependances for the webapp to run on your machine. Run:
```
python -m pip install -r requirements.txt
```
