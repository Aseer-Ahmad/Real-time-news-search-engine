# Real-time-news-search-engine

A live system that fetches news articles from live news APIs, serializes and streams messages to a Kafka Topic. 
It then uses Bytewax to streamline the messages from our Kafka Topic by further cleaning, parsing, chunking, embedding, and upserting vectors to a Vector Database followed by a UI finnally from which we can interact with our database.

## Tools used : 
- Bytewax
- Pydantic Models
- Python Threading
- Upstash Serverless Kafka
- Upstash Vector Database

<b>We need to set up the following : </b>

- A new Upstash Kafka Cluster [requires registration](https://console.upstash.com/) :
  - create cluster (chose closest region for our environment)
  - create topic (to send and get messages)
- A new Upstash Vector Index 
- Registering to News APIs and add your keys to the .env file
- Install environment using poetry


At this point, you can check to check if the producer are working or not by running the following. After running you can check in your Kafka topic if messages have been sent . 
```
python -m producer
```

This step shows that producer is thread safe and is sending messages based on the fetch window. 


