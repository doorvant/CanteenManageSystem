from canteenApp import models


def add_to_list(food_id, order_id):
    count = models.Including.objects.filter(foodid=food_id, orderid=order_id).count()
    if count:
        food_obj = models.Including.objects.get(foodid=food_id, orderid=order_id)
        food_num = food_obj.foodnum + 1
        models.Including.objects.filter(foodid=food_id, orderid=order_id).delete()
        foodId = models.Food.objects.get(foodid=food_id)
        orderId = models.Orderlist.objects.get(orderid=order_id)
        models.Including.objects.create(foodid=foodId,
                                        orderid=orderId,
                                        foodnum=food_num)

    else:
        foodId = models.Food.objects.get(foodid=food_id)
        orderId = models.Orderlist.objects.get(orderid=order_id)
        models.Including.objects.create(foodid=foodId,
                                        orderid=orderId,
                                        foodnum=1)

    orderId.ordersum += foodId.foodprice
    orderId.save()
    foodId.foodsold += 1
    foodId.save()


# 商品
def add_to_list2(good_id, order_id):
    count = models.Adding.objects.filter(goodid=good_id, orderid=order_id).count()
    if count:
        good_obj = models.Adding.objects.get(goodid=good_id, orderid=order_id)
        good_num = good_obj.goodnum + 1
        models.Adding.objects.filter(goodid=good_id, orderid=order_id).delete()
        goodId = models.Good.objects.get(goodid=good_id)
        orderId = models.Orderlist.objects.get(orderid=order_id)
        models.Adding.objects.create(goodid=goodId,
                                     orderid=orderId,
                                     goodnum=good_num)

    else:
        goodId = models.Good.objects.get(goodid=good_id)
        orderId = models.Orderlist.objects.get(orderid=order_id)
        models.Adding.objects.create(goodid=goodId,
                                     orderid=orderId,
                                     goodnum=1)

    orderId.ordersum += goodId.goodprice
    orderId.save()
    goodId.goodsold += 1
    goodId.save()
