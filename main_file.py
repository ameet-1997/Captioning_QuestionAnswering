import os

# Invoke the Show Attend and Tell
path = '/home/ubuntu/project/im2txt'
os.chdir(path)
os.system('bazel-bin/im2txt/run_inference --checkpoint_path=/home/ubuntu/project/Pretrained-Show-and-Tell-model/model.ckpt-2000000 --vocab_file=/home/ubuntu/project/Pretrained-Show-and-Tell-model/word_counts.txt --input_files=/home/ubuntu/test.jpg >output.txt')

f = open('output.txt','r')
lines = f.readlines()
for line in lines:
    temp = line.strip().split()
    if temp[0][0] == '0':
	answer = ' '.join(temp[1:-1])
	print(answer)

path = '/home/ubuntu/project/VQA_Demo'
os.chdir(path)
#os.system('sudo python demo.py -image_file_name test.jpg -question "Is there a phone in the picture?" > output.txt')
