import os
import ffmpy
import re
import logging
import sys
import shutil

infiles = list()
outfiles = list()
#parastr = '-c:v ' + codec + ' -crf 32 -c:a aac -b:a 128k'
codec = 'h264_nvenc'
parastr = '-c:v ' + codec + ' -rc vbr_hq -b:v 500K -maxrate:v 2M -vsync 2 -r 30 -c:a aac -b:a 128k'
#codec = 'hevc_nvenc'
#parastr = '-c:v ' + codec + ' -rc vbr_hq -b:v 1M -maxrate:v 2M -c:a aac -b:a 128k'
parain = '-hwaccel nvdec'
endings = '.mp4'
currentpath = os.path.dirname(os.path.abspath(__file__))
outfolder = 'out\\'

logging.basicConfig(filename='ffmlog.log',level=logging.DEBUG)

def initin(infiles):
    infiles = os.listdir(".\\")              # list in dir
    r = re.compile(".*.mp4")                 # sort out media
    infiles = list(filter(r.match, infiles)) # get media
    logging.debug('inside list: --------------')
    logging.debug(infiles)
    logging.debug('             --------------')
    return infiles

def initout(infiles, outfiles, codec, endings):
    codec = '_' + str(codec)
    for f in infiles:
        outfiles.append(str(f).replace(endings, codec + endings))
    logging.debug('outside list: --------------')
    logging.debug(infiles)
    logging.debug('              --------------')
    return outfiles

def conv(infile, outfile, params, outfolder):
    if os.path.isdir(currentpath + outfolder) is False:
        os.mkdir(currentpath + outfolder)
    else:
        print('dir vorhanden')

    try:
        ff = ffmpy.FFmpeg(inputs={infile:None}, outputs={outfolder + outfile:params})
        ff.run()
    except ffmpy.FFRuntimeError as e:
        logging.warning(e.args)
        logging.warning('SKIP CMD')
        try:
            shutil.copy2(infile, outfolder + '\\' + infile)
        except shutil.Error as e:
            logging.warn(e.args)

def doit(infiles, outfiles, parastr, outfolder):
    z = 0
    for f in infiles:
        print('working on: \"' + f + '\" | ' + str(len(infiles) - z) + ' file(s) left')
        logging.info('working on: \"' + f + '\" | ' + str(len(infiles) - z) + ' file(s) left')
        conv(infiles[z], outfiles[z], parastr, outfolder)
        z += 1

def printit():
    print(infiles[0])
    print(outfiles[0])

    print(infiles)
    print(outfiles)

#os.mkdir = '.\\out'

infiles = initin(infiles)
outfiles = initout(infiles, outfiles, codec, endings)

#conv
#conv(infiles[0], outfiles[0], parastr, outfolder)

doit(infiles, outfiles, parastr, outfolder)

#for f in files:
#    print(f)
#p = os.path.abspath('.\\') + '\\flg.mp4'
#print(p)
#s = ffmpeg.probe(p)
#ffmpeg.exe -i D:\dls\haley\h_01.mp4 -c:v h264_nvenc -crf 32 -c:a aac -b:a 128k h_01_264.mp4
#print(os.path.abspath('.\\'))
#n = p + '_neu.mp4'

#def test():
#    testi = 'hallo.mp4'
#    testi = testi.replace('.mp4','_new.mp4')
#    print(testi)
#