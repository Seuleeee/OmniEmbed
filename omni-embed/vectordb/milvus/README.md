# How to Setup
- [Docker Compose](https://milvus.io/docs/install_standalone-docker-compose.md)

```shell
wget https://github.com/milvus-io/milvus/releases/download/v2.5.3/milvus-standalone-docker-compose.yml -O docker-compose.yml

sudo docker compose up -d

Creating milvus-etcd  ... done
Creating milvus-minio ... done
Creating milvus-standalone ... done
```

- webui : http://localhost:9091/webui