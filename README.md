# Hybrid-Energy-Theft-Detection-using-Smart-Meters-and-Transformer-Validation
This project presents a hybrid energy theft detection framework for smart grids that overcomes the limitations of existing meter-only and infrastructure-only detection methods. Traditional ML approaches using smart meter data suffer from high false positives, while transformer-level monitoring can detect energy loss but cannot localize the offending consumer.

To address this, this project simulates a smart grid with multiple households and implements a multi-stage detection pipeline:

Smart meter data generation with simulated theft scenarios

Transformer-level load monitoring to detect hidden energy loss

Feature engineering and anomaly detection using machine learning

A hybrid validation rule that confirms theft only when meter anomalies align with transformer-level energy loss

The result is a system that accurately identifies theft while significantly reducing false alarms, demonstrating a practical and scalable approach for real-time grid monitoring.

This work is structured as a research prototype suitable for IEEE-style publication and further extension into real smart grid deployments.
