#####################################
#   DTDL Mobility model definition  #
#####################################

from azure.core.exceptions import HttpResponseError
from azure.identity import DefaultAzureCredential
from azure.digitaltwins.core import DigitalTwinsClient
import os
from azure.core.exceptions import ResourceNotFoundError
import json
import warnings
warnings.filterwarnings("ignore")
warnings.simplefilter("ignore")

# Building a connection with AzureDT platform
os.environ['AZURE_URL'] = 'https://mddteu.api.weu.digitaltwins.azure.net'
url = os.getenv('AZURE_URL')
credential = DefaultAzureCredential()
client = DigitalTwinsClient(url, credential)

# Creating Models Using BUML Classes
OccupancySensor={
    "@id": "dtmi:example:OccupancySensor;1",
    "@context": "dtmi:dtdl:context;2",
    "@type":"Interface",
    "displayName":"OccupancySensor",
    "contents": [
        {
            "@type":"Property",
            "name":"peopleIn",
            "schema":"integer"
        },
        {
            "@type":"Property",
            "name":"peopleOut",
            "schema":"integer"
        },
    ]
}
Vehicle={
    "@id": "dtmi:example:Vehicle;1",
    "@context": "dtmi:dtdl:context;2",
    "@type":"Interface",
    "displayName":"Vehicle",
    "contents": [
        {
            "@type":"Property",
            "name":"brand",
            "schema":"string"
        },
    ]
}
Bus={
    "@id": "dtmi:example:Bus;1",
    "@context": "dtmi:dtdl:context;2",
    "@type":"Interface",
    "displayName":"Bus",
    "extends": [
    "dtmi:example:Vehicle;1"
    ],
    "contents": [
        {
            "@type":"Property",
            "name":"distanceUnits",
            "schema":"string"
        },
        {
            "@type":"Property",
            "name":"distanceCovered",
            "schema":"float"
        },
        {
            "@type":"Property",
            "name":"tankCapacity",
            "schema":"integer"
        },
        {
        "@type":"Component",
        "name":"OccupancySensor",
        "schema": "dtmi:example:OccupancySensor;1"
        },
        {
        "@type":"Relationship",
        "name":"arrivesAt",
        "target": "dtmi:example:BusStop;1"
        },
    ]
}
BusStop={
    "@id": "dtmi:example:BusStop;1",
    "@context": "dtmi:dtdl:context;2",
    "@type":"Interface",
    "displayName":"BusStop",
    "contents": [
        {
            "@type":"Property",
            "name":"name",
            "schema":"string"
        },
        {
            "@type":"Property",
            "name":"busArrivalTime",
            "schema":"time"
        },
        {
        "@type":"Relationship",
        "name":"is_having",
        "target": "dtmi:example:Bus;1"
        },
    ]
}

# Pushing these models on Azure DT platform
models = client.create_models([OccupancySensor,Vehicle,Bus,BusStop])