# xmlToOther
Object detection data transform from voc to yolo/coco

A class VOC2YOLO is responsible for transformation of voc to yolo.

Generate data method is for generate random specified quantity train data and the others from src data is used for validation.
It will copy imgs from src to dst and generate two dir, train dir and val dir.
