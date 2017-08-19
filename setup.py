# Copyright (c) 2017, WSO2 Inc. (http://www.wso2.org) All Rights Reserved.
#
# WSO2 Inc. licenses this file to you under the Apache License,
# Version 2.0 (the "License"); you may not use this file except
# in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied. See the License for the
# specific language governing permissions and limitations
# under the License.

from setuptools import setup, find_packages


packages = find_packages()
filtered_packages = []
for package in packages:
    if package.startswith("Tests"):
        continue
    filtered_packages.append(package)

setup(
    name="PyDAS",
    version="0.1.dev",
    packages=filtered_packages,
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, <4',
    install_requires=["requests", "future", "enum34 ; python_version<'3.4'"],

    package_data={"DAS4PythonAPI":[]},

    # metadata for upload to PyPI
    author="wso2",
    author_email="dev@wso2.org",
    description="Distribution of WSO2 Data Analytics Server Python Client",
    license="Apache2",
    url="https://github.com/wso2/DASPythonClient",
)
