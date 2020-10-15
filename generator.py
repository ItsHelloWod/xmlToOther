#generate specified quantity train data, the others as val data
def generate_data(num,src,dst,classes = {'apple':90,'orange':90}):
    import random
    total_xml=os.listdir(src+'Annotations/')
    
    imgs={}
    imgs['train'] = []
    imgs['val'] = []
    for class_name in classes.keys():
        train = []
        val = []
        while len(train) + len(val)< classes[class_name]:
            index = random.randint(1,95)#95 is the size of each class, you can set it by yourself
            #避免缺失数据
            exsit = False
            while not exsit:
                index = random.randint(1,95)
                name=class_name+'_'+str(index)
                exsit = os.path.isfile(src+'Annotations/'+name+'.xml')
            
            img_name = class_name+'_'+str(index)
            if len(train) < num and img_name not in train:
                train.append(class_name+'_'+str(index))
            elif img_name not in val:
                val.append(class_name+'_'+str(index))
        imgs[class_name]={}
        imgs['train'].extend(train)
        imgs['val'].extend(val)
        print(len(train),len(val))
        val=[]
        train=[]
    
    random.shuffle(imgs['train'])
    random.shuffle(imgs['val'])

    train_xml_dir = [src +'Annotations/' + str(index) + '.xml' for index in imgs['train']]
    val_xml_dir = [src +'Annotations/' + str(index) + '.xml' for index in imgs['val']]

    train_VOC2COCO = VOC2COCO()
    val_VOC2COCO = VOC2COCO()
    
    train_VOC2COCO.parseXmlFiles(train_xml_dir,dst+'annotations/')
    val_VOC2COCO.parseXmlFiles(val_xml_dir,dst+'annotations/')

    #copy_imgs(src,dst,imgs)

#copy img from src to dst 
def copy_imgs(src,dst,indices):
  dst_train = dst + 'train2017/'
  dst_val = dst + 'val2017/'

  if os.path.exists(dst_train):
    shutil.rmtree(dst_train)
    shutil.rmtree(dst_val)

  os.mkdir(dst_train)
  os.mkdir(dst_val)

  for img_name in indices['train']:
    train_src_dir = src + 'JPEGImages/' + img_name + '.jpg'
    trian_dst_dir = dst_train + img_name + '.jpg'
    shutil.copyfile(train_src_dir,trian_dst_dir)

  for img_name in indices['val']:
    val__src_dir = src + 'JPEGImages/' + img_name + '.jpg'
    val_dst_dir = dst_val + img_name + '.jpg'
    shutil.copyfile(val__src_dir,val_dst_dir)
  
  print("copy {} and {} images on trainset and valset".format(len(os.listdir(dst+'train2017')),len(os.listdir(dst+'val2017'))))
