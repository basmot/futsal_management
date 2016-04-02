##############################################################################
#
# Copyright 2015-2016 Bastien Mottiaux
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
#
##############################################################################

AlertLevels = type(
    "AlertLevel",
    (),
    {
         'ERROR' : 'alert-danger',
         'WARNING' : 'alert-warning',
         'INFO' : 'alert-info',
         'SUCCESS' : 'alert-success'
    })


def new_message(level, content):
    """
    Construit un dictionnaire sous la forme
    {'level' = 'alert-info', # Peut être aussi 'alert-success', 'alert-danger'...
     'content' = "The message's content"}
    """
    return {'level' : level, 'content' : content}
