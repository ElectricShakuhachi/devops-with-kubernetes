FROM python

EXPOSE $PORT 

WORKDIR /usr/src/app

COPY src ./src

RUN cd src; source venv/bin/activate; pip install -r requirements.txt

CMD cd src; flask run --host=0.0.0.0 -p ${PORT}
