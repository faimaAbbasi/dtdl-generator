######################################
#   DTDL mobility twin definition  #
######################################

from azure.core.exceptions import HttpResponseError
from azure.identity import DefaultAzureCredential
from azure.digitaltwins.core import DigitalTwinsClient
import os
from azure.core.exceptions import ResourceNotFoundError
import json
import warnings
warnings.filterwarnings("ignore")
warnings.simplefilter("ignore")

# Building a connection with AzureDT Platform
os.environ['AZURE_URL'] = 'https://mddteu.api.weu.digitaltwins.azure.net'
url = os.getenv('AZURE_URL')
credential = DefaultAzureCredential()
client = DigitalTwinsClient(url, credential)

# Creating Digital Twins Using BUML Object Model
BusStop02={
    "$metadata": {
        "$model": "dtmi:example:BusStop;1"
    },
    "$dtId":"BusStop02",
    "name":"PortedeFrance",
    "busArrivalTime":"12:30:00",
}
# Adding Twins to Platform
add_twin = client.upsert_digital_twin("BusStop02",BusStop02)
BusStop01={
    "$metadata": {
        "$model": "dtmi:example:BusStop;1"
    },
    "$dtId":"BusStop01",
    "name":"PortedeSciences",
    "busArrivalTime":"14:30:00",
}
# Adding Twins to Platform
add_twin = client.upsert_digital_twin("BusStop01",BusStop01)
Bus01={
    "$metadata": {
        "$model": "dtmi:example:Bus;1"
    },
    "$dtId":"Bus01",
    "brand":"Ford",
    "tankCapacity":50,
    "distanceCovered":1000,
    "distanceUnits":"meters",
    "OccupancySensor":{
        "$metadata": {
        },
        "$dtId":"OccSensor01",
        "peopleIn":10,
        "peopleOut":50,
    }
}
# Adding Twins to Platform
add_twin = client.upsert_digital_twin("Bus01",Bus01)
Bus02={
    "$metadata": {
        "$model": "dtmi:example:Bus;1"
    },
    "$dtId":"Bus02",
    "brand":"Scania",
    "tankCapacity":70,
    "distanceCovered":100,
    "distanceUnits":"Kilo-meters",
    "OccupancySensor":{
        "$metadata": {
        },
        "$dtId":"OccSensor02",
        "peopleIn":5,
        "peopleOut":16,
    }
}
# Adding Twins to Platform
add_twin = client.upsert_digital_twin("Bus02",Bus02)

# Creating Relations between Twins
relationship_id="is_having"
source="BusStop02"
target="Bus02"
rel_name="is_having"
relationship={
    "$relationshipId": relationship_id,
    "$sourceId": source,
    "$relationshipName": rel_name,
    "$targetId": target,
}
# Adding Relations Between Twins
client.upsert_relationship(source, relationship_id, relationship)

relationship_id="arrivesAt"
source="Bus02"
target="BusStop02"
rel_name="arrivesAt"
relationship={
    "$relationshipId": relationship_id,
    "$sourceId": source,
    "$relationshipName": rel_name,
    "$targetId": target,
}
# Adding Relations Between Twins
client.upsert_relationship(source, relationship_id, relationship)
relationship_id="is_having"
source="BusStop01"
target="Bus01"
rel_name="is_having"
relationship={
    "$relationshipId": relationship_id,
    "$sourceId": source,
    "$relationshipName": rel_name,
    "$targetId": target,
}
# Adding Relations Between Twins
client.upsert_relationship(source, relationship_id, relationship)

relationship_id="arrivesAt"
source="Bus01"
target="BusStop01"
rel_name="arrivesAt"
relationship={
    "$relationshipId": relationship_id,
    "$sourceId": source,
    "$relationshipName": rel_name,
    "$targetId": target,
}
# Adding Relations Between Twins
client.upsert_relationship(source, relationship_id, relationship)
