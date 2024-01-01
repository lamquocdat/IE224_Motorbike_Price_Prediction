#IE224_Motorbike_Price_Prediction
Used motorbike price prediction project for Data Analysis subject IE224 UIT.

Details of the project can be read in the "Báo cáo".

# Web app
A website that shows the results of the model after training.

It is deployed at https://ie224-motorbike-price-prediction.onrender.com

The user enters the necessary parameters and presses the prediction button, the model will calculate the price of that car and display it on the screen.

How to run the web app is as follows:

## Create .env file
Copy the contents of the .env.example file and paste it into the .env file in the webapp directory (create an .env file if it doesn't exist).
Edit the content in the .env file accordingly.

## Run the web app
Then run the following commands to run the web app

``````
# Go to web app folder
cd .\webapp
# If there is no venv file, run the command
python -m venv venv

# Run one of the following two commands to run the project in a virtual environment
## For Windows
venv\Scripts\activate

## For macOS/Linux
venv/bin/activate

# Run the following files to install the necessary libraries. If you get an error about missing libraries, please install them yourself
pip install flask python-dotenv joblib scikit-learn pandas numpy
pip freeze > requirements.txt

# Run the following command to run the project
python app.py

# From now on, after opening the project, you can immediately run the following commands:
cd .\webapp
venv\Scripts\activate
python app.py
``````

## Docker
In the root, run these command to build Docker

``````
# buidl Docker image
docker-compose build

# run Container
docker-compose up

# stop and delete Container
docker-compose down
``````

## About machine learning models and related objects
After exporting the model, put it in the webapp/app/models folder

Other components such as encoder and scaler need to be put into webapp/app/utils after being exported

## Retrain model and update
Every time you need to update the model, run the notebook file again and export the model (including scaler and encoder if any) into a .joblib file.

Then put those files in the corresponding folders webapp/app/models and webapp/app/utils

Then run the web app again.
