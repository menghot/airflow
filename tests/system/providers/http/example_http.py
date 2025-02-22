#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
"""Example HTTP operator and sensor"""
from __future__ import annotations

import json
import os
from datetime import datetime

from airflow import DAG
from airflow.providers.http.operators.http import HttpOperator
from airflow.providers.http.sensors.http import HttpSensor

ENV_ID = os.environ.get("SYSTEM_TESTS_ENV_ID")
DAG_ID = "example_http_operator"


dag = DAG(
    DAG_ID,
    default_args={"retries": 1},
    tags=["example"],
    start_date=datetime(2021, 1, 1),
    catchup=False,
)

dag.doc_md = __doc__

# task_post_op, task_get_op and task_put_op are examples of tasks created by instantiating operators
# [START howto_operator_http_task_post_op]
task_post_op = HttpOperator(
    task_id="post_op",
    endpoint="post",
    data=json.dumps({"priority": 5}),
    headers={"Content-Type": "application/json"},
    response_check=lambda response: response.json()["json"]["priority"] == 5,
    dag=dag,
)
# [END howto_operator_http_task_post_op]
# [START howto_operator_http_task_post_op_formenc]
task_post_op_formenc = HttpOperator(
    task_id="post_op_formenc",
    endpoint="post",
    data="name=Joe",
    headers={"Content-Type": "application/x-www-form-urlencoded"},
    dag=dag,
)
# [END howto_operator_http_task_post_op_formenc]
# [START howto_operator_http_task_get_op]
task_get_op = HttpOperator(
    task_id="get_op",
    method="GET",
    endpoint="get",
    data={"param1": "value1", "param2": "value2"},
    headers={},
    dag=dag,
)
# [END howto_operator_http_task_get_op]
# [START howto_operator_http_task_get_op_response_filter]
task_get_op_response_filter = HttpOperator(
    task_id="get_op_response_filter",
    method="GET",
    endpoint="get",
    response_filter=lambda response: response.json()["nested"]["property"],
    dag=dag,
)
# [END howto_operator_http_task_get_op_response_filter]
# [START howto_operator_http_task_put_op]
task_put_op = HttpOperator(
    task_id="put_op",
    method="PUT",
    endpoint="put",
    data=json.dumps({"priority": 5}),
    headers={"Content-Type": "application/json"},
    dag=dag,
)
# [END howto_operator_http_task_put_op]
# [START howto_operator_http_task_del_op]
task_del_op = HttpOperator(
    task_id="del_op",
    method="DELETE",
    endpoint="delete",
    data="some=data",
    headers={"Content-Type": "application/x-www-form-urlencoded"},
    dag=dag,
)
# [END howto_operator_http_task_del_op]
# [START howto_operator_http_http_sensor_check]
task_http_sensor_check = HttpSensor(
    task_id="http_sensor_check",
    http_conn_id="http_default",
    endpoint="",
    request_params={},
    response_check=lambda response: "httpbin" in response.text,
    poke_interval=5,
    dag=dag,
)
# [END howto_operator_http_http_sensor_check]
# [START howto_operator_http_pagination_function]


def get_next_page_cursor(response) -> dict | None:
    """
    Take the raw `request.Response` object, and check for a cursor.
    If a cursor exists, this function creates and return parameters to call
    the next page of result.
    """
    next_cursor = response.json().get("cursor")
    if next_cursor:
        return dict(data={"cursor": next_cursor})


task_get_paginated = HttpOperator(
    task_id="get_paginated",
    method="GET",
    endpoint="get",
    data={"cursor": ""},
    pagination_function=get_next_page_cursor,
    dag=dag,
)
# [END howto_operator_http_pagination_function]
task_http_sensor_check >> task_post_op >> task_get_op >> task_get_op_response_filter
task_get_op_response_filter >> task_put_op >> task_del_op >> task_post_op_formenc
task_post_op_formenc >> task_get_paginated

from tests.system.utils import get_test_run  # noqa: E402

# Needed to run the example DAG with pytest (see: tests/system/README.md#run_via_pytest)
test_run = get_test_run(dag)
