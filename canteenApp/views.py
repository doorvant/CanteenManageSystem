from locale import atoi
from django.contrib import messages
from django.shortcuts import render, redirect
from canteenApp import models
from canteenApp.interface import *
# Create your views here.


# 初始化网页
def init(request):
    if request.method == "POST":
        if "user" in request.POST:
            # 登录功能实现
            username = request.POST.get("username")
            password = request.POST.get("password")
            count = models.Userinfo.objects.filter(username=username, userpw=password).count()
            if count == 1:
                # 登录成功后创建订单号
                order_id = models.Orderlist.objects.all().count() + 1
                user_obj = models.Userinfo.objects.get(username=username)
                models.Orderlist.objects.create(orderid=order_id,
                                                userphone=user_obj,
                                                ordernum=0,
                                                ordersum=0,
                                                ordertext="暂无备注")
                return redirect("/order_food1")
            else:
                messages.error(request, '用户名或密码不正确')
        else:
            username = request.POST.get("username")
            password = request.POST.get("password")
            count = models.Root.objects.filter(rootid=username, rootpw=password).count()
            if count == 1:
                return redirect("/food_list")
            else:
                messages.error(request, '用户名或密码不正确')
    return render(request, "login.html")


# 点菜
def order1(request):
    order_id = models.Orderlist.objects.all().count()
    if request.method == "POST":
        if "id1" in request.POST:
            add_to_list(1, order_id)
        if "id3" in request.POST:
            add_to_list(3, order_id)
        if "id6" in request.POST:
            add_to_list(6, order_id)
        if "id8" in request.POST:
            add_to_list(8, order_id)
        if "id9" in request.POST:
            add_to_list(9, order_id)
        if "ordered" in request.POST:
            order_food_list = models.Vieworderfood.objects.filter(orderid=order_id)
            order_good_list = models.Viewordergood.objects.filter(orderid=order_id)
            order_obj = models.Orderlist.objects.get(orderid=order_id)
            return render(request, "list.html", {"order_food_list": order_food_list,
                                                 "order_good_list": order_good_list,
                                                 "order_obj": order_obj})
        if "c2" in request.POST:
            return redirect('/order_food2')
        if "market" in request.POST:
            return redirect('/order_food3')
        if "addfood" in request.POST:
            return redirect('/order_food1')
        if "pay" in request.POST:
            return redirect('/payed')
        if "exit" in request.POST:
            return redirect('http://127.0.0.1:8000')
        if "score" in request.POST:
            return redirect('/score')
    return render(request, "order_1.html")


def order2(request):
    order_id = models.Orderlist.objects.all().count()
    if request.method == "POST":
        if "id2" in request.POST:
            add_to_list(2, order_id)
        if "id4" in request.POST:
            add_to_list(4, order_id)
        if "id5" in request.POST:
            add_to_list(5, order_id)
        if "id7" in request.POST:
            add_to_list(7, order_id)
        if "ordered" in request.POST:
            order_food_list = models.Vieworderfood.objects.filter(orderid=order_id)
            order_good_list = models.Viewordergood.objects.filter(orderid=order_id)
            order_obj = models.Orderlist.objects.get(orderid=order_id)
            return render(request, "list.html", {"order_food_list": order_food_list,
                                                 "order_good_list": order_good_list,
                                                 "order_obj": order_obj})
        if "c1" in request.POST:
            return redirect('/order_food1')
        if "market" in request.POST:
            return redirect('/order_food3')
        if "addfood" in request.POST:
            return redirect('/order_food1')
        if "pay" in request.POST:
            return redirect('/payed')
        if "exit" in request.POST:
            return redirect('http://127.0.0.1:8000')
        if "score" in request.POST:
            return redirect('/score')
    return render(request, "order_2.html")


