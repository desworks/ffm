import os
import ffmpy
import re

infiles = list()
outfiles = list()
codec = 'h264_nvenc'
parastr = '-c:v ' + codec + ' -crf 32 -c:a aac -b:a 128k'
endings = '.mp4'

def initin(infiles):
    infiles = os.listdir(".\\")              # list in dir
    r = re.compile(".*.mp4")                 # sort out media
    infiles = list(filter(r.match, infiles)) # get media
    return infiles

def initout(infiles, outfiles, codec, endings):
    codec = '_' + str(codec)
    for f in infiles:
        outfiles.append(str(f).replace(endings, codec + endings))
    return outfiles

def conv(infile, outfile, params):
    ff = ffmpy.FFmpeg(inputs={infile:None}, outputs={outfile:params})
    ff.run()

infiles = initin(infiles)
outfiles = initout(infiles, outfiles, codec, endings)


#printout
print(infiles)
print(outfiles)
#for f in files:
#    print(f)
#p = os.path.abspath('.\\') + '\\flg.mp4'
#print(p)
#s = ffmpeg.probe(p)
#ffmpeg.exe -i D:\dls\haley\h_01.mp4 -c:v h264_nvenc -crf 32 -c:a aac -b:a 128k h_01_264.mp4
#print(os.path.abspath('.\\'))
#n = p + '_neu.mp4'

def test():
    testi = 'hallo.mp4'
    testi = testi.replace('.mp4','_new.mp4')
    print(testi)
