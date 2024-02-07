package main

import (
    "net/http"

    "github.com/prometheus/client_golang/prometheus"
    "github.com/prometheus/client_golang/prometheus/promhttp"
)

func main() {
    // Register a sample counter metric
    counter := prometheus.NewCounterVec(
        prometheus.CounterOpts{
            Name: "sample_counter",
            Help: "A sample counter metric",
        },
        []string{"label"},
    )
    prometheus.MustRegister(counter)

    // Increment the counter with a specific label value
    counter.WithLabelValues("example").Inc()

    // Expose metrics on /metrics
    http.Handle("/metrics", promhttp.Handler())
    http.ListenAndServe(":1212", nil)
}

