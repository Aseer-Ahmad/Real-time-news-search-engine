# Real-time-news-search-engine

A live system that fetches news articles from live news APIs, serializes and streams messages to a Kafka Topic. 
It then uses Bytewax to streamline the messages from our Kafka Topic by further cleaning, parsing, chunking, embedding, and upserting vectors to a Vector Database. Finally a UI from which we can interact with our database.

## Tools used : 
- Bytewax
- Pydantic Models
- Python Threading
- Upstash Serverless Kafka
- Upstash Vector Database

<b>We need to set up the following : </b>

- A new Upstash Kafka Cluster [requires registration](https://console.upstash.com/) : create cluster (chose closest region for our environment) -> create topic (to send and get messages)
- A new Upstash Vector Index 
- Registering to News APIs
- Install environment

