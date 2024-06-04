
# DTDL Code Generator
A code generator is implemented to produce a <b>Digital Twin Definition Language (DTDL)</b> for <b>Model Graph</b> and <b>Twin Graph</b> using BESSER Structural and Object Model. 
This collection shows a <b>mobility scenario</b> implemented with BESSER, low-modeling low-code open-source platform, to be integrated with Azure DT Platform. 
Some of the significant highlights of code generator are stated as follow:

- [buml_Mobility:](#buml_Mobility.py) This contains mobility scenario implemented with BESSER structural and object model. 
- [dtdl_generator:](#dtdl_generator.py) This file contains the Generator Interface from BESSER to generate code for Model and Twin Graph to be push on Azure DT platform.
- [ModelGraph_template](#ModelGraph_template.j2) and [TwinGraph_template](#TwinGraph_template.j2) in template folder are jinja templates confirming to BESSER Structural and object model for Model and Twin Graph creation.
- [ModelGraph](#ModelGraph.py) and [TwinGraph](#TwinGraph.py) in output folder contains the generated code regarding the mobility scenario.
