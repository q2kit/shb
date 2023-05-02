from django.shortcuts import render
from django.http import JsonResponse, FileResponse
from django.views.decorators.csrf import csrf_exempt

import pandas as pd

from api.models import Sale, Contact


def convert(x):
    try:
        return int(x)
    except:
        if x == x: # check NaN
            return str(x)
        else:
            return None


def search(request):
    q = request.GET.get('q')
    obj = Sale.objects.filter(sdt=q).first()
    if not obj:
        return JsonResponse({
            "success": False,
        })
    response = JsonResponse({
        "success": True,
        "hang": obj.hang,
        "ten": obj.ten,
        "ma_gt": obj.ma_gt,
        "sdt": obj.sdt,
        "sl": obj.sl,
        "ky_gt": obj.ky_gt,
    })
    response["Access-Control-Allow-Origin"] = "*"
    return response


@csrf_exempt
def import_excel(request):
    if request.method == "GET":
        return render(request, 'import.html')
    else:
        file = request.FILES.get('file')
        df = pd.read_excel(file)
        print("df", df)
        lst = []
        for obj in list(df.to_dict('records')):
            obj = list(map(convert, obj.values()))

            lst.append(Sale(
                hang=obj[0],
                ten=obj[1],
                ma_gt=obj[2],
                sdt=obj[3],
                sl=obj[4],
                ky_gt=obj[5],
            ))

        Sale.objects.bulk_create(lst)

        return JsonResponse({
            "success": True,
            "message": "Import thành công %s dòng." % len(lst)
        })
    

@csrf_exempt
def contact(request):
    name = request.POST.get('name', '')
    phone = request.POST.get('phone', '')
    email = request.POST.get('email', '')
    address = request.POST.get('address', '')

    if name or phone or email or address:
        Contact.objects.create(
            name=name,
            phone=phone,
            email=email,
            address=address,
        )
    
    response = JsonResponse({
        "success": True,
        "message": "Cảm ơn bạn đã gửi phản hồi."
    })

    response["Access-Control-Allow-Origin"] = "*"
    return response


def export_excel(request):
    lst = list(Contact.objects.all().values())
    if not lst:
        return JsonResponse({
            "success": False,
            "message": "Không có dữ liệu."
        })
    df = pd.DataFrame(lst)
    df = df.drop(columns=['id'])
    df = df.rename(columns={
        'name': 'Họ và tên',
        'phone': 'Số điện thoại',
        'email': 'Email',
        'address': 'Địa chỉ',
    })
    df.to_excel('contact.xlsx', index=False)
    
    return FileResponse(open('contact.xlsx', 'rb'))