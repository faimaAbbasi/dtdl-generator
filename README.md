
# DTDL Code Generator
A code generator is implemented to produce a <b>Digital Twin Definition Language (DTDL)</b> for <b>Model Graph</b> and <b>Twin Graph</b> using BESSER Structural and Object Model. 
This collection shows a <b>mobility scenario</b> implemented with BESSER, low-modeling low-code open-source platform, to be integrated with Azure DT Platform. 
Some of the significant highlights of code generator are stated as follow:

- [buml_Mobility:](https://github.com/faimaAbbasi/dtdl-generator/blob/main/buml_Mobility.py) This contains mobility scenario implemented with BESSER structural and object model. 
- [dtdl_generator:](https://github.com/faimaAbbasi/dtdl-generator/blob/main/dtdl_generator.py) This file contains the Generator Interface from BESSER to generate code for Model and Twin Graph to be uploaded on Azure DT platform.
- [ModelGraph_template](https://github.com/faimaAbbasi/dtdl-generator/blob/main/templates/ModelGraph_template.j2) and [TwinGraph_template](https://github.com/faimaAbbasi/dtdl-generator/blob/main/templates/TwinGraph_template.j2) in template folder are jinja templates confirming to BESSER Structural and object model for Model and Twin Graph creation.
- [ModelGraph](https://github.com/faimaAbbasi/dtdl-generator/blob/main/output/ModelGraph.py) and [TwinGraph](https://github.com/faimaAbbasi/dtdl-generator/blob/main/output/TwinGraph.py) in output folder contains the generated code regarding the mobility scenario.

## Graphs on Azure DT Platform [Results]

### Model Graph

![ModelGraph](https://github.com/faimaAbbasi/dtdl-generator/assets/97727827/c212cc7e-eb11-4f73-8e56-0ed2d2b46d60)

### Twin Graph

![TwinGraph](https://github.com/faimaAbbasi/dtdl-generator/assets/97727827/51a134ca-37a1-4b88-a349-5e5f5449a114)


