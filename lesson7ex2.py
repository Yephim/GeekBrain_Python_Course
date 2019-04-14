
"""

2. Дан список, заполненный произвольными числами. Получить список из элементов исходного,
 удовлетворяющих следующим условиям:
1. Элемент кратен 3,
2. Элемент положительный,
3. Элемент не кратен 4.
    Примечание: Список с целыми числами создайте вручную в начале файла. Не забудьте включить туда отрицательные числа.
  10-20 чисел в списке вполне достаточно.
"""
import random

rstate= (3, (2147483648, 2675229758, 419452534, 2835351715, 3858745955, 463515009, 1325222269, 3112179823, 3770226173, 2433436854, 1440553429, 3282366495, 3912041750, 2439675825, 3937997632, 1734984581, 44602889, 3433812044, 451992443, 1511159448, 948202594, 84436112, 2265749624, 2629216798, 410025815, 2159672910, 3042700031, 474133435, 4043184582, 585056745, 22352268, 2706394413, 3031067403, 3786301795, 3592324332, 1976284682, 2659164755, 3790214149, 3325643790, 2401373660, 3075819313, 2940382410, 3837210318, 1360457346, 3300157164, 2814006661, 1092556815, 1209555031, 1718331230, 81797484, 3074878124, 2795836473, 677330869, 3597622870, 116817862, 215493207, 298162005, 1763492404, 2624898941, 3838473762, 3162049070, 4153031656, 597798936, 3104976695, 1074100612, 3531151150, 1688915362, 3051853508, 1053484096, 2900243704, 2029473316, 3924121117, 373416193, 1907659436, 206802759, 4187272883, 2966350021, 948029008, 2093340760, 1956782421, 2897515611, 634928075, 2562015414, 991289896, 1261422436, 4172083890, 2908764762, 50988901, 78467526, 583935735, 711303001, 2885855658, 2573256992, 1573999563, 347584865, 2795598670, 1582582254, 1002178790, 2747106686, 1693307062, 3286478874, 468758652, 221857334, 2537735812, 1626196849, 2767793909, 2669203676, 3962852332, 1350770109, 1244405155, 3614153545, 4180148224, 4178230068, 3273509859, 2675468233, 3601174263, 2789228318, 3520706830, 592479178, 322406494, 301270830, 951507441, 667633335, 37940933, 1059212424, 1044984973, 55862347, 3566943516, 841881864, 1465727866, 3585199302, 3385686326, 1469843325, 4178764695, 1434934215, 3148341023, 2335265063, 1261908006, 2937391421, 131377774, 3663584220, 2295023422, 4280295922, 156740247, 1492207858, 4129423794, 3425365581, 1241995637, 2356563736, 520758059, 3250153441, 3248011120, 3527946108, 540266474, 3430084494, 528621534, 1278253557, 1644281665, 3241959307, 3378848113, 3062801373, 3930778694, 2558958885, 3936999854, 888451241, 406462371, 2138079099, 1032625402, 2961262645, 2401736179, 1214328740, 3959613773, 2270282058, 3260135763, 3974659768, 4235111462, 410395258, 2661333759, 2729151229, 3380135183, 3850585934, 2706805870, 3116980917, 2065066705, 4145134861, 3064076909, 1376751292, 2656677208, 278953153, 930577860, 3881252888, 3144796482, 516997550, 4062839428, 169784453, 1077924772, 2442365399, 2429774706, 1918242273, 329719236, 1892427731, 3900165009, 526966623, 3580036422, 1453545640, 3181195784, 2996506479, 461847667, 3189949349, 277161553, 2828708892, 3960691308, 3461020547, 4062291699, 514174202, 3613814101, 3579322287, 885778810, 2210453360, 2287804147, 3430760623, 2704734625, 212315842, 2933634038, 410205672, 3583164487, 1759119807, 3530357101, 4003855725, 1557856820, 416059582, 3564844197, 1534626475, 1405592141, 422670240, 307072553, 1562320557, 1933255906, 4075138456, 2587929962, 1012305726, 1263168609, 1200549057, 2377649074, 3834909335, 3740296368, 3639290069, 584612231, 4287495001, 2871823193, 2729353933, 1672021025, 2891047586, 2785715670, 4269764647, 208554475, 206673598, 2358765548, 4261669845, 3032146295, 2107929951, 404455453, 1823207839, 2792941512, 3254579151, 2338527774, 2659994587, 2640971139, 2540290542, 4198093344, 3156251202, 2897708026, 3920905787, 1574501620, 1690161629, 1379865710, 2608854179, 3972235382, 1933677252, 250664203, 292149282, 1481252455, 856195149, 4277329614, 3269142958, 4102843631, 200748706, 4072213992, 1926966324, 3386805437, 1138252317, 3204355253, 3412345873, 1576081947, 4125382470, 612097417, 2891767832, 3707872093, 2805982677, 1292467432, 1686082459, 524783928, 100843449, 3477415373, 2912947136, 2191491670, 923340429, 24448530, 1533928440, 112704375, 2107493117, 4266660356, 1122041898, 1879574035, 940917753, 4194895260, 247151914, 2451540036, 4161449542, 2490766043, 2391841957, 263663440, 1032573815, 3857230665, 2388699645, 17926856, 2556948353, 1249826883, 3414356842, 3581362993, 865091424, 435122731, 3745855998, 391789845, 456219482, 1636657446, 3675042864, 3395099576, 363432879, 1523689758, 2163310806, 3618141631, 1171599363, 2786758630, 3796226289, 1065245486, 1762703044, 925913987, 1043089378, 258743539, 4220267593, 3207234511, 1284744394, 1017498359, 4176475711, 2099591889, 3430285361, 4014469493, 3923378002, 3788499492, 401624820, 2453968174, 1426603344, 3796162217, 3988036779, 1620428101, 3836956592, 4126049473, 721889840, 3657443336, 2523960236, 424476294, 1240939287, 3618073015, 1098274998, 3459902191, 1426821844, 1381470311, 1831117102, 3564956951, 1817575008, 4061885328, 1468741031, 22048019, 3141320738, 119955587, 2380020751, 1677764640, 264101571, 3784995739, 2588916087, 921830623, 400596611, 1030973166, 3900918406, 129513203, 1974858027, 3675282144, 2512666804, 3501695445, 683471396, 410558084, 4233858768, 31017400, 3649722050, 1645109981, 617178149, 4075174214, 3792289901, 218314168, 3213687732, 705793247, 2406660053, 4063947356, 2631913935, 2217743599, 1132872651, 2266433934, 2018333466, 1582303168, 984267114, 1312316357, 2644498961, 2088059773, 3880969685, 2436830117, 3137713548, 1141940081, 1590750805, 71265357, 1400898106, 1388296146, 3901811222, 1882551955, 640618661, 2614240323, 3830077103, 2070923792, 2334163046, 3710522940, 2966731011, 3444757038, 488391798, 415357227, 3600564489, 2293043217, 423860201, 3087629406, 1114745445, 2486203725, 3766744907, 1309373550, 2838299638, 130471352, 504464365, 247401239, 163884022, 3297665612, 2207658274, 2382846729, 2894302935, 2923130643, 8707663, 3873482392, 3390753021, 2503942483, 2680939807, 4158447687, 3848571410, 3870018350, 329498051, 4047341780, 1348792160, 1298563313, 1520063538, 2021347807, 2301864986, 3586361871, 15846200, 2765032706, 1488626123, 3207264607, 2290348253, 1109603619, 3262337730, 3913653891, 2299943901, 770374790, 2206458654, 3194334355, 1928402758, 1060602506, 2683323338, 1867211573, 1835521853, 2456026909, 3976137985, 1679236533, 780815613, 2037437352, 567120063, 2394983121, 2414126541, 618466205, 1588806750, 3081059538, 2473937989, 1493668963, 2103829382, 931961440, 1433159124, 1049091571, 2892768524, 70111248, 1558746927, 3932474018, 1217944169, 3774640644, 4275026999, 1317426787, 3945224964, 105001273, 3773878232, 2471926440, 4211239098, 101548578, 1985585787, 2916171040, 3624601440, 1247310408, 3245552137, 2055496017, 3212743793, 1527865183, 1299016230, 630485459, 1747295950, 260418690, 2752547181, 1784241819, 2821073845, 3165615640, 1156316388, 3146666462, 4075338726, 3721991251, 3926093106, 831582234, 1444909753, 2779260776, 25877642, 82365327, 512934546, 2587578850, 1934541451, 716776111, 436670654, 3816838834, 2840698078, 2251236540, 176666511, 3938654332, 2885600643, 2827451995, 3984422414, 882819422, 130160832, 3733940133, 813101920, 430603117, 1335273449, 1116803741, 1303518857, 3524992862, 3815971782, 1923958184, 1804510078, 3543311206, 1700074538, 2106367401, 1334952458, 3427571963, 165871953, 2394521799, 2970624735, 2932104726, 1584743886, 2510924404, 1848246841, 4202133620, 4253227041, 812034789, 173318589, 32295021, 2577204261, 3684403222, 2624960731, 1752453451, 1178099828, 2550176589, 3547092180, 58724404, 1539376164, 1895073918, 2911257972, 3614526118, 2582997748, 4131762603, 3238216203, 1625010701, 4114903844, 1188984049, 3852331389, 3082705134, 1291502784, 1221655433, 3663969252, 2735969032, 660885112, 327157360, 4002009999, 1459846131, 665037143, 2929397819, 624), None)
random.setstate(rstate)

list_1 = [random.randint(-100,100) for i in range(20)]
print(list_1)
list_2 = [num for num in list_1 if num % 3 == 0]
print(list_2)
list_3 = [num for num in list_1 if num > 0]
print(list_3)
list_4 = [num for num in list_1 if num % 4 != 0]
print(list_4)
