#!/usr/bin/python

import cv2
import os

def main():
  plot_type = "density"
  #images_dir = "/work/06143/tiwarvis/stampede2/runs/super3d_hd_new/run10_maxblock15/images/"
  #images_dir = "/work/06143/tiwarvis/stampede2/rahul_runs/run_179/images/"
  #images_dir = "/work/06143/tiwarvis/stampede2/runs/super3d_hd_new/run10_maxblock15/images/"
  #images_dir = "/work/06143/tiwarvis/stampede2/runs/super3d_hd_new/run11/images/"
  #images_dir = "/scratch/06143/tiwarvis/datasets/super_3d_new_data/run11_plt_files/images/"
  images_dir = "/home/vishal/UMassD/sem2/astro_phy/project/png/"
  
  video_name = "pre_ccsn.avi"
  
  os.chdir(images_dir)
  images = [img for img in os.listdir(images_dir) if img.endswith(".png")]
  
  frame = cv2.imread(images[0])
  height, width, layers = frame.shape
  video = cv2.VideoWriter(video_name , 0 , 24 , (width , height))

  # sort the file according to name.
  images.sort()
  for image_name in images:
    print(image_name)
    video.write(cv2.imread(image_name))

  video.release()

if __name__ == "__main__":
  main()
