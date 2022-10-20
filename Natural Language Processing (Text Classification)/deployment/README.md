# Deploying the random forest model as a RESTAPI using FastAPI, Docker, and Heroku

### You can view the deployed API [here](https://cyberbullying-classifier-app.herokuapp.com/)


### 1. Create Docker container

```bash
docker build -t app-name .

docker run -p 80:80 app-name
```

### 2. Create Git repo

If you clone this repo this step is not needed. Or you can delete this git repo with `rm -rf .git` and start with a new one:

```bash
git init
git add .
git commit -m "initial commit"
```

### 3. Create Heroku project

```bash
heroku login
heroku create your-app-name
heroku git:remote your-app-name
heroku stack:set container
git push heroku main
```
