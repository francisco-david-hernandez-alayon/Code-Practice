# PROYECTO PHP
Autor: Francisco David Hernández Alayón


### Instalar herramientas
```
sudo apt update
sudo apt install php php-mysql mysql-server -y
```

Instalar dotenv
```
sudo apt install composer -y
composer require vlucas/phpdotenv
```


### MySQL
Entrar en MySql
```
sudo mysql
```

Crear usuario API
```
CREATE USER 'api_user'@'localhost'
IDENTIFIED WITH mysql_native_password
BY 'PASSWORD';
```
Dar permisos al usuario
```
GRANT ALL PRIVILEGES ON api_db.*
TO 'api_user'@'localhost';
FLUSH PRIVILEGES;
```

Crear tabla de prueba
```
CREATE DATABASE api_db;

USE api_db;

CREATE TABLE usuarios(
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100),
    email VARCHAR(100)
);

INSERT INTO usuarios(nombre,email)
VALUES ("Juan","juan@mail.com");
```

### Ejecutar servidor php
```
php -S localhost:8000
```