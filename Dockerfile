FROM python:3.10.6
EXPOSE 5000
WORKDIR /app
COPY . .
ENV FLASK_APP=app.py
ENV FLASK_ENV=development 
RUN pip install -r requirements.txt 
ENTRYPOINT ["python"]
CMD ["app.py"]