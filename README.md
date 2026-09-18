## Versioning

Image tags follow the tags of the [agensgraph](https://github.com/skaiworldwide-oss/agensgraph)
repository, which are `v2.<PG major>.<PG minor>.<minor>` since v2.18.4.0, with
release candidates ending in `-rcN`. Every version there is a tag, released or
not; here each one gets a branch of the same name, and its Dockerfiles live in
`v<line>/v<version>/<os>/`, where the line is the version without its last
component:

```
v2.18.6/v2.18.6.0-rc1/bookworm/Dockerfile   <- branch v2.18.6.0-rc1, a candidate
v2.18.4/v2.18.4.0/bookworm/Dockerfile       <- branch v2.18.4.0, a release
v2.17/v2.17.0/bookworm/Dockerfile           <- older scheme, v2.<PG major> lines
```

Pushing such a branch publishes those images, candidates included:
`v2.18.6.0-rc1` yields `v2.18.6.0-rc1-bookworm` and its siblings.

The `latest` tag is built on `master` from the highest full release in the tree.
A release candidate never becomes `latest`, so `latest` never moves ahead of
what has actually shipped.

## Tag Info
* **v2.18.4.0**
  * v2.18.4.0-trixie
  * v2.18.4.0-bookworm
  * v2.18.4.0-rocky10
  * v2.18.4.0-rocky9
  * v2.18.4.0-alpine3.24
  * v2.18.4.0-alpine3.23
* **v2.17.0**
  * v2.17.0-trixie
  * v2.17.0-bookworm
  * v2.17.0-rocky
  * v2.17.0-alpine3.24
  * v2.17.0-alpine3.23
* **v2.16.0**
  * v2.16.0-trixie
  * v2.16.0-bookworm
  * v2.16.0-rocky
  * v2.16.0-alpine3.22
  * v2.16.0-alpine3.21
* **v2.15.0**
  * v2.15.0-bookworm
  * v2.15.0-rocky
  * v2.15.0-alpine3.21
  * v2.15.0-alpine3.20
  * v2.15.0-bullseye
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
$ docker run --name agensgraph -e POSTGRES_PASSWORD=agensgraph -d skaiworldwide/agensgraph:v2.18.4.0
# Username: agens
# Password: agensgraph
# Database: postgres
```

The default superuser is `agens`. The default database stays `postgres`, so it has
to be named when connecting as `agens`. Setting `POSTGRES_USER` yourself makes
`POSTGRES_DB` follow it, as in the upstream `postgres` image.

### Advanced

- All environment arguments compatibility with postgresql, so you can read more deeply in the README of postgresql docker.
    - https://hub.docker.com/_/postgres

```shell
$ docker run -d \
    --name agensgraph \
    -e POSTGRES_PASSWORD=agensgraph \
    -e PGDATA=/var/lib/postgresql/pgdata \
    -v /custom/mount:/var/lib/postgresql \
    skaiworldwide/agensgraph
```

> **Upgrading to v2.18.4.0 (PostgreSQL 18):** starting with v2.18.4.0 the default
> `PGDATA` is `/var/lib/postgresql/18/docker` and the declared `VOLUME` moved from
> `/var/lib/postgresql/data` to `/var/lib/postgresql`, matching the upstream
> `postgres` image for 18+. If you mount a host volume that was initialised by an
> earlier tag at `/var/lib/postgresql/data`, either keep pointing `PGDATA` at your
> existing directory (`-e PGDATA=/var/lib/postgresql/data -v /custom/mount:/var/lib/postgresql/data`)
> or migrate the data into the new layout before starting the container.

## Deep into AgensGraph

```shell
$ docker exec -it {NAME OR CONTAINER_ID} /bin/bash
bash-5.1# psql -U agens -d postgres
psql (18.4)
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
* AgensGraph Quick Guide : http://tech.skaiworldwide.com/docs/en/agensgraph/16/quick_guide/index.html
* Dockerfile repository : https://github.com/skaiworldwide-oss/agensgraph-docker.git
* Docker hub repository : https://hub.docker.com/r/skaiworldwide/agensgraph

