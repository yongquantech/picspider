# coding=utf-8
import requests, os, codecs, json, pdb

SERVER="https://unsplash.com"

class PictureDownloader():

    def __init__(self, page):
        self.page=str(page)

    def get_picture_ids(self):
        target = SERVER + "/napi/photos?page=" + self.page + "&per_page=12&order_by=latest"
        req = requests.get(url=target)
        html = json.loads(req.text)
        pic_ids = []
        for each in html:
            pic_ids.append(each['id'])
        return pic_ids

    def download_picture(self):
        ids = self.get_picture_ids()
        # https://unsplash.com/photos/Moj5L7OhpLI/download?force=true
        for each in ids:
            target = SERVER + "/photos/" + each + "/download?force=true"
            req = requests.get(url=target)
            path = os.path.expanduser('~')+'\\Downloads\\'+ each +".jpg"
            fl = open(path, 'wb')
            fl.write(req.content)
            fl.close()



if __name__ == '__main__':
    pd = PictureDownloader(4)
    pd.download_picture()
