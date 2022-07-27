FROM python:3.9.6

WORKDIR /bot
COPY . /bot
 
RUN pip install -r requirements.txt
 
ENTRYPOINT ["python"]
CMD ["-m", "bot"]
