<h1 align="left">Flask starter App 🚀</h1>

###

<h2 align="left">About ptoject</h2>

###

<p align="left">
  The purpose of this project is to provide a basic starter for beginners when starting coding with flask. I found the
  flask microframework setup more difficult than other stacks available like Symphony, Node, React.js... So I decided
  to make my life and other people's life easier with this.
</p>

###

### Techs
  - Flask
    - Flask==2.2.0
    - Flask-SQLAlchemy==3.0.2
    - Flask-Migrate==4.0.0 
  - PostgreSql
  - Docker
    - Dockerfile
    - docker-compose

###

<h2 align="left">Made with</h2>

###

<div align="left">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/flask/flask-original.svg" height="40" width="52" alt="flask logo"  />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" height="40" width="52" alt="python logo"  />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/html5/html5-original.svg" height="40" width="52" alt="html5 logo"  />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/css3/css3-original.svg" height="40" width="52" alt="css3 logo"  />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/postgresql/postgresql-original.svg" height="40" width="52" alt="postgresql logo"  />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/docker/docker-original.svg" height="40" width="52" alt="docker logo"  />
</div>

<br>

---

<br>

## Commands
> *In the root directory of the App:*

- `docker-compose up -d`, to start the app in background;
- `docker-compose down`, to stop the app;
- `docker attach [APP_NAME|ID]`, to start monitoring a container;
- `docker exec -it [CONTAINER] [COMMAND]`, to run a command in a container.

#### Migrations
> *Run the following lines when needs to manage migrations:*
- `docker exec -it main_flask flask db init`, to create a folder with set to migration;

- `docker exec -it main_flask flask db migrate -m "Initial migration."`, to generate a migration;

- `docker exec -it main_flask flask db [upgrade|downgrade]`, to up/down changes based on migration files.

<br>

## Urls
> *Accessible when the environment is running:*
  - [App](http://localhost:8000/)
  - [Adminer](http://localhost:8080/)

<br>

## Tips ✨
- Start the app in non background mode (Or attach them when already running), so you can see the log of error and print outputs!
