#  main.py Copyright (C) 2024  Konta Boáz
#      This program comes with ABSOLUTELY NO WARRANTY; for details type `show w'.
#      This is free software, and you are welcome to redistribute it
#      under certain conditions; type `show c' for details.
#   Last Modified: 2024. 06. 04. 11:23
import re

import torchvision.models as models
from ptflops import get_model_complexity_info

# Model thats already available
net = models.densenet161()
macs, params = get_model_complexity_info(
    net, (3, 224, 224), as_strings=True, print_per_layer_stat=True, verbose=False
)
# Extract the numerical value
flops = eval(re.findall(r"([\d.]+)", macs)[0]) * 2
flops_unit = re.findall(r"([A-Za-z]+)", macs)[0][0]

print("Computational complexity: {:<8}".format(macs))
print("Computational complexity: {} {} Flops".format(flops, flops_unit))
print("Number of parameters: {:<8}".format(params))
