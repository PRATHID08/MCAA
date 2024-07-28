names = ["Black", "Red", "Maroon", "Yellow"]
codes = ["#000000", "#FF0000", "#800000", "#FFFF00"]

colors_list = [dict(color_name=x, color_code=y) for (x,y) in zip(names, codes)]
print(colors_list)