def order3(request):
    order_id = models.Orderlist.objects.all().count()
    if request.method == "POST":
        if "id101" in request.POST:
            add_to_list2(101, order_id)
        if "id102" in request.POST:
            add_to_list2(102, order_id)
        if "id103" in request.POST:
            add_to_list2(103, order_id)
        if "ordered" in request.POST:
            order_food_list = models.Vieworderfood.objects.filter(orderid=order_id)
            order_good_list = models.Viewordergood.objects.filter(orderid=order_id)
            order_obj = models.Orderlist.objects.get(orderid=order_id)
            return render(request, "list.html", {"order_food_list": order_food_list,
                                                 "order_good_list": order_good_list,
                                                 "order_obj": order_obj})
        if "c1" in request.POST:
            return redirect('/order_food1')
        if "c2" in request.POST:
            return redirect('/order_food2')
        if "addfood" in request.POST:
            return redirect('/order_food1')
        if "pay" in request.POST:
            return redirect('/payed')
        if "exit" in request.POST:
            return redirect('http://127.0.0.1:8000')
        if "score" in request.POST:
            return redirect('/score')
    return render(request, "order_3.html")


# 已点
def order_list(request):
    return render(request, "list.html")


def payed(request):
    if request.method == "POST":
        if "exit" in request.POST:
            return redirect('http://127.0.0.1:8000')
        if "score" in request.POST:
            return redirect('/score')
    return render(request, "payed.html")


# 管理员添加菜品
def add_food(request):
    if request.method == "POST":
        if "manage" in request.POST:
            return redirect("/food_list")
        if "exit" in request.POST:
            return redirect('http://127.0.0.1:8000')
        if "money" in request.POST:
            return redirect("/money")
        # 获取输入内容
        food_name = request.POST.get("foodName")
        food_price = request.POST.get("foodPrice")
        food_cate = request.POST.get("foodCate")
        food_id = request.POST.get("foodId")
        food_info = request.POST.get("foodInfo")
        wid = request.POST.get("wId")
        # 写入数据库
        food_wid = models.Windows.objects.get(wid=wid)
        models.Food.objects.create(foodname=food_name,
                                   foodprice=food_price,
                                   foodcate=food_cate,
                                   foodid=food_id,
                                   wid=food_wid,
                                   foodsold=0,
                                   foodinfo=food_info)
        return redirect("/food_list")
    return render(request, "addFood.html")


def edit_food(request):
    if request.method == 'POST':
        if "add" in request.POST:
            return redirect("/add_food")
        if "exit" in request.POST:
            return redirect('http://127.0.0.1:8000')
        if "money" in request.POST:
            return redirect("/money")
        if "manage" in request.POST:
            return redirect("/food_list")
        # 获取数据
        food_name = request.POST.get("foodName")
        food_price = request.POST.get("foodPrice")
        food_cate = request.POST.get("foodCate")
        food_id = request.POST.get("foodId")
        food_info = request.POST.get("foodInfo")
        wid = atoi(request.POST.get("wId")[16])
        # 查询对象
        food_obj = models.Food.objects.get(foodid=food_id)
        food_wid = models.Windows.objects.get(wid=wid)
        # 修改内容
        food_obj.foodname = food_name
        food_obj.foodprice = food_price
        food_obj.foodcate = food_cate
        food_obj.foodinfo = food_info
        food_obj.wid = food_wid
        food_obj.save()
        return redirect("/food_list")
    else:
        # 获取id
        foodid = request.GET.get('foodid')
        food_obj = models.Food.objects.get(foodid=foodid)
        food_obj_list = models.Food.objects.all()
        return render(request, "editFood.html",
                      {"food_obj": food_obj, "food_obj_list": food_obj_list})


# 删除菜品
def delete_food(request):
    foodid = request.GET.get('foodid')
    models.Food.objects.filter(foodid=foodid).delete()
    return redirect("/food_list")


