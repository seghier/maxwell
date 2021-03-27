import os

from flask import Flask
import ghhops_server as hs
import rhino3dm

import _pymaxwell5 as pym

app = Flask(__name__) #flask
hops = hs.Hops(app) #flask

#hops = hs.Hops() #http

@hops.component(
    "/maxwell",
    name="Maxwell",
    description="render",
    icon="C://Users//archi//Dropbox//course//maxwell.png",
    inputs=[
        hs.HopsBoolean("run","run","render scene"),
        hs.HopsString("width","width",""),
        hs.HopsString("height","height",""),
        hs.HopsString("time","time",""),
        hs.HopsString("sl","sl",""),
        hs.HopsString("img","img",""),
        hs.HopsString("mxi","mxi",""),
        hs.HopsString("mxs_file","inPath",""),
        hs.HopsString("output_folder","outFolder",""),
    ],
    outputs=[
        hs.HopsString('image','image','')
    ]
)

def maxwell(run,width,height,time,sl,img,mxi,inPath, outFolder):
    if run:
        return run_maxwell_render(width,height,time,sl,img,mxi,inPath, outFolder)
    else:
        return outFolder + img

def run_maxwell_render(width,height,time,sl,img,mxi,inPath, outFolder):
    if not os.path.exists(outFolder):
        os.mkdir(outFolder)
    parameters = []
    parameters.append('-mxs:' + inPath)
    parameters.append('-o:' + outFolder + img)
    parameters.append('-mxi:' + outFolder + mxi)
    parameters.append('-res:' + width + 'x' + height)
    parameters.append('-time:' + time)
    parameters.append('-sl:' + sl)
    # parameters.append('-nowait')
    parameters.append('-nomxi:off')
    parameters.append('-noimage:off')
    pym.runMaxwell(parameters)
    return outFolder+img

if __name__ == "__main__":
    app.run() #flask
    #hops.start(debug=True) #http
