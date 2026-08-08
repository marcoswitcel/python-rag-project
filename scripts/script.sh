
sudo docker compose up --build -d

sudo docker compose build --no-cache
sudo docker compose --profile dev-server up -d --build --force-recreate

sudo docker stop $(sudo docker ps -q)


sudo docker compose down --volume

sudo docker logs --follow uvicorn-server-dev

sudo docker system prune -a --volumes -f

# full ground rebuild
sudo docker compose --profile dev-server build --no-cache && sudo docker compose --profile dev-server up -d --force-recreate && sudo docker logs --follow uvicorn-server-dev



# 1. Stop and remove existing containers, networks, and volumes
sudo docker compose --profile dev-server down -v --remove-orphans

# 2. Prune build cache to guarantee a completely fresh download
sudo docker builder prune -f

# 3. Rebuild with explicit --no-cache
sudo docker compose --profile dev-server build --no-cache

# 4. Start the stack and check logs
sudo docker compose --profile dev-server up -d --force-recreate && \
sudo docker logs --follow uvicorn-server-dev