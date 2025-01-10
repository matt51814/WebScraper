export MONGODB_VERSION=6.0-ubi8;
docker run --name mongodb -d --network mongodb -v $(pwd)/data:/data/db mongodb/mongodb-community-server:$MONGODB_VERSION;
docker run --network mongodb --mount type=bind,src="$(pwd)",target=/app alpine sh -c "apk add python3 && cd app && source webscraper/bin/activate && python3 src/scrapers/scrape_all.py && python3 src/db/insert_json.py";