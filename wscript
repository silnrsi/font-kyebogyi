APPNAME='KyebogyiSIL'
VERSION=1.1
LICENSE='OFL.txt'
COPYRIGHT="Copyright 2014, SIL International. All rights reserved"

font(target = process('KyebogyiSIL.ttf',
                cmd('hackos2 -u 100000000000000000000080000003 ${DEP} ${TGT}'),
                cmd('../tools/ttfaddemptyot -t gpos ${DEP} ${TGT}')),
     source = 'srcs/Kyebogyi_SIL.ttf',
     license = ofl('Kyebogyi'),
     copyright = COPYRIGHT)

