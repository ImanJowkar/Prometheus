Prometheus Node Exporter is designed to expose system metrics, but it doesn't support custom metrics out of the box. However, you can use the Node Exporter's textfile collector to achieve this. The textfile collector reads metrics from files in a specified directory and exports them to Prometheus.

* Enable the Textfile Collector:
```
./node_exporter --collector.textfile.directory=/path/to/textfile/directory
```

