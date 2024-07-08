
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
