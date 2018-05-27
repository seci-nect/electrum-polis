# Setup electrumx testnet server with docker

## 1. Setup secid node with docker

Used docker secid image has `txindex=1` setting in seci.conf,
which is need by electrumx server.

Create network to link with electrumx server.

```
docker network create seci-testnet
```

Create volume to store secid data and settings.

```
docker volume create secid-data-testnet
```

Start secid container.

```
docker run --restart=always -v secid-data-testnet:/seci \
    --name=secid-node-testnet --net seci-testnet -d \
    --env TESTNET=1 \
    -p 9819:9819 -p 127.0.0.1:19998:19998 zebralucky/secid:v0.12.2
```

**Notes**:
 - port 9819 is published without bind to localhost and can be
 accessible from out world even with firewall setup:
 https://github.com/moby/moby/issues/22054

Copy or change RPC password. Random password generated
on first container startup.

```
docker exec -it secid-node-testnet bash -l

# ... login to container

cat .secicore/seci.conf | grep rpcpassword
```

See log of secid.

```
docker logs secid-node-testnet
```

## 2. Setup electrumx server with docker

Create volume to store elextrumx server data and settings.

```
docker volume create electrumx-seci-data-testnet
```

Start elextrumx container.

```
docker run --restart=always -v electrumx-seci-data-testnet:/data \
    --name electrumx-seci-testnet --net seci-testnet -d \
    -p 51001:51001 -p 51002:51002 zebralucky/electrumx-seci:testnet
```

Change DAEMON_URL `rpcpasswd` to password from secid and creaate SSL cert.

**Notes**:
 - DAEMON_URL as each URL can not contain some symbols.
 - ports 51001, 51002 is published without bind to localhost and can be
 accessible from out world even with firewall setup:
 https://github.com/moby/moby/issues/22054

```
docker exec -it electrumx-seci-testnet bash -l

# ... login to container

cd /data/

# Edit and save env/DAEMON_URL
nano env/DAEMON_URL

# Create SSL self signed certificate

openssl genrsa -des3 -passout pass:x -out server.pass.key 2048 && \
openssl rsa -passin pass:x -in server.pass.key -out server.key && \
rm server.pass.key && \
openssl req -new -key server.key -out server.csr

openssl x509 -req -days 730 -in server.csr -signkey server.key \
  -out server.crt && rm server.csr


exit
# ... logout from container

# Restart electrumx container to switch on new RPC password

docker restart electrumx-seci-testnet
```

See log of electrumx server.

```
docker exec -it electrumx-seci-testnet bash -l

# ... login to container

tail /data/log/current

# or less /data/log/current
```

Wait some time, when electrumx sync with secid and
starts listen on client ports. It can be seen on `/data/log/current`.
