
# grafana

[ref](https://grafana.com/docs/grafana/latest/setup-grafana/installation/debian/)

## guied
```
grafana-cli plugins install grafana-googlesheets-datasource

systemctl restart grafana-server.service

cd /var/lib/grafana/plugins
chown -R grafana:grafana grafana-googlesheets-datasource/


```