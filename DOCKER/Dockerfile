FROM python:3.7

RUN mkdir /app
WORKDIR /app
ADD . /app/
RUN python install -r requirements.txt

EXPOSE 5000
CMD ["python","/app/render.py"]