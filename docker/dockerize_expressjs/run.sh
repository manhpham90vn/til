docker build . -t manhpv151090/dockerize_expressjs
docker run --rm -p 8080:8080 -e NODE_ENV=production -e PORT=8080 manhpv151090/dockerize_expressjs