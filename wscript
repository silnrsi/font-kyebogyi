APPNAME='KyebogyiSIL'
VERSION=1.1

font(target = process('KyebogyiSIL.ttf',
                cmd('hackos2 -u 100000000000000000000080000003 ${DEP} ${TGT}'),
                cmd('../tools/ttfaddemptyot -t gpos ${DEP} ${TGT}')),
     source = 'srcs/Kyebogyi_SIL.ttf',
)

