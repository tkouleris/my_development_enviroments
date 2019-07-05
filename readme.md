<h1>My Docker Development Environment</h1>

<p>
This repository contains my development enviroments
</p>

### 1. Nginx - PHP - MySql
* Nginx
* PHP latest
* MySQL 5.7
#### How to start
1. Run `docker-compose build`
2. Run `docker-compose run -d nginx php mysql`
3. Attach to container `docker -it --user=developer dev_php sh`