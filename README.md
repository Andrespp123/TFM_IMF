# This will serve as an implementation guide for this repository

## Python Package usability
To take advantage of the opportunities that come from working with a Python Module, the main thing to keep in mind is that the repository will need to be added to the system's $PYTHON_PATH variable, that way Python will navigate through the directory and recognize it all as Python executable code.

## Install requirements.txt
Please install requirements.txt recursively using pip install requirements.txt -r. The -r flag will make the installation process recursive through the file, allowing the installation of all the libraries that are indexed in it.

## Define dataset size
Once you have the repository installed you can customize the training of your model. Feel free to define the size of the training dataset considering your system's limitations, the default is 30.000. The file to accomplish this is json_processing.py

## We have decoupled training from predicting 
Entremaniento_modelo_nlp.ipnyb is the file that takes care of training and decouples training from predictions by exporting the model to a .pk1 file using the pickle library.

## Previous GCP setup
Make sure that before you take this tool into production you have a properly set up project in GCP with a billing account associated to it. This will be necessary to store the final dataframe in BigQuery before connecting it to the DataStudio Dashboard.
