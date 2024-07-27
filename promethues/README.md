# Prometheus

Prometheus is an open-source monitoring and alerting toolkit, to track and manage the performance and health of various systems and applications. Prometheus is widely used in the field of DevOps and is designed to help organizations gain insights into the behavior of their systems. 

1. **Data Collection:** Prometheus collects time-series data from various sources. This data can include metrics about system performance, application behavior, and other aspects of the infrastructure. Prometheus uses a pull-based model, where it periodically scrapes data from endpoints called "exporters."

2. **Storage:** Prometheus stores the collected data in a time-series database. This database is optimized for efficient storage and querying of time-series data. Data retention policies can be configured to determine how long data is kept.

3. **Data Querying:** Prometheus provides a query language called PromQL (Prometheus Query Language) that allows users to write custom queries to retrieve specific metrics or perform calculations on the data. PromQL is powerful and flexible, enabling users to gain insights into the system's behavior.

4. **Alerting:** Prometheus allows you to set up alerting rules based on the data it collects. When a certain condition is met, an alert is triggered, and notifications can be sent to notify relevant parties about potential issues.

5. **Visualization:** While Prometheus itself primarily focuses on data collection, storage, and querying, it is often used in conjunction with other tools, like Grafana, for data visualization. Grafana provides rich visualization capabilities to create dashboards and display Prometheus data in a user-friendly manner.

6. **Service Discovery:** Prometheus can dynamically discover and monitor new services and targets as they come online, making it well-suited for dynamic, cloud-native environments.



# installation of RHEL
[ref](https://www.cherryservers.com/blog/install-prometheus-ubuntu)

go to the promethues website and download the promethues

[download-prometheus](https://github.com/prometheus/prometheus/releases)

```

dnf install epel-release

dnf install mtr tcpdump net-snmp-utils bind-utils sysstat  htop screen wget curl vim bash-completion traceroute telnet net-tools btop


wget https://github.com/prometheus/prometheus/releases/download/v2.48.0-rc.0/prometheus-2.48.0-rc.0.linux-amd64.tar.gz

tar xvf prometheus-2.48.0-rc.0.linux-amd64.tar.gz




sudo mkdir -p /etc/prometheus
sudo mkdir -p /var/lib/prometheus


# create prometheus user

useradd prometheus -r -s /sbin/nologin -d /var/lib/prometheus/

sudo cp -r consoles /etc/prometheus/
sudo cp -r console_libraries/ /etc/prometheus/
sudo cp prometheus.yml /etc/prometheus/prometheus.yml
sudo cp prometheus /usr/local/bin/
sudo cp promtool /usr/local/bin/



sudo chown -R prometheus:prometheus /var/lib/prometheus/
sudo chown -R prometheus:prometheus /etc/prometheus/


cat > /etc/prometheus/prometheus.yml << EOF
# this is prom basic configuration
global:
  scrape_interval: 15s # Set the scrape interval to every 15 seconds. Default is every 1 minute.

scrape_configs:
  - job_name: "prometheus-srv"
    static_configs:
      - targets: ["localhost:9090"]

EOF





# Create Service

cat > /usr/lib/systemd/system/prometheus.service << EOF

[Unit]
Description=Prometheus
Wants=network-online.target
After=network-online.target

[Service]
User=prometheus
Group=prometheus
Type=simple
ExecReload=/usr/bin/kill -HUP $MAINPID

ExecStart=/usr/local/bin/prometheus \
--config.file=/etc/prometheus/prometheus.yml \
--storage.tsdb.path=/var/lib/prometheus/ \
--web.console.templates=/etc/prometheus/consoles \
--web.console.libraries=/etc/prometheus/console_libraries \
--web.listen-address=0.0.0.0:9090


SyslogIdentifier=prometheus
Restart=on-failure
RestartSec=60s

[Install]
WantedBy=multi-user.target
EOF





sudo systemctl daemon-reload
sudo systemctl enable prometheus
sudo systemctl start prometheus

```





# Install Node-Exporter

A Node Exporter is a small application that runs on the system you want to monitor and collects various metrics and information about the system's hardware and operating system. These metrics include details about CPU usage, memory usage, disk I/O, network statistics, and more. The Node Exporter then makes this information available to Prometheus for collection and analysis.




```
wget https://github.com/prometheus/node_exporter/releases/download/v1.6.1/node_exporter-1.6.1.linux-amd64.tar.gz

tar xvf node_exporter-1.6.1.linux-amd64.tar.gz

you can run in the tmux

```

for adding node exporter in promethues 
```
vim /etc/prometheus/prometheus.yml

##############
scrape_configs:
  - job_name: 'node*exporter-local-server(prometheus-server)'
    scrape_interval: 5s
    static_configs:
        - targets: ['<node-exporter>:9100']

##################


```

you can write a custom exporter with python and write a service for it.

```
sudo vim /etc/systemd/system/node-exporter.service

########################


[Unit]
Description=node-exporter
Wants=network-online.target
After=network-online.target


[Service]
Type=simple
User=prometheus
Group=prometheus
ExecReload=/bin/kill -HUP $MAINPID
ExecStart=/usr/local/bin/node_exporter

SyslogIdentifier=prometheus
Restart=always


[Install]
WantedBy=multi-user.target
############


sudo systemctl daemon-reload
sudo systemctl start node-exporter.service 
sudo systemctl status node-exporter.service
sudo systemctl enable node-exporter.service
```







# Install Grafana
install oss(open source) version

[ref](https://www.digitalocean.com/community/tutorials/how-to-install-and-secure-grafana-on-ubuntu-22-04)

```
wget -q -O - https://packages.grafana.com/gpg.key | gpg --dearmor | sudo tee /usr/share/keyrings/grafana.gpg > /dev/null

echo "deb [signed-by=/usr/share/keyrings/grafana.gpg] https://packages.grafana.com/oss/deb stable main" | sudo tee -a /etc/apt/sources.list.d/grafana.list

sudo apt update
sudo apt install grafana
sudo systemctl start grafana-server
sudo systemctl status grafana-server
sudo systemctl enable grafana-server
```



# Data Model in prometheus

