aws ecr get-login-password --region ap-southeast-1 | docker login --username AWS --password-stdin 047590809543.dkr.ecr.ap-southeast-1.amazonaws.com
docker build -t nginx .
docker tag nginx:latest 047590809543.dkr.ecr.ap-southeast-1.amazonaws.com/nginx:latest
docker push 047590809543.dkr.ecr.ap-southeast-1.amazonaws.com/nginx:latest