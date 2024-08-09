
# grafana

[ref](https://grafana.com/docs/grafana/latest/setup-grafana/installation/debian/)


## Installation

```
sudo apt-get install -y apt-transport-https software-properties-common wget

sudo mkdir -p /etc/apt/keyrings/
wget -q -O - https://apt.grafana.com/gpg.key | gpg --dearmor | sudo tee /etc/apt/keyrings/grafana.gpg > /dev/null



echo "deb [signed-by=/etc/apt/keyrings/grafana.gpg] https://apt.grafana.com stable main" | sudo tee -a /etc/apt/sources.list.d/grafana.list

# Updates the list of available packages
sudo apt-get update

# Installs the latest OSS release:
sudo apt-get install grafana

```







## guied
```
grafana-cli plugins install grafana-googlesheets-datasource
grafana-cli plugins install alexanderzobnin-zabbix-app



systemctl restart grafana-server.service

cd /var/lib/grafana/plugins
chown -R grafana:grafana grafana-googlesheets-datasource/


```


# dashborad ID-code
* 3662 : prometheus-srv
* 1860 : linux node exporter



## Install loki-promtail
[ref](https://grafana.com/docs/loki/latest/setup/install/local/)
```
# debain based
apt-get install loki promtail

# or on debian
dnf install loki promtail



# install audit log on your system

sudo apt update
sudo apt install auditd




# or you can download the binary from github

wget https://github.com/grafana/loki/releases/download/v3.1.1/promtail-linux-amd64.zip

unzip promtail-linux-amd64.zip

chmod a+x promtail-linux-amd64
mv promtail-linux-amd64 /usr/bin/promtail


mkdir /etc/promtail/


vim /etc/promtail/config.yml
-----
server:
  http_listen_port: <port>
  grpc_listen_port: <port>

positions:
  filename: /tmp/positions.yaml

clients:
- url: http://<loki-server>:3100/loki/api/v1/push

scrape_configs:
- job_name: system
  static_configs:
  - targets:
      - localhost
    labels:
      job: auditlog
      #NOTE: Need to be modified to scrape any additional logs of the system.
      __path__: /var/log/audit/audit.log
      host: prometheus-server

----

useradd promtail -r -s /sbin/nologin
sudo chown -R promtail: /etc/promtail/

chmod -R  o+r /var/log/audit/


vim /usr/lib/systemd/system/promtail.service

----

[Unit]
Description=Promtail service
After=network-online.target
Wants=network-online.target

[Service]
Type=simple
User=promtail
ExecStart=/usr/bin/promtail -config.file /etc/promtail/config.yml
# Give a reasonable amount of time for promtail to start up/shut down
TimeoutSec = 60
Restart = on-failure
RestartSec = 2

[Install]
WantedBy=multi-user.target


----


systemctl daemon-reload
systemctl start promtail.service




# add promtail user to adm group which can read the log file from /var/log/...

usermod -aG adm promtail









systemctl restart promtail.service
systemctl restart loki.service



```

# change loki data store
```
sudo chown -R loki:nogroup /loki/data

common:
  instance_addr: 127.0.0.1
  path_prefix: /loki/data
  storage:
    filesystem:
      chunks_directory: /loki/data/chunks
      rules_directory: /loki/data/rules
  replication_factor: 1

```



## add a new log file in promtail

```

vim /etc/promtail/config.yml
------------
server:
  http_listen_port: <port>
  grpc_listen_port: <port>

positions:
  filename: /tmp/positions.yaml

clients:
- url: http://localhost:3100/loki/api/v1/push

scrape_configs:
- job_name: system
  static_configs:
  - targets:
      - localhost
    labels:
      job: auditlog
      #NOTE: Need to be modified to scrape any additional logs of the system.
      __path__: /var/log/audit/audit.log

  - targets:
      - localhost
    labels:
      job: sshlog
      __path__: /var/log/auth.log
------




```


## some logQL

```

{job="auditlog"} |= "sshd res=failed"

{job="auditlog"} |~ "failed|success"

{job="auditlog"} |~ "failed" != "success"

{job="sshlog"} |~ "Invalid user (test|jack)"

{job="nginx-log"} |~ "status [45]03"

count_over_time({job="sshlog"} |~ "Invalid user (test|jack)"[1h])




## create dashboard
{job="auditlog"}
sum(count_over_time({job="auditlog"}[1m])) by (host, filename)


# add annotation query
{job="auditlog"} |= "failed" != "level=info"

```