def delete_order(request):
    foodId = request.GET.get('foodid')
    print(foodId)
    orderid = request.GET.get('orderid')
    order_id = atoi(orderid[18] + orderid[19])
    if request.method == "POST":
        if "addfood" in request.POST:
            return redirect('/order_food1')
        if "pay" in request.POST:
            return redirect('/payed')
        if "exit" in request.POST:
            return redirect('http://127.0.0.1:8000')
    if len(foodId) != 17:
        food_id = atoi(foodId[13])
        food_obj = models.Including.objects.get(foodid=food_id, orderid=order_id)
        food = models.Food.objects.get(foodid=food_id)
        order_obj = models.Orderlist.objects.get(orderid=order_id)
        order_obj.ordersum -= food.foodprice * food_obj.foodnum
        models.Including.objects.filter(foodid=food_id, orderid=order_id).delete()
        order_obj.save()
        order_food_list = models.Vieworderfood.objects.filter(orderid=order_id)
        order_good_list = models.Viewordergood.objects.filter(orderid=order_id)
        order_obj = models.Orderlist.objects.get(orderid=order_id)
        return render(request, "list.html", {"order_food_list": order_food_list,
                                             "order_good_list": order_good_list,
                                             "order_obj": order_obj})
    else:
        good_id = atoi(foodId[13] + foodId[14] + foodId[15])
        good_obj = models.Adding.objects.get(goodid=good_id, orderid=order_id)
        good = models.Good.objects.get(goodid=good_id)
        order_obj = models.Orderlist.objects.get(orderid=order_id)
        order_obj.ordersum -= good.goodprice * good_obj.goodnum
        models.Adding.objects.filter(goodid=good_id, orderid=order_id).delete()
        order_obj.save()
        order_food_list = models.Vieworderfood.objects.filter(orderid=order_id)
        order_good_list = models.Viewordergood.objects.filter(orderid=order_id)
        order_obj = models.Orderlist.objects.get(orderid=order_id)
        return render(request, "list.html", {"order_food_list": order_food_list,
                                             "order_good_list": order_good_list,
                                             "order_obj": order_obj})


# 菜品列表
def food_list(request):
    # 查询
    if request.method == "POST":
        if "manage" in request.POST:
            food_list = models.Food.objects.all()
            return render(request, "foodList.html", {"food_obj_list": food_list})
        if "add" in request.POST:
            return redirect("/add_food")
        if "exit" in request.POST:
            return redirect('http://127.0.0.1:8000')
        if "money" in request.POST:
            return redirect("/money")
        if "search" in request.POST:
            foodcate = request.POST.get('foodcate')
            food_list = models.Food.objects.filter(foodcate=foodcate)
            return render(request, "foodList.html", {"food_obj_list": food_list})
    food_list = models.Food.objects.all()
    return render(request, "foodList.html", {"food_obj_list": food_list})


# 收入查看
def money(request):
    if "add" in request.POST:
        return redirect("/add_food")
    if "exit" in request.POST:
        return redirect('http://127.0.0.1:8000')
    if "manage" in request.POST:
        return redirect("/food_list")
    goodMoney_list = models.Viewgoodsold.objects.all()
    foodMoney_list = models.Viewfoodsold.objects.all()
    return render(request, "money.html", {"goodMoney_list": goodMoney_list, "foodMoney_list": foodMoney_list})


def edit_score(request):
    if request.method == 'POST':
        if "exit" in request.POST:
            return redirect("http://127.0.0.1:8000")
        if "score" in request.POST:
            return redirect("/score")
        if "menu" in request.POST:
            return redirect("/order_food1")
        # 获取数据
        scores = request.POST.get("score")
        wid = request.POST.get("wId")
        # 查询对象
        score_obj = models.Scoring.objects.get(userphone=12345654321, wid=wid)
        # 修改内容
        score_obj.score = scores
        score_obj.save()
        return redirect("/score")
    else:
        # 获取id
        wid = request.GET.get('wid')
        w_obj = models.Scoring.objects.get(wid=wid)
        w_obj_list = models.Scoring.objects.all()
        return render(request, "edit_score.html",
                      {"w_obj": w_obj, "w_obj_list": w_obj_list})


def score(request):
    if request.method == "POST":
        if "exit" in request.POST:
            return redirect('http://127.0.0.1:8000')
        if "menu" in request.POST:
            return redirect('/order_food1')
    score_list = models.Viewscore.objects.all()
    return render(request, "score.html", {"score_list": score_list})
