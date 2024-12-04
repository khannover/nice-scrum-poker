FROM zauberzeug/nicegui:latest

RUN apt-get update && apt-get upgrade -y
COPY application/requirements.txt /app
WORKDIR /app
RUN python3 -m pip install --upgrade -r requirements.txt
COPY application /app
EXPOSE 9999
CMD ["python3", "main.py"]