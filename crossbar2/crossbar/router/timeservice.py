###############################################################################
##
##  Copyright (C) 2014 Tavendo GmbH
##
##  Licensed under the Apache License, Version 2.0 (the "License");
##  you may not use this file except in compliance with the License.
##  You may obtain a copy of the License at
##
##      http://www.apache.org/licenses/LICENSE-2.0
##
##  Unless required by applicable law or agreed to in writing, software
##  distributed under the License is distributed on an "AS IS" BASIS,
##  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
##  See the License for the specific language governing permissions and
##  limitations under the License.
##
###############################################################################

import datetime

from autobahn.twisted.wamp import ApplicationSession



class TimeService(ApplicationSession):
   """
   A simple time service application component.
   """
   def __init__(self, realm = None):
      ApplicationSession.__init__(self)
      self._realm = realm
      print "666"


   def onConnect(self):
      print "555"
      print self._realm
      self.join(self._realm)
      print "oioio"


   def onJoin(self, details):
      print "4555"

      def utcnow():
         now = datetime.datetime.utcnow()
         return now.strftime("%Y-%m-%dT%H:%M:%SZ")

      self.register(utcnow, 'com.timeservice.now')
