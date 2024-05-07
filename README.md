# 🗃️ Bases de Datos Avanzadas - Proyecto Final
## 👥 Integrantes
- Luis Cedillo Maldonado
- Javier Alejandro Rangel Murillo

## 📋 Descripción
🔍 *Dashboard para la visualización de datos de un conjunto de ciberataques en un periodo de tiempo determinado*.  
El dashboard permite visualizar los datos de los ciberataques en diferentes gráficas y realizar un análisis detallado de estos datos.

## ⚙️ Prerequisitos
- Docker  
- Navegador web compatible (Chrome, Firefox, Safari, etc.)  

## 🚀 Instalación
### Backend
1. Dirígete a la carpeta del backend ejecutando el siguiente comando en la carpeta raíz del proyecto:
    ```bash
    cd back
    ```
2. Levanta el contenedor de Docker con:
    ```bash
    docker compose --env-file .env.dev -f docker-compose.dev.yml up --build
    ```

### Frontend
1. Dirígete a la carpeta del frontend ejecutando:
    ```bash
    cd react_app
    ```
2. Levanta el contenedor de Docker con:
    ```bash
    docker compose up --build
    ```

## 📊 Uso
- Para acceder al dashboard, abre un navegador web y dirígete a:
    ```bash
    http://localhost:3000
    ```
- También puedes acceder a la base de datos de la API en:
    ```bash
    http://localhost:8080
    ```
    con las siguientes credenciales:
    - 🗃️ Motor: PostgreSQL
    - 👤 Usuario: `postgres`
    - 🔒 Contraseña: `postgres`
    - 🛢️ Base de datos: `postgres`
