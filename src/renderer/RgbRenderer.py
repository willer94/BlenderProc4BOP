import bpy, os, random
from src.renderer.Renderer import Renderer
from src.utility.Utility import Utility


class RgbRenderer(Renderer):
    """ Renders rgb images for each registered keypoint.

    Images are stored as PNG-files with 8bit color depth.
    """
    def __init__(self, config):
        Renderer.__init__(self, config)
        self.bg_img_dir = '/media/willer/data/BOP/BlenderProc4BOP/bg_img'
        self.bg_img_files = [item for item in os.listdir(self.bg_img_dir) if item.split('.')[-1] in ['jpg', 'png']]
        
    def run(self):
        with Utility.UndoAfterExecution():
            self._configure_renderer()

            # In case a previous renderer changed these settings
            bpy.context.scene.render.film_transparent = True
            bpy.context.scene.render.image_settings.color_mode = 'RGBA'
            #bpy.context.scene.render.image_settings.color_mode = "RGB"
            bpy.context.scene.render.image_settings.file_format = "PNG"
            bpy.context.scene.render.image_settings.color_depth = "8"

            self._render("rgb_")
        self._register_output("rgb_", "colors", ".png", "1.0.0")
