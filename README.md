# LogicPanel
Logic component 

## Running DB and phpmyadmin
```bash
docker-compose up -d
```
## Running FastAPI
```bash
uvicorn main:app --reload --host <IP> --port <port>
```
# Clearing DB data
1. 
```bash
docker exec -it mysql-db bash
```
2. 
```bash
mysql -u root -p
```
3. 
```sql
DROP DATABASE logicpanel_db;
CREATE DATABASE logicpanel_db;
```
4. 
```bash
docker-compose down
```
5. 
```bash
docker volume rm mysql-data
```