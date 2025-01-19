# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
import json
import logging
import os
import pickle
import numpy as np
import pandas as pd
import joblib

import azureml.automl.core
from azureml.automl.core.shared import logging_utilities, log_server
from azureml.telemetry import INSTRUMENTATION_KEY

from inference_schema.schema_decorators import input_schema, output_schema
from inference_schema.parameter_types.numpy_parameter_type import NumpyParameterType
from inference_schema.parameter_types.pandas_parameter_type import PandasParameterType
from inference_schema.parameter_types.standard_py_parameter_type import StandardPythonParameterType

data_sample = PandasParameterType(pd.DataFrame({"area_code": pd.Series(["example_value"], dtype="object"), "state_code": pd.Series(["example_value"], dtype="object"), "data_type_code": pd.Series(["example_value"], dtype="object"), "industry_code": pd.Series(["example_value"], dtype="object"), "supersector_code": pd.Series(["example_value"], dtype="object"), "series_id": pd.Series(["example_value"], dtype="object"), "year": pd.Series([0], dtype="int16"), "period": pd.Series(["example_value"], dtype="object"), "footnote_codes": pd.Series(["example_value"], dtype="object"), "seasonal": pd.Series(["example_value"], dtype="object"), "supersector_name": pd.Series(["example_value"], dtype="object"), "industry_name": pd.Series(["example_value"], dtype="object"), "data_type_text": pd.Series(["example_value"], dtype="object"), "state_name": pd.Series(["example_value"], dtype="object"), "area_name": pd.Series(["example_value"], dtype="object")}))
input_sample = StandardPythonParameterType({'data': data_sample})

result_sample = NumpyParameterType(np.array([0.0]))
output_sample = StandardPythonParameterType({'Results':result_sample})
sample_global_parameters = StandardPythonParameterType(1.0)

try:
    log_server.enable_telemetry(INSTRUMENTATION_KEY)
    log_server.set_verbosity('INFO')
    logger = logging.getLogger('azureml.automl.core.scoring_script_v2')
except:
    pass


def init():
    global model
    # This name is model.id of model that we want to deploy deserialize the model file back
    # into a sklearn model
    model_path = os.path.join(os.getenv('AZUREML_MODEL_DIR'), 'model.pkl')
    path = os.path.normpath(model_path)
    path_split = path.split(os.sep)
    log_server.update_custom_dimensions({'model_name': path_split[-3], 'model_version': path_split[-2]})
    try:
        logger.info("Loading model from path.")
        model = joblib.load(model_path)
        logger.info("Loading successful.")
    except Exception as e:
        logging_utilities.log_traceback(e, logger)
        raise

@input_schema('Inputs', input_sample)
@input_schema('GlobalParameters', sample_global_parameters, convert_to_provided_type=False)
@output_schema(output_sample)
def run(Inputs, GlobalParameters=1.0):
    data = Inputs['data']
    result = model.predict(data)
    return {'Results':result.tolist()}
