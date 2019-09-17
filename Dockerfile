FROM heroku/miniconda

# Grab requirements.txt.
ADD requirements.txt /tmp/requirements.txt

# Install dependencies
RUN pip install -qr /tmp/requirements.txt

# Add our code
ADD app.py
WORKDIR app.py

RUN conda install dlib

CMD gunicorn 
