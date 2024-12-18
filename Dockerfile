FROM pypy:latest
WORKDIR /project_quotient
COPY . /project_quotient
RUN pip install -r requirements.txt
CMD /bin/sh -c 'python manage.py migrate && echo "Starting development server at http://localhost:8000/ "; python manage.py runserver 0.0.0.0:8000'