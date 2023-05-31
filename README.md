# Caikit Template

GitHub Template with a boilerplate repository which serves an example AI model using [caikit](https://github.com/caikit/caikit).

## Before Starting

The following tools are required:

- [python](https://www.python.org) (v3.8+)
- [pip](https://pypi.org/project/pip/) (v23.0+)

**Note:** Before installing dependencies and to avoid conflicts in your environment, it is advisable to use a virtual environment. The subsection which follows provides an example of a virtual environment, python venv.

Install the dependencies: `pip install -r requirements.txt`

### (Optional) Setting Up Virtual Environment using Python venv

For [(venv)](https://docs.python.org/3/library/venv.html)], make sure you are in an activated `venv` when running `python` in the example commands that follow. Use `deactivate` if you want to exit the `venv`.

For example, to create and activate a virtual environment using `venv`:

```shell
python3 -m venv venv
source venv/bin/activate
```

## Repository Layout

```text
├── caikit-template/:               top-level package directory (will change to your repo name after template is deployed)
│   │── client/:                    a directory which contains artifacts to use (infer and train) the AI model spceified in the `example` package
|       ├── config.yml:             caikit runtime configuration file
│       ├── infer_model.py:         sample client which calls the Caikit runtime to perform inference on a model is is serving
│       ├── models/:                a directory that contains the metadata of the models
│       │   ├── example/config.yml: metadata that defines the example Caikit model 
|       ├── train_data/:            a directory which contains the training data
|       |   ├── sample_data.csv:    sample training dataset to perform training of the model
│       ├── train_model.py:         sample client which calls the Caikit runtime to perform training on a model is is serving
│   │── example/:                   a directory that defines Caikit module(s) that can include algorithm(s) implementation that can train/run an AI model 
│   │   ├── data_model/:            a directory that contains the data format of the Caikit module
│   │   │   ├── hello_world.py:     data class that represents the AI model attributes in code
│   │   │   ├── __init__.py:        makes the hello_world class visible in the project
│   │   ├── runtime_model/:         a directory that contains the Caikit runtime code of the model
│   │   │   ├── hello_world.py:   a class that bootstraps the AI model in Caikit so it can be served and used (infer/train)
│   │   │   ├── __init__.py:        makes the hello_world class visible in the project
|   |   |── __init__.py:            makes the data_model and runtime_model packages visible
│   │── server/:                    a directory which contains artifacts to start Caikit runtime
|       ├── config.yml:             configuration for handling the model by the Caikit runtime
│       ├── start_runtime.py:       a wrapper to start the Caikit runtime as a gRPC server. The runtime will load the model at startup
└── └── requirements.txt:           specifies library dependencies
```

## Starting the Caikit Runtime

In one terminal, start the runtime server:

```shell
cd client
python3 start_runtime.py
```

You should see output similar to the following:

```ShellSession
$ python3 start_runtime.py

[...]
{"channel": "GP-SERVICR-I", "exception": null, "level": "info", "log_code": "<RUN76884779I>", "message": "Constructed inference service for library: example, version: unknown", "num_indent": 0, "thread_id": 8641488384, "timestamp": "2023-05-17T10:19:17.413518"}
{"channel": "SERVER-WRAPR", "exception": null, "level": "info", "log_code": "<RUN81194024I>", "message": "Intercepting RPC method /caikit.runtime.Example.ExampleService/ExampleBlockPredict", "num_indent": 0, "thread_id": 8641488384, "timestamp": "2023-05-17T10:19:17.413578"}
{"channel": "SERVER-WRAPR", "exception": null, "level": "info", "log_code": "<RUN33333123I>", "message": "Wrapping safe rpc for Predict", "num_indent": 0, "thread_id": 8641488384, "timestamp": "2023-05-17T10:19:17.414160"}
{"channel": "SERVER-WRAPR", "exception": null, "level": "info", "log_code": "<RUN30032825I>", "message": "Re-routing RPC /caikit.runtime.Example.ExampleService/ExampleBlockPredict from <function _ServiceBuilder._GenerateNonImplementedMethod.<locals>.<lambda> at 0x7fba90382310> to <function CaikitRuntimeServerWrapper.safe_rpc_wrapper.<locals>.safe_rpc_call at 0x7fba90392670>", "num_indent": 0, "thread_id": 8641488384, "timestamp": "2023-05-17T10:19:17.414217"}
{"channel": "SERVER-WRAPR", "exception": null, "level": "info", "log_code": "<RUN24924908I>", "message": "Interception of service caikit.runtime.Example.ExampleService complete", "num_indent": 0, "thread_id": 8641488384, "timestamp": "2023-05-17T10:19:17.414273"}
[...]
"channel": "GT-SERVICR-I", "exception": null, "level": "info", "log_code": "<RUN76884779I>", "message": "Constructed train service for library: example, version: unknown", "num_indent": 0, "thread_id": 8641488384, "timestamp": "2023-05-17T10:19:17.415673"}
{"channel": "SERVER-WRAPR", "exception": null, "level": "info", "log_code": "<RUN81194024I>", "message": "Intercepting RPC method /caikit.runtime.Example.ExampleTrainingService/RuntimeExampleBlockExampleBlockTrain", "num_indent": 0, "thread_id": 8641488384, "timestamp": "2023-05-17T10:19:17.415724"}
{"channel": "SERVER-WRAPR", "exception": null, "level": "info", "log_code": "<RUN33333123I>", "message": "Wrapping safe rpc for Train", "num_indent": 0, "thread_id": 8641488384, "timestamp": "2023-05-17T10:19:17.415809"}
{"channel": "SERVER-WRAPR", "exception": null, "level": "info", "log_code": "<RUN30032825I>", "message": "Re-routing RPC /caikit.runtime.Example.ExampleTrainingService/RuntimeExampleBlockExampleBlockTrain from <function _ServiceBuilder._GenerateNonImplementedMethod.<locals>.<lambda> at 0x7fba90392430> to <function CaikitRuntimeServerWrapper.safe_rpc_wrapper.<locals>.safe_rpc_call at 0x7fba80ba8ca0>", "num_indent": 0, "thread_id": 8641488384, "timestamp": "2023-05-17T10:19:17.415848"}
{"channel": "SERVER-WRAPR", "exception": null, "level": "info", "log_code": "<RUN24924908I>", "message": "Interception of service caikit.runtime.Example.ExampleTrainingService complete", "num_indent": 0, "thread_id": 8641488384, "timestamp": "2023-05-17T10:19:17.415910"}
[...]
```

## Inferencing the Served Model

In another terminal, run the client code to infer the model:

```shell
cd client
python3 infer_model.py
```

The client code calls the model and queries for generated text using text passed from the client.

You should see output similar to the following after the word `World` is passed:

```ShellSession
$ python3 infer_model.py

RESPONSE: greeting: "Hello World"
```

## Training the Served Model

In another terminal, run the client code to train the model:

```shell
cd client
python3 train_model.py
```

The client code trains the model with sample data in `train_data/` and outputs the
trained model to `training_output/` by default.

You should see output similar to the following:

```ShellSession
$ python3 train_model.py

RESPONSE: training_id: "ace2fd4c-0a50-49ef-b4db-9d9bbe2eefaf"
model_name: "example"
```
