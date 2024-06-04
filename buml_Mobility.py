from besser.BUML.metamodel.structural import DomainModel
from besser.BUML.metamodel.structural import NamedElement, Type, Class, \
        Property, PrimitiveDataType, Multiplicity, Association, BinaryAssociation, Generalization, \
        GeneralizationSet, AssociationClass 
from besser.utilities import ModelSerializer
from dtdl_generator import ModelGraph
from dtdl_generator import TwinGraph
from datetime import datetime
from besser.BUML.metamodel.object import *
from datetime import time


#####################################
#   BUML Mobility model definition  #
#####################################

# Primitive DataTypes
t_int: PrimitiveDataType = PrimitiveDataType("int")
t_float: PrimitiveDataType = PrimitiveDataType("float")
t_str: PrimitiveDataType = PrimitiveDataType("str")
t_date: PrimitiveDataType = PrimitiveDataType("date")
t_time: PrimitiveDataType = PrimitiveDataType("time")

# Vehicle Attribute Definition
brand: Property = Property(name="brand", type=t_str)
# Vehicle class definition
Vehicle: Class = Class (name="Vehicle", attributes={brand})

# Occupancy Sensor Attribute Definition
peopleIn: Property = Property(name="peopleIn", type=t_int)
peopleOut: Property = Property(name="peopleOut", type=t_int)
# Occupancy Sensor definition
OccSensor: Class = Class (name="OccupancySensor", attributes={peopleIn, peopleOut})


# Bus Attribute Definition
tankCapacity: Property = Property(name="tankCapacity", type=t_int)
disatnceUnits: Property = Property(name="distanceUnits", type=t_str)
disatnceCovered: Property = Property(name="distanceCovered", type=t_float)
# Bus class definition
Bus: Class = Class (name="Bus", attributes={tankCapacity,disatnceUnits,disatnceCovered})


# Bus Stop Attribute Definition
name: Property = Property(name="name", type=t_str)
busArrivalTime: Property = Property(name="busArrivalTime", type=t_time)
# Bus Stop class definition
Station: Class = Class (name="BusStop", attributes={busArrivalTime, name})


gen_Vehicle: Generalization = Generalization(general=Vehicle, specific=Bus)
Vehicle_gen_set: GeneralizationSet = GeneralizationSet(name="Vehicle_gen_set", generalizations={gen_Vehicle}, is_complete=True, is_disjoint=True)

arrivesAt: Property = Property(name="arrivesAt", type=Station, multiplicity=Multiplicity(1, 1))
is_having: Property = Property(name="is_having", type=Bus, multiplicity=Multiplicity(1, "*"))
bus_station_assoc: BinaryAssociation = BinaryAssociation(name="bus_station_assoc", ends={arrivesAt, is_having})


located_in: Property = Property(name="locatedIn",type=Bus, multiplicity=Multiplicity(1, 1), is_composite=True)
has: Property = Property(name="has", type=OccSensor, multiplicity=Multiplicity(0, "*"))
sensor_bus_assoc: BinaryAssociation = BinaryAssociation(name="composition", ends={located_in, has})


mobility_model: DomainModel = DomainModel(name="mobility_model", types={Vehicle, OccSensor, Bus, Station, },
                                associations={arrivesAt,located_in,has, is_having,bus_station_assoc,sensor_bus_assoc},
                                generalizations={gen_Vehicle,Vehicle_gen_set})

mg_generator: ModelGraph = ModelGraph(model=mobility_model)
mg_generator.generate()

######################################
#   BUML mobility Object definition  #
######################################

# Occupancy Sensor 01 Attributes
peopleIn_val1: AttributeLink = AttributeLink(attribute=peopleIn, value=DataValue(classifier=t_int, value=10))
peopleOut_val1: AttributeLink = AttributeLink(attribute=peopleOut, value=DataValue(classifier=t_int, value=50))
# Occupancy Sensor 01 Object
sensorObj01: Object = Object(name="OccSensor01", classifier=OccSensor, slots=[peopleIn_val1, peopleOut_val1])


# Occupancy Sensor 02 Attributes
peopleIn_val2: AttributeLink = AttributeLink(attribute=peopleIn, value=DataValue(classifier=t_int, value=5))
peopleOut_val2: AttributeLink = AttributeLink(attribute=peopleOut, value=DataValue(classifier=t_int, value=16))
# Occupancy Sensor 02 Object
sensorObj02: Object = Object(name="OccSensor02", classifier=OccSensor, slots=[peopleIn_val2, peopleOut_val2])



