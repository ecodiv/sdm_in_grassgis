# Import libraries
import grass.script as gs
import os

os.chdir("path_to_working_directory")

# Variable
variable = "model01_presabschange"
name = "model01_presabschange"

# Set region
gs.run_command("g.region", raster=variable, n="n+5")

# Output settings
width_image = 1200
title = "-"

# Get width/height ratio of image
region_settings = gs.region()
height = float(region_settings["n"]) - float(region_settings["s"])
width = float(region_settings["e"]) - float(region_settings["w"])
height_image = width_image / (width / height)

# Set environmental variables
os.environ["GRASS_RENDER_IMMEDIATE"] = "cairo"
os.environ["GRASS_RENDER_HEIGHT"] = str(height_image)
os.environ["GRASS_RENDER_WIDTH"] = str(width_image)
os.environ["GRASS_RENDER_BACKGROUNDCOLOR"] = "#e7f7fe"
os.environ["GRASS_RENDER_FRAME"] = f"0,{height_image},0,{width_image}"
os.environ["GRASS_RENDER_FILE_READ"] = "TRUE"
os.environ["GRASS_FONT"] = "DejaVuSansCondensed"

outputfile = f"{name}.png"
try:
    os.remove(outputfile)
except FileNotFoundError:
    pass
os.environ["GRASS_RENDER_FILE"] = outputfile

gs.run_command("d.rast", map=variable)
gs.run_command(
    "d.vect", map="map_inset", type="area", color="red", fill_color="none", width=2
)

gs.run_command(
    "d.legend",
    flags="bt",
    raster=variable,
    font="Arial:Regular",
    fontsize=16,
    at=[75, 94, 80, 84],
)

os.environ["GRASS_RENDER_FRAME"] = f"0,{height_image/2},20,{width_image/2}"

gs.run_command("g.region", vector="map_inset")
gs.run_command("d.rast", map=variable)
gs.run_command(
    "d.vect", map="map_inset", type="area", color="red", fill_color="none", width=4
)
