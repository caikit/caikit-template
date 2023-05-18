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
import grpc

# Local
from caikit.config import configure
from caikit.runtime.service_factory import ServicePackageFactory
from example.data_model.hello_world import HelloWorldInput

inference_service = ServicePackageFactory().get_service_package(
    ServicePackageFactory.ServiceType.INFERENCE,
    ServicePackageFactory.ServiceSource.GENERATED,
)

port = 8085
channel = grpc.insecure_channel(f"localhost:{port}")
client_stub = inference_service.stub_class(channel)

## Create request object
hello_world_proto = HelloWorldInput(name="World").to_proto()
request = inference_service.messages.ExampleBlockRequest(text_input=hello_world_proto)

## Fetch predictions from server (infer)
response = client_stub.ExampleBlockPredict(
    request, metadata=[("mm-model-id", "example")]
)

## Print response
print("RESPONSE:", response)