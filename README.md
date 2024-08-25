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
- Registering to News APIs and add your keys to a .env file
- Install environment and library manager poetry by running 
  - ```
    make install
    ```

This step shows that producer is thread safe and is sending messages based on a fetch window. The data after being fetched from APIs is modelled into a CommonDocument format . For each API , a KafkaProducerThread is instantiated inside a KafkaProducerSwarm. To check if the producer are working run the following, after which you will find the messages being sent to your Kafka cluster topic.
```
make run_producer
```

Next, you can start your consumer pipeline which will then consume messages and using Bytewax dataflow programming model eventually upserting the final created embeddings using sentence transformers to Upstash Vectors. Run this using the following make target.
```
make run_pipeline
```

Finally , you can start the UI that will fetch from the Upstash vector client by mathcing the question embedding. Run , 
```
make run_ui
```

