import os
from glob import glob

from visualizer import Visualizer
from converter import Converter

width = 640
height = 640
square_size = 32

annotation_path = "example_annotations.xml"

in_images_path = "debug"
out_images_path = "./out/"

converter = Converter(annotation_path, width, height, square_size)
# recursevly find all images in in_image_path
images = [y for x in os.walk(in_images_path) for y in glob(os.path.join(x[0], '*.jpg'))]
for image_path in images:
    image_name = os.path.basename(image_path)
    print(image_path)

    polylines = converter.get_polylines(image_name)
    squares = converter.to_cartesian(polylines)

    img = Visualizer(image_path, width, height, square_size)
    img.draw_grid()
    img.draw_cartesian_predictors(squares)
    img.draw_true_polylines(polylines)
    img.draw_cartesian_intersections(squares)
    img.save_image(out_path=out_images_path)
