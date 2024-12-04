# How to install

After cloning this repo, do one of the following...

## With Docker (recommended)

```bash
cd nice-scrum-poker
docker build -t nice-scrum-poker . # build the image
docker run --rm --name -d nice-scrum-poker -p 9999:9999 nice-scrum-poker # run the image
```

##  Without Docker

```bash
cd cd nice-scrum-poker/application
pip install -r requirements.txt
python main.py
```

