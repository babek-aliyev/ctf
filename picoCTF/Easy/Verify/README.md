# Verify | picoCTF

## Analysis
After connecting to machine, `ls` command gives us:
```bash
ctf-player@pico-chall$ ls
checksum.txt  decrypt.sh  files
```
Here, checksum is the `sha-256` hash of the required file for us.

## Solution

When we enter `files/` directory and run `cd`, we see:
```bash
ctf-player@pico-chall$ cd files
ctf-player@pico-chall$ ls
0SgkM1fC  4gMs4KnO  9wXkj9wB  Dq8qjJ8S  JLuwL5UE  NHSLSull  RXQH6a3z  WnOWGw9n  bnahMLHf  jnOnhjk8  nxx3UCp8  rzQKjmcB  yOmzIQym
0aer7B0J  4l9DWh5d  9wzwojIO  Dr3JaQz7  JVT3ckAg  NYT2nPuv  RrQhgxZJ  WwobUdQA  cO1o2qFY  kDlGNWXG  oLZldZsM  s3TrU3bC  yTiWOwXD
0b3lt0HK  5HAN1XjT  A2SZHgJV  Dt7YKSAq  JhHZxLSp  NlN25jkt  Rrq6u3VG  WzxM1rI6  cVywfT1b  kQMlzWUP  oNfmBvds  sGOAdKy2  yb3Ro4yS
0ia8IBYb  5ntikrlo  A8X4q2Hn  E1grB9Sb  JrbVOugk  NlymPzCl  STlIDlxJ  X3z7ayAf  cZXSF7wu  kTDaKoIe  oWfAJ9wj  sKOkwRCd  ypzAaM0c
0uUAy06x  5ymaOO07  ABh1G8a0  ETctMG1o  KAS20Z1p  NrbmwP3r  Scml7yYd  X5Vhdb8H  cdZ1Ao5D  kvSPifOB  ocTCyt2G  svPh5fI5  yzW64294
17iH5ioj  6GzNwIbL  AUijzvDq  EYaK1nX6  KCoDTFB7  O3c1wd4r  Sn9XVrp6  Y4FnPPHX  chvVzQdY  kvpk6rIp  ocoustRi  t4IiokLf  z1DTGQLy
1CY2Hque  6dZQoo4O  AWnJiVoE  FYfLvi5w  Ka9uxW6u  OkXybbh3  TWbymLFA  YEOowfPv  cmhkISVH  l70cIeRx  orQXAz13  tenQzijC  z5y1jgty
1LPOMJE7  6mT8PiGl  AfnUEE9s  FcWqkSIP  Kc5sfOun  OtnjktH8  TXecNl9L  YZc8J6Vf  cvnPhBaQ  l8tB6vEL  oxeNN5uA  tkv0UoX3  zHpAJtSR
1P5dsfLj  760ZV0rr  AgQhab96  FhDH2g8j  KhnreD4t  PNNRiq3F  Tx4sSuiN  YjEaz92U  d0OYmJbG  lEjMl22a  oyrMYyZY  tmkJMhbV  zJHj9Wev
1Tst6fbt  7KoII9M8  AlhLQIGI  FkO80Me6  L9tRKUkW  PkxFO6fj  UCbhwrDb  YkYjwuGz  d0rJvLyw  lMIM4IQe  p0qmvEGQ  ud4LEsxA  zQZjRCvK
2CyEUmhf  7NBIv8bi  Au8Ov7jr  FlEOSTL0  LZgQIZ9b  PoAr7OrB  UgDsmf5L  ZEEtJ79A  d1usLAwO  lbsGcfLr  p3lVedu9  uhLtbHVL  zmrLJtwD
2MgqiK3F  7Snixk9W  B8RXEf4S  GEtA0Z9a  LnKLtxdL  PtRzswzh  V3xeKcD7  ZK4affS3  dxJZggkO  lbszmcDf  pREkecwB  vQmN5k6y  zoSxd2Nl
2R1dcXMM  7eaPaid5  BMlbLM49  GFWqPjn6  LoSmsO5t  QBtXtwy6  VBHAXd7G  ZO3IvMwL  eRcEh616  mDzgzkrP  pV3BIyJh  vQtPAQBH  zp4ssY0Q
2SLEujSI  7ylewstJ  BpkwKiOq  GhwoHV4M  MAd4OQmU  QCHOeksH  VM5DLaA2  ZQ7ftng7  eoW9IJAR  mMNEp8Zi  pVFybOWo  vmLoCSN5
2cdcb2de  7zsihLxd  C0PnAa7J  Gpbebiyr  MBaThKzn  QOHEW95s  VU1Tnx8J  ZZzeAnnA  fpXvjTBY  mg4g9Eoi  qAUGa8Jx  vt86VpBP
2eijwTPh  8N3DHyAn  C3l9qdYz  H6Mlhvd5  MLDxW9mt  QTetbcxE  VZqopSEM  aDI9kNj8  fw6XlbF3  mqsieQoa  qIqcOTDP  vzBdlMd6
3FOFUCD5  8NfqFqEn  CChBmQFs  HS8wBLPJ  MV2AJR5r  QcXjRtBd  Vc1VEpYz  aUzSODcp  g1qINnts  myF2mI2w  qKIr0SCL  w2pqQhei
3aMAegi2  8OpGe3TY  CDg6fdfa  IMoTEVt4  MXItXLsj  Qm0B85oQ  Vc6sosw2  agmwERM5  gewOpz6a  n1PE7llz  qMqcX95Y  w80nVzZO
3laJICck  8WA32dcd  CTTDdMGJ  IjkDI0gL  MYdMdURn  Qxx5KB3R  VhrXhFPH  b5TZpaRr  gr99Nl0G  n6yqXRv8  qfWh95Q9  w8E8Jd9J
3mHrLQG2  8WYKhs9b  CXVq5spu  IwVJbP5E  MavUz60O  R84tLxGR  W7K36eZ0  b8hbdeFv  gru5fnYQ  nSepPhk6  rPOS47wB  wHR2ydKC
3nroY5Wt  8d6678sz  Cwfv60OS  J7BJ7tAo  Md3PHwRz  RKOBoCMd  WYlISi4n  bMcbuEVi  hRF2XNzg  nTEqj1Ol  rXWuGW1m  wvNy3kRU
4BRDZhS7  9LMKbufv  DGOlVleK  JD0ZwfH8  MvDDPtoW  RSQ5Ynin  WaA6y2oF  bVoP3eel  iKH9t6m9  nU797aVT  rgZiIAPZ  xZDQnhCn
4EqhTV10  9YFDyvy5  DINN9cgG  JIPRVMlG  NAwNCfiS  RV6BgBu6  WjUfazgU  bZEwUIec  ih4q9ziU  nVO17uZV  rjta4881  y2XXKk9C
4Fegg7AZ  9rtRtn1R  DNwq8kf8  JLE4rtY5  NB0dzXJg  RWol5Yvg  WnH4XGQ0  blsMKCvn  jQXi84ic  npy5LylP  ryxNv3Er  y8THzTYH
```
This are the files we need to check for hash. It is very basic if you know the linux basics.

We can simply run:
```bash
ctf-player@pico-chall$ sha256sum * | grep 55b983afdd9d10718f1db3983459efc5cc3f5a66841e2651041e25dec3efd46a
55b983afdd9d10718f1db3983459efc5cc3f5a66841e2651041e25dec3efd46a  2cdcb2de
```
## Answer
After finding out our file is `2cdcb2de`, we can simply run:
```bash
ctf-player@pico-chall$ ./decrypt.sh files/2cdcb2de 
picoCTF{------------------------}
```
