## Tag Info
* **v2.14.1**
  * v2.14.1-bookworm
  * v2.14.1-alpine3.20
  * v2.14.1-alpine3.19
  * v2.14.1-bullseye
  * v2.14.1-rockylinux8
* **v2.13.2**
  * v2.13.2-bookworm
  * v2.13.2-alpine3.20
  * v2.13.2-alpine3.19
  * v2.13.2-bullseye
  * v2.13.2-rockylinux8
* older than **v2.13.2**
  * Based on CentOS 7 and debian

## Getting started

### Quick start

```shell
$ docker run --name agensgraph -e POSTGRES_PASSWORD=agensgraph -d bitnine/agensgraph:v2.14.1
# Username: postgres
# Password: agensgraph
```

### Advanced

- All environment arguments compatibility with postgresql, so you can read more deeply in the README of postgresql docker.
    - https://hub.docker.com/_/postgres

```shell
$ docker run -d \
    --name agensgraph \
    -e POSTGRES_PASSWORD=agensgraph \
    -e PGDATA=/var/lib/postgresql/data/pgdata \
    -v /custom/mount:/var/lib/postgresql/data \
    bitnine/agensgraph:v2.14.1
```

## Deep into AgensGraph

```shell
$ docker exec -it {NAME OR CONTAINER_ID} /bin/bash
bash-5.1# psql -U postgres
psql (10.4)
Type "help" for help.

postgres=# CREATE GRAPH AGENS;
CREATE GRAPH
postgres=# SET GRAPH_PATH=AGENS;
SET
postgres=# CREATE (:person {name: 'Tom'})-[:knows]->(:person {name: 'Summer'});
UPDATE 3
postgres=# CREATE (:person {name: 'Pat'})-[:knows]->(:person {name: 'Nikki'});
UPDATE 3
postgres=# CREATE (:person {name: 'Olive'})-[:knows]->(:person {name: 'Todd'});
UPDATE 3
postgres=# MATCH (n) RETURN n;
               n               
-------------------------------
 person[3.7]{"name": "Tom"}
 person[3.8]{"name": "Summer"}
 person[3.9]{"name": "Pat"}
 person[3.10]{"name": "Nikki"}
 person[3.11]{"name": "Olive"}
 person[3.12]{"name": "Todd"}
(6 rows)
```

# Reference
* AgensGraph Quick Guide : https://www.skaiworldwide.com/en-US/resources?filterKey=manual
* Dockerfile repository : https://github.com/skaiworldwide-oss/agensgraph-docker.git

