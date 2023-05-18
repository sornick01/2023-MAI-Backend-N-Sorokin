docker exec -it lab2-gunicorn-1 apt update
docker exec -it lab2-nginx-1 apt update
docker exec -it lab2-gunicorn-1 apt install -y apache2-utils
docker exec -it lab2-nginx-1 apt install -y apache2-utils
docker exec -it lab2-gunicorn-1 ab -n 10 -c 2 -t 1 -v 2 http://localhost:8000/
docker exec -it lab2-nginx-1 ab -n 10 -c 2 -t 1 -v 2 http://localhost:8080/public/pepe.jpg
docker exec -it lab2-nginx-1 ab -n 10 -c 2 -t 1 -v 2 http://localhost:8080/gunicorn/