# Real-time-news-search-engine

A live system that fetches news articles from live news APIs, serializes and streams messages to a Kafka Topic. 
It then uses Bytewax to streamline the messages from our Kafka Topic by further cleaning, parsing, chunking, embedding, and upserting vectors to a Vector Database. Finally a UI from which we can interact with our database.

Tools used : 
1. Bytewax
2. Pydantic Models
3. Python Threading
4. Upstash Serverless Kafka
5. Upstash Vector Database

We need to set up the following : 
1. A new Upstash Kafka Cluster (requires registration)
1.1 create cluster (chose closest region for our environment) -> create topic (to send and get messages)
2. A new Upstash Vector Index 
3. Registering to News APIs
4. Install environment

