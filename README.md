# Streamlit_Dashboard

This project is a modified version of the original Pytopia Dashboard created by Hejazizo.

## How to Run

### Install Dependencies
First, you need to install the dependencies. You can do this by running the following command:
```bash
pip install -r requirements.txt
```

Then, run the following command to start the export environment variables in main repo directory:
```bash
source .env
```
Run the following command to add the current directory to the Python path:
```bash
export PYTHONPATH=${PWD}
```
Build django migrations by running the following command:
```bash
python src/manage.py makemigrations db
python src/manage.py migrate
```
Then, you can run the dashboard by running the following command:
```bash
streamlit run src/app.py
```
In latest version of streamlit, you need also install ```altair==4.2.2```