# Bus 01 object attributes
brand_name1: AttributeLink = AttributeLink(attribute=brand, value=DataValue(classifier=t_str, value="Ford"))
tankCapacity_val1: AttributeLink = AttributeLink(attribute=tankCapacity, value=DataValue(classifier=t_int, value=50))
disatnceCovered_val1: AttributeLink = AttributeLink(attribute=disatnceCovered, value=DataValue(classifier=t_int, value=1000))
disatnceUnits_val1: AttributeLink = AttributeLink(attribute=disatnceUnits, value=DataValue(classifier=t_str, value="meters"))
# Bus 01 object
Bus_obj01: Object = Object(name="Bus01", classifier=Bus, slots=[brand_name1, tankCapacity_val1, disatnceCovered_val1, disatnceUnits_val1])


# Bus object 02 attributes
brand_name2: AttributeLink = AttributeLink(attribute=brand, value=DataValue(classifier=t_str, value="Scania"))
tankCapacity_val2: AttributeLink = AttributeLink(attribute=tankCapacity, value=DataValue(classifier=t_int, value=70))
disatnceCovered_val2: AttributeLink = AttributeLink(attribute=disatnceCovered, value=DataValue(classifier=t_int, value=100))
disatnceUnits_val2: AttributeLink = AttributeLink(attribute=disatnceUnits, value=DataValue(classifier=t_str, value="Kilo-meters"))
# Bus 02 object
Bus_obj02: Object = Object(name="Bus02", classifier=Bus, slots=[brand_name2, tankCapacity_val2, disatnceCovered_val2, disatnceUnits_val2])

# Bus stop 1 object attributes
name_val1: AttributeLink = AttributeLink(attribute=name, value=DataValue(classifier=t_str, value="PortedeSciences"))
busArrivalTime_val1: AttributeLink = AttributeLink(attribute=busArrivalTime, value=DataValue(classifier=t_time, value=time(14, 30, 0)))
Station_obj01: Object = Object(name="BusStop01", classifier=Station, 
                             slots=[name_val1, busArrivalTime_val1])


# Bus stop 2 object attributes
name_val2: AttributeLink = AttributeLink(attribute=name, value=DataValue(classifier=t_str, value="PortedeFrance"))
busArrivalTime_val2: AttributeLink = AttributeLink(attribute=busArrivalTime, value=DataValue(classifier=t_time, value=time(12, 30, 0)))
Station_obj02: Object = Object(name="BusStop02", classifier=Station, 
                             slots=[name_val2, busArrivalTime_val2])


#  Station and Bus object link 1
station_link_end1: LinkEnd = LinkEnd(name="station_end", association_end=is_having, object=Bus_obj01)
bus_link_end1: LinkEnd = LinkEnd(name="bus_end", association_end=arrivesAt, object=Station_obj01)
bus_station_link1: Link = Link(name="bus_station_link", association=bus_station_assoc, connections=[station_link_end1,bus_link_end1])

#  Occupancy Sensor and Bus object link 1
sensor_link_end1: LinkEnd = LinkEnd(name="sensor_end", association_end=has, object=sensorObj01)
comp_bus_link_end1: LinkEnd = LinkEnd(name="bus_end", association_end=located_in, object=Bus_obj01)
bus_sensor_link1: Link = Link(name="composition", association=sensor_bus_assoc, connections=[sensor_link_end1,comp_bus_link_end1])


#  Station and Bus object link 2
station_link_end2: LinkEnd = LinkEnd(name="station_end", association_end=is_having, object=Bus_obj02)
bus_link_end2: LinkEnd = LinkEnd(name="bus_end", association_end=arrivesAt, object=Station_obj02)
bus_station_link2: Link = Link(name="bus_station_link", association=bus_station_assoc, connections=[station_link_end2,bus_link_end2])

#  Occupancy Sensor and Bus object link 2
sensor_link_end2: LinkEnd = LinkEnd(name="sensor_end", association_end=has, object=sensorObj02)
comp_bus_link_end2: LinkEnd = LinkEnd(name="bus_end", association_end=located_in, object=Bus_obj02)
bus_sensor_link2: Link = Link(name="composition", association=sensor_bus_assoc, connections=[sensor_link_end2,comp_bus_link_end2])

# Object model definition
object_model: ObjectModel = ObjectModel(name="Object model", instances={sensorObj01, Bus_obj01, Station_obj01, sensorObj02, Bus_obj02, Station_obj02}, links={bus_station_link1, bus_sensor_link1, bus_station_link2, bus_sensor_link2})
tg_generator: TwinGraph = TwinGraph(obj=object_model)
tg_generator.generate()