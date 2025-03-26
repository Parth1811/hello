import os
import sys

folder_name = sys.argv[1]
only_prop = True

def find_cbmc_xml_files(folder):
    cbmc_xml_files = []
    property_files = []
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file == "cbmc.xml":
                cbmc_xml_files.append(os.path.join(root, file))
                property_files.append(os.path.join(root, "property.xml"))
    return cbmc_xml_files, property_files

cbmc_xml_files, property_files = find_cbmc_xml_files(folder_name)

for i ,file_name in enumerate(cbmc_xml_files):
    name = os.path.basename(os.path.dirname(file_name))

    with open(file_name, 'r') as file:
        lines = file.readlines()
    
    with open(property_files[i], 'r') as file:
        prop_lines = file.readlines()
        total_props = len([line for line in prop_lines if line.count("</property") > 0])


    iter = 1
    total = 0
    # total_props = 0
    if only_prop:
        print(f"Total properties for {name}: {total_props} properties")
    else:
        for i, line in enumerate(lines):
            if line.count("Runtime Solver:") > 0:
                runtime = line
                prop_updated = lines[i+4]

                runtime = runtime.split("Solver:")[1].split("s</text>")[0].strip()
                prop_updated = prop_updated.split("properties:")[1].split("</text>")[0].strip()

                print(f"Harness: {name}, Iteration {iter}: Runtime: {runtime}s, Properties Updated: {prop_updated}")
                iter += 1
                total += float(runtime)
                # total_props += int(prop_updated)

        print(f"Total runtime for {name}: {total:.06f}s, Total properties updated: {total_props} properties")