"""
Copyright 2015 Zalando SE

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the
License. You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an
"AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific
 language governing permissions and limitations under the License.
"""
import flask
import json


def problem(status: int, title: str, detail: str, type='about:blank',  instance: str=None):
    """
    Returns a `Problem Details <https://tools.ietf.org/html/draft-ietf-appsawg-http-problem-00>`_ error response.

    :param type: An absolute URI that identifies the problem type.  When dereferenced, it SHOULD provide human-readable
                 documentation for the problem type (e.g., using HTML).  When this member is not present its value is
                 assumed to be "about:blank".
    :param title: A short, human-readable summary of the problem type.  It SHOULD NOT change from occurrence to
                  occurrence of the problem, except for purposes of localisation.
    :param detail: An human readable explanation specific to this occurrence of the problem.
    :param status: The HTTP status code generated by the origin server for this occurrence of the problem.
    :param instance: An absolute URI that identifies the specific occurrence of the problem.  It may or may not yield
                     further information if dereferenced.
    :return: Json serialized error response
    """
    problem_response = {'type': type, 'title': title, 'detail': detail, 'status': status, }
    if instance:
        problem_response['instance'] = instance

    return flask.current_app.response_class(json.dumps(problem_response),
                                            mimetype='application/problem+json',
                                            status=status)
