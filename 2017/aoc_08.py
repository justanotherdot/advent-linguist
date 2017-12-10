from collections import defaultdict
from pprint import pprint

s = """b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10"""

s = """av inc 167 if f > -9
av inc 640 if uea == 0
fk dec -960 if tn > -9
tn dec 438 if fk == 960
uc dec -907 if av >= 800
pr dec 176 if s < 4
njb dec 861 if l <= 3
njb dec 964 if mr >= -2
l dec 360 if p == 0
mr inc 372 if fk >= 958
njb dec 612 if s > -8
dou inc -672 if dou < 1
f inc 747 if njb <= -2447
pr dec -247 if d == 0
me dec 928 if p == 0
e dec -568 if f != 0
fk dec 680 if me != -937
e inc -786 if rj >= -5
r inc -66 if ku != 10
k dec 422 if av > 800
me inc 344 if mr == 372
fk dec 479 if eva != -10
p inc 908 if mr >= 370
d inc -29 if ntq == 0
mr dec -531 if njb >= -2427
eva dec -57 if f <= 2
eva dec 515 if uea != 3
fk dec 540 if k > -427
mr dec -144 if me < -580
k dec -484 if njb >= -2437
tn dec 534 if s < 8
fk inc 91 if y < 1
e dec -34 if e > -792
y inc -151 if uea != 0
me inc 259 if eva != -456
fk inc 226 if tn >= -980
p dec 616 if rj == 0
dou dec 249 if eva > -450
k inc 204 if e != -760
ntq dec 474 if njb < -2434
njb inc 395 if ntq < -473
mr dec 223 if uea == 0
pr inc -642 if ntq != -474
f inc 438 if mr != 303
ku dec 570 if ku <= 5
uc dec -560 if p <= 298
mr inc 240 if s == 0
me inc 908 if p < 297
pr inc -323 if pr >= 65
me dec -365 if njb != -2050
rj inc 344 if uc == 1467
d dec -652 if uc > 1471
me dec -300 if uc <= 1463
r inc 130 if r == -72
k inc -594 if ntq != -483
l inc 584 if s >= -1
s dec 129 if njb > -2045
d inc 698 if njb >= -2042
p inc -284 if njb == -2042
me inc 375 if d <= 662
rj dec 132 if e > -748
mr dec -435 if k < -327
k dec -680 if p > 1
y dec 560 if dou == -672
fk inc 293 if k >= 351
uea inc 718 if r > -74
fk inc 802 if ntq > -481
y dec 834 if ntq > -479
r dec 659 if l < 221
p inc -537 if rj == 344
dou dec -307 if fk == 673
av inc 446 if l != 219
p dec 527 if y >= -1400
k inc -538 if rj != 354
uea dec -586 if tn != -972
ku inc 16 if fk >= 668
pr inc -791 if me <= 951
s inc 610 if uc == 1467
mr dec -642 if njb <= -2037
uea dec -866 if ntq < -468
av inc -627 if e < -744
ntq inc -779 if r != -75
njb inc -779 if rj >= 337
pr inc -886 if k >= -185
mr inc -145 if njb == -2821
uea inc 508 if mr <= 1461
uea dec 707 if d <= 669
eva inc 92 if f == 438
dou dec -52 if me >= 948
uea inc -267 if fk <= 675
y inc 314 if l >= 218
y dec 469 if rj > 339
l inc -796 if e == -752
e inc 285 if uea < 613
fk dec 283 if d == 669
e inc -329 if e >= -461
f inc 524 if ntq == -1253
me dec 751 if uc >= 1465
fk dec 85 if k >= -183
pr dec -593 if uc <= 1474
k dec -495 if uc < 1477
p dec 470 if tn != -973
av inc -579 if ku < -544
ku inc 587 if k != 313
ku inc -876 if eva > -373
uea inc 432 if ntq == -1253
eva dec 740 if pr != -455
me inc -718 if s <= 487
me dec 643 if tn <= -966
e dec -995 if tn < -968
ku inc -71 if av < 56
l inc 184 if s > 477
k dec 633 if r <= -66
dou dec -335 if y <= -1542
av inc 974 if eva < -1101
r dec 140 if ku > -923
r dec -205 if njb != -2820
eva inc -52 if e >= 526
eva inc -620 if ntq != -1253
p dec 700 if uea >= 1038
rj dec 589 if s == 481
mr inc 270 if ntq != -1250
dou inc -576 if fk == 390
e inc -684 if y != -1539
njb dec 867 if k <= -315
mr inc -767 if rj >= -254
f inc -207 if l <= -387
ntq inc -140 if r != -3
me inc 185 if d > 659
s inc -689 if uc >= 1460
ku inc 681 if ntq < -1384
fk dec 394 if ku == -233
ku dec 988 if k <= -320
pr inc -256 if pr == -450
me inc -57 if r < -10
me inc 117 if fk <= -12
p inc 312 if dou > -559
e dec -575 if eva != -1158
d inc 107 if l >= -392
tn inc 279 if mr > 964
d inc -78 if uc >= 1461
mr dec 273 if pr <= -711
dou inc -156 if pr > -703
rj inc 192 if pr >= -714
p dec 881 if d != 691
eva dec -870 if mr >= 963
av inc 991 if l <= -387
e dec -665 if me > -982
uea dec 916 if uc == 1467
f dec 893 if av >= 2011
e inc -109 if njb < -3689
tn inc -489 if eva > -280
rj inc 143 if njb < -3680
rj inc -5 if me == -978
e inc -567 if k > -334
tn dec -626 if av < 2020
r inc 989 if e == -58
p dec 709 if fk >= -7
k dec 459 if uea > 126
e inc -311 if pr >= -708
r inc 235 if njb < -3684
y dec 788 if p < -3496
s dec -649 if me >= -983
pr dec -319 if ntq < -1387
uea dec -399 if me != -981
uc dec -33 if f <= -136
e inc -802 if uc == 1504
ku dec -808 if d != 689
k inc -701 if uea != 530
me inc -695 if fk == -4
uc dec -84 if y != -2346
me dec 404 if tn <= -60
fk inc 316 if e == -361
f dec 72 if k < -1017
p inc 1000 if uc <= 1590
njb inc -497 if dou != -553
l inc -75 if l < -380
av dec -826 if r > 1214
ntq dec -12 if ku == -420
pr inc -157 if e > -373
p inc 822 if pr != -541
tn dec -718 if eva <= -288
y dec -530 if tn <= 659
tn inc 33 if p < -1689
e inc 411 if e > -371
mr dec 477 if me <= -2074
rj inc 576 if k > -1034
dou dec 965 if f <= -205
av dec -17 if uc == 1584
uc inc -277 if l != -459
fk dec 293 if y < -1803
e dec 596 if rj == 666
y dec -125 if uea > 519
e inc -496 if uc == 1307
tn inc -145 if uea <= 526
p inc -91 if p != -1675
tn inc -408 if e != -1040
eva dec -66 if ku < -419
uc dec 98 if njb == -4185
k inc 683 if k != -1016
av dec 846 if ntq == -1394
tn inc -955 if ntq != -1399
p inc 971 if av < 2850
tn dec 755 if tn > -866
me inc -708 if mr != 491
l dec 508 if k == -342
l dec -378 if k == -349
uea dec 588 if me == -2078
tn inc -334 if njb == -4185
pr dec 42 if uc == 1211
pr inc -6 if y != -1684
l inc 702 if tn < -1943
y dec 601 if l > -269
f inc -242 if d != 704
k dec -307 if fk != -292
rj dec 284 if ku != -422
dou inc 456 if p == -1773
ntq dec 410 if tn > -1955
r inc 673 if d == 698
p inc 304 if f > -457
rj inc 432 if tn > -1948
ku inc 962 if k == -35
dou dec -228 if s > 437
fk inc -132 if rj < 818
l inc 513 if k < -26
me inc 827 if uea != -62
y dec 768 if ntq >= -1800
f inc -143 if me < -1241
fk dec 816 if pr == -550
ntq inc 447 if fk < -1242
av dec -282 if k > -34
s dec 427 if fk != -1245
p dec 998 if tn <= -1942
rj dec -786 if av <= 2845
uc dec -743 if f < -595
uc inc 206 if eva <= -284
fk inc -182 if s >= 448
uea dec -784 if mr >= 489
l inc -127 if av != 2858
e dec -29 if njb == -4185
l dec -412 if tn == -1946
uea inc 388 if y >= -1685
av inc 526 if ku < 557
rj dec -240 if me <= -1254
uea inc 990 if pr <= -553
d inc -806 if av > 3376
y dec 981 if ku == 549
s dec 282 if ku <= 550
l inc -241 if ku <= 552
uc inc -243 if uea <= 1108
uea dec 648 if dou < -827
s inc 0 if f < -592
f dec 776 if p > -2470
rj inc -700 if y > -2669
uea inc -988 if y < -2659
r dec -132 if r == 1897
uc dec -341 if me > -1253
ku dec 940 if mr <= 500
d inc -595 if mr >= 491
p dec 785 if s < 166
f dec -184 if ku > -395
d inc -208 if s != 168
fk dec -538 if av >= 3372
y inc 204 if ntq != -1362
r dec 868 if r < 1894
rj inc 182 if av < 3386
tn dec 183 if eva == -297
l inc 596 if tn > -1945
mr inc -207 if k >= -27
pr dec -857 if p == -3252
s inc -937 if eva > -294
ntq inc -984 if ntq == -1356
mr dec 713 if me > -1245
tn dec -584 if eva > -296
av inc 992 if ku == -391
av inc 94 if dou != -836
ntq inc -611 if mr < 494
eva inc 313 if e > -1025
ku dec 940 if y == -2465
e dec 15 if l <= 281
uc inc -95 if rj < 299
pr inc -574 if mr < 497
pr inc 364 if rj >= 293
mr dec 953 if s >= -787
ku dec 963 if uc >= 1665
f inc 197 if y < -2452
ntq inc -400 if p < -3242
s inc 490 if me > -1253
d dec 390 if l >= 285
d dec 965 if eva <= 29
e dec -621 if eva > 23
p inc -344 if me != -1256
y inc 903 if r >= 1895
p dec -994 if tn != -1360
tn dec 80 if f > -998
k inc -58 if rj == 296
me dec 823 if dou == -835
y inc -547 if njb > -4188
d inc -459 if d == -2266
d inc 4 if l >= 280
eva dec -975 if av >= 4460
fk inc 350 if ku > -396
rj dec 89 if rj == 286
mr inc 10 if y != -2094
rj dec -700 if tn >= -1447
p inc 151 if p != -2608
ku inc -983 if fk > -355
eva dec 106 if rj > 989
me dec 46 if tn <= -1448
s dec 476 if p == -2451
njb inc 671 if fk == -357
njb inc 687 if s == -764
r dec 470 if ntq <= -3351
fk inc 784 if rj >= 992
y inc -573 if tn == -1442
me inc -410 if ntq > -3355
dou inc 951 if av != 4458
d dec 555 if dou != 126
ntq inc 543 if fk != 434
dou inc -175 if av > 4474
uea inc 990 if ku == -391
dou inc -10 if fk == 427
pr inc -274 if r != 1434
dou dec 68 if p >= -2455
ku inc -46 if ntq != -2815
me dec -76 if rj != 994
r inc -40 if uea < 470
njb inc -446 if dou != 47
ku inc 552 if r > 1383
tn inc 520 if f == -990
f inc 975 if mr <= -452
av dec -566 if k != -89
me inc -578 if ntq < -2801
rj inc 796 if rj >= 987
uea inc -379 if ntq >= -2811
ku inc 618 if d > -3286
s dec -990 if av == 5033
njb dec 612 if rj >= 1784
av inc 92 if av != 5033
s inc -904 if mr <= -450
tn inc -214 if me > -2996
e dec -887 if ku == 733
av inc 580 if mr == -452
uc inc -967 if rj == 1792
njb inc 221 if mr != -446
f inc 670 if r <= 1389
uc inc -132 if eva >= 892
fk dec 669 if l >= 282
uc inc 76 if p > -2457
s inc 727 if rj == 1792
uea inc 381 if d > -3274
f inc 0 if me == -2986
uea dec -208 if pr != -167
uea dec -728 if l > 283
eva dec -853 if e < 480
dou inc -561 if av <= 5620
s dec -412 if s != 39
eva dec -816 if eva == 894
p dec -443 if me != -2989
d dec 104 if fk < -240
rj inc -56 if e != 489
tn inc -147 if me != -2983
av dec -308 if ntq != -2811
fk dec 440 if l > 286
rj inc 43 if me >= -2994
d dec -517 if k <= -98
tn inc -724 if mr <= -449
av dec 595 if y < -2667
rj inc -524 if s != 466
uc inc 815 if l < 295
f inc 75 if fk >= -690
mr dec 898 if ku > 738
d dec 598 if k > -92
tn dec 844 if fk == -680
pr inc 885 if me == -2986
uc dec -457 if l < 290
fk dec 825 if eva > 1716
uea inc 439 if pr > 704
k inc -107 if k <= -89
fk dec -711 if uc <= 1916
eva dec -412 if d == -3380
njb inc 303 if mr == -452
mr dec -374 if y >= -2669
p inc 341 if njb == -3355
f dec 538 if tn >= -2007
r dec 672 if fk < 31
me dec 442 if fk > 20
d dec -768 if p < -2015
rj inc 0 if s != 464
me inc 67 if y <= -2670
uea dec 889 if f == 192
eva inc 226 if s >= 461
p dec -646 if fk <= 20
mr inc 153 if njb > -3366
rj inc 240 if njb != -3365
f dec -61 if fk < 38
pr dec 750 if pr >= 707
pr inc 656 if s > 458
uc inc 366 if l > 284
p dec -574 if uc < 2279
d dec -88 if ku <= 739
l inc 466 if rj == 1495
d dec -335 if ntq < -2806
dou inc 708 if uea > 567
e inc 702 if av >= 5323
k dec 962 if s > 467
d inc 665 if uc < 2284
fk inc 849 if d < -2284
y inc 761 if me < -3354
njb dec 30 if ntq != -2808
e dec 67 if f >= 248
mr inc -690 if mr <= -308
e dec -40 if k == -200
pr inc -323 if av > 5320
pr dec -432 if y <= -1915
f inc -832 if tn >= -2006
njb dec -555 if pr == 730
ntq dec 525 if rj <= 1499
f inc -147 if mr < -290
d inc -322 if njb > -3371
mr inc 476 if s < 468
f dec 125 if eva < 2349
me dec -964 if njb < -3369
ntq inc 514 if dou >= 181
s inc -491 if uc != 2276
r dec -966 if fk != 878
e inc -971 if f < -15
uea dec -238 if uc < 2271
d dec 193 if p == -1434
e inc -98 if tn > -2011
av inc -362 if d > -2812
av dec 230 if r >= 709
e dec 858 if d >= -2816
av dec -370 if f != -12
mr dec 820 if njb != -3370
uc inc -376 if k >= -203
s dec -3 if p <= -1431
me dec -223 if uea >= 569
fk dec 266 if uea > 563
pr inc 18 if njb > -3368
ku inc 143 if fk > 602
s inc 917 if fk > 620
f inc -128 if r >= 709
dou dec -732 if f > -153
uc dec -457 if njb != -3365
y dec -318 if f == -147
me dec 366 if f > -143
r dec -203 if uea >= 577
rj dec -430 if uea != 572
tn inc 623 if mr >= -644
mr dec 85 if njb > -3367
dou inc 371 if njb != -3366
rj dec -329 if p > -1444
tn dec 659 if r >= 714
l dec 336 if e != -765
p dec 233 if tn > -2046
ntq inc 432 if s >= 456
l inc -743 if fk != 607
pr inc 749 if l < 12
fk dec 754 if pr == 1482
eva inc 125 if tn == -2043
f inc -693 if tn <= -2053
e inc -812 if r != 714
e inc -857 if njb == -3361
d inc -182 if tn == -2043
njb inc 666 if fk <= 615
s inc -187 if k != -202
mr inc 933 if k != -204
eva inc 221 if f != -140
l dec -146 if ntq > -2378
k dec -504 if f == -147
y inc 148 if me == -3138
tn dec -800 if eva < 2700
rj dec -458 if k >= 299
y dec 290 if tn != -1237
eva dec 188 if r != 714
p inc -406 if r <= 719
dou dec -730 if p < -2070
pr dec -422 if rj <= 2721
fk inc -73 if rj > 2706
av dec -196 if f < -144
s inc 670 if uea <= 573
rj dec -41 if av >= 5298
dou inc -463 if k < 304
l dec -248 if av <= 5300
r dec -897 if av != 5304
ku inc 678 if k >= 303
dou inc 773 if p == -2073
tn dec 399 if me < -3129
s dec 157 if p <= -2066
uea dec 624 if rj > 2744
k dec 451 if av < 5304
p dec -475 if uea == -54
me inc 481 if uc >= 2356
njb dec 194 if k > -153
r inc 517 if p <= -1593
eva inc -869 if fk > 545
njb inc 270 if y == -1739
y dec 468 if pr >= 1909
e dec 713 if eva != 2694
s inc 973 if ku != 1550
uea dec -325 if r > 2118
mr dec 812 if l != 269
f inc 146 if y == -2207
njb inc -476 if uea <= 278
eva inc -358 if y > -2210
ntq dec -904 if l > 257
me dec -499 if ku == 1554
me dec 38 if uc > 2350
ku inc -255 if rj != 2746
eva inc 389 if pr >= 1913
ku dec 76 if e <= -1620
l dec -254 if ku <= 1231
tn dec 880 if ku == 1229
p dec 516 if fk <= 541
d inc -423 if rj >= 2760
p inc 145 if uea != 271
pr inc 755 if fk > 538
av dec -945 if p > -2115
y inc 974 if njb == -3100
r inc -688 if tn > -1633
uea dec 54 if d >= -2996
dou inc -876 if fk >= 537
uea dec 379 if mr == -607
rj inc 760 if f != 3
av inc 124 if pr != 2677
mr dec -565 if eva > 2333
k dec 382 if ku <= 1225
s inc -856 if eva <= 2336
k dec 357 if d != -2980
fk dec -926 if y > -2208
f inc -198 if r <= 2133
l dec 582 if uc <= 2361
me dec 288 if uc != 2362
me inc 757 if dou >= 1908
tn inc -697 if me == -1720
eva inc 776 if rj >= 3509
av dec 944 if s != 911
fk inc -310 if fk != 1457
l inc 91 if d < -2984
mr dec 296 if ntq == -1483
eva dec 151 if s <= 914
njb dec 122 if njb != -3095
dou inc 252 if l == 16
pr inc -473 if tn > -1652
tn dec 442 if me != -1720
fk inc -24 if y < -2202
k inc -818 if uc <= 2360
ku inc 597 if eva != 2966
ntq inc -970 if k != -1714
y dec -747 if pr >= 2188
s dec 876 if eva >= 2954
tn dec 599 if k != -1713
av dec 408 if pr != 2201
e inc 676 if me < -1726
s inc -515 if tn == -2683
s dec -626 if s == -484
l inc 745 if f <= -191
njb dec -458 if eva < 2971
njb inc 346 if s == 151
tn dec -303 if ntq == -2453
av inc 222 if ku >= 1821
r inc 810 if uc >= 2357
ntq inc -490 if s != 132
r dec -448 if rj >= 3509
eva dec 39 if me <= -1725
l dec 510 if f <= -192
mr dec -382 if f <= -198
me dec -1 if ku == 1820
eva inc 366 if s == 143
njb dec -109 if e > -955
e inc -386 if tn != -2380
pr dec 633 if rj == 3513
y inc -556 if s == 142
s inc 992 if p <= -2114
tn dec 333 if eva != 2922
tn dec -569 if k > -1709
eva inc 263 if rj != 3520
ntq dec -671 if r > 3393
fk inc -686 if e < -942
y inc 779 if pr > 1560
s dec 257 if uc < 2360
e inc 234 if pr != 1560
e inc -299 if pr <= 1560
k inc -58 if fk <= 454
tn inc 534 if uc >= 2354
e inc 404 if k > -1763
tn inc -768 if dou < 1921
tn inc 737 if eva >= 3193
ku dec -734 if tn > -2050
njb inc 956 if ntq < -2940
tn inc 476 if p != -2120
dou inc 958 if r == 3386
fk inc -491 if e <= -308
me dec -272 if l > 256
ntq inc 274 if pr >= 1556
e dec -341 if p < -2113
tn inc 983 if av < 5018
rj dec 658 if tn == -586
me dec 766 if dou != 2876
me inc -116 if y < -1230
l inc 849 if e <= 41
k inc -241 if fk <= -39
d dec 939 if me <= -2335
tn inc 361 if k >= -1998
k dec -345 if s > 868
s dec 280 if uea == -162
l dec -745 if pr > 1558
dou dec -964 if d >= -3935
s dec 189 if njb == -1572
av inc -344 if me <= -2333
e dec -453 if k < -1664
d inc 968 if mr < 54
rj inc 993 if fk < -45
d inc -686 if f >= -197
dou inc -485 if s < 411
tn inc 206 if rj == 3848
fk inc 241 if av != 4683
p dec 251 if l < 1858
dou dec -750 if e > 24
p dec 917 if uc > 2354
r dec 202 if r == 3386
e dec 896 if uea == -162
me dec -287 if me > -2331
ku dec -878 if d >= -2954
eva dec -313 if uc > 2352
ku inc -456 if av <= 4669
e inc -551 if k == -1658
r inc -328 if y > -1247
uc dec 936 if rj == 3838
r dec -204 if pr < 1559
uc inc -138 if dou >= 4101
ntq inc -575 if dou != 4095
e dec -413 if dou < 4107
dou dec -609 if s <= 416
tn dec -275 if r >= 2851
fk inc 365 if av < 4680
ntq dec 898 if fk > 551
mr dec 896 if l > 1842
fk inc -304 if rj != 3848
k dec -10 if av > 4672
tn dec -427 if k != -1641
fk inc -362 if fk != 566
rj inc 163 if l == 1851
fk inc 614 if uc < 2212
ku inc 942 if tn >= 319
s dec -341 if rj <= 4016
njb inc -443 if r < 2857
d inc 51 if ku != 3496
rj dec 266 if s <= 753
s inc 918 if ntq != -4151
mr dec -363 if s == 1667
ntq dec 52 if uea != -162
ku inc -69 if rj == 3745
uc inc -196 if r > 2863
mr dec -200 if uc < 2229
f inc 206 if rj < 3751
fk inc 771 if dou < 4721
e inc 880 if me <= -2333
rj inc -811 if av >= 4667
dou inc 447 if s < 1673
tn dec -512 if l < 1842
fk inc 535 if l > 1843
f dec -837 if tn != 330
av dec 588 if f <= 845
njb inc -988 if uea >= -164
k inc 726 if l <= 1855
l dec 297 if uea < -152
tn inc -718 if rj >= 2925
ntq dec -902 if rj <= 2942
l inc 532 if uea != -162
rj dec 277 if d > -2968
rj dec 628 if rj == 2657
mr inc 709 if d != -2962
av dec 951 if uc == 2219
d inc 107 if tn < -401
me inc 17 if e != -111
e inc -927 if mr >= 422
l dec 263 if k != -926
uc dec 883 if ntq != -3241
p dec 752 if e == -130
e inc 989 if r != 2853
me inc -673 if ku < 3433
f inc -143 if d > -2970
eva dec -905 if eva != 3498
ku dec 696 if njb != -2993
r inc 424 if mr < 426
uc inc -790 if e == 868
me inc 577 if f > 692
l inc 962 if eva < 3508
eva dec 626 if dou > 5153
pr dec 928 if rj == 2029
p dec 849 if rj >= 2021
uc dec -297 if me < -2407
uc dec -439 if p <= -4122
njb inc -800 if me != -2418
uea inc -159 if ku > 2723
k inc -71 if eva != 2867
eva dec 186 if eva != 2865
s inc 131 if njb < -3798
p inc -913 if e > 861
l dec 478 if y != -1237
njb dec 398 if d != -2967
njb inc 981 if dou <= 5159
f inc 641 if d <= -2957
y inc -277 if fk != 1495
d inc -53 if ntq <= -3238
r dec 570 if s >= 1791
s inc 779 if r >= 2708
pr dec -890 if njb == -3220
me inc 825 if ntq >= -3245
r dec -738 if tn > -404
k dec -544 if uc >= 1276
dou dec -110 if s <= 2580
pr dec -882 if njb >= -3227
mr dec 302 if k != -441
njb dec 500 if ntq <= -3237
r inc -45 if uea != -320
ku dec 956 if pr < 2404
fk inc -942 if eva < 2688
s inc 834 if uea < -320
rj inc -972 if ku > 2729
d dec -99 if k == -449
f dec -106 if ntq <= -3232
uea dec 805 if uc <= 1291
me dec 548 if f == 1448
uc inc -898 if me == -2138
y inc -403 if ntq <= -3232
s dec -959 if dou > 5260
uc dec -456 if l >= 2244
k dec -448 if mr > 111
r dec -854 if ku > 2727
pr inc -662 if pr == 2405
e inc 838 if rj >= 1063
l inc -807 if e != 869
f inc -791 if l <= 1453
ntq dec -948 if av == 3134
p inc 567 if uea > -1130
ntq inc -88 if s != 4367
njb dec -665 if ntq <= -2379
uc dec -243 if me == -2138
e inc 588 if av <= 3130
f inc 564 if s != 4368
l dec 17 if e <= 860
uc dec 358 if ntq == -2380
k dec 29 if rj == 1057
e dec 978 if e == 868
k dec -424 if pr == 1743
fk dec 502 if dou == 5268
l dec -578 if tn != -396
f inc 657 if av == 3134
eva dec 690 if uea > -1131
rj inc -639 if f < 1870
dou dec 545 if p <= -4476
y dec 170 if l >= 1447
av dec 872 if mr == 126
k inc -51 if k < 396
f dec 655 if mr >= 114
ku dec -952 if r <= 4250
e inc -220 if k < 351
me inc 254 if p <= -4484
f dec -242 if d == -2908
ku inc 595 if r == 4257
rj dec -66 if s != 4360
eva dec 944 if s > 4367
ku dec -240 if njb > -3059
f inc -693 if ku < 3560
e inc -328 if eva > 1042
l dec -773 if dou <= 4714
av dec -367 if k >= 337
pr inc -639 if av <= 3496
d inc 804 if e != -663
fk inc 217 if d > -2117
l dec -995 if d < -2117
tn inc 667 if p != -4479
r inc 620 if r > 4258
y dec -226 if p > -4483
uc dec -427 if uc == 719
dou inc -716 if p != -4475
mr inc 788 if njb >= -3059
l dec -433 if l <= 1454
l inc -139 if tn < 278
fk inc 224 if d != -2118
av dec -164 if av < 3502
pr inc 427 if rj < 1132
y dec 148 if f != 1220
d inc -514 if tn != 271
dou dec 971 if k <= 347
uea inc 140 if rj <= 1122
fk dec 243 if rj >= 1123
s inc 666 if e > -666
ntq dec -438 if eva >= 1058
rj inc -521 if njb >= -3064
fk inc 286 if e == -658
e inc -408 if p > -4484
dou dec 429 if f <= 1230
fk dec 722 if pr > 2164
rj dec 277 if k < 351
d dec 648 if fk >= -185
l inc 761 if s != 5036
l inc -417 if uc > 715
dou inc 842 if k >= 343
k inc -810 if fk > -188
p dec -962 if e != -1059
p inc -953 if av < 3674
r inc -217 if r != 4261
tn dec -726 if rj == 325
y dec -443 if k <= -469
eva dec -246 if e > -1076
fk inc 950 if dou != 3459
rj dec -905 if e >= -1057
tn inc 663 if f == 1223
mr dec 991 if eva < 1307
uc dec 45 if tn == 1660
dou dec 298 if l == 1323
r inc 324 if rj > 325
me dec 26 if pr < 2173
eva dec -672 if f < 1232
e inc -991 if rj > 316
pr inc 751 if y <= -1832
rj dec 421 if uea == -1126
me inc -169 if k < -457
y dec 335 if r <= 4031
uea dec 677 if y < -1848
y dec 56 if me != -2339
r dec -579 if av <= 3671
k dec -479 if ku == 3576
av inc -690 if ku >= 3565
r dec -574 if av == 2975
tn inc 443 if av != 2981
eva inc -180 if uea < -1116
ntq dec 726 if me < -2331
mr inc 879 if l >= 1318
f inc 838 if r > 5191
fk inc 582 if k < -461
rj dec -663 if dou >= 3145
k dec -725 if k <= -458
me inc -590 if y != -1885
av inc 206 if rj <= 557
s inc 941 if uc < 678
uc dec 951 if uea >= -1135
tn inc 770 if njb > -3057
mr inc -619 if me < -2921
eva inc 682 if av == 2975
uea dec 682 if pr <= 2927
s dec 951 if ku != 3570
rj dec 274 if pr <= 2924
ku inc 526 if uea > -1811
e inc 153 if me == -2923
fk dec -398 if r == 5189
uc dec -768 if dou >= 3153
pr dec -375 if p == -4468
rj dec -161 if pr != 3291
me dec 227 if dou == 3151
av inc -845 if ntq == -3106
p dec -595 if pr == 3296
ku dec 847 if ntq != -3096
me inc -60 if f > 2059
s dec -811 if k > 255
dou dec 588 if uc > -274
f inc -535 if eva <= 2481
s inc -759 if tn >= 2871
rj inc 375 if s <= 4139
uc inc 659 if av < 2127
f inc -240 if f == 1526
s inc 453 if d == -2755
njb inc 789 if e > -1913
fk inc 570 if njb <= -2258
njb dec 579 if rj >= 826
s inc 638 if fk < 1928
f dec 648 if fk == 1924
ntq dec -217 if ku >= 3244
ntq dec 919 if me > -3214
av inc -450 if me != -3213
k inc -306 if ntq == -3808
r inc -902 if uea <= -1803
l inc 319 if fk != 1915
mr dec -785 if av > 1679
d dec 222 if l == 1636
f dec 89 if mr >= 960
eva dec 839 if f > 540
ku dec -894 if e < -1894
d inc 463 if p < -3874
r dec 0 if fk >= 1923
ntq inc 276 if uc > -274
av dec -90 if e != -1905
eva inc 742 if eva == 1633
l inc 417 if l < 1652
r dec -223 if njb != -2835
dou dec 931 if tn < 2877
k dec -470 if ku >= 4137
me dec 332 if r != 4507
p dec -543 if uea < -1812
mr inc 339 if tn <= 2873
d inc 818 if r == 4514
ku dec -584 if l == 2059
k dec 852 if mr != 1308
s dec 406 if r < 4524
s inc 477 if pr <= 3305
pr inc -867 if dou != 1634
pr inc 155 if f < 556
d inc 444 if y == -1895
uc inc 641 if s != 4842
e inc 378 if njb != -2847
ku dec 489 if ntq < -3527
l inc -501 if me <= -3534
e inc -660 if k > -440
me dec 512 if d <= -1492
y dec 410 if y < -1886
k inc 666 if tn < 2878
k inc 744 if ku < 4244
r inc 105 if eva > 2383
mr inc 930 if uea <= -1811
p dec -907 if e >= -2195
fk inc 835 if e <= -2178
s inc 85 if p == -2966
uea inc 680 if d < -1497
tn dec 524 if l >= 1555
y dec 195 if eva < 2379
l inc -333 if tn == 2349
uea dec 478 if av <= 1766
av dec -174 if pr >= 2579
njb dec -255 if fk <= 2761
rj inc 509 if e < -2184
r dec 309 if s < 4937
uea inc 757 if s >= 4924
uea dec -456 if eva < 2378
fk inc 919 if fk < 2763
eva dec 808 if mr > 1295
e dec 475 if uea == -595
fk dec -277 if s == 4935
r inc 822 if p != -2962
k dec 440 if l != 1234
pr inc -222 if r > 5027
eva inc -437 if njb == -2590
uc inc 297 if mr <= 1308
r dec -350 if ntq != -3533
eva inc -550 if me >= -4049
y dec 587 if p < -2957
rj dec -371 if l > 1228
tn inc 353 if tn == 2356
dou dec 888 if uea >= -603
me inc 816 if pr == 2584
uc dec 473 if tn < 2351
av dec -804 if y <= -3085
d dec -824 if uc > 202
av inc -860 if s >= 4939
ntq inc 168 if uea > -596
tn dec 50 if mr > 1297
ntq dec -852 if uea <= -588
l inc -732 if r >= 5376
av dec 301 if k >= 531
r dec -396 if eva > 1120
pr inc 664 if dou <= 747
y inc -176 if av != 2446
eva dec -431 if uc == 194
tn dec -735 if p > -2975
d dec 70 if p != -2963
fk dec 100 if fk <= 3687
tn dec 99 if s >= 4923
ku inc -68 if s < 4939
ku dec -81 if l < 485
s dec -576 if njb <= -2598
e dec -439 if k >= 536
l inc -899 if ku > 4167
tn dec 639 if av < 2454
njb dec 121 if mr >= 1299
dou dec -218 if uea < -586
tn dec -161 if e == -2220
s dec -132 if rj >= 1334
r inc 700 if dou != 962
l inc -525 if fk >= 3576
y inc -102 if d == -1560
ku inc -843 if ntq == -2512
eva inc -318 if me != -3248
e inc 618 if uea > -597
p inc -598 if fk < 3587
r inc -537 if pr != 3248
d dec 858 if dou <= 970
uea dec -521 if y != -3268
pr dec 870 if ku > 3330
p dec 293 if ku == 3323
ntq dec 363 if f < 543
tn inc -855 if ku >= 3320
av inc 438 if uc == 194
rj inc -649 if pr > 3248
y inc 76 if p > -3867
e dec 303 if fk > 3569
uea dec -500 if av > 2875
rj dec 571 if d > -2426
rj inc 771 if pr != 3240
k inc -815 if f < 559
av inc -430 if s < 5071
k inc -404 if uc < 200
l inc 372 if f < 552
mr dec -133 if f != 553
s inc 949 if y >= -3196
fk dec -576 if ntq != -2514
y dec 373 if ntq == -2512
e inc -223 if ku >= 3325"""

