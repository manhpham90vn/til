aws ecr get-login-password --region ap-southeast-1 | docker login --username AWS --password-stdin 047590809543.dkr.ecr.ap-southeast-1.amazonaws.com
docker build -t wordpress .
docker tag wordpress:latest 047590809543.dkr.ecr.ap-southeast-1.amazonaws.com/wordpress:latest
docker push 047590809543.dkr.ecr.ap-southeast-1.amazonaws.com/wordpress:latest