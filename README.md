# FreezeCasting-AI Prediction
1. This tool is coded by Python 3.6. Please install Python 3.6.
2. Necessary packages: numpy, pandas, tensorflow (version > 1.12), keras. Please install all these packages before using this tool.
3. How to use it:
	1) Run ANNTool.py in python environment, or just double click ANNTool.py in windows environment. You will see a panel.
	2) Choose the "Material Group", "Solid Material", "Solvent" from the listboxes, and input the volume fraction of solid.
	3) Click "Calculate" button to get a predicted porosity.
	4) Click "Clear" to remove the current result.
	
4. Files introduction:
	GUI_parts.py --including supporting functions
	model.h5 --a well-trained ANN model
	Material_Dictionary.csv --the dictionary of materials and their one-hot encoding
	ANNTool --main program
