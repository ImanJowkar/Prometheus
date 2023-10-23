# Prometheus
Prometheus monitoring refers to the use of Prometheus, an open-source monitoring and alerting toolkit, to track and manage the performance and health of various systems and applications. Prometheus is widely used in the field of DevOps and is designed to help organizations gain insights into the behavior of their systems. Here's an overview of what Prometheus monitoring entails:

1. **Data Collection:** Prometheus collects time-series data from various sources. This data can include metrics about system performance, application behavior, and other aspects of the infrastructure. Prometheus uses a pull-based model, where it periodically scrapes data from endpoints called "exporters."

2. **Storage:** Prometheus stores the collected data in a time-series database. This database is optimized for efficient storage and querying of time-series data. Data retention policies can be configured to determine how long data is kept.

3. **Data Querying:** Prometheus provides a query language called PromQL (Prometheus Query Language) that allows users to write custom queries to retrieve specific metrics or perform calculations on the data. PromQL is powerful and flexible, enabling users to gain insights into the system's behavior.

4. **Alerting:** Prometheus allows you to set up alerting rules based on the data it collects. When a certain condition is met, an alert is triggered, and notifications can be sent to notify relevant parties about potential issues.

5. **Visualization:** While Prometheus itself primarily focuses on data collection, storage, and querying, it is often used in conjunction with other tools, like Grafana, for data visualization. Grafana provides rich visualization capabilities to create dashboards and display Prometheus data in a user-friendly manner.

6. **Service Discovery:** Prometheus can dynamically discover and monitor new services and targets as they come online, making it well-suited for dynamic, cloud-native environments.

Prometheus is popular for its simplicity, reliability, and ability to scale. It is commonly used for monitoring cloud-native applications, containerized environments, and microservices due to its adaptability and support for modern architectural patterns. It helps organizations ensure the availability, performance, and reliability of their systems by providing real-time insights and timely alerts when issues arise.


# installation
[ref](https://www.cherryservers.com/blog/install-prometheus-ubuntu)

go to the promethues website and download the promethues
```
wget https://github.com/prometheus/prometheus/releases/download/v2.48.0-rc.0/prometheus-2.48.0-rc.0.linux-amd64.tar.gz

tar xvf prometheus-2.48.0-rc.0.linux-amd64.tar.gz

sudo cp prometheus /usr/local/bin/
sudo cp promtool /usr/local/bin/

sudo mkdir /etc/prometheus
sudo cp prometheus.yml /etc/prometheus/prometheus.yml


sudo cp -r consoles /etc/prometheus/
sudo cp -r console_libraries/ /etc/prometheus/




# create prometheus use
sudo groupadd --system prometheus
sudo useradd -s /sbin/nologin --system -g prometheus prometheus

sudo chown prometheus:prometheus /usr/local/bin/prometheus
sudo chown prometheus:prometheus /usr/local/bin/promtool


sudo chown prometheus:prometheus /etc/prometheus
sudo chown -R prometheus:prometheus /etc/prometheus/consoles
sudo chown -R prometheus:prometheus /etc/prometheus/console_libraries
sudo chown -R prometheus:prometheus /var/lib/prometheus



# Create Service
sudo vim /etc/systemd/system/prometheus.service

################


[Unit]
Description=Prometheus
Wants=network-online.target
After=network-online.target


[Service]
User=prometheus
Group=prometheus
Type=simple
ExecStart=/usr/local/bin/prometheus \ 
        --config.file=/etc/prometheus/prometheus.yml \ 
        --storage.tsdb.path=/var/lib/prometheus/data \ 
        --web.console.templates=/etc/prometheus/consoles \ 
        --web.console.libraries=/etc/prometheus/console_libraries

[Install]
WantedBy=multi-user.target


##############



sudo systemctl daemon-reload
sudo systemctl enable prometheus
sudo systemctl start prometheus

```

# Install Node-Exporter

A Node Exporter is a small application that runs on the system you want to monitor and collects various metrics and information about the system's hardware and operating system. These metrics include details about CPU usage, memory usage, disk I/O, network statistics, and more. The Node Exporter then makes this information available to Prometheus for collection and analysis.

Here are some key features and functions of a Node Exporter:

1. **System Metrics Collection:** Node Exporters collect a wide range of system-level metrics, providing insights into the health and performance of the host system.

2. **Prometheus Integration:** Node Exporters are designed to work seamlessly with Prometheus. They expose the collected metrics using the Prometheus exposition format, making it easy for Prometheus to scrape and store this data.

3. **Exposition Formats:** Node Exporters can export metrics in various formats, including plaintext (the most common format for Prometheus), JSON, and Protobuf. This flexibility allows for integration with different monitoring systems.

4. **Custom Metrics:** In addition to standard system metrics, Node Exporters can also be configured to collect custom metrics specific to your applications or services running on the host.

5. **Service Discovery:** Node Exporters can be configured to dynamically discover and scrape metrics from new hosts and services as they come online. This is particularly valuable in dynamic, cloud-native environments.

Node Exporters are part of the broader Prometheus ecosystem and play a crucial role in monitoring infrastructure and applications. They help DevOps and IT teams gain insights into the resource utilization and performance of individual hosts, which is essential for troubleshooting issues, optimizing system resources, and ensuring the reliability and availability of systems.

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
  # The job name is added as a label `job=<job_name>` to any timeseries scraped from this config.
  - job_name: 'node*exporter-local-server(prometheus-server)'
    scrape_interval: 5s
    static_configs:
        - targets: ['<node-exporter>:9100']

##################



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