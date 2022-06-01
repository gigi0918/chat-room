# Quick Start

## Install Kafka

- Make sure you have docker environment
    ``` bash
    # Start the Kafka broker
    cd kafka
    docker-compose up -d

    # Create a topic
    docker exec broker \
    kafka-topics --bootstrap-server broker:9092 \
                --create \
                --topic test-topic
    ```

- Detailed installation resources - [here](#references)


## Virtual environment

- Creating virtual environment
    ```bash
    $ python3 -m venv kafka-env
    ```

- Activate virtual environment
    ```bash 
    $ kafka-env\Scripts\activate.bat # On Windows
    $ source kafka-env/bin/activate  # On Unix or MacOS
    ```

- Install packages
    ```bash
    $ pip3 install kafka-python
    $ pip3 install googletrans==3.1.0a0
    ```

## Now you can chat with yourself
- Open three terminals and run programs individually
    ```bash
    # Terminal #1
    $ python3 src/room.py
    # Terminal #2
    $ python3 src/user1.py
    # Terminal #3
    $ python3 src/user2.py
    ```

# Demo 

<video width="320" height="240" controls>
    <source src="https://github.com/gigi0918/chat-room/demo.mp4" type="video/mp4">
</video>

# References
- [Virtual Environments and Packages](https://docs.python.org/3/tutorial/venv.html)
    - Generate requirements.txt
        ```bash
        $ pip3 freeze > requirements.txt
- [Apache Kafka® Quick Start](https://developer.confluent.io/quickstart/kafka-docker/)
- [Quick Start for Confluent Platform](https://docs.confluent.io/platform/current/quickstart/ce-docker-quickstart.html?utm_medium=sem&utm_source=google&utm_campaign=ch.sem_br.brand_tp.prs_tgt.confluent-brand_mt.mbm_rgn.apac_lng.eng_dv.all_con.confluent-docker&utm_term=%2Bconfluent%20%2Bdocker&creative=&device=c&placement=&gclid=Cj0KCQjw1tGUBhDXARIsAIJx01lwYgqx1b_K3FvlnuEW_P824alPG0DtouHE3zHO3DHDL7vPxAXwoV8aAlxaEALw_wcB)
