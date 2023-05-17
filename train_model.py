# Copyright The Caikit Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Third Party
from os import path
import grpc

# Local
from caikit.runtime.service_factory import ServicePackageFactory
from example.data_model import HelloWorldInput

training_service = ServicePackageFactory().get_service_package(
    ServicePackageFactory.ServiceType.TRAINING,
    ServicePackageFactory.ServiceSource.GENERATED,
)

port = 8085
channel = grpc.insecure_channel(f"localhost:{port}")
client_stub = training_service.stub_class(channel)

## Create request
training_data = path.join("train_data", "sample_data.csv")
request = training_service.messages.RuntimeExampleBlockExampleBlockTrainRequest(
    training_data={"file": {"filename": training_data}}, model_name="example",
)

## Kick off training from server
response = client_stub.RuntimeExampleBlockExampleBlockTrain(request)

print("RESPONSE:", response)