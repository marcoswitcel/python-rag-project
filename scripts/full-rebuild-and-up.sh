#

# 1. Stop and remove existing containers, networks, and volumes
sudo docker compose --profile dev-server down -v --remove-orphans

# 2. Prune build cache to guarantee a completely fresh download
sudo docker builder prune -f

# 3. Rebuild with explicit --no-cache
sudo docker compose --profile dev-server build --no-cache

# 4. Start the stack and check logs
sudo docker compose --profile dev-server up -d --force-recreate && \
sudo docker logs --follow uvicorn-server-dev