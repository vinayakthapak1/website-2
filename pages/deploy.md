<!--
.. title: Deploy
.. slug: deploy
.. date: 2020-05-12 12:55:42 UTC+02:00
.. tags: 
.. category: 
.. link: 
.. description: 
.. type: text
-->


## Deploy on you server

AskOmics can be easily deploy with docker and docker-compose.

### Step 1: install docker and docker-compose

- Follow [docker docs](https://docs.docker.com/engine/install/) to install docker.
- Install `docker-compose`

```bash
# Debian/Ubuntu
apt install -y docker-compose
# Fedora
dnf install -y docker-compose
```

### Step 2: Get docker-compose files

Clone [flaskomics-docker-compose](https://github.com/askomics/flaskomics-docker-compose)

```bash
git clone https://github.com/askomics/flaskomics-docker-compose.git
```

### Step 3: Deploy


```bash
cd flaskomics-docker-compose/standalone
docker-compose pull
docker-compose up -d
```

Your AskOmics will be available at [localhost](http://localhost)

For a production deployment, read [AskOmics docs](https://flaskomics.readthedocs.io/en/latest/production-deployment/) to configure your instance.


## Deploy on IFB cloud

AskOmics can be deployed on [IFB cloud](https://biosphere.france-bioinformatique.fr/catalogue/appliance/166/)