# Because zero is always a sane default ...
registers = defaultdict(int)

def parse(line):
    ps = line.split()
    reg, op, amt = ps[0], ps[1], ps[2]
    cond = ps[4:6] + [int(ps[6])] # Skip the 'if'
    return reg, op, int(amt), cond

def eval_cond(cond):
    c_reg, c_op, c_amt = cond
    if c_op == '==':
        return registers[c_reg] == c_amt
    elif c_op == '<=':
        return registers[c_reg] <= c_amt
    elif c_op == '>=':
        return registers[c_reg] >= c_amt
    elif c_op == '!=':
        return registers[c_reg] != c_amt
    elif c_op == '<':
        return registers[c_reg] < c_amt
    elif c_op == '>':
        return registers[c_reg] > c_amt
    raise Exception('Unrecognized binary operator in command: ' + str(cond))

def eval_op(reg, op, amt):
    if op == 'inc':
        registers[reg] += amt
    elif op == 'dec':
        registers[reg] -= amt
    else:
        raise Exception('Unrecognized instruction in command: ' + op)

instructions = [parse(l) for l in s.splitlines()]
for i in instructions:
    reg, op, amt, cond = i
    if eval_cond(cond):
        eval_op(reg, op, amt)

counts = [v for k, v in registers.items()]
print(max(counts))
#  pprint(dict(registers))
