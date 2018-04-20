# FireHose

# Install Firehose
`# git clone https://github.com/minikai/FireHose.git`

`# pip install requests pandas influxdb numpy configparser`

# Execute Firehose
### For training, from local to InfluxDB
`# python to_influixdb.py`
### For testing(/predicting), from local to inference engine
`# python to_inference_engine.py`

# Data sets
1. `training_data.txt`: simulating past sensor data and sending data to WISE-PaaS in every `1 second`
2. `testing_data.txt`: simulating current sensor data and requesting for prediction result in every `10 seconds`

# Scenario
1. load `training_data.txt` and insert (every `1 second`) to influxDB (simulate SCADA SDK)
2. load `testing_data.txt` and send request (every `10 seconds`) to inference engine (simulate Labview) 
3. write prediction result into `predict_result.txt`
