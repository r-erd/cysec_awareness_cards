import os
import subprocess
import argparse

if __name__ == "__main__":
    def watermark_images(image_folder, watermark_path, output_folder):
        # Get all png files in the image folder
        images = [f for f in os.listdir(image_folder) if f.endswith('.png')]
        for image in images:
            image_path = os.path.join(image_folder, image)
            output_path = os.path.join(output_folder, image)

            # Make sure that the output path exists, if it does not, create the folder
            os.makedirs(output_folder, exist_ok=True)

            # Use ImageMagick to add watermark
            subprocess.run(['composite', '-dissolve', '30%', '-gravity', 'South', watermark_path, image_path, output_path])
            # Use ExifTool to remove sensitive information
            subprocess.run(['exiftool', '-all=', output_path])

            # Delete all files in output_folder that are not images (png)
            for f in os.listdir(output_folder):
                if not f.endswith('.png'):
                    os.remove(os.path.join(output_folder, f))

    if __name__ == "__main__":
        parser = argparse.ArgumentParser(description='Add watermark to images and remove sensitive information.')
        parser.add_argument('image_folder', help='Path to the folder containing the images')
        parser.add_argument('watermark_path', help='Path to the watermark image')
        parser.add_argument('--output_folder', default='assets', help='Path to the output folder (default: assets)')
        args = parser.parse_args()

        watermark_images(args.image_folder, args.watermark_path, args.output_folder)
