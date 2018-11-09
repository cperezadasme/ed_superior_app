# ed_superior_app

Crear entorno virtual con python 3.5.0

### Instalar postgresql
```bash
$ brew install postgresql
```

### Iniciar servicio
```bash
$ brew services start postgresql
```

### Instalar dependencias
```bash
$ pip install -r requirements.txt
```

### Crear base de datos
```sql
CREATE USER postgres SUPERUSER;
CREATE DATABASE ed_superior;
GRANT ALL PRIVILEGES ON DATABASE ed_superior TO postgres;
```

### Aplicar migraciones
```bash
$ python manage.py migrate
```

### Cargar archivos CSV a la base de datos
```sql
\COPY visualizacion_matricula(...) FROM 'file_path' WITH DELIMITER ',' CSV HEADER;
\COPY visualizacion_titulados(...) FROM 'file_path' WITH DELIMITER ';' CSV HEADER;
```