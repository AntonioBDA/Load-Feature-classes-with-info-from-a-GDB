#Importing libraries
import arcpy
import os

#Defining the gdb path
path = arcpy.GetParameterAsText(0)
arcpy.env.workspace = path

#Listing datasets and adding datasets to the list
datasets = arcpy.ListDatasets(feature_type='feature')
datasets = [''] + datasets if datasets is not None else []

#Defining the mxd and dataframe to be used
mxd = arcpy.mapping.MapDocument('CURRENT')
df = arcpy.mapping.ListDataFrames(mxd)[0]

#Iterate datasets and feature classes to load only those who had some information
for ds in datasets:
    for fc in arcpy.ListFeatureClasses(feature_dataset=ds):
        path = os.path.join(arcpy.env.workspace, ds, fc)
        count  = int(arcpy.GetCount_management(path).getOutput(0))
        if count > 0:
            addLayer = arcpy.mapping.Layer(fc)
            arcpy.mapping.AddLayer(df, addLayer, "AUTO_ARRANGE")
            arcpy.AddMessage("Loaded {0}".format(fc))
