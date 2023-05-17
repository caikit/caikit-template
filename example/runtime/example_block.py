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

import alog
from caikit.core.blocks import base, block, BlockSaver
from caikit.core.data_model import DataStream
from caikit.core.module import ModuleConfig
from caikit.core.toolkit.errors import error_handler
from example.data_model.hello_world import (HelloWorldInput,
                                                   ExampleBlockPrediction,
                                                   ExampleTrainingType)

import os

logger = alog.use_channel("<SMPL_BLK>")
error = error_handler.get(logger)



@block(
    id="00110203-0405-0607-0809-0a0b02dd0e0f",
    name="ExampleBlock",
    version="0.0.1"
)
class ExampleBlock(base.BlockBase):

    def __init__(self, model=None) -> None:
        """Function to initialize the ExampleBlock.
        This function gets called by `.load` and `.train` function
        which initializes this module.
        """
        super().__init__()
        self.model = model

    @classmethod
    def load(cls, model_path: str, **kwargs):
        """Load a caikit model
        Args:
            model_path: str
                Path to caikit model.
        """
        config = ModuleConfig.load(model_path)

        # Utilize config to access parameters needed.
        # For example, if you need to extract tokenizer path, you can do:
        # config.tokenizer_path
        # You can do a type check on it, using:
        # error.type_check("<TMP94715366E>", str, tokenizer_path=config.tokenizer_path)

        # Load model artifact
        model = None  # replace this with model load code such as `torch.load`
        return cls(model)

    def run(self, text_input: HelloWorldInput) -> ExampleBlockPrediction:
        """Run inference on model.
        Args:
            text_input: str
                Input text to be processed
        Returns:
            ExampleBlockPrediction: the output
        """
        # This is the main function used for inferencing.
        # NOTE:
        # 1. Output of a run function needs to be a data model. In this case
        #    we have used ExampleBlockPrediction as an example.
        # 2. The input and output data model, i.e ExampleBlockPrediction
        #    are only used for demo purposes. A developer of new module
        #    can use any data model (as output). There are a lot of pre-built
        #    data models provided already, but if those are not suitable for the use-case,
        #    then one can choose to build their own data model as well.
        # 3. It is required for the `run` function to have proper doc strings as
        #    these gets used for runtime automation
        # 4. This function is meant to process single example inference only.
        #    For a batch request, please implement `run_batch` function, which would
        #    accept list of text (as example) as input and return List of
        #    `ExampleBlockPrediction` (as an example) as output.

        return ExampleBlockPrediction(f"Hello {text_input.name}")

    def save(self, model_path, *args, **kwargs):
        """Function to save model in caikit format.
        This will generate store models on disk in a folder, which would be directly
        consumable by caikit.runtime framework.

        Args:
            model_path: str
                Path to store model into
        """
        block_saver = BlockSaver(
            self,
            model_path=model_path,
        )
        with block_saver:

            temp_model_file = os.path.join(model_path,  "temp_model.txt")
            # Write into temp_model_file as example
            with open(temp_model_file, "w") as f:
                for idx in range(3):
                    f.write(str(idx))

            config_options = {
                "tokenizer_path": "<EXAMPLE>",
                "temp_model_path": temp_model_file
            }
            block_saver.update_config(config_options)



    @classmethod
    def train(cls, training_data: DataStream[ExampleTrainingType], *args, **kwargs) -> "ExampleBlock":
        """Function to take a data stream as input and train a model.

        Note:
        - This function is primary entry point for all types of models that require
        either training, tuning, fine-tuning or just configuration.
        - This function is also used by training API in caikit.runtime to kick off
        a training in cloud environment.
        - Input data has to be of `DataStream` type

        Args:
            training_data: DataStream
                Training data stream of `ExampleTrainingType` type
        Returns:
            ExampleBlock
                Object of ExampleBlock as output that can be used to make
                inference call using `.run` function or persist the model using
                `.save` function.
        """

        return cls(model=None)

    @classmethod
    def bootstrap(cls, pretrained_model_path):
        """Optional: Function that allows to load a non-caikit model artifact
        such as open source models from TF hub or HF and load them into
        this module.
        """
        # Replace following with model load code such as `transformers.from_pretrained`
        model = None
        return cls(model)
