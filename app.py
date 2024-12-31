from flask_cors import CORS, cross_origin
from flask import Flask, render_template, request, jsonify
from scrapperImage.ScrapperImage import ScrapperImage
from businesslayer.BusinessLayerUtil import BusinessLayer
import os


app = Flask(__name__)

@app.route('/')
@cross_origin()
def home():
    return render_template('index.html')

@app.route('/showImages')
@cross_origin()
def displayImages():
    list_images = os.listdir('static')
    print(list_images)
    try:
        if(len(list_images)>0):
            return render_template('showImage.html',user_images=list_images)
        else:
            return "Images are not present"
    except Exception as e:
        print("No images found",e)
        return "Please try with a different search keyword"
    
@app.route('/searchImages', methods=['GET','POST'])
def searchImage():
    if request.method == 'POST':
        search_term=request.form['keyword']
    else:
        print("Please enter something")
    imagescrapperutil=BusinessLayer
    imagescrapper=ScrapperImage()
    list_images=os.listdir('static')
    imagescrapper.delete_downloaded_images(list_images)

    image_name=search_term.split()
    image_name="+".join(image_name)

    header={
        'User-Agent':"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
    }
    lst_images=imagescrapperutil.downloadImages(search_term, header)
    return displayImages()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)