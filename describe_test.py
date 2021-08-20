
desc = arcpy.Describe(shapefiles)
print("Name: {}".format(desc.name))
if hasattr(desc, "layer"):
    print("Layer name: {}".format(desc.layer.name))
    print("Layer data source: {}".format(desc.layer.catalogPath))
    print(".lyr file: {}".format(desc.catalogPath))
if hasattr(desc, "name"):
        print("Name:        " + desc.name)
else:
    print("Layer name: {}".format(desc.name))
    print("Layer data source: {}".format(desc.catalogPath))

print("Children:")
for child in desc.children:
    print("\t%s = %s" % (child.name, child.dataType))


###
field_types = arcpy.ListFields(shapefiles)

for field in field_types:
    print('field type =' + field.type)

field_names = [f.name for f in arcpy.ListFields(shapefiles)]
print(field_names[3])
