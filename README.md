

# Intro

This repo contains experiments in generating images from context-free grammars using turtle graphics.  Based on [l3kn/generative_cfg](https://github.com/l3kn/generative_cfg/tree/master?tab=readme-ov-file).
The contents of `generative_cfg` and `examples` are veratim copies from [l3kn/generative_cfg](https://github.com/l3kn/generative_cfg/tree/master?tab=readme-ov-file).  They are, to the extent
needed, updated to python 3.12.4 running in virtual enviorment as listed below.


# Run examples

```
$ source/env/bin/activate
$ python examples/rect_spiral.py
$ open rect_spiral.svg  # open the generated svg file
$ deactivate
```

# Dependencies

Use `pip freeze > requirements.txt` to make this list:

```
contourpy==1.2.1
cycler==0.12.1
fonttools==4.53.1
kiwisolver==1.4.5
matplotlib==3.9.1
numpy==2.0.0
packaging==24.1
pillow==10.4.0
pyparsing==3.1.2
python-dateutil==2.9.0.post0
scipy==1.14.0
setuptools==71.0.4
six==1.16.0
svgwrite==1.4.3
```

This list needs to be edited to remove unneeded dependencies.

