# InpGenerator

This inp generator is an easy tool to generate .inp file for the MATLAB FE analyzer written for the DMS course in POLITECNICO DI MILANO

## Setup
To run the tool, just download all the files in the same folder:
Run it locally using:

```
$ python3 main.py
```

### Add a new material
Only the 2 main materials are currently added in the software
In order to add a new one, just add it in the marerials.py file following the pattern
To add it to the Tool menu, just add a line at the end of the config.py file

## WARNING
The tool is pretty raw and doesn't always generate the best files. Always check the files before putting them into MATLAB
### Common Issues
-Negative sign before 0
