from django.shortcuts import render
from django.core.paginator import Paginator
from myapp.models import Pic
from django.http import HttpResponse
import time
from PIL import Image


# Create your views here.

def index(request):
    return render(request, 'myapp/index.html')


def pictures(request, pIndex=1):
    ob = Pic.objects.all()
    p = Paginator(ob, 5)
    if pIndex < 1:
        pIndex = 1
    elif pIndex > p.num_pages:
        pIndex = p.num_pages
    ulist = p.page(pIndex)
    context = {'ps': ulist, 'pIndex': pIndex, 'plist': p.page_range}

    return render(request, 'myapp/pictures.html', context)


def upload(request):
    return render(request, 'myapp/upload.html')


def doupload(request):
    try:
        ob = Pic()
        ob.name = request.POST['name']
        ob.save()
        context = {'info': '添加成功'}
        myfile = request.FILES.get('pic', None)
        if not myfile:
            return HttpResponse('没有图片信息')
        filename = str(time.time()) + "." + myfile.name.split('.').pop()
        destination = open("./static/pics/" + filename, "wb+")
        for chunk in myfile.chunks():  # 分块写入文件
            destination.write(chunk)
        destination.close()
        #图片缩放代码
        im = Image.open("./static/pics/" + filename)
        # 缩放到75*75(缩放后的宽高比例不变):
        im.thumbnail((75, 75))
        # 把缩放后的图像用jpeg格式保存:
        im.save("./static/pics/s_" + filename, None)

        # 执行图片删除
        # os.remove("./static/pics/"+filename)
    except:
        context = {'info': '添加失败'}
    return render(request, 'myapp/doupload.html', context)


def edit(request, uid=0):
    try:
        ob = Pic.objects.get(id=uid)
        context = {'ps': ob}
        return render(request, 'myapp/edit.html', context)
    except:
        context = {'info': '没有找到要修改的信息'}
        return render(request, 'myapp/doupload.html', context)


def delete(request, uid=0):
    try:
        ob = Pic.objects.get(id=uid)
        ob.delete()
        context = {'info': '删除成功'}
        return render(request, 'myapp/doupload.html', context)
    except:
        context = {'info': '没有找到要删除的信息'}
        return render(request, 'myapp/doupload.html', context)
