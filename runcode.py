# Import libraries
import grass.script as gs
import os

# Set working directory
os.chdir("/home/paulo/SDM/Outputs/")

# Set region
gs.run_command("g.region", region="region_aoi@climate")

# Variable
variables = [f"bio.{num}" for num in list(range(1, 20))]

names = [
    "BIO1 - Annual Mean Temperature",
    "BIO2 - Mean Diurnal Range",
    "BIO3 - Isothermality",
    "BIO4 - Temperature Seasonality",
    "BIO5 - Max Temperature of Warmest Month",
    "BIO6 - Min Temperature of Coldest Month",
    "BIO7 - Temperature Annual Range",
    "BIO8 - Mean Temperature of Wettest Quarter",
    "BIO9 - Mean Temperature of Driest Quarter",
    "BIO10 - Mean Temperature of Warmest Quarter",
    "BIO11 - Mean Temperature of Coldest Quarter",
    "BIO12 - Annual Precipitation",
    "BIO13 - Precipitation of Wettest Month",
    "BIO14 - Precipitation of Driest Month",
    "BIO15 - Precipitation Seasonality",
    "BIO16 - Precipitation of Wettest Quarter",
    "BIO17 - Precipitation of Driest Quarter",
    "BIO18 - Precipitation of Warmest Quarter",
    "BIO19 - Precipitation of Coldest Quarter",
]

# Output settings

# Output settings
width_image = 1200
title = "-"

# Get width/height ratio of image
region_settings = gs.region()
height = float(region_settings["rows"])
width = float(region_settings["cols"])
height_image = width_image/width * height

# Set environmental variables
os.environ["GRASS_RENDER_IMMEDIATE"] = "cairo"
os.environ["GRASS_RENDER_HEIGHT"] = str(height_image)
os.environ["GRASS_RENDER_WIDTH"] = str(width_image)
os.environ["GRASS_RENDER_BACKGROUNDCOLOR"] = "#e7f7fe"
os.environ["GRASS_RENDER_FILE_READ"] = "TRUE"
os.environ["GRASS_FONT"] = "DejaVuSansCondensed"

for i, variable in enumerate(variables):

    j = i + 1

    outputfile = f"futbio_{j}.png"
    os.environ["GRASS_RENDER_FILE"] = outputfile

    # Render image
    gs.run_command(
        "d.rast",
        map=f"{variable}@EC_Earth3_Veg",
    )
    gs.run_command(
        "d.vect",
        map="countries",
        type="area",
        color="white",
        fill_color="none",
        width=0.75,
    )
    gs.run_command(
        "d.vect",
        map="rangemap@Erebia_alberganus",
        type="area",
        color="255:0:0",
        fill_color="none",
        width=2,
    )
    gs.run_command(
        "d.legend",
        flags="bd",
        raster=variable,
        font="Arial:Regular",
        fontsize=12,
        at=[7, 9, 75, 97],
        title=names[i],
    )