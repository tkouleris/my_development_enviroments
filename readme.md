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
2. Run `docker-compose up -d nginx php mysql`
3. Attach to container `docker exec -it --user=developer dev_php sh`

### 2. .NetCore
* .NetCore
#### How to start
1. Run 'docker-compose build'
2. Run 'docker-compose up -d dotnetcore'
3. Attach to container 'docker exec -it --user=developer dev_dotnetcore sh
4. Create project 'dotnet new mvc'
5. Run server 'dotnet watch run --no-restore --urls http://0.0.0.0:5000
